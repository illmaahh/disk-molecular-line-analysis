import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px

def static_plot(df):
    plt.scatter(df["disk_mass"], df["C18O_flux"])
    plt.xlabel("Disk Mass")
    plt.ylabel("C18O Flux")
    plt.title("C18O Flux vs Disk Mass")
    plt.tight_layout()
    plt.savefig("figures/static_summary.png")
    plt.show()

def animated_plot(df):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 0.1)
    ax.set_ylim(0, 2)
    ax.set_xlabel("Disk Mass")
    ax.set_ylabel("Molecular Flux")
    ax.set_title("Animated Molecular Line Trends")

    scat = ax.scatter([], [])

    molecules = [
        "C18O_flux", "C2H_flux", "CN_flux", "HCN_flux", "HCO_plus_flux"
    ]

    def update(frame):
        scat.set_offsets(list(zip(df["disk_mass"], df[molecules[frame]])))
        ax.set_title(f"{molecules[frame]} vs Disk Mass")
        return scat,

    ani = animation.FuncAnimation(
        fig, update, frames=len(molecules), interval=1200
    )

    ani.save("figures/animated_disk_analysis.gif", writer="pillow")
    plt.show()

def interactive_plot(df):
    fig = px.scatter(
        df,
        x="disk_mass",
        y="C18O_flux",
        title="Interactive Disk Chemistry Explorer",
        labels={
            "disk_mass": "Disk Mass",
            "C18O_flux": "C18O Flux"
        }
    )
    fig.show()
