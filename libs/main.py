from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

from libs.screens.home_page import HomePage

class RedApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file('screens/home_page.kv')
        Builder.load_file('components/appbar.kv')

        Builder.load_file('components/bottom_nav.kv')

    def on_start(self):
        self.root.dispatch('on_enter')

if __name__ == "__main__":
    RedApp().run()

