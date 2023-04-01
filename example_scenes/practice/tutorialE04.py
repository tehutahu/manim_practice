from manim import *


class AllUpdaterTypes(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(start=ORIGIN, end=RIGHT).next_to(red_dot, LEFT)
        pointer.add_updater(  # place arrow left of dot
            lambda mob: mob.next_to(red_dot, LEFT)
        )

        def shifter(mob, dt):  # make dot move 2 munits RIGHT/sec
            mob.shift(2 * dt * RIGHT)

        red_dot.add_updater(shifter)

        def scene_scaler(dt):  # scale mobjects depending on distance to ORIGIN
            for mob in self.mobjects:
                mob.set(width=2 / (1 + np.linalg.norm(mob.get_center())))

        self.add_updater(scene_scaler)

        self.add(red_dot, pointer)
        self.update_self(0)
        self.wait(1)
        self.play(red_dot.animate.shift(UP))
        self.wait(3)


class UpdaterAndAnimation(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        rotating_square = Square()
        rotating_square.add_updater(lambda mob, dt: mob.rotate(0.5 * PI * dt))

        def shifter(mob, dt):
            mob.shift(2 * dt * RIGHT)

        red_dot.add_updater(shifter)

        self.add(red_dot, rotating_square)
        self.wait(1)
        red_dot.suspend_updating()
        self.wait(1)
        self.play(
            red_dot.animate.shift(UP),
            rotating_square.animate.move_to([-2, -2, 0]),
        )
        self.wait(1)


class ValueTrackerPlot(Scene):
    def construct(self):
        def sigmoid(x):
            return 1 / (1 + np.exp(a.get_value() * -x))

        a = ValueTracker(1)
        ax = Axes(x_range=[-4, 4, 1], y_range=[-1.5, 1.5, 1],)
        parabola = ax.plot(sigmoid, color=RED)
        parabola.add_updater(
            lambda mob: mob.become(ax.plot(sigmoid, color=RED))
        )
        a_number = DecimalNumber(
            number=a.get_value(),
            num_decimal_places=3,
            show_ellipsis=True,
            color=RED,
        )
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(parabola, RIGHT)
        )
        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))
