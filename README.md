# gpmb

gpmb with kivy


要装的程序


$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt-get install xrdp xclip viewnior ttf-wqy-zenhei

$ sudo apt-get install python-rpi.gpio python3-rpi.gpio

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

