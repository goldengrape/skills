---
type: Schema
title: Localization Taxonomy
description: Stable taxonomy for neuro-localization labels.
tags: [schema, taxonomy]
timestamp: 2026-07-07T07:38:01+00:00
---

# Localization Taxonomy

## Tag Format

```yaml
localization_tag:
  axis_level: supratentorial | brainstem | cerebellar | spinal_cord | nerve_root | plexus | peripheral_nerve | neuromuscular_junction | muscle | multiple_levels
  system: motor | sensory | cranial_nerve | cortical_function | coordination | gait | reflex | autonomic
  side_relation: ipsilateral | contralateral | bilateral | crossed | midline | not_applicable
  confidence: high | medium | low
```

## A-Level Tags

| Tag | Meaning | Positive features | Negative features |
|---|---|---|---|
| `supratentorial.cortical` | 大脑皮层定位 | 失语、忽视、皮层感觉、偏盲、癫痫 | 单个周围神经分布无法解释 |
| `supratentorial.subcortical` | 皮层下/内囊 | 纯运动或纯感觉偏瘫，皮层体征少 | 同侧脑神经核性体征不支持 |
| `brainstem.crossed` | 脑干交叉定位 | 同侧脑神经体征 + 对侧长束体征 | 单纯半球病变不完整 |
| `spinal_cord.level` | 脊髓节段定位 | 感觉平面、双侧长束、括约肌 | 手套袜套样更像周围 |
| `spinal_cord.hemicord` | 脊髓半切 | 同侧运动/深感觉 + 对侧痛温 | 单根病变不能解释双束模式 |
| `nerve_root.radicular` | 神经根 | 皮节疼痛、肌节无力、相关反射改变 | 单一外周神经分布不完整 |
| `plexus.patchy` | 神经丛 | 多根多神经组合，片状分布 | 长度依赖对称不支持 |
| `peripheral_nerve.mononeuropathy` | 单神经 | 单一神经运动感觉区 | 皮节型疼痛不完整 |
| `peripheral_nerve.polyneuropathy` | 多发周围神经 | 对称远端、手套袜套 | 明确感觉平面不支持 |
| `neuromuscular_junction.fatigable` | 神经肌接头 | 波动、疲劳、眼咽受累、感觉正常 | 感觉缺损不支持 |
| `muscle.proximal` | 肌肉 | 近端无力、感觉正常、反射早期可保留 | 束颤和显著感觉缺损不支持 |

## Rule

定位标签是课程包内部通用接口。模块、题库和状态记录只能引用标签，不直接互相读取正文。
