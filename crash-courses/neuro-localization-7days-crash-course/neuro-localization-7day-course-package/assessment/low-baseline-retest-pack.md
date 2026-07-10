---
type: Retest Pack
title: Low-Baseline Retest Pack
description: Retest pack generated from SIM-LOW-BASE-001 failure modes.
tags: [assessment, retest, low-baseline]
timestamp: 2026-07-07T11:55:00-07:00
---

# Low-Baseline Retest Pack

```yaml
source: simulation/low-baseline-student-001
use_when: learner_score_below_70_percent_or_repeats_same_misconception
visibility: student_prompt
answer_release: after_student_answer
```

## Retest 1 — Side and UMN

```text
患者右侧肢体无力，右侧 Babinski 阳性，无明显肌萎缩。请写病灶侧别、层级范围和两个继续分层线索。
```

## Retest 2 — Hemisphere vs Brainstem

```text
A 患者：左侧周围性面瘫 + 右侧 Babinski。B 患者：右侧偏瘫 + 失语。分别定位，并写出为什么二者不能互换答案。
```

## Retest 3 — Spinal vs Peripheral

```text
A 患者：胸部以下痛温觉下降 + 双下肢痉挛 + 尿潴留。B 患者：双足麻木上行 + 踝反射减弱 + 无感觉平面。分别定位。
```

## Retest 4 — NMJ vs Myopathy vs Peripheral Neuropathy

```text
A 患者：下午眼睑下垂和复视加重，感觉正常，反射正常。
B 患者：上楼、蹲起、梳头困难，感觉正常，反射早期保留，无明显波动。
C 患者：双足麻木，远端感觉下降，踝反射减弱。
分别定位，并各写一个排除理由。
```

## Retest 5 — Root vs Mononeuropathy

```text
患者小指和环指尺侧麻木，第一骨间肌萎缩。请说明它可能是尺神经病，也可能是 C8/T1 根病；分别还要查什么线索。
```

## Pass Rule

```yaml
minimum_score: 70_percent
must_not_repeat:
  - disease_name_before_localization
  - missing_exclusion_reasoning
  - side_reversal
```
