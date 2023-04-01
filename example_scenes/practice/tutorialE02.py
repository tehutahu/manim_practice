from manim import *


class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        # next_to from episode 01
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)  # RIGHT == [1, 0, 0]
        self.add(red_dot, green_dot)

        # shift
        s = Square(color=ORANGE)
        s.shift(2 * UP + 4 * RIGHT)
        self.add(s)

        # move_to
        c = Circle(color=PURPLE)
        c.move_to([-3, -2, 0])
        self.add(c)

        # align_to
        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)  # type: ignore
        c4 = c2.copy().set_color(ORANGE)  # type: ignore
        c2.align_to(s, UP)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UR)
        self.add(c2, c3, c4)


class CriticalPoints(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0, 0, 0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity=0.5)
        s.move_to([1, 0, 0], aligned_edge=UL)
        s_text = Text(
            "(1,0) aligned_edge=UL",
            fill_opacity=0.8,
            font_size=DEFAULT_FONT_SIZE // 3,
        )
        s_text.next_to(s, DOWN)
        self.add(s, s_text)


from manim.utils.unit import Percent, Pixels


class UsefullUnits(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        for perc in range(5, 51, 5):
            self.add(Circle(radius=perc * Percent(axis=X_AXIS)))
            self.add(
                Square(
                    side_length=2 * perc * Percent(axis=X_AXIS), color=YELLOW
                )
            )

        # different potision for rendering Pixels, in other words `--quality` option
        d = Dot()
        d.shift(100 * Pixels * RIGHT)
        self.add(d)


class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, green_dot, blue_dot)
        dot_group.to_edge(edge=RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(direction=UP, buff=0.5)
        self.add(circles)

        stars = VGroup(
            *[
                Star(color=YELLOW, fill_opacity=0.8).scale(0.5)
                for _ in range(20)
            ]
        )
        stars.arrange_in_grid(rows=4, cols=5, buff=0.2)
        self.add(stars)


config.background_color = DARK_BLUE
# config.frame_width = 16
# config.frame_height = 9

# config.pixel_width = 1920
# config.pixel_height = 1080


class SimpleScene(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(-8, 8), y_range=(-4.5, 4.5))
        t1 = Triangle(color=PURPLE, fill_opacity=0.8)
        self.add(plane, t1)


config.background_color = BLACK


class ChangeDefault(Scene):
    def construct(self):
        # Setting
        Text.set_default(color=GREEN)
        t1 = Text("Hello World", font_size=100)

        # overwrite
        t2 = Text("Good Bye!", color=RED).next_to(t1, DOWN)

        # Default
        Text.set_default()
        t3 = Text("See you!").next_to(t2, DOWN)
        self.add(t1, t2, t3)
