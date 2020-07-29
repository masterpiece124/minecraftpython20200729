# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:33:01 2020

@author: user
"""
#小挑戰:只能打到石頭才能變金礦

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    hits=mc.events.pollBlockHits()
    #判斷方塊是不是被打到
    if len (hits)>0:
        block=hits[0]
        x,y,z=block.pos.x,block.pos.y,block.pos.z
        mc.setBlock(x,y,z,46)