import manim as mn
from scipy.special import beta
from functools import partial
from numpy import arange


def lamda_beta_dist(x: float, lamda: float) -> float | None:
    if lamda <= 0:
        return (1 - x) ** (-lamda) / beta(1, 1 - lamda)
    return (x) ** lamda / beta(1 + lamda, 1)


def plot_distribution(
    lamda: float, scene: mn.Scene, ax: mn.Axes, label: mn.MathTex
) -> None:
    graph = ax.plot(
        partial(lamda_beta_dist, lamda=lamda),
        x_range=(0, 1),
        color=mn.BLACK,
        use_smoothing=True,
    )
    scene.add(graph)
    scene.wait(0.1)
    scene.remove(graph)
    label[1].become(mn.Tex(f"{lamda:.2f}", color=mn.BLACK).next_to(label[0]))


values_x = {0: r"\theta_1", 1: r"\theta_2"}


class CustomAxes(mn.Axes):
    def add_custom_labels(self, labels: dict):
        self.x_axis_labels = mn.VGroup()
        for x_val, x_tex in labels.items():
            tex = mn.MathTex(x_tex, color=mn.BLACK).next_to(
                self.x_axis.n2p(x_val), mn.DOWN
            )
            self.x_axis.add(tex)


class ThreePar(mn.Scene):
    def construct(self):
        ax = CustomAxes(
            x_range=(-0.25, 1.25),
            y_range=(-0.5, 2.5),
            axis_config={"color": mn.BLACK},
            x_axis_config={"include_ticks": True},
            y_axis_config={"include_ticks": False},
            tips=True,
        )
        ax.x_axis.add_labels({0: r"$\theta_2$", 1: r"$\theta_1$"})

        label = mn.MathTex(r"\lambda = ", r"4.00",
                           color=mn.BLACK).to_edge(mn.UP)

        self.add(ax, label)
        for lamda in arange(-4, 4, 0.1):
            plot_distribution(lamda, self, ax, label)
        for lamda in arange(-4, 4, 0.1):
            plot_distribution(-lamda, self, ax, label)
