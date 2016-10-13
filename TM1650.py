#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smbus
import time

class TM1650(object):
    NumTab={
    '0':0x3F,
    '1':0x06,
    '2':0x5B,
    '3':0x4F,
    '4':0x66,
    '5':0x6D,
    '6':0x7D,
    '7':0x07,
    '8':0x7F,
    '9':0x6F,
    '.':0x80,
    ' ':0x00,
    '-':0x40,
    '_':0x08
    }
    bus=object

    def __init__(self):
        # open /dev/i2c-1
        self.bus = smbus.SMBus(1)
        self.bus.write_byte( 0x27 , 0x05 )
        # set brightness 8 highest , 8 point 0x05
        self.bus.write_byte( 0x34 , 0x00)
        self.bus.write_byte( 0x35 , 0x00)
        self.bus.write_byte( 0x36 , self.NumTab['0'])
        self.bus.write_byte( 0x37 , 0x00)

    def L(self,schar):
        # open /dev/i2c-1
        # self.bus = smbus.SMBus(1)
        # set brightness 8 highest , 8 point 0x05
        # self.bus.write_byte( 0x27 , 0x05 )
        self.bus.write_byte( 0x34 , self.NumTab[schar[0]])
        self.bus.write_byte( 0x37 , self.NumTab[schar[1]])
        pass
            
    def R(self,schar):
        # open /dev/i2c-1
        # self.bus = smbus.SMBus(1)
        # set brightness 8 highest , 8 point 0x05
        # self.bus.write_byte( 0x27 , 0x05 )
        # clear screen
        if schar=='  ':
            self.bus.write_byte( 0x35 , 0x00)
            self.bus.write_byte( 0x36 , 0x00)
            return

        if int(schar)<10:
            schar=' '+schar
        self.bus.write_byte( 0x35 , self.NumTab[schar[0]])
        self.bus.write_byte( 0x36 , self.NumTab[schar[1]])
        pass
            
    def _test(self):
        while True:
            self.bus.write_byte( 0x34 , self.NumTab['0'] )
            self.bus.write_byte( 0x35 , self.NumTab['1']|self.NumTab['.'])
            self.bus.write_byte( 0x36 , self.NumTab['2'] )
            self.bus.write_byte( 0x37 , self.NumTab['3'] )
            time.sleep(0.1)
            self.bus.write_byte( 0x34 , self.NumTab['4'] )
            self.bus.write_byte( 0x35 , self.NumTab['5'] )
            self.bus.write_byte( 0x36 , self.NumTab['6'] )
            self.bus.write_byte( 0x37 , self.NumTab['7'] )
            time.sleep(0.1)
            self.bus.write_byte( 0x34 , self.NumTab['8'] )
            self.bus.write_byte( 0x35 , self.NumTab['9'] )
            self.bus.write_byte( 0x36 , self.NumTab['.'])
            self.bus.write_byte( 0x37 , self.NumTab['8'] )
            time.sleep(0.1)
        pass

