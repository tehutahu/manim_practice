from itertools import combinations

from manim import *


class Triangle(Scene):
    def construct(self):
        dots = VGroup(
            *[
                Dot().shift(
                    UP * np.random.uniform(-3, 3)
                    + RIGHT * np.random.uniform(-5, 5)
                )
                for _ in range(3)
            ]
        )

        labels = VGroup(
            *[
                Tex(f"{l}").add_updater(
                    lambda mob, i=i: mob.next_to(dots[i], UP)
                )
                for i, l in enumerate(("X", "Y", "Z"))
            ]
        )

        lines = VGroup(
            *[
                Line().add_updater(
                    lambda mob, i=i, j=j: mob.become(
                        Line(
                            start=dots[i].get_center(),
                            end=dots[j].get_center(),
                        )
                    )
                )
                for i, j in combinations(range(len(dots)), 2)
            ]
        )

        circle = Circle().add_updater(
            lambda mob: mob.become(
                Circle.from_three_points(*[dot.get_center() for dot in dots])
            )
        )

        self.play(Create(dots, lag_ratio=0.5))
        self.wait()
        self.play(Create(lines))
        self.wait()
        self.play(FadeIn(labels, shift=UP))
        self.wait()
        self.play(Create(circle))
        self.wait()
        self.play(dots[1].animate.shift(LEFT), dots[2].animate.shift(UP))
        self.wait()
        self.play(FadeOut(VGroup(dots, labels, lines, circle)))
