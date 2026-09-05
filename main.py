from kivy.app import App
from kivy.uix.label import Label


class SpaceInvadersApp(App):
    def build(self):
        return Label(
            text="SPACE INVADERS",
            font_size="32sp"
        )


SpaceInvadersApp().run()
