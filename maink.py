#! /usr/bin/python3.4
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.vkeyboard import VKeyboard
from kivy.clock import Clock
from kivy.graphics import Color,Ellipse
import datetime as datetime
import RPi.GPIO as GPIO
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os,random
import configparser

from TM1650 import TM1650
myTM1650=object
#from pyomxplayer import OMXPlayer
#omx=object
from feh import FEH
myfeh=object

kconfig=configparser.ConfigParser()
kconfig.read('/home/pi/gpmb/'+"set.ini")
s1=kconfig.get("gpmb","s1")
s2=kconfig.get("gpmb","s2")
s3=kconfig.get("gpmb","s3")
s4=kconfig.get("gpmb","s4")
s5=kconfig.get("gpmb","s5")
s6=kconfig.get("gpmb","s6")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
io_jx1=26#
io_jx2=16#
io_jx3=19#
io_jx4=13#
io_jx5=20#
io_jx6=21#
io_jx7=6
io_jx8=5
GPIO.setup(io_jx1, GPIO.OUT)
GPIO.setup(io_jx2, GPIO.OUT)
GPIO.setup(io_jx3, GPIO.OUT)
GPIO.setup(io_jx4, GPIO.OUT)
GPIO.setup(io_jx5, GPIO.OUT)
GPIO.setup(io_jx6, GPIO.OUT)
GPIO.setup(io_jx7, GPIO.OUT)
GPIO.setup(io_jx8, GPIO.OUT)
GPIO.output(io_jx1, 1)
GPIO.output(io_jx2, 1)
GPIO.output(io_jx3, 1)
GPIO.output(io_jx4, 1)
GPIO.output(io_jx5, 1)
GPIO.output(io_jx6, 1)
GPIO.output(io_jx7, 1)
GPIO.output(io_jx8, 1)

