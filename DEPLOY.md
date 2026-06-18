# AIcoper 部署指南（简化版）

## 总览

```
你的电脑 → git push → GitHub
                          ├── backend/ → Railway（后端API）
                          └── web/    → GitHub Pages（前端网站）
```

## 第一步：推送到 GitHub

```bash
cd /Users/wesley/Downloads/aicoper-prototype
git init
git add .
git commit -m "AIcoper v0.3"
git branch -M main
git remote add origin https://github.com/你的用户名/aicoper.git
git push -u origin main
```

## 第二步：后端部署到 Railway

1. 打开 [railway.app](https://railway.app) → 用GitHub登录
2. 点击 **New Project → Deploy from GitHub repo** → 选择 `aicoper`
3. Railway自动检测 `railway.json`，开始构建
4. 构建完成后，点击 **Variables** 添加环境变量：

| 变量名 | 值 |
|--------|-----|
| `DEEPSEEK_API_KEY` | sk-f1eab68300ae4f53b695aa41f521986f |
| `QWEN_API_KEY` | sk-ws-H.RPDHDHM.LcBY.MEUCIDMf_G7oi8fXe7_c3dmKWp0ITabGf6AXEhaWO4YuJ-kLAiEAog4y_ZwYj-2u58wv7JaJWkaqi3uSxXcjS_p78mEHkjs |
| `GLM_API_KEY` | fb07af50fbd4425a823e4e31624e49ff.nYaBN4Xp2OG0rtnp |
| `KIMI_API_KEY` | sk-e8RR7vTt6C3KnukFR4BhICTKiz9XNlaQBduO7DRXFq3hEa98 |
| `DOUBAO_API_KEY` | ark-62858e70-b654-4a8d-8550-3838856583bf-b4fe5 |

5. 部署完成后获得URL（如 `https://aicoper.up.railway.app`）
6. 验证：打开 `https://aicoper.up.railway.app/api/health`

## 第三步：更新前端API地址

修改 `web/aggregate.html` 中的：
```javascript
var API_BASE = 'http://localhost:8000';
```
改为：
```javascript
var API_BASE = 'https://aicoper.up.railway.app';  // 你的Railway URL
```

提交并推送：
```bash
git add web/aggregate.html
git commit -m "update API_BASE"
git push
```

## 第四步：前端部署到 GitHub Pages

GitHub仓库 → Settings → Pages → Source: GitHub Actions
`.github/workflows/deploy-pages.yml` 已配置，push 即自动部署。

几分钟后访问：`https://你的用户名.github.io/aicoper/`

## 本地开发

```bash
cd backend && bash start.sh     # 启动后端
open web/aggregate.html         # 打开前端

curl http://localhost:8000/api/health            # 验证后端
curl -X POST http://localhost:8000/api/chat \    # 测试聊天
  -H "Content-Type: application/json" \
  -d '{"message":"你好","models":["deepseek","qwen","glm"]}'
```
