from manim import *


class TypingAnimationWithCursor(Scene):
    def construct(self):
        # Create a text object
        text = Text("Hi, My name is Bilal.", font_size=48)

        self.play(AddTextLetterByLetter(text))
        # Position the text at the center of the screen
        text.move_to(ORIGIN)

        # Create a cursor (a blinking vertical line)
        cursor = Text("|", font_size=48)

        # Position the cursor initially at the start of the text
        cursor.next_to(text, RIGHT, buff=0.1)

        # Add the cursor to the scene
        self.add(text, cursor)

        # Create the text content to be typed
        text_content = "This is a typing animation"

        # Create a Typing animation
        typing_speed = 0.1  # Adjust the typing speed as needed
        for char in text_content:
            text.text += char
            self.wait(typing_speed)
            self.play(cursor.animate.set_opacity(0))
            self.wait(typing_speed)
            self.play(cursor.animate.set_opacity(1))

        # Wait for a few seconds
        self.wait(2)
