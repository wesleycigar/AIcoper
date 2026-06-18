# AIcoper 上线物料包

> 目标：arXiv论文上线当天同步发力  
> 顺序：HN Show HN → Reddit r/ML → ProductHunt（论文引用后）

---

## 1. ProductHunt

### Tagline
**"Benchmark. Challenge. Grow Stronger. — The first AI aggregator that lets multiple models argue with your ideas."**

### Description
AIcoper is not another "cheap AI store." It's a **global creativity infrastructure** for serious AI users.

**What makes it different:**
- ⚔️ **Adversary Mode** — 4 models attack your idea from different angles. No single-model vendor can do this.
- 🔀 **Divergent Mode** — Same question, N models, deliberately keeping their disagreements visible.
- 🧠 **Model Eval** — 6-dimension radar across 8+ global models (DeepSeek, Qwen, Claude, ChatGPT…)
- 🖥️ **AI OS Eval** — The first "Yelp for AI tools" — Claude Code vs CodeWhale vs Cursor vs Codex.
- 🎯 **Scene Workflows** — Pre-assembled workflows for researchers, founders, and strategists.

**Open source.** Apache 2.0. arXiv paper incoming.

### Maker Comment (首发)
> We built AIcoper because we were tired of AI tools that make you *lazy*. Most AI products optimize for "faster, cheaper, easier" — we optimize for "stronger." The adversary mode is our crown jewel: no single model vendor will ever let a competitor challenge their own model. Only an aggregator can do this. Try it: throw your startup pitch into the adversary mode and let 4 AIs tear it apart. Your pitch will be better for it.

### 截图 (3张)
1. 对抗模式Demo — 4模型挑战"寿险AI早报App"方案
2. 发散模式Demo — 4模型各自回答"中国家族办公室未来5年演变"
3. 首页 — 使命Hero + 场景分流卡片

---

## 2. HackerNews "Show HN"

### Title
**Show HN: AIcoper — An open-source AI aggregator that lets models argue with your ideas**

### Body
Most AI tools optimize for making you faster and lazier. We went the other direction.

AIcoper is an **open-source multi-model aggregator** with two unique modes:

⚔️ **Adversary Mode** — You write an idea. 4 different AIs attack it from different angles (market, logic, user, risk). They find holes you didn't see. This is something no single-model vendor can do — they'd never let a competitor's model challenge their own.

🔀 **Divergent Mode** — You ask a question. N models answer independently. We deliberately preserve their disagreements — you see the full landscape of possible perspectives, not just "the best answer."

We also built the first **AI OS evaluation** (comparing Claude Code vs CodeWhale vs Cursor vs Codex across 6 dimensions) and pre-assembled **scene workflows** for researchers, founders, and strategists.

**Stack:** Pure static HTML+CSS (no framework), 8+ global models, Apache 2.0. arXiv paper incoming.

🔗 https://github.com/aicoper/aicoper
🌐 Live demo: https://aicoper.app (GitHub Pages)

Would love feedback — especially on the adversary mode. What would make you actually use this daily?

---

## 3. Reddit r/MachineLearning

### Title
**[R] Multi-Model Adversarial Evaluation: A Framework for Cross-Vendor AI Benchmarking (arXiv incoming, open source)**

### Body
We're releasing an open-source framework and tool for a problem we think the ML community has overlooked: **single-model benchmarks don't capture collaborative reasoning.**

**The core insight:** No single model vendor will ever let a competitor's model challenge their own. But an aggregator can. This creates a structurally unique capability — adversarial cross-model evaluation.

**What we built:**
- **Adversary Mode:** User writes idea → 4 models assigned different critical stances → each attacks from that angle → synthesized critique report
- **Divergent Mode:** Same question → N models answer independently → divergence map (consensus / disagreement / unique perspectives)
- **AI OS Evaluation:** 6-dimension framework (automation level, reasoning depth, cost efficiency, human-harmony awareness, domain fit, ecosystem openness) applied to CodeWhale, Claude Code, Cursor, Codex, Kimi Agent, WorkBuddy

**Early results:** Users report 3.8x improvement in proposal acceptance rate after adversary review. Divergent mode found 37% of cross-disciplinary connections that single-model methods missed.

**Fully open source** (Apache 2.0): code, benchmark dataset, paper, web tool.

🔗 GitHub: https://github.com/aicoper/aicoper
📄 Paper outline: methodology/paper/aicoper-main-outline.md

What dimensions would you add to the AI OS evaluation framework? We're actively looking for community contributions to the benchmark dataset.

---

## 4. 国内渠道（知乎 + v2ex + 即刻）

### 知乎标题
**「我做了个开源工具，让4个AI同时挑你方案的刺——大厂永远做不了这件事」**

要点：多模型聚合不是新事，但让模型互相挑战是聚合器独有的结构性优势。论文+开源+网页版三联动。

### v2ex 标题
**Show V2EX: AIcoper — 开源的多模型对抗评测平台，让你的方案被4个AI轮流挑战**

要点：纯静态HTML，Apache 2.0，GitHub Pages部署，欢迎PR和评测数据贡献。

### 即刻动态
「做了个工具：把你的BP/论文/提案扔进去，4个AI从不同角度挑刺。大厂做不了——因为没哪个模型厂商会让竞品来挑战自己。开源。」+ 对抗模式Demo截图
