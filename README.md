# gpmb

gpmb with kivy


Ҫװ�ĳ���


$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt-get install xrdp xclip viewnior ttf-wqy-zenhei

$ sudo apt-get install python-rpi.gpio python3-rpi.gpio

sudo pip3 install pexpect aiohttp aiohttp_jinja2


ֱ����ͼ�ν�������:�̶�IP

raspi-config:ѡ��zh_CN.UTF-8, UTC=HongKong



#��������Python�ű��ķ���
�� /home/pi/.config �´���һ���ļ��У�����Ϊ autostart�����ڸ��ļ����´���һ��xxx.desktop�ļ����ļ�����.desktop��β��ǰ������Զ��壩���ļ��������£�

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


#samba��PC�ļ�����
sudo apt-get install samba samba-common-bin

sudo leafpad /etc/samba/smb.conf

[homes]

   browseable = yes

   read only = no

   create mask = 0755

   directory mask = 0755

����samba�û���
sudo smbpasswd -a pi

������������

����samba����
/etc/init.d/samba restart
or
sudo service samba restart


��������������

/etc/lightdm/lightdm.conf

- locate [Seat Defaults] section
- edit existing line "#xserver-command=X"
and change text to

xserver-command=X -s o -dpms

���߰�װxscreensaver��Ȼ����ϵͳ���������������


#feh-С�ɵĲ鿴ͼƬ����

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


