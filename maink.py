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
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

watch_dog=1

Builder.load_file('gpv1.kv')

def save_set():
    kconfig.set("gpmb","s1",setscr.time1.text)
    kconfig.set("gpmb","s2",setscr.time2.text)
    kconfig.set("gpmb","s3",setscr.time3.text)
    kconfig.set("gpmb","s4",setscr.time4.text)
    kconfig.set("gpmb","s5",setscr.time5.text)
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
        Clock.unschedule(self.chpic)
        pass

    def update_sta(self,dt):
        if GPIO.input(22)==GPIO.LOW or GPIO.input(27)==GPIO.LOW:
            sm.current='menu'
            Clock.unschedule(self.chpic)

class PWDScreen(Screen):
    def press_am(self,txtn,val):
        if txtn=="bt1":
            cnum=int(self.pt1.text)
            if val>0:
                if cnum<9:
                    self.pt1.text=str(cnum+val)
                else:
                    self.pt1.text='0'
            elif val<0:
                if cnum>0:
                    self.pt1.text=str(cnum+val)
                else:
                    self.pt1.text='9'
        elif txtn=="bt2":
            cnum=int(self.pt2.text)
            if val>0:
                if cnum<9:
                    self.pt2.text=str(cnum+val)
                else:
                    self.pt2.text='0'
            elif val<0:
                if cnum>0:
                    self.pt2.text=str(cnum+val)
                else:
                    self.pt2.text='9'
        elif txtn=="bt3":
            cnum=int(self.pt3.text)
            if val>0:
                if cnum<9:
                    self.pt3.text=str(cnum+val)
                else:
                    self.pt3.text='0'
            elif val<0:
                if cnum>0:
                    self.pt3.text=str(cnum+val)
                else:
                    self.pt3.text='9'
        elif txtn=="bt4":
            cnum=int(self.pt4.text)
            if val>0:
                if cnum<9:
                    self.pt4.text=str(cnum+val)
                else:
                    self.pt4.text='0'
            elif val<0:
                if cnum>0:
                    self.pt4.text=str(cnum+val)
                else:
                    self.pt4.text='9'
        elif txtn=="bt5":
            cnum=int(self.pt5.text)
            if val>0:
                if cnum<9:
                    self.pt5.text=str(cnum+val)
                else:
                    self.pt5.text='0'
            elif val<0:
                if cnum>0:
                    self.pt5.text=str(cnum+val)
                else:
                    self.pt5.text='9'
        elif txtn=="bt6":
            cnum=int(self.pt6.text)
            if val>0:
                if cnum<9:
                    self.pt6.text=str(cnum+val)
                else:
                    self.pt6.text='0'
            elif val<0:
                if cnum>0:
                    self.pt6.text=str(cnum+val)
                else:
                    self.pt6.text='9'
        elif txtn=="bt7":
            cnum=int(self.pt7.text)
            if val>0:
                if cnum<9:
                    self.pt7.text=str(cnum+val)
                else:
                    self.pt7.text='0'
            elif val<0:
                if cnum>0:
                    self.pt7.text=str(cnum+val)
                else:
                    self.pt7.text='9'
        elif txtn=="bt8":
            cnum=int(self.pt8.text)
            if val>0:
                if cnum<9:
                    self.pt8.text=str(cnum+val)
                else:
                    self.pt8.text='0'
            elif val<0:
                if cnum>0:
                    self.pt8.text=str(cnum+val)
                else:
                    self.pt8.text='9'

    def press_back(self):
        global watch_dog
        watch_dog=1
        sm.current='menu'
        pass
        
    def press_submit(self):
        if  self.pt1.text!='2' or \
            self.pt2.text!='0' or \
            self.pt3.text!='9' or \
            self.pt4.text!='7' or \
            self.pt5.text!='9' or \
            self.pt6.text!='3' or \
            self.pt7.text!='8' or \
            self.pt8.text!='9':

            self.lbe.text='密码错误'
            return;
        sm.current='settings'
        pass
       

