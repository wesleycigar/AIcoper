#!/bin/bash
# AIcoper 后端启动脚本
# 用法: bash start.sh

cd "$(dirname "$0")"

# 安装依赖
pip install -q fastapi uvicorn httpx pydantic python-dotenv 2>/dev/null

# 加载.env并启动
echo "🚀 AIcoper API 启动中..."
echo "   DeepSeek   ✅"
echo "   通义千问   ✅"
echo "   GLM        ✅"
echo "   Kimi       ⚠️ 429限流（稍后重试可用）"
echo "   豆包       ⚠️ 需在火山引擎控制台创建推理接入点(Endpoint)"
echo ""
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
