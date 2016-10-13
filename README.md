# gpmb

gpmb with kivy
3个屏幕，一个屏幕为控制，另一个屏幕为图片展示，一个为设置屏幕。
逻辑已经完成，5个定时。
只要修改进入屏保，屏保切换延迟即可。

sudo leafpad /etc/apt/sources.list
deb http://mirrors.aliyun.com/raspbian/raspbian/ jessie main non-free contrib
deb-src http://mirrors.aliyun.com/raspbian/raspbian/ jessie main non-free contrib

要装的程序
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y python3-smbus i2c-tools xrdp xclip feh ttf-wqy-zenhei ttf-wqy-microhei python-rpi.gpio python3-rpi.gpio samba-common-bin samba
sudo pip3 install pexpect aiohttp aiohttp_jinja2 configparser


直接在图形界面设置:固定IP
raspi-config:设置中文，设置时区，设置背景,关闭设置里接口


开机运行Python脚本
sudo pcmanfm 复制desktop文件到 /home/pi/.config/autostart


samba文件共享
sudo leafpad /etc/samba/smb.conf  
[homes]段
browseable = yes
read only = no
create mask = 0755
directory mask = 0755
增加samba用户
sudo smbpasswd -a pi 输入两次密码，重启
重启samba服务：
/etc/init.d/samba restart
or
sudo service samba restart

禁用屏保和休眠
sudo leafpad /etc/lightdm/lightdm.conf
- locate [Seat Defaults] section
- line "#xserver-command=X" to
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

vkeyboard 行662 改字体 为 80
sudo leafpad /home/pi/kivy/uix/vkeyboard.py
sudo leafpad /usr/local/lib/python3.4/dist-packages/kivy/uix/vkeyboard.py

Install Kivy
sudo apt-get update
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev cython
sudo pip3 install cython
sudo pip3 install git+https://github.com/kivy/kivy.git@master
sudo pip3 install pexpect


sudo leafpad /home/pi/.kivy/config.ini
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
