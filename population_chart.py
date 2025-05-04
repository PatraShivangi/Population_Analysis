import matplotlib.pyplot as plt
import seaborn as sns

#Population Data (2025 estimates in millions).
countries = ["India", "China", "USA", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh"]
population = [1420, 1412, 331, 280, 216, 240, 223, 170]  
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Bar Chart
sns.barplot(x=countries, y=population, palette="magma", ax=axs[0])
axs[0].set_xlabel("Countries", fontsize=12)
axs[0].set_ylabel("Population (millions)", fontsize=12)
axs[0].set_title("Population Comparison (2025)", fontsize=14)
axs[0].tick_params(axis='x', rotation=45)
axs[0].grid(axis='y', linestyle="--", alpha=0.7)
for i, pop in enumerate(population):
    axs[0].text(i, pop + 10, f"{pop}M", ha="center", fontsize=10, color="black", fontweight="bold")

# Histogram
axs[1].hist(population, bins=6, color="skyblue", edgecolor="black", alpha=0.75)
axs[1].set_xlabel("Population (millions)", fontsize=12)
axs[1].set_ylabel("Frequency", fontsize=12)
axs[1].set_title("Population Distribution (2025)", fontsize=14)
axs[1].grid(axis='y', linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
