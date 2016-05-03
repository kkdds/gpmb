import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
# textinput need install xclip
from kivy.uix.textinput import TextInput
from kivy.uix.vkeyboard import VKeyboard
from kivy.clock import Clock
from kivy.graphics import Color,Ellipse

import RPi.GPIO as GPIO
    
			
class MyscreenApp(BoxLayout):
        
	# This callback will be bound to the LED toggle and Beep button:
	def press_callback(self,obj):
		print("Button pressed,")
		if obj.state == "down":
			print ("button on")
			obj.text='Running'
			self.lb2.text='Rrrr'
			self.lb2.bkcolor=[0,1,0,.5]
			self.lb1.bkcolor=[0,1,0,.5]
			#GPIO.output(ledPin, GPIO.HIGH)
		else:
			print ("button off")
			obj.text='Stopping'
			self.lb2.text='ppps'			
			self.lb2.bkcolor=[1,0,0,.5]
			self.lb1.bkcolor=[1,0,0,.5]
			#GPIO.output(ledPin, GPIO.LOW)
			
	def press_btn_b1(self,val):
		print("b1 : ",val.pos[0])
		#print("enter : ",txt1.text)
			
	def press_btn_b2(self,val):
		print("b2 : ",val.pos[0])
			
	def press_btn_b3(self,val):
		print("b3 : ",val.pos[0])
		print("t: ",int(self.txt3.text))
			
	def on_enter(self,val):
		print("enter : ",self , val)
		

def up_sta(self):
        #print("up_sta : ")
        pass
        
		
class TestApp(App):
	def build(self):
		myscr=MyscreenApp()
		Clock.schedule_interval(up_sta,1/5)
		return myscr

if __name__ == '__main__':
	TestApp().run()
