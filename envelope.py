from draw import Drawing

import math
import kivy	 
kivy.require('1.9.0') 
def trade(a,b): return b,a

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Line, Triangle, Color
from kivy.graphics import Ellipse #for debugging purposes

from kivy.core.text import LabelBase
LabelBase.register(name='font', fn_regular="font3.otf")
#font1: 17B FunZone
#font2: Mont by FontFabric
#font3: OfficialBook.ttf by Vladimir Nikolik

class DrawingApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(Drawing(name="drawing"))
		return sm
		
DrawingApp().run()