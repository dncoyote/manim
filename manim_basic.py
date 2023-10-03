from manim import *


class Test(Scene):
    def construct(self):
        c = Circle(2, color=RED, fill_opacity=0.1)

        self.play(DrawBorderThenFill(c), run_time=0.5)

        title = Text("Manim", font_size=72, slant="ITALIC").shift(UP * 0.3)
        subtitle = Text("Basics", slant="ITALIC").shift(DOWN * 0.3)
        self.play(Write(title), Write(subtitle))

        a = Arc(2.2, TAU * 1 / 4, color=BLUE, stroke_width=15)
        self.play(Create(a))

        self.wait(3)
