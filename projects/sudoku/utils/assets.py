#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:15:04 2017

@author: Anderson Banihirwe
"""

import os
import pygame

def load_image(name):
    fullpath = os.path.join("images", name)
    try:
        image = pygame.image.load(fullpath)
        if image.get_alpha() == None:
            image = image.convert()
            
        else:
            image = image.convert_alpha()
            
        
    except pygame.error:
        print("Oops! Could not load image:", fullpath)
        
    return image, image.get_rect()
