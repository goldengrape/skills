# Metrics & Simulation: The Startup Vitals

## 1. 0-to-1 Survival Metrics

The EOD Agent monitors these metrics to ensure the startup does not run out of fuel.

### Financial Vitals
- **Cash Zero Date**: The exact calendar day when bank balance hits §0 based on current burn rate.
- **Runway**: Remaining months of life. `Total Cash / Monthly Burn`.
- **Cash Conversion Cycle**: Time taken for $1 of cost to become $1.XX of revenue.

### Product-Market Fit (PMF) Signals
- **Sean Ellis Test**: Survey users: "How would you feel if you could no longer use the product?" Target >40% "Very Disappointed".
- **Cohort Retention**: If the retention curve flattens > 0, PMF is present. If it hits 0, the product is "Leaking Bucket".

### Growth Efficiency
- **Magic Number**: `(Current Q Net New Revenue * 4) / Previous Q S&M Spend`. Target > 1.0.
- **CAC Payback**: Months to recover Customer Acquisition Cost. Target < 12 months for venture-scale.

## 2. Digital Twin of Organization (DTO)

The EOD maintains a virtual model of the company's resources and workflows.

### Scenario Planning (What-If Analysis)
Before approving high-cost or high-risk actions, the EOD should simulate:
- **Scenario A (Aggressive)**: Double ads budget. *Result: Support queue overflow, high churn.*
- **Scenario B (Conservative)**: Hire 1 dev. *Result: Feature delivery improves by 10%, runway drops by 2 months.*

### DTO Modeling Principles
- **Agent-Based Modeling (ABM)**: Focus on individual actors (customers, staff) and their interactions.
- **Discrete Event Simulation (DES)**: Focus on the flow of work items through a pipeline.
- **Choice of Simulation Tool**: 
  - *AnyLogic*: Best for ABM (human behavior).
  - *Simul8*: Best for DES (linear processes).
