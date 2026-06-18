# AIcoper — Benchmark. Challenge. Grow Stronger.

<p align="center">
  <img src="https://img.shields.io/badge/status-prototype-blue" alt="Status">
  <img src="https://img.shields.io/badge/license-Apache%202.0-green" alt="License">
  <img src="https://img.shields.io/badge/models-8%2B-orange" alt="Models">
  <img src="https://img.shields.io/badge/OS%20tools-6%2B-purple" alt="OS Tools">
</p>

> **"扩展人类创造未来的能力与自由。"**  
> 不卖便宜AI。我们做的是全球创造力基础设施——让中度到重度的AI使用者，在一个地方比较大脑、比较操作系统、锤炼想法。

---

## 🤔 AIcoper 是什么

一个**跨厂商AI聚合平台**，但和OpenRouter/LMSYS不一样：

| 功能 | OpenRouter | LMSYS Arena | **AIcoper** |
|------|-----------|-------------|-------------|
| 多模型聚合调用 | ✅ | ❌ | ✅ |
| 模型评分排行榜 | ❌ | ✅ ELO | ✅ 6维雷达+用户评价 |
| **多模型对抗挑战** | ❌ | ❌ | ⭐ **独有** |
| **多模型发散探索** | ❌ | ❌ | ⭐ **独有** |
| AI操作系统评测 | ❌ | ❌ | ⭐ **独有** |
| 场景工作流 | ❌ | ❌ | ✅ |
| 开源 | 部分 | 部分 | ✅ 全栈开源 |

> **核心差异化**：AIcoper不只是让你用AI——它让多个AI从不同立场挑战你的想法、发散你的视角。单一模型厂商绝不会让竞品来挑自己模型的刺。这是聚合器独有的结构性优势。

---

## 🧠 比较大脑（模型评测）

覆盖全球主要模型，6维能力雷达：

| 模型 | 成本 | 逻辑 | 原创 | 抗幻觉 | 理论深度 | 速度 |
|------|------|------|------|--------|----------|------|
| DeepSeek-R1 | 95 | 94 | 80 | 88 | 92 | 82 |
| 通义千问 Qwen | 86 | 85 | 84 | 90 | 86 | 88 |
| Claude 4 | 72 | 95 | 88 | 92 | 93 | 80 |
| ChatGPT | 68 | 90 | 93 | 89 | 90 | 85 |

> 完整评测数据见 [`methodology/benchmarks/model-eval/`](methodology/benchmarks/model-eval/)

---

## 🖥️ 比较操作系统（AI工作系统评测）

不只比较"谁回答得好"——更比较"谁更能干活"。

| 工具 | 自动化 | 逻辑 | 成本 | 和谐度 | 适配 | 生态 | 综评 |
|------|--------|------|------|--------|------|------|------|
| CodeWhale | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ | 8.4 |
| Claude Code | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ | 8.2 |
| Cursor | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | 7.8 |

> 评测方法论见 [`methodology/M-OS-BENCH.md`](methodology/M-OS-BENCH.md)

---

## ⚡ 快速开始

### 在线体验
👉 **[aicoper.app](https://aicoper.app)** （即将上线）

### 本地运行
```bash
git clone https://github.com/aicoper/aicoper.git
cd aicoper/web
# 直接用浏览器打开 index.html
# 或
python3 -m http.server 8080
```

### 部署到 GitHub Pages
```bash
# Fork 本仓库，Settings → Pages → Source: GitHub Actions
# 或手动推送到 gh-pages 分支
```

---

## 📁 仓库结构

```
aicoper/
├── methodology/          ← 评测方法论（论文+数据集）
│   ├── paper/            # arXiv预印本 (LaTeX+PDF)
│   ├── benchmarks/       # 标准化评测数据集 (JSONL)
│   ├── M-ADVERSARY.md    # 对抗模式方法论
│   ├── M-DIVERGE.md      # 发散模式方法论
│   └── M-OS-BENCH.md     # AI OS 多维评测框架
├── web/                  ← 网页版工具源码
│   ├── index.html        # 首页
│   ├── advocate.html     # 对抗模式（皇冠明珠）
│   ├── diverge.html      # 发散模式（皇冠明珠）
│   ├── eval.html         # 模型评测
│   ├── os-eval.html      # OS评测
│   ├── scenes.html       # 场景工作流
│   └── assets/style.css  # 设计系统
├── README.md             # 👈 你在这
├── CONTRIBUTING.md       # 社区贡献指南
└── LICENSE               # Apache 2.0
```

---

## 🤝 贡献指南

我们欢迎任何形式的贡献——提交新模型评测、修正评分、改进方法论、翻译文档。

详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)

### 贡献者协议
所有贡献基于 Apache 2.0 许可证。评测数据贡献者保留署名权，AIcoper保留数据使用权。详见GOVERNANCE.md（规划中）。

---

## 📄 论文

> **"Multi-Model Adversarial Evaluation: A Framework for Cross-Vendor AI Benchmarking and Collaborative Reasoning"**
>
> 预印本即将上线 arXiv (cs.AI / cs.HC)
>
> 摘要：现有AI评测体系以单模型ELO排名为主，忽略了多模型协同推理的认知价值。本文提出对抗评测框架（Adversary Mode）和发散评测框架（Divergent Mode），利用跨厂商多模型聚合的结构性优势，实现单一大厂无法复制的"陪练式"AI使用范式。

---

## 📜 许可证

本项目代码采用 [Apache License 2.0](LICENSE)。评测数据和论文采用 CC BY 4.0。

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=aicoper/aicoper&type=Date)](https://star-history.com/#aicoper/aicoper&Date)

---

<p align="center">
  <b>AIcoper</b> — 让AI成为你的杠杆，而不是拐杖。<br>
  <sub>Made with ❤️ by the AIcoper community</sub>
</p>
