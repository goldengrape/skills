---
type: Remediation Drill
title: Peripheral Terminal-Level Drill
description: Drill for NMJ vs myopathy vs peripheral neuropathy and root vs mononeuropathy.
tags: [remediation, peripheral, nmj, myopathy, mononeuropathy]
timestamp: 2026-07-07T11:46:00-07:00
---

# Peripheral Terminal-Level Drill

## Why This Exists

The low-baseline simulation repeatedly confused **肌病、神经肌接头病、周围神经病** and answered root/mononeuropathy questions too vaguely.

## Decision Table

| Layer | Distribution | Sensory | Reflex | Time pattern | High-yield clue |
|---|---|---|---|---|---|
| 多发周围神经病 | 远端对称，手套袜套样 | 常异常 | 常先减弱，尤其踝反射 | 慢性或亚急性 | 远端感觉 + 反射减弱 |
| 神经根病 | 皮节痛/麻木 + 肌节无力 | 按皮节 | 对应反射可减弱 | 可有放射痛 | 跨越单一周围神经 territory |
| 单神经病 | 某一命名神经支配区 | 按该神经 | 可局限改变 | 局部压迫/损伤 | median/ulnar/peroneal 等具体 territory |
| NMJ | 眼肌、延髓、近端可受累 | 正常 | 通常保留 | 波动、易疲劳 | 越用越弱，休息改善 |
| 肌病 | 近端对称为主 | 正常 | 早期保留 | 相对稳定或缓慢 | 上楼、蹲起、梳头困难 |

## Retest Items

### R-PER-001

```text
患者双足麻木 3 年，踝反射减弱，远端痛觉下降，上肢远端也开始麻。定位层级？排除 NMJ 的理由？
```

### R-PER-002

```text
患者复视和上睑下垂，下午加重，休息后改善，感觉正常，腱反射正常。定位层级？排除肌病的理由？
```

### R-PER-003

```text
患者上楼、蹲起、梳头困难，感觉正常，腱反射早期保留，无明显波动。定位层级？需与哪两个层级区分？
```

### R-PER-004

```text
患者小指和环指尺侧麻木，第一骨间肌萎缩，夹纸试验差。请判断单神经病还是神经根病，并写出还需补充的 C8/T1 线索。
```

### R-PER-005

```text
患者颈部疼痛向拇指放射，肱二头肌反射减弱，拇指区域感觉异常。请判断神经根病还是单神经病，并说明依据。
```

## Pass Rule

```yaml
minimum_correct: 4/5
must_include:
  - sensory status
  - reflex status
  - distribution pattern
  - one exclusion reason
```
