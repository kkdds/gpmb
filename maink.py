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
import datetime as datetime
import RPi.GPIO as GPIO


class MyscreenApp(BoxLayout):
    r_sta=False
    # This callback will be bound to the LED toggle and Beep button:
    def press_callback(self,obj):
        #print("Button pressed,")
        if obj.state == "down":
            #print ("button on",datetime.datetime.now())
            obj.text='Running'
            self.lb2.text='Rrrr'
            self.lb2.bkcolor=[0,1,0,.5]
            self.lb1.bkcolor=[0,1,0,.5]
            #GPIO.output(ledPin, GPIO.HIGH)
            #self.start_loop()
        else:
            print ("button off")
            obj.text='Stopping'
            self.lb2.text='ppps'
            self.lb2.bkcolor=[1,0,0,.5]
            self.lb1.bkcolor=[1,0,0,.5]
            self.txt3.text='1'
            #GPIO.output(ledPin, GPIO.LOW)

    def press_btn_b1(self,val):
        #print("b1 : ",val.pos[0])
        #print("enter : ",txt1.text)
        pass

    def press_btn_b2(self,val):
        #print("b2 : ",val.pos[0])
        pass

    def press_btn_b3(self,val):
        #print("b3 : ",val.pos[0])
        #print("t: ",int(self.txt3.text))
        pass

    def on_enter(self,val):
        print("enter : ",self , val)

    def sch_m1(self,dt):            
        print("sch_m1 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m2,3)
        pass

    def sch_m2(self,dt):
        print("sch_m2 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m3,3)
        pass

    def sch_m3(self,dt):
        print("sch_m3 done: ",datetime.datetime.now())
        print("Loop done")
        self.r_sta=False        
        self.btnb1.disabled=False
        self.btnb2.disabled=False
        self.btnb3.disabled=False
        self.txt1.disabled=False
        self.txt2.disabled=False
        self.txt3.disabled=False
        count=int(self.txt3.text)
        count=count-1
        self.txt3.text=str(count) 

    def update_sta(self,dt):
        if self.tgbtn.state == "down" and int(self.txt3.text)>0 and self.r_sta==False:
            self.r_sta=True
            self.btnb1.disabled=True
            self.btnb2.disabled=True
            self.btnb3.disabled=True
            self.txt1.disabled=True
            self.txt2.disabled=True
            self.txt3.disabled=True
            print("start loop : ",datetime.datetime.now())
            Clock.schedule_once(self.sch_m1,3)

        try:
            if int(self.txt3.text)==0:
                self.tgbtn.state='normal'
                self.tgbtn.text='Stopping'
        except:
            self.tgbtn.state='normal'
            self.tgbtn.text='Stopping'
            
        #print("up_sta : ")
        pass


class TestApp(App):
    def build(self):
        myscr=MyscreenApp()
        myscr.r_sta=False
        Clock.schedule_interval(myscr.update_sta,1/15)
        return myscr

if __name__ == '__main__':
    TestApp().run()
