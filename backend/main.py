# AIcoper Backend
# FastAPI 多模型聚合引擎
# 部署：pip install -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8000

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import httpx
import os
import asyncio
import sqlite3
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()  # 加载 .env 文件中的 API 密钥

app = FastAPI(title="AIcoper API", version="1.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ========== 配置（从环境变量读取）==========
API_KEYS = {
    "deepseek": os.getenv("DEEPSEEK_API_KEY", ""),
    "qwen": os.getenv("QWEN_API_KEY", ""),
    "doubao": os.getenv("DOUBAO_API_KEY", ""),
    "kimi": os.getenv("KIMI_API_KEY", ""),
    "glm": os.getenv("GLM_API_KEY", ""),
    "claude": os.getenv("CLAUDE_API_KEY", ""),
    "openai": os.getenv("OPENAI_API_KEY", ""),
}

# ========== 数据库初始化 ==========
def init_db():
    conn = sqlite3.connect("aicoper.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            plan TEXT DEFAULT 'free',
            paid_at TEXT,
            expires_at TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id TEXT,
            amount REAL,
            plan TEXT,
            paid_at TEXT DEFAULT (datetime('now')),
            confirmed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ========== 数据模型 ==========
class ChatRequest(BaseModel):
    message: str
    models: List[str]  # ["deepseek","qwen","doubao","kimi"]
    member_id: Optional[str] = None

class ChatResponse(BaseModel):
    results: List[dict]  # [{"model":"deepseek","content":"..."}]

class PaymentConfirm(BaseModel):
    member_id: str
    amount: float
    plan: str  # "monthly" / "quarterly" / "yearly"
    screenshot_url: Optional[str] = None

# ========== 模型调用路由 ==========
MODEL_ENDPOINTS = {
    "deepseek": {
        "url": "https://api.deepseek.com/v1/chat/completions",
        "model": "deepseek-chat",
        "headers": lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    },
    "qwen": {
        "url": "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        "model": "qwen-plus",
        "headers": lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    },
    "doubao": {
        "url": "https://ark.cn-beijing.volces.com/api/v3/chat/completions",
        "model": "doubao-pro-32k",
        "headers": lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    },
    "kimi": {
        "url": "https://api.moonshot.cn/v1/chat/completions",
        "model": "moonshot-v1-8k",
        "headers": lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    },
    "glm": {
        "url": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
        "model": "glm-4",
        "headers": lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    },
    "claude": {
        "url": "https://api.anthropic.com/v1/messages",
        "model": "claude-3-haiku-20240307",
        "headers": lambda key: {"x-api-key": key, "Content-Type": "application/json", "anthropic-version": "2023-06-01"}
    },
    "gpt": {
        "url": "https://api.openai.com/v1/chat/completions",
        "model": "gpt-3.5-turbo",
        "headers": lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    }
}

async def call_model(model_id: str, message: str):
    """调用单个模型API"""
    key = API_KEYS.get(model_id, "")
    if not key:
        return {"model": model_id, "content": f"[{model_id}] 未配置API密钥", "error": True}

    endpoint = MODEL_ENDPOINTS.get(model_id)
    if not endpoint:
        return {"model": model_id, "content": f"[{model_id}] 不支持的模型", "error": True}

    try:
        headers = endpoint["headers"](key)

        if model_id == "claude":
            body = {
                "model": endpoint["model"],
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": message}]
            }
        else:
            body = {
                "model": endpoint["model"],
                "messages": [{"role": "user", "content": message}],
                "max_tokens": 1024
            }

        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(endpoint["url"], headers=headers, json=body)
            data = resp.json()

            if model_id == "claude":
                return {"model": model_id, "content": data["content"][0]["text"]}
            else:
                return {"model": model_id, "content": data["choices"][0]["message"]["content"]}

    except Exception as e:
        return {"model": model_id, "content": f"[{model_id}] 调用失败: {str(e)}", "error": True}

# ========== API路由 ==========

@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """并行调用多个模型"""
    tasks = [call_model(m, req.message) for m in req.models]
    results = await asyncio.gather(*tasks)
    return ChatResponse(results=list(results))

@app.get("/api/models")
async def list_models():
    """返回可用模型列表及状态"""
    models = []
    for mid, endpoint in MODEL_ENDPOINTS.items():
        models.append({
            "id": mid,
            "name": endpoint["model"],
            "available": bool(API_KEYS.get(mid, ""))
        })
    return {"models": models}

@app.post("/api/payment/confirm")
async def confirm_payment(req: PaymentConfirm):
    """手动确认付款（收到用户截图后）"""
    plan_days = {"monthly": 30, "quarterly": 90, "yearly": 365}
    days = plan_days.get(req.plan, 30)
    expires = (datetime.now() + timedelta(days=days)).isoformat()

    conn = sqlite3.connect("aicoper.db")
    exists = conn.execute("SELECT id FROM members WHERE id=?", (req.member_id,)).fetchone()

    if exists:
        conn.execute("UPDATE members SET plan=?, paid_at=datetime('now'), expires_at=? WHERE id=?",
                     (req.plan, expires, req.member_id))
    else:
        conn.execute("INSERT INTO members (id, plan, paid_at, expires_at) VALUES (?,?,datetime('now'),?)",
                     (req.member_id, req.plan, expires))

    conn.execute("INSERT INTO payments (member_id, amount, plan, confirmed) VALUES (?,?,?,1)",
                 (req.member_id, req.amount, req.plan))
    conn.commit()
    conn.close()

    return {"ok": True, "expires_at": expires, "plan": req.plan}

@app.get("/api/member/{member_id}")
async def get_member(member_id: str):
    """查询会员状态"""
    conn = sqlite3.connect("aicoper.db")
    row = conn.execute("SELECT * FROM members WHERE id=?", (member_id,)).fetchone()
    conn.close()

    if not row:
        return {"member_id": member_id, "plan": "free", "active": False}

    expires = datetime.fromisoformat(row[4]) if row[4] else None
    active = expires and expires > datetime.now()
    days_left = (expires - datetime.now()).days if active else 0

    return {
        "member_id": row[0],
        "name": row[1],
        "plan": row[3],
        "active": active,
        "days_left": days_left,
        "expires_at": row[4]
    }

@app.get("/api/health")
async def health():
    return {"status": "ok", "models_configured": sum(1 for k in API_KEYS.values() if k)}

# ========== 启动 ==========
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
