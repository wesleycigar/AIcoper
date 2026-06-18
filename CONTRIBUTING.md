# Contributing to AIcoper

感谢你对AIcoper的兴趣！我们欢迎任何形式的贡献。

## 贡献方式

### 1. 提交新模型评测
如果你的模型不在我们的评测列表中：
1. 在 Issues 中打开 `[New Model Request]`，说明模型名称、可用API、你的初步评测
2. 或直接提交 PR：在 `methodology/benchmarks/model-eval/` 下添加评测数据

### 2. 修正评分/方法论
如果你对某个评分有异议：
1. 打开 Issue，附带你的评测证据（截图、对比数据）
2. 标注 `[Benchmark Dispute]`

### 3. 改进网页版
- 所有前端代码在 `web/` 目录
- 纯静态HTML+CSS，无需构建工具
- 提交PR前请在本地验证所有页面正常

### 4. 翻译文档
- 欢迎提交多语言README和文档

## 开发环境

```bash
git clone https://github.com/aicoper/aicoper.git
cd aicoper/web
python3 -m http.server 8080
# 浏览器打开 http://localhost:8080
```

## PR规范

- 一个PR只做一件事
- 描述清楚"为什么"而不仅是"做了什么"
- 评测数据修改需附带测试证据
- 前端改动请附带截图

## 行为准则

- 尊重不同意见——这正是AIcoper发散模式的精髓
- 评测数据基于实测，不接受厂商"自评"
- 对抗模式的挑战精神也适用于社区讨论：欢迎质疑，但请基于事实

## 许可证

所有贡献基于 Apache 2.0。提交PR即表示你同意在此许可证下发布你的贡献。
