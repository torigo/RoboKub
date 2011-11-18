#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       robot.py
#
#       Copyright 2011 Alexandr Posazhennikov <elfjse@gmail.com>
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import pygame
from random import choice

class radar():
    pass

class robot():
    '''
    Основной интерфейс робота
    '''
    v_range = 0
    hp = 3 # Hit Point
    position = [0,0]
    color = [255,150,255]

    def __init__(self, field):
        self.field = field

    def set_position(self,x,y):
        #~ print self.field
        self.position = [x,y]
        pygame.draw.circle(self.field, self.color, self.position, 6)

    def move(self, coord):
        return 0

    def rmove(self):
        pX, pY = self.position

        def gran(p):
            s = 10
            t = [-s,s]
            bmin = 5
            bmax = 495
            if p > bmin and p < bmax:
                p += choice(t)
            elif p <= bmin:
                p += s
            elif p >= bmax:
                p += -s

            return p

        x = gran(pX)
        y = gran(pY)
        self.set_position(x,y)

    def turn(self):
        '''
        Метод описывает ход робота
        '''
        self.rmove()
        return 0

    def shoot(self):
        '''
        Метод описывает стрельбу
        '''
        return 0



if __name__ == '__main__':
    pass #main()

