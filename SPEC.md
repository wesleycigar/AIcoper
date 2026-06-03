# AIcoper / AI合作社 — 原型规格 (v0.1)

## 定位
中立的「AI能力合作社」：跨厂商聚合国产大模型，自动选最优模型，把规模采购的成本优势返还给每个成员。
**不是卖 token，是做用户的采购代理人。** Slogan：用 AI 的人越多，AI 越便宜。

## 合规底线（硬约束，所有页面遵守）
- **只用国产合规模型**：DeepSeek、通义千问 Qwen、豆包(Doubao)、Kimi、智谱 GLM。
- **禁止出现**任何境外模型(GPT/Claude/Gemini)、跨境/翻墙/外汇/代充等字样。
- 每个页面底部放一行合规角标：`仅聚合国内已备案合规大模型 · 境内闭环`（用 `.compliance` 类）。

## 技术约定
- 纯静态 HTML，单文件即可打开，移动端优先。
- 引入共享样式：`<link rel="stylesheet" href="assets/style.css">`。**不要新建/修改 style.css**，只用其中已有的类。
- 中文 UI。数据用合理的假数据（演示用）。交互可用极简内联 `<script>`（点击切换、tab 高亮即可），无需后端。
- 每页结构：`<div class="phone"> <div class="topbar">…</div> <div class="scroll">…内容…</div> <nav class="tabbar">…</nav> </div>`

## 共享底部 tabbar（每页都放，把当前页加 class="on"）
```html
<nav class="tabbar">
  <a href="index.html" class="on"><span class="ic">🏠</span>首页</a>
  <a href="aggregate.html"><span class="ic">💬</span>用AI</a>
  <a href="eval.html"><span class="ic">📊</span>评测</a>
  <a href="referral.html"><span class="ic">🤝</span>合作社</a>
</nav>
```
（各页把自己对应的那个 `<a>` 改成 `class="on"`，其余去掉 on）

## 可用样式类速查
- 布局：`.phone .scroll .topbar .card .row .divider .section-title`
- 数据：`.hero .stat .num .lbl`（金额用 accent 金色）
- 组件：`.btn(.primary/.accent/.ghost/.sm) .badge(.brand/.green/.amber/.gray) .li(.ic/.meta/.right) .bar`
- 聊天：`.bubble(.me/.ai) .route`
- 表格：`table th td .tag-best`
- 合规：`.compliance`

## 四个页面分工
1. index.html — 首页（省钱可视化 + 合作社人数 + 当前折扣 + 入口）
2. aggregate.html — 用AI（聊天 + 自动路由演示 + 单次成本对比）
3. eval.html — AI效能评估（六维雷达图 + 任务→最优模型推荐）★ 护城河
4. referral.html — 合作社（拼多多式分销，两级封顶，折扣随人数加深）
