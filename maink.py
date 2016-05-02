import kivy
kivy.require('1.8.6') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.vkeyboard import VKeyboard
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle,Line

import RPi.GPIO as GPIO
    
			
class MyscreenApp(BoxLayout):
        # This callback will be bound to the LED toggle and Beep button:
        def press_callback(self,obj):
                print("Button pressed,")
                if obj.state == "down":
                        print ("button on")
                        obj.text='Running'
                        self.btx.text='Rrrr'
                        self.btx.state='down'
                        with self.tlb.canvas:
                                Color(1,1,1,1)
                                Rectangle(pos=self.tlb.pos,size=self.tlb.size)
                        #GPIO.output(ledPin, GPIO.HIGH)
                        #VKeyboard()
                else:
                        print ("button off")
                        print (self.btx.pos)
                        print (self.btx.pos[1])
                        obj.text='Stopping'
                        self.btx.text='ppps'
                        self.btx.state='normal'
                        self.btx.background_color=[1,0,0,.8]
                        #self.tlb=Color(1,0,0,.8)
                        self.tlb.font_size=32
                        self.tlb.background_color=[1,0,0,.3]
                        #self.tlb.canvas.clear()


                        with self.tlb.canvas:
                                Color(1,1,0,.8)
                                Rectangle(pos=self.tlb.pos,size=self.tlb.size)
                        #GPIO.output(ledPin, GPIO.LOW)
                        
        def show_selected_value(self,txt):
                print("spinner : ",txt.text)

                

class TestApp(App):
	def build(self):
		# Start flashing the LED
		return MyscreenApp()
		#return Button()
		#return Button(text='hhh')

if __name__ == '__main__':
	TestApp().run()
