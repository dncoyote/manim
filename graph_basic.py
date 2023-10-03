from manim import *


class GraphAnimation(Scene):
    def construct(self):
        pass
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 5],
            axis_config={"color": BLUE},
        )

        graph = axes.plot(lambda x: x**2, color=WHITE)

        self.play(Create(axes), Create(graph))
        self.wait(2)
