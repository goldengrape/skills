# Market Sizing Protocol (TAM, SAM, SOM)

Market sizing is the foundation of any startup project and investor evaluation. This protocol details the rigorous methods to be applied by the Market Insight Analyst.

## 1. Dynamic Definitions

- **TAM (Total Addressable Market)**: The theoretical revenue ceiling if the product had 100% market share in every accessible geographic region. Handle this as a long-term vision.
- **SAM (Serviceable Available Market)**: The subset of TAM reachable considering practical constraints (geography, regulations like GDPR, distribution channels).
- **SOM (Serviceable Obtainable Market)**: The realistic market share achievable in 1-3 years, accounting for competition and sales capacity.

## 2. Calculation Methods

### 2.1 Top-Down Analysis (Macro Check)
- Start with macro reports (Gartner, IDC).
- Apply weighted averages across multiple reports.
- **Usage**: Only as a "ceiling" to verify if the bottom-up results are off by orders of magnitude.

### 2.2 Bottom-Up Analysis (Core Logic)
This is the preferred path for investor-grade reports.
- **Formula**: $TAM_{bottom-up} = (\text{Total Potential Customers}) \times (\text{Annual Contract Value (ACV)})$
- **Steps**:
    1. Define the **Atomic Unit**: Seat-based, API call, per transaction.
    2. Estimate **Customer Count**: Use enterprise directories, LinkedIn numbers, or proxy user bases from similar products.
    3. Determine **Value Multiplier**: Use competitive pricing or value-based assumptions to set ACV.

### 2.3 Value Theory (Blue Ocean Sizing)
Used for innovations where no current spending exists.
- **Logic**: Calculate the economic value created per user (e.g., hours saved $\times$ hourly wage).
- **Capture Rate**: Assume a reasonable percentage of that value as the price (e.g., 10-20%).
- **Calculation**: $Value_{Total} = (\text{Total Users}) \times (\text{Value per User}) \times (\text{Capture \%})$.

## 3. Triangulation Protocol
The analyst must compare results from at least two methods.
- **Convergence**: If numbers align within a reasonable range (e.g., 30-50%), provide the result with a 95% confidence interval.
- **Divergence**: If methods differ by $>5\times$, trigger an **Explosion Warning**. Re-evaluate ACV and customer count assumptions.

## 4. Output Formatting
Present numbers in a table followed by a Monte Carlo simulation summary:
- **Low Case**: 25th percentile.
- **Base Case**: 50th percentile.
- **High Case**: 75th percentile.
