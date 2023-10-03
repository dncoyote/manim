from manim import *


class AllAnimations(Scene):
    def construct(self):

        some_text = Text("Hi! I am Bilal.")
        self.play(AddTextLetterByLetterWithCursor(some_text))

        self.play(RemoveTextLetterByLetterWithCursor(some_text))


class AddTextLetterByLetterWithCursor(AddTextLetterByLetter):
    def create_cursor(self):
        cursor = Text("_")
        cursor.next_to(self.mobject[0], RIGHT)
        self.cursor = cursor
        return cursor

    def show_cursor(self):
        self.add(self.cursor)

    def hide_cursor(self):
        self.remove(self.cursor)

    def get_all_letters_animation(self):
        cursor_shown = False
        for mob in self.mobject:
            yield mob
            if not cursor_shown:
                self.show_cursor()
                cursor_shown = True
            yield
            self.hide_cursor()


class RemoveTextLetterByLetterWithCursor(RemoveTextLetterByLetter):
    def create_cursor(self):
        cursor = Text("_")
        cursor.next_to(self.mobject[0], LEFT)
        self.cursor = cursor
        return cursor

    def show_cursor(self):
        self.add(self.cursor)

    def hide_cursor(self):
        self.remove(self.cursor)

    def get_all_letters_animation(self):
        cursor_shown = False
        for mob in self.mobject:
            yield mob
            if not cursor_shown:
                self.show_cursor()
                cursor_shown = True
            yield
            self.hide_cursor()


# if __name__ == "__main__":
#     config.pixel_height = 1080
#     config.pixel_width = 1920
#     config.frame_height = 6.0
#     config.frame_width = 6.0
#     config.frame_rate = 30
#     config.renderer = "opengl"  # Use the OpenGL renderer

#     # Use Manim to render the scene
#     scene = AllAnimations()
#     scene.render()
