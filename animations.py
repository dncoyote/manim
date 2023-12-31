from manim import * 
import numpy as np

class AllAnimations(Scene):
    def construct(self):
        text = Text("Animations").shift(UP*2.5)
        self.play(Write(text))
        self.wait(1)

        self.play(Transform(text,Text("Create").shift(UP*2.5)), run_time=0.5)
        start = Star()
        self.play(Create(start))
        self.play(Transform(text,Text("Uncreate").shift(UP*2.5)), run_time=0.5)
        self.play(Uncreate(start))
        
        self.play(Transform(text,Text("AnimatedBoundary").shift(UP*2.5)), run_time=0.5)
        circle = Circle()
        animated_boundary = AnimatedBoundary(circle, cycle_rate=3, colors=[RED, GREEN, BLUE])
        self.add(circle, animated_boundary)
        self.wait(2)
        self.remove(circle, animated_boundary)

        self.play(Transform(text,Text("TracedPath").shift(UP*2.5)), run_time=0.5)
        dot = Dot(color=RED)
        trace = TracedPath(dot.get_center)
        self.add(dot, trace)
        self.wait(0.5)
        self.play(dot.animate.shift(UP), run_time=0.5)
        self.play(dot.animate.shift(LEFT), run_time=0.5)
        self.play(dot.animate.shift(DOWN+RIGHT), run_time=0.5)
        self.remove(dot, trace)
        
        self.play(Transform(text,Text("AddTextLetterByLetter").shift(UP*2.5)), run_time=0.5)
        some_text = Text("Here is a text")
        self.play(AddTextLetterByLetter(some_text))
        self.play(Transform(text,Text("RemoveTextLetterByLetter").shift(UP*2.5)), run_time=0.5)
        self.play(RemoveTextLetterByLetter(some_text))

        self.play(Transform(text,Text("Write").shift(UP*2.5)), run_time=0.5)
        some_text = Text("Here is more text")
        self.play(Write(some_text))
        self.play(Transform(text,Text("Unwrite").shift(UP*2.5)), run_time=0.5)
        self.play(Unwrite(some_text))
        self.remove(some_text)

        self.play(Transform(text,Text("DrawBorderThenFill").shift(UP*2.5)), run_time=0.5)
        square = Square(color=BLUE, fill_opacity=1).set_fill(YELLOW)
        self.play(DrawBorderThenFill(square))
        self.remove(square)

        self.play(Transform(text,Text("ShowIncreasingSubsets").shift(UP*2.5)), run_time=0.5)
        circles = VGroup(
            Circle().shift(UP*0.5),
            Circle().shift((DOWN+LEFT)*0.5),
            Circle().shift((DOWN+RIGHT)*0.5)
        )
        self.play(ShowIncreasingSubsets(circles))
        self.wait()
        self.remove(circles)

        self.play(Transform(text,Text("ShowSubmobjectsOneByOne").shift(UP*2.5)), run_time=0.5)
        circles2 = VGroup(
            Circle().shift(UP*0.5),
            Circle().shift((DOWN+LEFT)*0.5),
            Circle().shift((DOWN+RIGHT)*0.5)
        )
        self.play(ShowSubmobjectsOneByOne(circles2))
        self.play(Uncreate(circles2))

        self.play(Transform(text,Text("FadeIn").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(FadeIn(square))
        self.play(Transform(text,Text("FadeOut").shift(UP*2.5)), run_time=0.5)
        self.play(FadeOut(square))
        self.remove(square)

        self.play(Transform(text,Text("GrowArrow").shift(UP*2.5)), run_time=0.5)
        arrow = Arrow()
        self.play(GrowArrow(arrow))
        self.remove(arrow)

        self.play(Transform(text,Text("GrowFromCenter").shift(UP*2.5)), run_time=0.5)
        triangle = Triangle()
        self.play(GrowFromCenter(triangle))
        self.remove(triangle)

        self.play(Transform(text,Text("GrowFromEdge - DOWN").shift(UP*2.5)), run_time=0.5)
        squares = [Square() for _ in range(4)]
        self.play(GrowFromEdge(squares[0], DOWN))
        self.play(Transform(text,Text("GrowFromEdge - RIGHT").shift(UP*2.5)), run_time=0.5)
        self.play(GrowFromEdge(squares[1], RIGHT))
        self.play(Transform(text,Text("GrowFromEdge - UP").shift(UP*2.5)), run_time=0.5)
        self.play(GrowFromEdge(squares[2], UP))
        self.play(Transform(text,Text("GrowFromEdge - LEFT").shift(UP*2.5)), run_time=0.5)
        self.play(GrowFromEdge(squares[3], LEFT))
        self.remove(*squares)

        self.play(Transform(text,Text("GrowFromPoint").shift(UP*2.5)), run_time=0.5)
        dot = Dot().shift(UP+RIGHT*2)
        star = Star()
        self.add(dot)
        self.wait(0.5)
        self.play(GrowFromPoint(star, dot))
        self.remove(dot, star)

        self.play(Transform(text,Text("SpinInFromNothing").shift(UP*2.5)), run_time=0.5)
        triangle = Triangle()
        self.play(SpinInFromNothing(triangle))
        self.remove(triangle)

        self.play(Transform(text,Text("ApplyWave").shift(UP*2.5)), run_time=0.5)
        some_text = Text("Mathematical Animations")
        self.play(ApplyWave(some_text))
        self.play(ApplyWave(some_text, direction=RIGHT))
        self.remove(some_text)

        self.play(Transform(text,Text("Circumscribe").shift(UP*2.5)), run_time=0.5)
        some_text = Text("Look Here")
        self.add(some_text)
        self.play(Circumscribe(some_text))
        self.play(Circumscribe(some_text, Circle))
        self.remove(some_text)

        self.play(Transform(text,Text("Flash").shift(UP*2.5)), run_time=0.5)
        some_text = Text("Ta Da").set_color(YELLOW)
        self.add(some_text)
        self.play(Flash(some_text))
        self.remove(some_text)

        self.play(Transform(text,Text("FocusOn").shift(UP*2.5)), run_time=0.5)
        some_text = Text("Here!")
        self.add(some_text)
        self.play(FocusOn(some_text))
        self.remove(some_text)

        self.play(Transform(text,Text("Indicate").shift(UP*2.5)), run_time=0.5)
        some_text = Text("This is important")
        self.play(Indicate(some_text))
        self.remove(some_text)

        self.play(Transform(text,Text("Wiggle").shift(UP*2.5)), run_time=0.5)
        some_text = Text("THIS")
        self.play(Wiggle(some_text))
        self.remove(some_text)

        self.play(Transform(text,Text("ShowPassingFlash").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(ShowPassingFlash(square))
        self.remove(square)

        self.play(Transform(text,Text("ShowPassingFlashWithThinningStrokeWidth").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(ShowPassingFlashWithThinningStrokeWidth(square))
        self.remove(square)

        self.play(Transform(text,Text("MoveAlongPath").shift(UP*2.5)), run_time=0.5)
        l1 = Line(LEFT+DOWN, RIGHT+UP)
        self.add(l1)
        d1 = Dot().shift(LEFT+DOWN)
        self.play(Create(d1), run_time=0.5)
        self.play(MoveAlongPath(d1, l1), rate_func=linear)
        self.remove(l1,d1)

        self.play(Transform(text,Text("Rotate").shift(UP*2.5)), run_time=0.5)
        star = Star()
        self.play(Rotate(star))
        self.wait(0.5)
        self.remove(star)

        self.play(Transform(text,Text("Rotating").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(Rotating(square))
        self.wait(0.5)
        self.remove(square)

        self.play(Transform(text,Text("Broadcast").shift(UP*2.5)), run_time=0.5)
        triangle = Triangle()
        self.play(Broadcast(triangle))
        self.remove(triangle)

        self.play(Transform(text,Text("ChangeSpeed").shift(UP*2.5)), run_time=0.5)
        d = Dot().shift(LEFT)
        self.play(ChangeSpeed(d.animate.shift(RIGHT*2), speedinfo={0.3: 1, 0.4: 0.1, 0.6: 0.1, 1: 1}, rate_func=linear))
        self.remove(d)

        self.play(Transform(text,Text("Transform").shift(UP*2.5)), run_time=0.5)
        square = Square()
        star = Star()
        self.play(Transform(square,star))
        self.remove(square,star)
        
        self.play(Transform(text,Text("ClockwiseTransform").shift(UP*2.5)), run_time=0.5)
        square = Square()
        star = Star()
        self.play(ClockwiseTransform(square,star))
        self.remove(square,star)

        self.play(Transform(text,Text("CounterclockwiseTransform").shift(UP*2.5)), run_time=0.5)
        square = Square()
        star = Star()
        self.play(CounterclockwiseTransform(square,star))
        self.remove(square,star)

        self.play(Transform(text,Text("CyclicReplace").shift(UP*2.5)), run_time=0.5)
        square = Square()
        star = Star()
        circle = Circle()
        triangle = Triangle()
        vg = VGroup(square,star,circle,triangle)
        vg.arrange(RIGHT)
        self.play(CyclicReplace(*vg))
        self.wait()
        self.remove(square,star,circle,triangle)

        self.play(Transform(text,Text("FadeToColor").shift(UP*2.5)), run_time=0.5)
        square = Square(fill_opacity=1).set_fill(RED)
        self.play(FadeToColor(square,color=YELLOW))
        self.remove(square)

        self.play(Transform(text,Text("FadeTransform").shift(UP*2.5)), run_time=0.5)
        square = Square(fill_opacity=1).set_fill(BLUE)
        star = Star(fill_opacity=1).set_fill(YELLOW)
        self.play(FadeTransform(square,star))
        self.remove(square,star)

        self.play(Transform(text,Text("MoveToTarget").shift(UP*2.5)), run_time=0.5)
        circle = Circle().shift(LEFT)
        circle.generate_target()
        circle.move_to(RIGHT)
        self.play(MoveToTarget(circle))
        self.remove(circle)

        self.play(Transform(text,Text("ReplacementTransform").shift(UP*2.5)), run_time=0.5)
        circle = Circle().shift(LEFT)
        square = Square().shift(RIGHT)
        self.play(ReplacementTransform(circle,square))
        self.remove(circle,square)

        self.play(Transform(text,Text("Restore").shift(UP*2.5)), run_time=0.5)
        circle = Circle()
        square = Square(fill_opacity=1).set_fill(RED).shift(DOWN+RIGHT)
        self.play(Create(circle), run_time=0.5)
        circle.save_state()
        self.wait(0.5)
        self.play(Transform(circle,square), run_time=0.3)
        self.play(circle.animate.shift(RIGHT), run_time=0.3)
        self.play(circle.animate.rotate(0.5), run_time=0.4)
        self.wait(0.5)
        self.play(Restore(circle))
        self.wait(0.2)
        self.remove(circle,square)

        self.play(Transform(text,Text("ScaleInPlace").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(ScaleInPlace(square, scale_factor=2))
        self.remove(square)

        self.play(Transform(text,Text("ShrinkToCenter").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(ShrinkToCenter(square))
        self.remove(square)

        self.play(Transform(text,Text("TransformMatchingShapes").shift(UP*2.5)), run_time=0.5)
        source_text = Text("tom marvolo riddle")
        dest_text = Text("lord voldemort")
        self.play(Write(source_text))
        self.wait(0.5)
        self.play(TransformMatchingShapes(source_text, dest_text, path_arc=PI/2))
        self.wait(0.5)
        self.remove(source_text,dest_text)

        self.play(Transform(text,Text("TransformMatchingTex").shift(UP*2.5)), run_time=0.5)
        eq1 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq2 = MathTex("{{a}}^2", "+", "-{{c}}^2", "=", "-{{b}}^2")
        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(eq1, eq2, path_arc=PI/2))
        self.wait(0.5)
        self.remove(eq1,eq2)

        self.play(Transform(text,Text("animate.shift").shift(UP*2.5)), run_time=0.5)
        circle = Circle()
        self.play(circle.animate.shift(UP), run_time=0.5)
        self.play(circle.animate.shift(DOWN), run_time=0.5)
        self.play(circle.animate.shift(LEFT), run_time=0.5)
        self.play(circle.animate.shift(RIGHT), run_time=0.5)
        self.remove(circle)

        self.play(Transform(text,Text("animate.set_fill").shift(UP*2.5)), run_time=0.5)
        square = Square(fill_opacity=1)
        self.play(square.animate.set_fill(RED))
        self.remove(square)

        self.play(Transform(text,Text("animate.rotate").shift(UP*2.5)), run_time=0.5)
        triangle = Triangle(fill_opacity=1)
        self.play(triangle.animate.rotate(PI))
        self.remove(triangle)

        self.play(Transform(text,Text("animate.scale").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.scale(scale_factor=1.5))
        self.remove(square)

        self.play(Transform(text,Text("animate.rotate_about_origin").shift(UP*2.5)), run_time=0.5)
        star = Star().shift(RIGHT*2)
        self.play(star.animate.rotate_about_origin(PI))
        self.remove(star)

        self.play(Transform(text,Text("animate.rotate").shift(UP*2.5)), run_time=0.5)
        triangle = Triangle()
        self.play(triangle.animate.rotate(PI))
        self.remove(triangle)

        self.play(Transform(text,Text("animate.flip").shift(UP*2.5)), run_time=0.5)
        triangle = Triangle()
        self.play(triangle.animate.flip())
        self.remove(triangle)

        self.play(Transform(text,Text("animate.stretch").shift(UP*2.5)), run_time=0.5)
        circle = Circle()
        self.play(circle.animate.stretch(2,1))
        self.remove(circle)

        self.play(Transform(text,Text("animate.wag").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.wag())
        self.remove(square)

        self.play(Transform(text,Text("animate.pose_at_angle").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.pose_at_angle())
        self.remove(square)

        self.play(Transform(text,Text("animate.center").shift(UP*2.5)), run_time=0.5)
        square = Square().shift(LEFT*2)
        self.play(square.animate.center())
        self.remove(square)

        self.play(Transform(text,Text("animate.align_on_border").shift(UP*2.5)), run_time=0.5)
        square = Square().shift(LEFT*2)
        self.play(square.animate.align_on_border(direction=np.array([0,1,0])))
        self.remove(square)

        self.play(Transform(text,Text("animate.to_corner").shift(UP*2.5)), run_time=0.5)
        square = Square().shift(LEFT*2)
        self.play(square.animate.to_corner())
        self.remove(square)

        self.play(Transform(text,Text("animate.to_edge").shift(UP*2.5)), run_time=0.5)
        square = Square().shift(LEFT*2)
        self.play(square.animate.to_edge())
        self.remove(square)

        self.play(Transform(text,Text("animate.next_to").shift(UP*2.5)), run_time=0.5)
        dot = Dot().shift((RIGHT+UP)*2)
        square = Square().shift(LEFT*2)
        self.add(dot)
        self.play(square.animate.next_to(dot))
        self.remove(square,dot)

        self.play(Transform(text,Text("animate.scale_to_fit_width").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.scale_to_fit_width(5))
        self.remove(square)

        self.play(Transform(text,Text("animate.stretch_to_fit_width").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.stretch_to_fit_width(5))
        self.remove(square)

        self.play(Transform(text,Text("animate.scale_to_fit_height").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.scale_to_fit_height(3))
        self.remove(square)

        self.play(Transform(text,Text("animate.stretch_to_fit_height").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.stretch_to_fit_height(3))
        self.remove(square)

        self.play(Transform(text,Text("animate.set_coord").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.set_coord(-1,0))
        self.remove(square)

        self.play(Transform(text,Text("animate.set_x").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.set_x(-1))
        self.remove(square)

        self.play(Transform(text,Text("animate.set_y").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.play(square.animate.set_y(-1))
        self.remove(square)

        self.play(Transform(text,Text("animate.space_out_submobjects").shift(UP*2.5)), run_time=0.5)
        circle = Circle()
        star = Star()
        circle.add(star)
        self.play(circle.animate.space_out_submobjects(factor=2))
        self.remove(circle,star)

        self.play(Transform(text,Text("animate.move_to").shift(UP*2.5)), run_time=0.5)
        circle = Circle()
        self.play(circle.animate.move_to(RIGHT+UP))
        self.remove(circle)

        self.play(Transform(text,Text("animate.replace").shift(UP*2.5)), run_time=0.5)
        circle = Circle().shift(LEFT)
        star = Star().shift(RIGHT)
        self.add(circle, star)
        self.play(circle.animate.replace(star))
        self.remove(circle,star)

        self.play(Transform(text,Text("animate.surround").shift(UP*2.5)), run_time=0.5)
        circle = Circle().shift(LEFT)
        star = Star().shift(RIGHT)
        self.add(circle,star)
        self.play(circle.animate.surround(star))
        self.remove(circle,star)

        self.play(Transform(text,Text("animate.add_background_rectangle").shift(UP*2.5)), run_time=0.5)
        square = Square()
        self.add(square)
        self.play(square.animate.add_background_rectangle())
        self.remove(square)

        self.play(Transform(text,Text("animate.set_color").shift(UP*2.5)), run_time=0.5)
        square = Square(fill_opacity=1)
        self.add(square)
        self.play(square.animate.set_color(BLUE))
        self.remove(square)

        self.play(Transform(text,Text("animate.set_color_by_gradient").shift(UP*2.5)), run_time=0.5)
        square = Square(fill_opacity=1)
        self.add(square)
        self.play(square.animate.set_color_by_gradient(RED,BLUE,YELLOW))
        self.remove(square)

        self.play(Transform(text,Text("animate.fade_to").shift(UP*2.5)), run_time=0.5)
        square = Square(fill_opacity=1).set_fill(RED)
        self.add(square)
        self.play(square.animate.fade_to(GREEN, 0.5))
        self.remove(square)

        self.play(Transform(text,Text("animate.fade").shift(UP*2.5)), run_time=0.5)
        square = Square(fill_opacity=1).set_fill(RED)
        self.add(square)
        self.play(square.animate.fade())
        self.remove(square)

        self.play(Transform(text,Text("animate.match_color").shift(UP*2.5)), run_time=0.5)
        circle = Circle(fill_opacity=1).set_fill(RED).shift(LEFT*2)
        square = Square(fill_opacity=1).shift(RIGHT*2)
        self.add(circle)
        self.play(Create(square))
        self.play(square.animate.match_color(circle))
        self.remove(square,circle)

        self.play(Transform(text,Text("animate.match_dim_size").shift(UP*2.5)), run_time=0.5)
        circle = Circle().scale(2)
        square = Square()
        self.add(circle,square)
        self.play(square.animate.match_dim_size(circle, 0))
        self.remove(square,circle)
        
        self.play(Transform(text,Text("animate.match_width").shift(UP*2.5)), run_time=0.5)
        circle = Circle().scale(2)
        square = Square()
        self.add(circle,square)
        self.play(square.animate.match_width(circle))
        self.remove(square,circle)

        self.play(Transform(text,Text("animate.match_height").shift(UP*2.5)), run_time=0.5)
        circle = Circle().scale(2)
        square = Square()
        self.add(circle,square)
        self.play(square.animate.match_height(circle))
        self.remove(square,circle)

        self.play(Transform(text,Text("animate.match_x").shift(UP*2.5)), run_time=0.5)
        dot = Dot().shift((LEFT+UP)*2)
        star = Star()
        self.add(dot,star)
        self.play(star.animate.match_x(dot))
        self.remove(star,dot)

        self.play(Transform(text,Text("animate.match_y").shift(UP*2.5)), run_time=0.5)
        dot = Dot().shift((LEFT+UP)*2)
        star = Star()
        self.add(dot,star)
        self.play(star.animate.match_y(dot))
        self.remove(star,dot)

        self.play(Transform(text,Text("animate.arrange").shift(UP*2.5)), run_time=0.5)
        t1 = Text("3").shift(LEFT)
        t2 = Text("1")
        t3 = Text("2").shift(RIGHT)
        vg = VGroup(t2,t3,t1)
        self.add(t2,t3,t1)
        self.wait(0.5)
        self.play(vg.animate.arrange(buff=1.0))
        self.remove(t1,t2,t3)

        self.play(Transform(text,Text("animate.arrange_in_grid").shift(UP*2.5)), run_time=0.5)
        boxes=VGroup(*[Square().scale(0.5) for s in range(0,6)])
        boxes.arrange(buff=1.0)
        self.add(*boxes)
        self.wait(0.5)
        self.play(boxes.animate.arrange_in_grid(rows=2, buff=0.5))
        self.remove(*boxes)

        self.play(Transform(text,Text("animate.become").shift(UP*2.5)), run_time=0.5)
        circ = Circle(fill_color=RED, fill_opacity=0.8).shift(RIGHT*1.5)
        square = Square(fill_color=BLUE, fill_opacity=0.2).shift(LEFT*1.5)
        self.add(circ,square)
        self.wait(0.5)
        self.play(circ.animate.become(square))
        self.remove(circ,square)

        self.play(Transform(text,Text("animate.match_points").shift(UP*2.5)), run_time=0.5)
        circ = Circle(fill_color=RED, fill_opacity=0.8).shift(RIGHT*1.5)
        square = Square(fill_color=BLUE, fill_opacity=0.2).shift(LEFT*1.5)
        self.add(circ,square)
        self.wait(0.5)
        self.play(circ.animate.match_points(square))
        self.wait(0.5)
        self.play(FadeOut(circ),FadeOut(square))

        self.wait(0.5)
        self.play(FadeOut(text))
        self.wait()




        

        
        