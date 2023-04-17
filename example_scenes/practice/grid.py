from manim import *


class grid_mask(Scene):
    def construct(self):
        def create_square(side_length, text):
            sq = Square(side_length=side_length)
            text = Text(text).move_to(sq)
            return VGroup(sq, text)
        
        squares = VGroup(*[create_square(1, f'{i}') for i in range(9)]).arrange_in_grid(buff=0).set(height=3)
        targets = squares.copy()
        gr = VGroup(squares, targets).arrange(buff=1)
        index_tracker = ValueTracker(0)
        
        sq = Square(side_length=squares[0].height, color=BLUE)
        sq_copy = sq.copy()
        sq.add_updater(lambda m: m.move_to(squares[int(index_tracker.get_value())]))
        sq_copy.add_updater(lambda m: m.move_to(targets[int(index_tracker.get_value())]))

        masks = VGroup(*[Square(color=BLACK, fill_opacity=1, stroke_width=DEFAULT_STROKE_WIDTH+0.5) for _ in range(len(targets))]).arrange_in_grid(buff=0).move_to(targets).set(height=3)
        masks.add_updater(lambda m: m.set_opacity(1))
        masks.add_updater(lambda m: m[:int(index_tracker.get_value()) + 1].set_opacity(0))
        mask_first = masks[0].copy()
        
        self.add(targets, mask_first, masks)
        self.play(FadeIn(squares))
        self.play(
            AnimationGroup(
                Create((VGroup(sq, sq_copy))),
                mask_first.animate.set_opacity(0),
                lag_ratio=0.5
            ),
        )
        ex1 = squares[0].copy()
        ex2 = targets[0].copy()
        ex1.save_state()
        ex2.save_state()
        
        self.play(
            Succession(
                AnimationGroup(
                    ex1.animate.shift(UP).scale(3),
                    ex2.animate.shift(UP).scale(3),
                ),
                AnimationGroup(
                    Indicate(ex1),
                    Indicate(ex2),
                ),
                AnimationGroup(
                    ex1.animate.restore(),
                    ex2.animate.restore(),
                ),
            )
        )
        self.remove(ex1, ex2)
        self.wait()
        self.play(index_tracker.animate.set_value(8), run_time=3)
        self.wait()


class ImageGridMask(Scene):
    def construct(self):
        def create_img():
            img = ImageMobject(np.uint8(
                [
                    [63, 0, 0, 0],
                    [0, 127, 0, 0],
                    [0, 0, 191, 0],
                    [0, 0, 0, 255]
                ]))
            return img
        
        squares = Group(*[create_img() for i in range(9)]).arrange_in_grid(buff=0).set(height=3)
        targets = Group(*[create_img().set_opacity(0) for i in range(9)]).arrange_in_grid(buff=0).set(height=3)
        gr = Group(squares, targets).arrange()
        
        index_tracker = ValueTracker(0)
        
        sq = Square(side_length=squares[0].height, color=BLUE, z_index=99)
        sq_copy = sq.copy()
        sq.add_updater(lambda m: m.move_to(squares[int(index_tracker.get_value())]))
        sq_copy.add_updater(lambda m: m.move_to(targets[int(index_tracker.get_value())]))

        targets.add_updater(lambda m: [sub.set_opacity(0) for sub in m])
        targets.add_updater(lambda m: [sub.set_opacity(1) for sub in m[:int(index_tracker.get_value()) + 1]])
        
        self.play(FadeIn(squares))
        self.play(
            Succession(
                Create((VGroup(sq, sq_copy))),
                FadeIn(targets),
            )
        )
        ex1 = squares[0].copy()
        ex2 = targets[0].copy()
        ex1.save_state()
        ex2.save_state()
        
        self.play(
            Succession(
                AnimationGroup(
                    ex1.animate.shift(UP).scale(3),
                    ex2.animate.shift(UP).scale(3),
                ),
                AnimationGroup(
                    Indicate(ex1),
                    Indicate(ex2),
                ),
                AnimationGroup(
                    ex1.animate.restore(),
                    ex2.animate.restore(),
                ),
            )
        )
        self.remove(ex1, ex2)
        self.wait()
        self.play(index_tracker.animate.set_value(8), run_time=3)
        self.wait()
