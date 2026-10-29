# 热度对齐与术语闸门（L3）

完整标题优化默认优先考察近一年引用增长，执行
[citation-momentum.md](citation-momentum.md)。单独热词推荐也走该流程。
普通标题润色、全量写作及单独撞名检查不启动此模块。

## 指标与资格

| 指标 | 用途 | 不能声称 |
| --- | --- | --- |
| 相关文献滚动 365 天相对此前 365 天的引用增长 | 同等语义匹配下优先推荐增长充分的术语 | 搜索量、标题改写的因果收益或全球排行 |
| arXiv 按年发文趋势 | 发现候选和补充研究活跃度背景 | 引用增长或搜索热度 |
| 顶会标题词频 | 判断社区惯用措辞 | 当前引用增长 |

标题资格取决于真实且核心的关系；只作 baseline 不足以成为标题标签。
增长推荐须有可追溯的窗口数据，同时检查基数、增量、增速、样本规模和单篇
集中度。表达必须自然，不堆词、不改变科学含义。必要专业术语即使趋势下降
也应保留。arXiv 脚本的 rising/background/flat/stale 仅是发文趋势标签，
不再作为标题/摘要准入硬规则，更不能解释为引用增长。

## 现有辅助资源

- references/title-optimization/term-pool.csv 是历史发文量种子池。检查
  collected_at，超过 90 天只能用于候选发现；本次引用增长另行测量。
- scripts/paper-title-optimizer/arxiv-trend.mjs 测按年发文量，部分年份
  年化值尤其在年初不稳定，不是引用测量工具。
- references/title-optimization/title-word-pool.csv 及 title-numbers-stats.json
  是历史录用标题统计，使用时标年份；不冒充当前语料。
- scripts/paper-title-optimizer/title-stats.mjs 可在有新语料时重算标题统计。

引用数据缺失就标未测量，继续正常写作，不用发文趋势冒充引用结果。
完整计数口径、推荐表与标题版本要求由 citation-momentum.md 统一维护。
