﻿# gpmb

gpmb with kivy

两个个屏幕，一个屏幕为控制，另一个屏幕为图片展示。
逻辑已经完成，5个定时。
只要修改进入屏保，屏保切换延迟即可。


要装的程序


$ sudo apt-get update

$ sudo apt-get upgrade

sudo apt-get install xrdp xclip viewnior ttf-wqy-zenhei ttf-wqy-microhei
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo pip3 install pexpect aiohttp aiohttp_jinja2


直接在图形界面设置:固定IP

raspi-config:选择zh_CN.UTF-8, UTC=HongKong



#开机运行Python脚本的方法
在 /home/pi/.config 下创建一个文件夹，名称为 autostart，并在该文件夹下创建一个xxx.desktop文件（文件名以.desktop结尾，前面可以自定义），文件内容如下：

[Desktop Entry]

Name=lmf

Comment=My Python Program

Exec=python3 /home/pi/lmf/lmfv7.py

Icon=/home/pi/lmf/imagetmb/004.7.04.jpg

Terminal=false

MultipleArgs=false

Type=Application

Categories=Application;Development;

StartupNotify=true


#samba与PC文件共享
sudo apt-get install samba samba-common-bin

sudo leafpad /etc/samba/smb.conf

[homes]

   browseable = yes

   read only = no

   create mask = 0755

   directory mask = 0755

增加samba用户：
sudo smbpasswd -a pi

输入两次密码

重启samba服务：
/etc/init.d/samba restart
or
sudo service samba restart


禁用屏保和休眠

/etc/lightdm/lightdm.conf

- locate [Seat Defaults] section
- edit existing line "#xserver-command=X"
and change text to

xserver-command=X -s o -dpms

或者安装xscreensaver，然后在系统设置里面禁用屏保


#feh-小巧的查看图片工具

feh -Y -x -q -D 5 -B black -F -Z -z -r /media/
man feh
-Z Auto Zoom

-x Borderless

-F Fullscreen

-Y hide pointer

-B image background

-q quiet no error reporting

-z Randomise

-r Recursive search all folders in folders

-D Slide delay in seconds

vkeyboard 行662 改字体
/usr/local/lib/python3.4/dist-packages/kivy/uix/vkeyboard.py

config.ini
keyboard_mode = dock


旋转屏幕
/home/pi/.kivy/config.ini line 24 ratation=>90

sudo leafpad /boot/config.txt
display_rotate=0 Normal
display_rotate=1 90 degrees
display_rotate=2 180 degrees
display_rotate=3 270 degrees

$ sudo apt-get install xinput

xinput --list
(if you're on the Rasp Pi via SSH)
    DISPLAY=:0 xinput --list


/HOME/PI下面创建文件 rot.sh ，内容为

#!/bin/bash
xinput set-prop 'FT5406 memory based driver' 'Evdev Axes Swap' 1
xinput --set-prop 'FT5406 memory based driver' 'Evdev Axis Inversion' 0 1


赋予rot.sh执行权限！！！
sudo chmod 755 /home/pi/rot.sh


sudo leafpad /home/pi/.config/lxsession/LXDE-pi/autostart
加入一行
@/home/pi/rot.sh