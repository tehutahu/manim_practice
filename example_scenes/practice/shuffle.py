import math
import random

from manim import *


class RandomShulle(Scene):
    def create_circles(self, n_circle: int):
        circles = VGroup(
            *[
                Circle(radius=0.5, color=WHITE, fill_opacity=0.8)
                for _ in range(n_circle)
            ]
        ).arrange(RIGHT, buff=0.5)
        return circles

    def construct(self):
        n_circle = 10
        circles = self.create_circles(n_circle)

        target = circles[random.randint(0, n_circle - 1)]
        self.play(DrawBorderThenFill(circles))
        self.play(Indicate(target, color=ORANGE))
        self.wait()

        n_shuffle = 15
        speed_start = 1
        speed_end = 0.2
        array = np.arange(n_circle)
        for n in range(n_shuffle):
            speed = speed_start - (speed_start - speed_end) / n_shuffle * n
            i, j = np.random.permutation(array)[:2]
            self.play(
                Swap(circles[i], circles[j], path_arc=135 * DEGREES),
                run_time=speed,
            )
        self.wait()
        self.play(Indicate(target))
        self.wait()


class RandomShuffleGrid(RandomShulle):
    def create_circles(self, n_circle: int):
        return (
            super()
            .create_circles(n_circle)
            .arrange_in_grid(rows=math.ceil(n_circle / 5), cols=5)
        )

