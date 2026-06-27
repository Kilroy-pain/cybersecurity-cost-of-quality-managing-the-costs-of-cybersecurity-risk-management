The paper focuses on mapping cybersecurity costs to a quality cost model. Since this is a conceptual paper, there is no direct algorithm or computational model provided. However, I can implement a Python script that simulates the categorization and calculation of cybersecurity costs based on the quality cost model (e.g., prevention, appraisal, internal failure, external failure). This script will allow organizations to input cost data and categorize them accordingly.

```python
import numpy as np
import torch

class CybersecurityCostModel:
    def __init__(self):
        self.cost_categories = {
            "prevention": [],
            "appraisal": [],
            "internal_failure": [],
            "external_failure": []
        }

    def add_cost(self, category, cost):
        if category not in self.cost_categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.cost_categories.keys())}")
        self.cost_categories[category].append(cost)

    def calculate_total_costs(self):
        total_costs = {category: sum(costs) for category, costs in self.cost_categories.items()}
        return total_costs

    def calculate_percentage_distribution(self):
        total_cost = sum(sum(costs) for costs in self.cost_categories.values())
        if total_cost == 0:
            return {category: 0 for category in self.cost_categories}
        percentage_distribution = {category: (sum(costs) / total_cost) * 100 for category, costs in self.cost_categories.items()}
        return percentage_distribution

if __name__ == '__main__':
    # Initialize the model
    model = CybersecurityCostModel()

    # Dummy data for testing
    np.random.seed(42)
    torch.manual_seed(42)

    # Add random costs to each category
    for _ in range(10):
        model.add_cost("prevention", np.random.randint(100, 500))
        model.add_cost("appraisal", np.random.randint(50, 300))
        model.add_cost("internal_failure", np.random.randint(200, 600))
        model.add_cost("external_failure", np.random.randint(300, 800))

    # Calculate total costs
    total_costs = model.calculate_total_costs()
    print("Total Costs by Category:")
    for category, cost in total_costs.items():
        print(f"{category}: ${cost:.2f}")

    # Calculate percentage distribution
    percentage_distribution = model.calculate_percentage_distribution()
    print("\nPercentage Distribution of Costs:")
    for category, percentage in percentage_distribution.items():
        print(f"{category}: {percentage:.2f}%")