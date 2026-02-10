# Growth Metrics: The Startup's Core Optimization Function

Based on Paul Graham's theory: "A startup is a company designed to grow fast." Growth is the compass and the lifeline of any high-potential venture.

## Startup vs. Ordinary Business: The Fundamental Difference

### Differentiation Criteria

| Dimension | Small Business | Startup |
| :--- | :--- | :--- |
| **Target Market** | Limited local market | The entire market (global) |
| **Core Objective** | Stable profitability | Rapid growth |
| **Scalability** | Limited by geography/resources | Extremely high scalability |
| **Examples** | Barber shops, consultancies | Google, Airbnb |

### Agent Selection Logic

**Evaluation Flow**:
```
1. Assess TAM (Total Addressable Market)
   ├─ TAM < $100M → Small Business Mode
   └─ TAM > $1B → Startup Potential

2. Assess Scalability 
   ├─ Increasing marginal costs → Small Business (e.g., Service-based)
   └─ Decreasing marginal costs → Startup (e.g., SaaS, Marketplaces)

3. Switch Operating Mode
   ├─ Small Business → "SME Consultant Mode"
   └─ Startup → "High-Growth Startup Mode"
```

## The 5-7% Weekly Growth Rate: A Categorical Imperative

### Why "Weekly" Instead of "Monthly" or "Yearly"?

- **Rapid Feedback**: You can test new strategies and iterate every week.
- **Urgency**: Keeps the team focused and action-oriented.
- **The Power of Compounding**: Small weekly gains lead to astronomical annual growth.

### Growth Rate Standards

| Weekly Rate | Annual Multiplier | Strategic Meaning | Recommended Action |
| :--- | :--- | :--- | :--- |
| 1% | 1.7x | ☠️ **Death Zone** | Stagnation; invisible to VCs |
| 2% | 2.8x | ⚠️ **Mediocrity** | Barely surviving; easily overtaken |
| **5%** | **12.6x** | ✅ **VC Threshold** | Healthy trajectory; Series A potential |
| **7%** | **33.7x** | 🦄 **Unicorn Trajectory** | Ideal goal |
| 10% | 142.0x | 🚀 **Breakout** | Often accompanied by viral loops |

### Formulas

```
Weekly Growth Rate = (Current Week Metric - Previous Week Metric) / Previous Week Metric * 100%

Annual Multiplier = (1 + Weekly Growth Rate) ^ 52
```

## Agent Algorithm Logic

### Automated Alert System

**When a user reports new user counts**:

```python
# Pseudo-logic
if weekly_growth_rate < 5%:
    🚨 ALERT(f"""
    Warning: Weekly growth rate is only {weekly_growth_rate}%
    At this pace, you will only grow {annual_multiplier}x by year-end.
    
    We need to find tactics to hit a 5% growth target:
    1. What are your current acquisition channels?
    2. Which channels haven't been tested?
    3. Does the product need adjustment to improve retention?
    """)
```

### Critical Question Checklist

1. **What is the current growth rate?**
   - Calculate weekly, not monthly or quarterly.
   
2. **What is the primary growth driver?**
   - Organic vs. Paid acquisition.
   - Sustainable vs. One-off campaigns.

3. **How do we move from X% to 5-7%?**
   - What needs to change in the experiment loop?
   - Where is the bottleneck?

## The Growth S-Curve: Stage Identification

### Three Stages

```
Growth Curve:

    │      ╱────────  ③ Maturation: Growth tapers off
    │     ╱
    │    │  ② Climbing: 5-7% Weekly Growth
    │   ╱
    │  ╱
    │ │  ① Exploration: Searching for PMF
    │╱___________________________
           Time →
```

### Stage-Based Strategies

| Stage | Characteristics | Agent Focus |
| :--- | :--- | :--- |
| **① Exploration** | Slow/No growth | Qualitative feedback, Manual tactics, "Do things that don't scale" |
| **② Climbing** | 5-7% Weekly | Key hires, Server scaling, Process standardization |
| **③ Maturation** | Growth slows | Market expansion, Product innovation, M&A |

### Identifying Your Current Stage

**Diagnostic Questions**:
- No paying users yet? → **Exploration Phase**
- Weekly growth stable at 5%+? → **Climbing Phase**
- Rising CAC and slowing growth? → **Maturation Phase**

## The Metric Trap: Absolute Value vs. Growth Rate

### Common Error

❌ **False Thinking**: "We add 100 new users every week. We're stable!"

✅ **Correct Thinking**:
```
Week 1: 100 total → +100 (100% Growth) ✅
Week 2: 200 total → +100 (50% Growth)  ⚠️
Week 3: 300 total → +100 (33% Growth)  ❌
```

**Static Absolute Growth = Declining Growth Rate**

### Agent Correction Logic

**When a user says "We consistently add X users every week"**:

```
🚨 WARNING: Stable absolute numbers mean a plummeting growth rate!

To maintain a 5% weekly rate, new customer volume MUST increase as the base expands:

Base      Target New Users (5%)
1,000   →  50
2,000   → 100
4,000   → 200
8,000   → 400
```

## Selecting the Right Metric

### North Star Metrics by Stage

| Stage | Core Metric | Secondary Metrics |
| :--- | :--- | :--- |
| **Exploration** | Retention Rate | Qualitative feedback, NPS |
| **Climbing** | Active User Growth | CAC, LTV/CAC Ratio |
| **Maturation** | Revenue Growth | Profit Margin, Market Share |

### Vanity Metric Warnings

**Beware of**:
- ❌ Registered users (if not active)
- ❌ App downloads (if not opened)
- ❌ Website visits (if not converted)

**Focus on**:
- ✅ Active Users (DAU/MAU)
- ✅ Retention (D7/D30)
- ✅ Paid Conversion Rate
- ✅ NPS (Net Promoter Score)

## Stagnation Diagnostic Framework

### When Growth Drops Below 5%

```
Diagnostic Tree:

Growth < 5%?
├─ Acquisition Problem
│  ├─ CAC too high → Optimize channels/Conversion
│  └─ Channel exhaustion → Discover new channels
│
├─ Retention Problem
│  ├─ No Product-Market Fit → Return to Exploration
│  └─ Friction in UX → Optimize onboarding
│
└─ Activation Problem
   └─ Registered but not using → Improve Value Delivery
```

## Key Principles Summary

1. **Growth is the Sole Standard**: Differentiate startups from small businesses.
2. **Measure Weekly**: Maintain urgency and rapid iteration loops.
3. **5-7% is the Floor**: Anything lower requires immediate diagnosis.
4. **Beware the Absolute Value Trap**: Focus on rates, not static volume.
5. **Stage-Specific Strategy**: Manual in Exploration, Scaled in Climbing.
