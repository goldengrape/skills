# Data Strategy: From "Big Data" to "Deep Data"

For early-stage startups, data is scarce and noisy. The Intelligent Technical Advisor prioritizes information density and creative data acquisition.

## The "Deep Data" Philosophy
- **Information Density**: Focus on high-quality, domain-specific data that provides unique insights.
- **Expert Injection**: Combine deep domain knowledge (e.g., botany for agriculture, clinical expertise for health-tech) with data science.
- **Data Foundations**: Establish robust data schemas and collection early, as this is the prerequisite for AI maturity.

## Solving the "Cold Start" Problem

### Synthetic Data & Augmentation
- **GANs**: Use Generative Adversarial Networks to create realistic synthetic samples, especially for rare edge cases (e.g., semiconductor defect patterns).
- **SMOTified-GAN**: A hybrid strategy that combines oversampling with GANs to better define decision boundaries in imbalanced datasets.
- **Basic Augmentation**: Simple geometric transforms (rotation, scaling) and algorithms like "Flood Fill" for image data expansion.

### Transfer & Meta-Learning
- **Transfer Learning**: Fine-tune large pre-trained models (Foundation Models) on small, domain-specific datasets.
- **Meta-Learning (MAML)**: Use Model-Agnostic Meta-Learning for few-shot learning, enabling the system to adapt to new tasks with minimal data.

### Product-Led Data Collection
- **Rules First**: Implement rule-based features initially to capture user behavior data before deploying complex AI.
- **Incentive Design**: Build product loops that naturally encourage users to contribute or label data.
- **"Sense-Decide-Act" Loops**: Build closed-loop systems (like Blue River Technology) where the product's operation continuously generates new training data.
