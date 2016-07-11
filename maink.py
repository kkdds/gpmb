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
import configparser

kconfig=configparser.ConfigParser()
kconfig.read('/home/pi/gpmb/'+"set.ini")
s1=kconfig.get("gpmb","s1")
s2=kconfig.get("gpmb","s2")
s3=kconfig.get("gpmb","s3")
s4=kconfig.get("gpmb","s4")
s5=kconfig.get("gpmb","s5")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
io_jx1=21
io_jx2=20
io_jx3=16
io_jx4=26
io_jx5=19
io_jx6=13
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
io_gt=io_jx1 #滚筒
io_sb=io_jx2 #水泵
io_ld=io_jx3 #漏斗

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

    def save_set(self):
        kconfig.set("gpmb","s1",self.time1.text)
        kconfig.set("gpmb","s2",self.time2.text)
        kconfig.set("gpmb","s3",self.time3.text)
        kconfig.set("gpmb","s4",self.time4.text)
        kconfig.set("gpmb","s5",self.time5.text)
        kconfig.write(open('/home/pi/gpmb/'+"set.ini","w"))
        print("saved "+self.time1.text)
        pass

    def on_focus(self):
        sm.current_screen.watch_dog=1
        pass

    def on_text(self, value):
        self.save_set()
        pass

    def press_btn_b1(self,val):
        print("b1 1: ",val.pos[0])
        self.watch_dog=1
        GPIO.output(io_gt, GPIO.LOW)
        pass
    def release_btn_b1(self,val):
        print("b1 0: ",val.pos[0])
        self.watch_dog=1
        GPIO.output(io_gt, GPIO.HIGH)
        pass

    def press_btn_b2(self,val):
        print("b2 1: ",val.pos[0])
        self.watch_dog=1
        GPIO.output(io_sb, GPIO.LOW)
        pass
    def release_btn_b2(self,val):
        print("b2 0: ",val.pos[0])
        self.watch_dog=1
        GPIO.output(io_sb, GPIO.HIGH)
        pass

    def press_btn_b3(self,val):
        print("b3 1: ",val.pos[0])
        self.watch_dog=1
        GPIO.output(io_ld, GPIO.LOW)
        pass
    def release_btn_b3(self,val):
        print("b3 0: ",val.pos[0])
        self.watch_dog=1
        GPIO.output(io_ld, GPIO.HIGH)
        pass

    def press_tgb(self):
        if self.tgbtn.state == "down" and self.r_sta==False:
            self.tgbtn.text='运行中'
            GPIO.output(io_jx4, GPIO.LOW)
        else:
            print ("tgbtn off")
            self.tgbtn.text='已停止'
            self.tgbtn.state = "normal"
            self.txt3.text='1'

    def sch_m1(self,dt):            
        print("sch_m1 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m2,int(self.time2.text)/10)
        GPIO.output(io_jx5, GPIO.LOW)
        pass

    def sch_m2(self,dt):
        print("sch_m2 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m3,int(self.time3.text))
        GPIO.output(io_jx6, GPIO.LOW)
        pass

    def sch_m3(self,dt):
        print("sch_m3 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_m4,int(self.time4.text)/2)
        GPIO.output(io_jx7, GPIO.LOW)
        pass

    def sch_m4(self,dt):
        print("sch_m4 done: ",datetime.datetime.now())
        Clock.schedule_once(self.sch_fin,int(self.time5.text)/2)
        GPIO.output(io_jx8, GPIO.LOW)
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
        GPIO.output(io_jx4, GPIO.HIGH)
        GPIO.output(io_jx5, GPIO.HIGH)
        GPIO.output(io_jx6, GPIO.HIGH)
        GPIO.output(io_jx7, GPIO.HIGH)
        GPIO.output(io_jx8, GPIO.HIGH)

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
        if self.watch_dog>1600:
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

myscr.time1.text=s1
myscr.time2.text=s2
myscr.time3.text=s3
myscr.time4.text=s4
myscr.time5.text=s5

class TestApp(App):
    def build(self):        
        sescr.getfile()
        Clock.schedule_interval(myscr.update_sta,1/15)
        return sm

if __name__ == '__main__':
    TestApp().run()
