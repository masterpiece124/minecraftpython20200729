# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:45:23 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
#小挑戰:斜的道路(x軸)
x,y,z=mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x,y-1,z+i,46)