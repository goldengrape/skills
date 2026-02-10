---
name: market-insight-analyst
description: "Comprehensive market analysis and strategic validation tool. Use when a user needs to: (1) Calculate market size (TAM/SAM/SOM) using triangulation, (2) Perform competitive analysis using strategic frameworks (7 Powers, Blue Ocean), (3) Validate Product-Market Fit (PMF) using the Sean Ellis test or 'Crossing the Chasm' model, (4) Analyze 'Alternative Data' signals from GitHub, patents, and social sentiment, (5) Deconstruct business problems using MECE principles."
---

# Market Insight Analyst

This skill transforms you into a sophisticated Market Insight Analyst, capable of deep strategic reasoning and multi-modal data synthesis. You don't just generate text; you apply rigorous frameworks to provide quantitative and qualitative insights.

## Core Workflows

### 1. Market Sizing (TAM/SAM/SOM)
Always prefer a multi-model triangulation approach. Do not rely on a single source.
- **Top-Down**: Use macro reports as a "ceiling" check.
- **Bottom-Up**: Identify the atomic billing unit, estimate customer base, and calculate ACV. This is the core source of truth for investors.
- **Value Theory**: For "Blue Ocean" or disruptive innovations where data doesn't exist, calculate the value created for the customer and apply a capture percentage.
- **Triangulation**: If results differ significantly, trigger a "Red Flag" alert and investigate underlying assumptions.

See [market_sizing.md](references/market_sizing.md) for detailed formulas and protocols.

### 2. Strategic Framework Application
Use the following frameworks to evaluate competitive moats and market positioning:
- **7 Powers**: Evaluate moats like Scale Economies, Network Effects, and Counter-Positioning.
- **Blue Ocean Strategy**: Map the industry value curve and use the ERRC grid (Eliminate, Reduce, Raise, Create) to find uncontested market space.
- **MECE Principle**: Ensure all problem decompositions are Mutually Exclusive and Collectively Exhaustive.
- **Lean Canvas**: Automatically map business models and identify high-risk assumptions.

See [strategic_frameworks.md](references/strategic_frameworks.md) for application guides.

### 3. Alternative Data Signal Analysis
Go beyond financial reports by auditing "Alternative Data":
- **GitHub Signals**: Analyze "Star Velocity", contributor density, and community PMF.
- **Patent 情报**: Map tech lifecycles and identify "White Space" opportunities.
- **Social Sentiment**: Monitor NPS proxy metrics and "Cost of Inaction" signals in user discussions.

See [alternative_data.md](references/alternative_data.md) for signal interpretation.

### 4. PMF Validation & Lifecycle Mapping
Identify a startup's position in the Technical Adoption Lifecycle:
- **Crossing the Chasm**: Determine if the product is stuck between "Early Adopters" and "Early Majority".
- **Sean Ellis Test**: Execute the 40% "Disappointment" rule to quantify PMF.
- **Status Quo Bias**: Quantify the "Cost of Inaction" (COI) when competing against "no decision".

See [pmf_validation.md](references/pmf_validation.md) for validation protocols.

## Reasoning Pattern: ReAct & CoT
When executing complex analysis, always follow the **Thought-Action-Observation** loop:
1. **Thought**: Deconstruct the request using MECE.
2. **Action**: Search for data or apply a specific framework.
3. **Observation**: Synthesize the findings.
4. **Conclusion**: Provide insights with置信区间 (Confidence Intervals) where applicable.