io_in1=23
io_in2=24
io_in3=17
io_in4=27
io_in4=22
GPIO.setup(io_in1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(io_in2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)

watch_dog=1

Builder.load_file('gpv1.kv')

def save_set():
    kconfig.set("gpmb","s1",setscr.time1.text)
    kconfig.set("gpmb","s2",myscr.time2.text)
    kconfig.set("gpmb","s3",setscr.time3.text)
    kconfig.set("gpmb","s4",setscr.time4.text)
    kconfig.set("gpmb","s5",myscr.time5.text)
    kconfig.set("gpmb","s6",setscr.time6.text)
    kconfig.write(open('/home/pi/gpmb/'+"set.ini","w"))
    print("saved ")
    pass

class SaveScreen(Screen):
    global watch_dog,omx,myfeh
    caifiles=[]
    froot='/home/pi/gpmb/img'
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
        f=os.path.join(self.froot,self.caifiles[self.PIno])
        self.PIno+=1
        if(self.PIno>=self.PIlen):
            self.PIno=0
        #print (f,watch_dog)
        self.img.source=f        
        pass

    def backbtn(self):
        #omx.stop()
        #myfeh.stop()
        sm.current='menu'
        #Clock.unschedule(sescr.chpic)
        pass
        
    def update_sta(self,dt):
        if GPIO.input(22)==GPIO.LOW or GPIO.input(27)==GPIO.LOW:
            sm.current='menu'
            

class SettingsScreen(Screen):    

    def on_text(self, value):
        save_set()
        pass

    def press_save(self):        
        global watch_dog
        watch_dog=1
        sm.current='menu'
        pass


class MyscreenApp(Screen):
    
    r_sta=False
    key_delay=0
    key_delay2=0

    def on_focus(self):
        global watch_dog
        print("on_focus")
        watch_dog=0
        pass

    def on_text2(self, value):
        global watch_dog
        print("on_text 2")
        watch_dog=1    
        pass
        
    def on_text(self, value):
        global watch_dog
        print("on_text")
        watch_dog=1
        if self.r_sta==False:
            save_set()        
        pass

    def press_btn_b1(self,val):
        global watch_dog
        #print("b1 1: ")
        watch_dog=0
        GPIO.output(io_jx1, GPIO.LOW)
        Clock.schedule_once(self.release_btn_b1,5)
        pass
    def release_btn_b1(self,val):
        global watch_dog
        #print("b1 0: ")
        watch_dog=1
        GPIO.output(io_jx1, GPIO.HIGH)        
        self.btnb1.state = "normal"
        pass

    def press_btn_b2(self,val):
        global watch_dog
        watch_dog=0
        #print("b3 1: ",val.pos[0])
        GPIO.output(io_jx4, GPIO.LOW)
        GPIO.output(io_jx3, GPIO.LOW)
        Clock.schedule_once(self.release_btn_b2,5)
        pass
    def release_btn_b2(self,val):
        global watch_dog
        watch_dog=1
        #print("b3 0: ",val.pos[0])
        GPIO.output(io_jx4, GPIO.HIGH)
        GPIO.output(io_jx3, GPIO.HIGH)        
        self.btnb2.state = "normal"
        pass

    def press_btn_b3(self,val):
        global watch_dog
        watch_dog=0
        #print("b2 1: ",val.pos[0])
        GPIO.output(io_jx5, GPIO.LOW)
        pass
    def release_btn_b3(self,val):
        global watch_dog
        watch_dog=1
        #print("b2 0: ",val.pos[0])
        GPIO.output(io_jx5, GPIO.HIGH)
        pass

    def press_am(self,txtn,val):
        if txtn=="time2":
            self.time2.text=str(int(self.time2.text)+val)
        elif txtn=="time5":
            self.time5.text=str(int(self.time5.text)+val)
        elif txtn=="txt3":
            self.txt3.text=str(int(self.txt3.text)+val)
        pass
        
    def press_set(self):
        sm.current='settings'
        pass

    def press_tgb(self):
        if self.tgbtn.state == "down" and self.r_sta==False:
            self.tgbtn.text='运行中'
        else:
            print ("tgbtn off")
            self.tgbtn.text='已停止'
            self.tgbtn.state = "normal"
            self.txt3.text='1'

    def sch_m1(self,dt):            
        print("sch_m1 done: ",datetime.datetime.now())
        GPIO.output(io_jx3, GPIO.LOW)
        GPIO.output(io_jx4, GPIO.LOW)
        Clock.schedule_once(self.sch_m2,int(self.time2.text)/10)
        pass

    def sch_m2(self,dt):
        print("sch_m2 done: ",datetime.datetime.now())
        GPIO.output(io_jx1, GPIO.HIGH)
        Clock.schedule_once(self.sch_m3,int(setscr.time3.text)/10)
        pass

    def sch_m3(self,dt):
        print("sch_m3 done: ",datetime.datetime.now())
        GPIO.output(io_jx3, GPIO.HIGH)
        GPIO.output(io_jx4, GPIO.HIGH)
        Clock.schedule_once(self.sch_m4,int(setscr.time4.text))
        pass

    def sch_m4(self,dt):
        print("sch_m4 done: ",datetime.datetime.now())
        GPIO.output(io_jx5, GPIO.LOW)
        Clock.schedule_once(self.sch_m5,int(self.time5.text)/10)
        pass

    def sch_m5(self,dt):
        print("sch_m5 done: ",datetime.datetime.now())
        GPIO.output(io_jx2, GPIO.HIGH)
        GPIO.output(io_jx5, GPIO.HIGH)
        Clock.schedule_once(self.sch_fin,int(setscr.time6.text))
        pass

    def sch_fin(self,dt):
        global myTM1650
        print("schfin done: ",datetime.datetime.now(),self.txt3.text)
        self.r_sta=False        
        self.btnb1.disabled=False
        self.btnb2.disabled=False
        self.btnb3.disabled=False
        #setscr.time1.disabled=False
        self.time2.disabled=False
        #setscr.time3.disabled=False
        #setscr.time4.disabled=False
        self.time5.disabled=False
        self.txt3.disabled=False
        self.setbtn.disabled=False
        count=int(self.txt3.text)
        if count>0:
            count=count-1
        self.txt3.text=str(count)
        myTM1650.R(self.txt3.text)
        myTM1650.L('  ')
        GPIO.output(io_jx1, GPIO.HIGH)
        GPIO.output(io_jx2, GPIO.HIGH)
        GPIO.output(io_jx3, GPIO.HIGH)
        GPIO.output(io_jx4, GPIO.HIGH)
        GPIO.output(io_jx5, GPIO.HIGH)
        GPIO.output(io_jx6, GPIO.HIGH)

    def update_sta(self,dt):
        global watch_dog
        global omx,myfeh,myTM1650

        self=sm.current_screen
        
        if self.name!='menu':
            return 0

        if self.tgbtn.state == "down" and int(self.txt3.text)>0 and self.r_sta==False:
            if GPIO.input(23)==GPIO.HIGH:
                self.tgbtn.state='normal'
                self.tgbtn.text='已停止'
                return 0
            if GPIO.input(24)==GPIO.HIGH:
                self.tgbtn.state='normal'
                self.tgbtn.text='已停止'
                return 0
            self.r_sta=True
            self.btnb1.disabled=True
            self.btnb2.disabled=True
            self.btnb3.disabled=True
            #setscr.time1.disabled=True
            self.time2.disabled=True
            #setscr.time3.disabled=True
            #setscr.time4.disabled=True
            self.time5.disabled=True
            self.txt3.disabled=True
            self.setbtn.disabled=True
            print("start loop : ",datetime.datetime.now())
            GPIO.output(io_jx1, GPIO.LOW)
            GPIO.output(io_jx2, GPIO.LOW)
            GPIO.output(io_jx6, GPIO.LOW)
            myTM1650.L('--')
            myTM1650.R(self.txt3.text)
            Clock.schedule_once(self.sch_m1,int(setscr.time1.text)/10)

        if self.r_sta:
            watch_dog=1    
            self.lb1.bkcolor=[0,1,0,.5]
        else:
            self.lb1.bkcolor=[1,0,0,.5]
            
        if GPIO.input(23)==GPIO.LOW:
            self.lb2.text='就绪'
            self.lb2.bkcolor=[0,1,0,.5]
            self.tgbtn.disabled=False
            self.btnb1.disabled=True
        else:
            self.lb2.text='准备'
            self.lb2.bkcolor=[1,0,0,.5]
            self.tgbtn.disabled=True
            self.btnb1.disabled=False
            
        if GPIO.input(24)==GPIO.LOW:
            self.lb3.bkcolor=[0,1,0,.5]
            self.tgbtn.disabled |= 0
            self.btnb2.disabled=True
        else:
            self.lb3.bkcolor=[1,0,0,.5]
            self.tgbtn.disabled=True
            self.btnb2.disabled=False

        #manual +10 and start
        if GPIO.input(22)==GPIO.LOW:
            if self.key_delay2==0:
                self.txt3.text=str(int(self.txt3.text)+10)
                myTM1650.R(self.txt3.text)
                myTM1650.L('--')
            #if self.r_sta==False:
                self.tgbtn.text='运行中'
                self.tgbtn.state = "down"
            self.key_delay2+=1
            if self.key_delay2==15:
                self.key_delay2=0
        else:
             self.key_delay2=0

        #manual +1 and start
        if GPIO.input(27)==GPIO.LOW:
            if self.key_delay==0:
                self.txt3.text=str(int(self.txt3.text)+1)
                myTM1650.R(self.txt3.text)
                myTM1650.L('--')
            #if self.r_sta==False:
                self.tgbtn.text='运行中'
                self.tgbtn.state = "down"
            self.key_delay+=1
            if self.key_delay==15:
                self.key_delay=0
        else:
             self.key_delay=0

        #manual stop
        if GPIO.input(17)==GPIO.LOW:
            print ("man btn off")
            self.tgbtn.text='已停止'
            self.tgbtn.state = "normal"
            self.txt3.text='0'
            myTM1650.R('0')
            if self.r_sta==True:
                myTM1650.L('__')

        try:
            if int(self.txt3.text)==0:
                self.tgbtn.state='normal'
                self.tgbtn.text='已停止'
        except:
            self.tgbtn.state='normal'
            self.tgbtn.text='已停止'

        if watch_dog>0:
             watch_dog+=1
        if watch_dog>450:
            watch_dog=1
            #sescr.chpic(dt)
            Clock.schedule_interval(sescr.chpic,5)
            sm.current='scrsave'
            #print('play video')
            #omx = OMXPlayer('/home/pi/gpmb/video.avi')
            #myfeh = FEH('/home/pi/gpmb/img/')
        pass


# Create the screen manager
sm = ScreenManager()
myscr=MyscreenApp(name='menu')
sm.add_widget(myscr)
sescr=SaveScreen(name='scrsave')
sm.add_widget(sescr)
setscr=SettingsScreen(name='settings')
sm.add_widget(setscr)

setscr.time1.text=s1
setscr.time3.text=s3
setscr.time4.text=s4
setscr.time6.text=s6
myscr.time2.text=s2
myscr.time5.text=s5

myTM1650=TM1650()
print(myTM1650.OK);
class TestApp(App):
    def build(self):        
        sescr.getfile()
        Clock.schedule_interval(myscr.update_sta,1/15)
        Clock.schedule_interval(sescr.update_sta,1/15)
        return sm

if __name__ == '__main__':
    TestApp().run()
