from typing import Callable
import manim as mn
from scipy.special import beta
from functools import partial
from numpy import arange

theta_1 = 1
theta_2 = 0.2


def threepar_beta_dist(
    x: float, theta_1: float, theta_2: float, lamda: float
) -> float | None:
    if lamda <= 0:
        return (theta_1 - x) ** (-lamda) / (
            (theta_1 - theta_2) ** (1 - lamda) * beta(1, 1 - lamda)
        )
    return (x - theta_2) ** lamda / (
        (theta_1 - theta_2) ** (1 + lamda) * beta(1 + lamda, 1)
    )


def fourpar_beta_dist(x: float, theta_1: float, theta_2: float, a: float, b: float):
    return (
        (x - theta_2) ** (a - 1)
        * (theta_1 - x) ** (b - 1)
        / ((theta_1 - theta_2) ** (a + b - 1) * beta(a, b))
    )


def plot_distribution(
    func: Callable[[float]],
    lamda: float,
    scene: mn.Scene,
    ax: mn.Axes,
    label: mn.MathTex,
) -> None:
    graph = ax.plot(
        func,
        x_range=(theta_2, theta_1),
        color=mn.BLUE_A,
        use_smoothing=True,
        stroke_width=2 * mn.DEFAULT_STROKE_WIDTH,
    )
    line_1 = mn.DashedLine(ax.x_axis.n2p(theta_1), graph[-1], color=mn.BLUE_E)
    line_2 = mn.DashedLine(ax.x_axis.n2p(theta_2), graph[0], color=mn.BLUE_E)
    scene.add(graph, line_1, line_2)
    scene.wait(0.1)
    scene.remove(graph, line_1, line_2)
    label[1].become(mn.Tex(f"{lamda:.2f}", color=mn.BLACK).next_to(label[0]))


class ThreePar(mn.Scene):
    def construct(self):
        ax = mn.Axes(
            x_range=(0, 1.2 * theta_1),
            y_range=(0, 2.5 / (theta_1 - theta_2)),
            axis_config={"color": mn.BLACK},
            x_axis_config={"include_ticks": False, "length": 2},
            y_axis_config={"include_ticks": False},
            tips=True,
        )
        theta_1_location = ax.x_axis.n2p(theta_1)
        theta_1_label = mn.MathTex(r"\theta_1", color=mn.BLACK).next_to(
            theta_1_location, mn.DOWN
        )
        theta_1_tick = mn.Line(
            theta_1_location + mn.UP * 0.2,
            theta_1_location + mn.DOWN * 0.2,
            color=mn.BLACK,
        )

        theta_2_location = ax.x_axis.n2p(theta_2)
        theta_2_label = mn.MathTex(r"\theta_2", color=mn.BLACK).next_to(
            ax.x_axis.n2p(theta_2), mn.DOWN
        )
        theta_2_tick = mn.Line(
            theta_2_location + mn.UP * 0.2,
            theta_2_location + mn.DOWN * 0.2,
            color=mn.BLACK,
        )

        label = mn.MathTex(r"\lambda = ", r"4.00", color=mn.BLACK).to_edge(mn.UP)

        self.add(ax, label, theta_1_label, theta_1_tick, theta_2_label, theta_2_tick)
        for lamda in arange(-4, 4, 0.1):
            plot_distribution(
                partial(
                    threepar_beta_dist,
                    lamda=lamda,
                    theta_1=theta_1,
                    theta_2=theta_2,
                ),
                lamda,
                self,
                ax,
                label,
            )
        for lamda in arange(-4, 4, 0.1):
            plot_distribution(
                partial(
                    threepar_beta_dist,
                    lamda=-lamda,
                    theta_1=theta_1,
                    theta_2=theta_2,
                ),
                -lamda,
                self,
                ax,
                label,
            )
