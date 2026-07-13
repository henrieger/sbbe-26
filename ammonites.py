import manim as mn
import numpy as np
import scipy as sp

ab = 7
n = 10


class Ammonites(mn.Scene):
    def construct(self) -> None:
        ax = mn.Axes(
            x_range=[-0.2, 1.2],
            x_axis_config={
                "color": mn.BLACK,
                "include_ticks": False,
                "stroke_width": 2 * mn.DEFAULT_STROKE_WIDTH,
            },
            y_axis_config={"color": mn.WHITE, "include_ticks": False},
        )
        graph = ax.plot(
            sp.stats.beta(ab, ab).pdf,
            x_range=[0, 1],
            color=mn.DARK_BLUE,
            stroke_width=2 * mn.DEFAULT_STROKE_WIDTH,
        )

        theta_1_location = ax.x_axis.n2p(0)
        theta_1_label = mn.MathTex(r"\theta_1", color=mn.BLACK).next_to(
            theta_1_location, mn.DOWN
        )
        theta_1_tick = mn.Line(
            theta_1_location + mn.UP * 0.2,
            theta_1_location + mn.DOWN * 0.2,
            color=mn.BLACK,
        )

        theta_2_location = ax.x_axis.n2p(1)
        theta_2_label = mn.MathTex(r"\theta_2", color=mn.BLACK).next_to(
            theta_2_location, mn.DOWN
        )
        theta_2_tick = mn.Line(
            theta_2_location + mn.UP * 0.2,
            theta_2_location + mn.DOWN * 0.2,
            color=mn.BLACK,
        )

        self.add(ax, graph, theta_1_tick, theta_1_label, theta_2_tick, theta_2_label)

        np.random.seed(2001)
        data = np.random.beta(ab, ab, 10)
        for datum in data:
            self.add(
                mn.ImageMobject("assets/ammonite.png")
                .move_to(ax.x_axis.n2p(datum))
                .scale(0.02)
            )

        fad_location = ax.x_axis.n2p(min(data))
        fad_label = (
            mn.Text("FAD", color=mn.BLACK)
            .next_to(fad_location, mn.DOWN)
            .shift(mn.DOWN)
            .scale(0.5)
        )
        fad_arrow = mn.Arrow(
            fad_label.get_edge_center(mn.UP), fad_location, color=mn.BLACK
        )

        lad_location = ax.x_axis.n2p(max(data))
        lad_label = (
            mn.Text("LAD", color=mn.BLACK)
            .next_to(lad_location, mn.DOWN)
            .shift(mn.DOWN)
            .scale(0.5)
        )
        lad_arrow = mn.Arrow(
            lad_label.get_edge_center(mn.UP), lad_location, color=mn.BLACK
        )

        self.add(fad_label, lad_label, fad_arrow, lad_arrow)
