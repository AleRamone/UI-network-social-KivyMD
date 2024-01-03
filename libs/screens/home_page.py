from kivymd.uix.screen import MDScreen
import json

from libs.components.circular_avatar_image import CircularAvatarImage
ruta = 'assets/datta/stories.json'
class HomePage(MDScreen):
        profile_picture = "https://1000logos.net/wp-content/uploads/2020/03/Ramones-Logo-500x313.png"

        def on_enter(self):
                pass
        # self.list_stories()
        '''
        def list_stories(self):

                with open(ruta) as file:
                        data = json.load(file)
                        for name in data:
                                self.ids.stories.add_widget(CircularAvatarImage(
                                        avatar = data[name]['avatar'],
                                        name = name
                                ))

        '''

