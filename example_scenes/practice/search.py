from manim import *


class BinarySearch(Scene):
    def __init__(self):
        super().__init__()
        self.values = sorted(
            np.random.randint(low=0, high=30, size=12, dtype=np.uint8)
        )
        target_idx = 3
        self.target = self.values[target_idx]

    def binary_search(self):
        i, j = 0, len(self.values) - 1
        k = (i + j) // 2
        yield (i, j, k)

        while i < j:
            if self.values[k] == self.target:
                i = j = k
                break
            elif self.values[k] < self.target:
                i = k
            else:
                j = k
            k = (i + j) // 2
            yield (i, j, k)
        yield (i, j, k)

    def construct(self):
        title = Tex(f"Target: {self.target}").to_edge(UP)

        squares = VGroup(
            *[Square().scale(0.5) for _ in range(len(self.values))]
        ).arrange()
        labels = VGroup(*[Tex(f"{v}") for v in self.values])
        for i in range(len(labels)):
            labels[i].add_updater(
                lambda mob, i=i: mob.move_to(squares[i].get_center())
            )

        self.play(
            AnimationGroup(
                AnimationGroup(Write(squares), Write(labels)),
                Write(title),
                lag_ratio=0.8,
            )
        )
        self.wait()

        # initialize arrows
        bs = iter(self.binary_search())
        i, j, k = next(bs)
        arrow_i = (
            Arrow(start=DOWN, end=UP).scale(0.7).next_to(squares[i], DOWN)
        )
        arrow_j = (
            Arrow(start=DOWN, end=UP).scale(0.7).next_to(squares[j], DOWN)
        )
        arrow_k = (
            Arrow(start=DOWN, end=UP, color=ORANGE)
            .scale(0.7)
            .next_to(squares[k], DOWN)
        )
        self.play(
            AnimationGroup(
                AnimationGroup(Write(arrow_i), Write(arrow_j)),
                Write(arrow_k),
                lag_ratio=0.5,
            )
        )

        for i, j, k in bs:
            self.play(
                arrow_i.animate.next_to(squares[i], DOWN),
                arrow_j.animate.next_to(squares[j], DOWN),
                arrow_k.animate.set_opacity(0),
            )
            if i == j == k:
                self.play(
                    VGroup(squares[k], labels[k]).animate.set_color(GREEN)
                )
            else:
                self.play(
                    arrow_k.animate.set_opacity(1).next_to(squares[k], DOWN),
                )
        self.wait()
