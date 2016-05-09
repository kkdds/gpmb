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
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os,random


Builder.load_file('test.kv')

class SettingsScreen(Screen):
    caifiles=[]
    froot='/home/pi/lmf/image'
    PIlen=0
    PIno=0
    def getfile(self):        
        for i in os.listdir(self.froot):
                if os.path.isfile(os.path.join(self.froot,i)):
                        self.caifiles.append(i)
        self.caifiles.sort()
        self.PIlen=len(self.caifiles)
        pass

    def chpic(self,dt):
        #i=random.randint(0,len(self.caifiles))
        #i=random.randint(0,35)
        f=os.path.join(self.froot,self.caifiles[self.PIno])		
        self.PIno+=1
        if(self.PIno>=self.PIlen):
            self.PIno=0
        print (f,myscr.watch_dog)
        self.img.source=f        
        pass

    def backbtn(self):
        #print("textd")
        sm.current='menu'
        Clock.unschedule(sescr.chpic)
        pass


class MyscreenApp(Screen):
    r_sta=False
    watch_dog=1

    def on_focus(self):
        #print("textd")
        sm.current_screen.watch_dog=1
        pass

    def press_tgb(self):
        if self.tgbtn.state == "down" and self.r_sta==False:
            self.tgbtn.text='运行中'
        else:
            print ("button off")
            self.tgbtn.text='已停止'
            self.tgbtn.state = "normal"
            self.txt3.text='1'

    def press_btn_b1(self,val):
        print("b1 : ",val.pos[0])
        self.watch_dog=1
        #GPIO.output(ledPin, GPIO.LOW)
        pass

    def press_btn_b2(self,val):
        print("b2 : ",val.pos[0])
        self.watch_dog=1
        #GPIO.output(ledPin, GPIO.LOW)
        pass

    def press_btn_b3(self,val):
        print("b3 : ",val.pos[0])
        self.watch_dog=1
        #GPIO.output(ledPin, GPIO.LOW)
        pass

    def sch_m1(self,dt):            
        print("sch_m1 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m2,int(self.time2.text)/10)
        pass

    def sch_m2(self,dt):
        print("sch_m2 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m3,int(self.time3.text))
        pass

    def sch_m3(self,dt):
        print("sch_m3 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m4,int(self.time4.text)/2)
        pass

    def sch_m4(self,dt):
        print("sch_m4 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_fin,int(self.time4.text)/2)
        pass

    def sch_fin(self,dt):
        print("schfin done: ",datetime.datetime.now(),self.txt3.text)
        self.r_sta=False        
        self.btnb1.disabled=False
        self.btnb2.disabled=False
        self.btnb3.disabled=False
        self.time1.disabled=False
        self.time2.disabled=False
        self.time3.disabled=False
        self.time4.disabled=False
        self.time5.disabled=False
        self.txt3.disabled=False
        count=int(self.txt3.text)
        count=count-1
        self.txt3.text=str(count) 

    def update_sta(self,dt):
        self=sm.current_screen
        
        if self.name!='menu':
            return 0
        
        if self.tgbtn.state == "down" and int(self.txt3.text)>0 and self.r_sta==False:
            self.r_sta=True
            self.btnb1.disabled=True
            self.btnb2.disabled=True
            self.btnb3.disabled=True
            self.time1.disabled=True
            self.time2.disabled=True
            self.time3.disabled=True
            self.time4.disabled=True
            self.time5.disabled=True
            self.txt3.disabled=True
            print("start loop : ",datetime.datetime.now())
            Clock.schedule_once(self.sch_m1,int(self.time1.text))
                        
        if self.r_sta:
            self.watch_dog=1    
            self.lb1.bkcolor=[0,1,0,.5]
        else:
            self.lb1.bkcolor=[1,0,0,.5]
            
        if 0:
            self.lb2.text='准备'
            self.lb2.bkcolor=[1,0,0,.5]
            self.tgbtn.disabled=True
        else:
            self.lb2.text='就绪'
            self.lb2.bkcolor=[0,1,0,.5]
            self.tgbtn.disabled=False
            
        if 1:
            self.lb3.bkcolor=[0,1,0,.5]
        else:
            self.lb3.bkcolor=[1,0,0,.5]

        try:
            if int(self.txt3.text)==0:
                self.tgbtn.state='normal'
                self.tgbtn.text='已停止'
        except:
            self.tgbtn.state='normal'
            self.tgbtn.text='已停止'
            
        self.watch_dog+=1
        if self.watch_dog>60:
            self.watch_dog=1
            #sescr.chpic()
            Clock.schedule_interval(sescr.chpic,5)
            sm.current='settings'
            
        pass


# Create the screen manager
sm = ScreenManager()
myscr=MyscreenApp(name='menu')
sm.add_widget(myscr)
sescr=SettingsScreen(name='settings')
sm.add_widget(sescr)

class TestApp(App):
    def build(self):        
        sescr.getfile()
        Clock.schedule_interval(myscr.update_sta,1/15)
        return sm

if __name__ == '__main__':
    TestApp().run()
