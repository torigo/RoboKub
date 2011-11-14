#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       battle_field.py
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

class battle_field():
    field_size = [500,500]
    field_name = 'Поле брани'
    field = 0
    robots = []

    def __init__(self):
        pygame.init()
        self.field = pygame.display.set_mode(self.field_size)
        pygame.display.set_caption(self.field_name)

    def set_size (self, x, y):
        self.field_size = [x,y]
        field=pygame.display.set_mode(self.field_size)

    def set_name (self, name):
        self.field_name = name
        pygame.display.set_caption(self.field_name)

    def add_robot(self, robot):
        '''
        Метод принимает ссылку на объект robot
        '''
        trobo = robot(self.field)
        print self.robots
        if not self.robots:
            print 'ok'
            trobo.set_position(6,6) # стартовая координата робота, заменить на функцию
        else:
            x,y = self.robots[-1].position
            trobo.set_position(x+20,y+20)

        self.robots.append(trobo)
        print self.robots[0].position

    def begin_battle(self):
        '''
        Запускает битву между роботами (бесконечный цикл, пока не останется один)
        '''
        alive_robots = 2
        while alive_robots > 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive_robots = 0

            alive_robots = len(self.robots)

            for i in range(alive_robots):
                if self.robots[i].hp == 0:
                    del(self.robots[i])
                else:
                    self.robots[i].turn()

            pygame.display.flip()

def main():
    from robot import robot

    x = battle_field()
    x.add_robot(robot)
    x.add_robot(robot)
    x.begin_battle()

    return 0

if __name__ == '__main__':
    main()

