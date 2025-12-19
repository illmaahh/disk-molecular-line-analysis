import pandas as pd
import matplotlib.pyplot as plt

print("Loading molecular line data...")

df = pd.read_csv("data/molecular_lines.csv")
print(df)

stats = df.describe()
stats.to_csv("results/statistics_summary.csv")

molecules = [
    "C18O_flux",
    "C2H_flux",
    "CN_flux",
    "HCN_flux",
    "HCO_plus_flux"
]

for mol in molecules:
    plt.figure()
    plt.scatter(df["disk_mass"], df[mol])
    plt.xlabel("Disk Mass")
    plt.ylabel(mol)
    plt.title(f"{mol} vs Disk Mass")
    plt.savefig(f"figures/{mol}_vs_disk_mass.png")
    plt.show()

print("Analysis completed successfully")
from config import set_style
from data_loader import load_data
from analysis import compute_statistics
from visualization import static_plot, animated_plot, interactive_plot

def main():
    set_style()

    df = load_data()
    stats = compute_statistics(df)
    stats.to_csv("results/statistics_summary.csv")

    static_plot(df)
    animated_plot(df)
    interactive_plot(df)

    print("Project completed successfully")

if __name__ == "__main__":
    main()
