from random import uniform

from manim import *


class SequenceSort(Scene):
    def check_and_swap(self, b1: Mobject, b2: Mobject, run_time=1.0):
        p = b1.get_edge_center(DOWN)
        b1.set_color(YELLOW)
        b2.set_color(YELLOW)
        self.wait(0.15)
        if b1.height > b2.height:
            self.play(
                b1.animate.stretch_to_fit_height(b2.height).align_to(p, DOWN),
                b2.animate.stretch_to_fit_height(b1.height).align_to(p, DOWN),
                run_time=run_time,
            )
        else:
            self.wait(run_time)
        b1.set_color(WHITE)
        b2.set_color(WHITE)

    def sort(self, bars: Mobject):
        self.bubble_sort(bars)

    def bubble_sort(self, bars: Mobject):
        end = len(bars)
        speed_first = 2
        speed_second = 0.2
        for i in range(end - 1, 0, -1):
            if i == 0:
                speed = speed_first
            else:
                speed = speed_second
            for j in range(i):
                self.check_and_swap(bars[j], bars[j + 1], run_time=speed)

    def construct(self):
        title = Tex(r"Bubble \,Sort").to_edge(UP)
        self.play(Write(title))

        n_bars = 10
        bars = VGroup(
            *[
                Square(
                    side_length=0.2, color=WHITE, fill_opacity=0.8
                ).stretch_to_fit_height(uniform(1.0, 5.0))
                for _ in range(n_bars)
            ]
        ).arrange()
        [bar.align_to([0, -2, 0], DOWN) for bar in bars]

        self.play(DrawBorderThenFill(bars))
        self.wait()
        self.sort(bars)
        self.wait()

