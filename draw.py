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
LabelBase.register(name='font', fn_regular="font3.ttf")
#font1: 17B FunZone
#font2: Mont by FontFabric
#font3: OfficialBook.ttf by Vladimir Nikolik

#.kv file:
from kivy.lang.builder import Builder
Builder.load_file('RibbonDrawing.kv')
Builder.load_file('EnvelopeDrawing.kv')
 
# Create the Widget class
class Paintbrush(Widget):
	color=0,0,0,0
	def build(self,color=(0,0,0,0)):
		self.color=color
	
class BrushDrawing(Widget):
	dot_color = "purple"
	prev_dot_color = "red"
	'''
	purple: the line is going up
	red: the line is staying still
	yellow: the line is going down
	'''
	
	thickness_threshold = 5
	thickness = thickness_threshold
	prev_thickness = thickness#Not intended to be used every time; more of a fall-back in case some calculations don't work out.
	
	start_point = (150,100)
	prev_x = start_point[0] # (The previous location of the user's cursor)
	prev_y = start_point[1]
	prev_pointC = start_point
	prev_pointD = start_point
	one_touch_ago = start_point

	#Very small, near-trivial detail, but inkdrop_dot is to represent the little blotch that gets drawn when the user draws a single point that's not connected to a main brushstroke. Purely for cosmetics, the program will know what the most recent inkdrop_dot was so that it can erase it if it starts drawing a brushstroke again. (The "if eucl_dist>_:" if-statement will determine whether a small inkblot gets drawn instead of a 'proper' brushstroke.)
	inkdrop_dot=None
	
	def on_touch_down(self, touch):
		pb = Paintbrush()
		pb.center = touch.pos
		self.add_widget(pb)
 
 
	def on_touch_move(self, touch):
		self.prev_x = self.start_point[0]
		self.prev_y = self.start_point[1]
	
		#Incase of ZeroDivisionError, revert to the previous thing (for pointC & pointD):
		pointA = self.prev_pointC
		pointB = self.prev_pointD
		pointC = self.prev_pointC
		pointD = self.prev_pointD
	
		x_diff = (touch.pos[0] - self.prev_x)
		y_diff = (touch.pos[1] - self.prev_y)
		eucl_dist = math.sqrt(math.pow(x_diff,2) + math.pow(y_diff,2)) #Euclidean distance from the previous point.
		
		#Draw the current point, with the desired thickness:
		self.thickness = (self.thickness_threshold*(1/(1+math.exp((eucl_dist-40)/10))))*(4/5)*(self.thickness_threshold/5) #A sigmoid function, plus a minor mapping transformation compounded on it.
					
		try:
			#Do some geometry to make trapezoids that connect the dots in a visually neat way:
			slope = (touch.pos[1] - self.prev_y) / (touch.pos[0] - self.prev_x) # m=(y2-y1)/(x2-x1)
			theta = math.atan(slope) #theta=arctan(slope)
			
			prev_hyp = self.prev_thickness*(4/5)+10
			prev_opp = prev_hyp * math.sin(theta)
			prev_adj = prev_hyp * math.cos(theta)
			
			#Find points of trapezoid that are prev_dot:
			curr_hyp = self.thickness*(4/5)+10
			curr_opp = curr_hyp * math.sin(theta)
			curr_adj = curr_hyp * math.cos(theta)
			pointC = (touch.pos[0]-curr_opp, touch.pos[1]-curr_adj)
			pointD = (touch.pos[0]+curr_opp, touch.pos[1]+curr_adj)
			pointsCD = pointC, pointD
			pointC = min(pointsCD, key=lambda t:t[0])
			pointD = max(pointsCD, key=lambda t:t[0])
		
			
			if touch.pos[1]==self.start_point[1]:
				self.dot_color = "red"
			elif touch.pos[1]<self.start_point[1]:
				self.dot_color = "yellow"
			elif touch.pos[1]>self.start_point[1]:
				self.dot_color = "purple"

			
			#Draw:
			if eucl_dist>100:
				with self.canvas:
					#TODO: Write functionality that changes the size of the self.inkdrop_dot.
					self.inkdrop_dot = Ellipse(pos=(touch.pos[0]-.5,touch.pos[1]-.5), size=(1,1))
			else:
				with self.canvas:				
					#Current position adapted to ensure the ellipse starts central with the mouse cursor as it's clicking (if you're using the mouse to draw, and not a touch screen, it'll be more precisely apparent if the marking is off-kilter.)
					adpt_curr_pos = (self.prev_x-self.thickness/2 , self.prev_y-self.thickness/2)
					
					#Solves the full cuts (by turning them into partial cuts):
					#The full cut happens when the dot is red -- that is, when the y-coordinate of the current touch.pos point is measured to be the same as the touch.pos point from the previous moment.
					if self.dot_color is "red":
						pointC = (touch.pos[0], touch.pos[1]+(pointA[1]-touch.pos[1]))
						pointD = (touch.pos[0], touch.pos[1]+(pointB[1]-touch.pos[1]))

					#Solves the partial cuts:
					#Without the following if-statement, the ribbon being drawn would have visible "cuts" in it, at the top of every hill and the bottom of every crest. The system of imagining colored dots was made to determine when these "cuts" happen. The cuts happen in the following circumstance:
					if not self.dot_color is self.prev_dot_color:
					
						#Draw an extra triangle to fill in that partial cut. (A partial cut is where, instead of all four corners drawing complementary triangles that combine to a quadrangle, the two triangles overlap & then leave a gap that caves halfway in, usually at the top or bottom. The following statement is to cover that gap:
						Triangle(points=[pointA[0],pointA[1], pointB[0],pointB[1], pointC[0],pointC[1]])

					#Drawing the main triangles:
					Triangle(points=[pointA[0],pointA[1], pointC[0],pointC[1], pointD[0],pointD[1]])
					Triangle(points=[pointA[0],pointA[1], pointB[0],pointB[1], pointD[0],pointD[1]])
					
			self.prev_pointC = pointC
			self.prev_pointD = pointD
			self.prev_dot_color = self.dot_color
			
		#The following exception seems to occur whenever the previous timestep and the current timestep have the same x-coordinate in their touch.pos:
		except ZeroDivisionError:
			pointA = self.prev_pointC
			pointB = self.prev_pointD
			pointC = (touch.pos[0], touch.pos[1]+20)
			pointD = (touch.pos[0], touch.pos[1]-20)

		self.prev_thickness=self.thickness
		self.prev_x=touch.pos[0]; self.prev_y=touch.pos[1]
		self.start_point = touch.pos
		
class EnvelopeDrawing(Screen):
	xaxis_lowness = 400 #How low it is relative to the center of the canvas
	xaxis_length = 600
	yaxis_height = 360
	'''
		Note that for some reason, in the .kv file, the background color is affected by strange factors at the moment... the background color is effected both by the EnvelopeDrawing object and the BrushDrawing object, one being a widget that gets grafted atop the other one.
	'''
		
if __name__=="__main__":
	class DrawingApp(App):
		def build(self):
			sm = ScreenManager()
			sm.add_widget(EnvelopeDrawing(name="drawing"))
			return sm
	DrawingApp().run()