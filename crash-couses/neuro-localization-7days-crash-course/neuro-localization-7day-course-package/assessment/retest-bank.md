---
type: Retest Bank
title: High-risk Misconception Retest Bank
description: Targeted retest prompts used after common neuro-localization errors.
tags: [assessment, retest, misconceptions, v3]
timestamp: 2026-07-07T10:05:00-07:00
---

# High-risk Misconception Retest Bank

```yaml
visibility: student_prompt
answer_visibility: teacher_private_after_answer
use_rule: select_only_items_linked_to_active_misconceptions
score_type: blind_score
prompt_visibility: hidden_until_answer
```

## RETEST-MC-001 — 定位诊断写成病名

**Linked misconception:** `MC-RISK-001`

```text
患者突发右侧肢体无力，右侧 Babinski 阳性。请不要写疾病名称。只写：定位层级、支持证据、还需补充的两个定位线索。
```

Pass criteria:

```yaml
possible_points: 6
pass_threshold: 5
required:
  - 写出左侧 UMN/锥体束交叉以上方向
  - 不把答案直接写成脑梗死、脑出血或肿瘤
  - 能提出皮层、脑干、脊髓区分线索
```

## RETEST-MC-002 — 一看到偏瘫就写半球

**Linked misconception:** `MC-RISK-002`

```text
患者右侧周围性面瘫，左侧肢体无力，左侧 Babinski 阳性。请定位病灶层级与侧别，并说明为什么不能写左侧大脑半球。
```

Pass criteria:

```yaml
possible_points: 8
pass_threshold: 6
required:
  - 写出右侧脑桥/脑干方向
  - 说明同侧脑神经体征 + 对侧长束体征
  - 明确排除单纯半球定位
```

## RETEST-MC-003 — 手套袜套样感觉异常误作感觉平面

**Linked misconception:** `MC-RISK-003`

```text
A 患者双足麻木向上发展，踝反射减弱，无躯干感觉水平。B 患者脐以下痛温觉下降，双下肢痉挛性无力，尿潴留。请分别定位，并指出哪一个有感觉平面。
```

Pass criteria:

```yaml
possible_points: 8
pass_threshold: 6
required:
  - A 定位远端对称性多发周围神经病方向
  - B 定位脊髓方向
  - 能说明“长度依赖”不等于“感觉平面”
```

## RETEST-MC-004 — 失语与构音障碍混淆

**Linked misconception:** `MC-RISK-004`

```text
患者说话含糊但能命名、复述和执行复杂命令。另一患者表达不流利、命名困难，但发音器官力量基本可。请分别判断更支持构音障碍还是失语，并说明定位意义。
```

Pass criteria:

```yaml
possible_points: 6
pass_threshold: 5
required:
  - 第一例偏构音障碍
  - 第二例偏失语/优势半球语言网络
  - 不把“说话困难”一概等同于失语
```

## RETEST-MC-005 — 根、丛、周围神经按名称乱选

**Linked misconception:** `MC-RISK-005`

```text
患者从颈部向拇指放射痛，肱二头肌反射减弱，肘屈无力；另一患者感觉缺损严格符合正中神经分布。请分别定位到神经根还是单一周围神经，并说明依据。
```

Pass criteria:

```yaml
possible_points: 8
pass_threshold: 6
required:
  - 第一例用皮节/肌节/反射解释根病
  - 第二例用命名神经 territory 解释单神经病
  - 明确“疼痛或麻木”本身不足以定位
```