class SettingsScreen(Screen):

    def on_text(self, value):
        #save_set()
        pass

    def press_save(self):
        global watch_dog
        watch_dog=1
        myscr.lbtime2.text=setscr.time2.text
        myscr.lbtime5.text=setscr.time5.text
        save_set()
        sm.current='menu'
        pass

    def press_am(self,txtn,val):
        #global watch_dog
        #watch_dog=1
        if txtn=="time1":
            cnum=int(self.time1.text)
            if val>0:
                if cnum<999:
                    self.time1.text=str(cnum+val)
            elif val<0:
                if cnum>0:
                    self.time1.text=str(cnum+val)
        elif txtn=="time2":
            cnum=int(self.time2.text)
            if val>0:
                if cnum<999:
                    self.time2.text=str(cnum+val)
            elif val<0:
                if cnum>0:
                    self.time2.text=str(cnum+val)
        elif txtn=="time3":
            cnum=int(self.time3.text)
            if val>0:
                if cnum<999:
                    self.time3.text=str(cnum+val)
            elif val<0:
                if cnum>0:
                    self.time3.text=str(cnum+val)
        elif txtn=="time4":
            cnum=int(self.time4.text)
            if val>0:
                if cnum<999:
                    self.time4.text=str(cnum+val)
            elif val<0:
                if cnum>0:
                    self.time4.text=str(cnum+val)
        elif txtn=="time5":
            cnum=int(self.time5.text)
            if val>0:
                if cnum<999:
                    self.time5.text=str(cnum+val)
            elif val<0:
                if cnum>0:
                    self.time5.text=str(cnum+val)
        elif txtn=="time6":
            cnum=int(self.time6.text)
            if val>0:
                if cnum<999:
                    self.time6.text=str(cnum+val)
            elif val<0:
                if cnum>0:
                    self.time6.text=str(cnum+val)
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
        if txtn=="txt3":
            cnum=int(self.txt3.text)
            if val>0:
                if cnum<99:
                    self.txt3.text=str(cnum+val)
            elif val<0:
                if cnum>0:
                    self.txt3.text=str(cnum+val)
        pass

    def press_set(self):
        #sm.current='settings'
        sm.current='pwdscr'
        pwdscr.pt1.text='0'
        pwdscr.pt2.text='0'
        pwdscr.pt3.text='0'
        pwdscr.pt4.text='0'
        pwdscr.pt5.text='0'
        pwdscr.pt6.text='0'
        pwdscr.pt7.text='0'
        pwdscr.pt8.text='0'
        pwdscr.lbe.text=''
        pass

    def press_tgb(self):
        if self.tgbtn.state == "down" and self.r_sta==False:
            self.tgbtn.text='运行中'
        else:
            print ("tgbtn off")
            self.tgbtn.text='停止中'
            self.tgbtn.state = "normal"
            self.txt3.text='1'

    def sch_m1(self,dt):
        print("sch_m1 done: ",datetime.datetime.now())
        GPIO.output(io_jx3, GPIO.LOW)
        GPIO.output(io_jx4, GPIO.LOW)
        Clock.schedule_once(self.sch_m2,int(setscr.time2.text)/10)
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
        Clock.schedule_once(self.sch_m5,int(setscr.time5.text)/10)
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
        #self.time2.disabled=False
        #setscr.time3.disabled=False
        #setscr.time4.disabled=False
        #self.time5.disabled=False
        self.txt3.disabled=False
        self.setbtn.disabled=False
        count=int(self.txt3.text)
        if count>0:
            count=count-1
        self.txt3.text=str(count)
        myTM1650.L('  ')
        myTM1650.R(self.txt3.text)
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
                self.tgbtn.text='已停止, 点击运行'
                return 0
            if GPIO.input(24)==GPIO.HIGH:
                self.tgbtn.state='normal'
                self.tgbtn.text='已停止, 点击运行'
                return 0
            self.r_sta=True
            self.btnb1.disabled=True
            self.btnb2.disabled=True
            self.btnb3.disabled=True
            #setscr.time1.disabled=True
            #self.time2.disabled=True
            #setscr.time3.disabled=True
            #setscr.time4.disabled=True
            #self.time5.disabled=True
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

        if GPIO.input(4)!=GPIO.LOW:
            myTM1650.OK=0
        else:
            if myTM1650.OK==0:
                myTM1650.on()

        #manual +5 and start
        if GPIO.input(22)==GPIO.LOW:
            if self.key_delay2==0:
                if int(self.txt3.text)<95:
                    self.txt3.text=str(int(self.txt3.text)+5)
                myTM1650.L('--')
                myTM1650.R(self.txt3.text)
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
                if int(self.txt3.text)<99:
                    self.txt3.text=str(int(self.txt3.text)+1)
                myTM1650.L('--')
                myTM1650.R(self.txt3.text)
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
            self.tgbtn.text='停止中'
            self.tgbtn.state = "normal"
            self.txt3.text='0'
            if self.r_sta==True:
                myTM1650.L('__')
            myTM1650.R('0')

        try:
            if int(self.txt3.text)==0:
                self.tgbtn.state='normal'
                self.tgbtn.text='已停止, 点击运行'
        except:
            self.tgbtn.state='normal'
            self.tgbtn.text='已停止, 点击运行'

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
pwdscr=PWDScreen(name='pwdscr')
sm.add_widget(pwdscr)

setscr.time1.text=s1
setscr.time3.text=s3
setscr.time4.text=s4
setscr.time6.text=s6
setscr.time2.text=s2
setscr.time5.text=s5
myscr.lbtime2.text=s2
myscr.lbtime5.text=s5

myTM1650=TM1650()

class TestApp(App):
    def build(self):
        sescr.getfile()
        Clock.schedule_interval(myscr.update_sta,1/15)
        Clock.schedule_interval(sescr.update_sta,1/15)
        return sm

if __name__ == '__main__':
    TestApp().run()
