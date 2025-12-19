import matplotlib.pyplot as plt

def set_style():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "figure.figsize": (7, 5),
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 12,
        "savefig.dpi": 300
    })
