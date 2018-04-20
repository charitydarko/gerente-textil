from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import webbrowser
import random

from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen, WipeTransition
from kivy.utils import get_color_from_hex

from arithmetic import Arithmetic
from json_settings import json_settings

Window.clearcolor = get_color_from_hex("#16203B")
Builder.load_file("kv/middle.kv")
Builder.load_file("kv/clothes.kv")
Builder.load_file("kv/screens.kv")
Builder.load_file("kv/play.kv")


class MiddleScreen(Screen):
    pass

class RecordsScreen(Screen):
    pass

class NewsScreen(Screen):
    pass

################################################################################################
class OthersScreen(Screen):
    pass

class PlayScreen(Screen):
	pass


class AboutScreen(Screen):
	pass

class MathScreen(Screen, Arithmetic):
	pass


########################################################################################################

class GTPScreen(Screen):
    pass


class WoodinScreen(Screen):
    pass


class HollandScreen(Screen):
    pass

class GTPLine(Screen):
	pass

class WoodinLine(Screen):
	pass

class HollandLine(Screen):
	pass


class TextileManager(ScreenManager):
    sales_screen = ObjectProperty(None)
    records_screen = ObjectProperty(None)
    news_screen = ObjectProperty(None)
    others_screen = ObjectProperty(None)
    gtp_screen = ObjectProperty(None)
    woodin_screen = ObjectProperty(None)
    holland_screen = ObjectProperty(None)
    about_screen = ObjectProperty()
    kivy_screen_manager = ObjectProperty()



    def __init__(self, **kwargs):
    	super(TextileManager, self).__init__(**kwargs)

    def changeScreen(self, next_screen):
    	operations = "addition subtraction multiplication division".split()
    	question = None

    	if next_screen == "about this app":
    		self.ids.kivy_screen_manager.current = "about_screen"
    

class TextileManagerApp(App):
	#---------------------------------------------------------------------------
    def build(self):
        m = TextileManager(transition=WipeTransition())
        return TextileManager()

    def __init__(self, **kwargs):
    	super(TextileManagerApp, self).__init__(**kwargs)

    def getText(self):
    	return ("Hey There!\nThis App was built using"
                "[b][ref=kivy]kivy[/ref][/b]\n"
                "Feel free to look at the source code "
                "[b][ref=source]here[/ref][/b].\n"
                "This app is under the [b][ref=mmm]mmm License[/ref][/b]")

    def on_ref_press(self, instance, ref):
    	_dict = {
            "source": "https://github.com/afyacy/Kivy-App",
            "website": "http://www.afyacy.com",
            "kivy": "http://kivy.org/#home",
            "ttt": "https://github.com/afyacy/Kivy/blob/master/LICENSE"
        }

        webbrowser.open(_dict[ref])
	
if __name__ == '__main__':
    TextileManagerApp().run()