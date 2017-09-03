#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 15:36:28 2017

@author: Anderson Banihirwe

Simple Particle Swarm Optimization (PSO) 
"""

import random 
import math
import time
import numpy as np

#---------- COST FUNCTION -----------------------------#

# function to optimize (minimize)
def cost_func(x):
    total = 0.0
    for i in range(len(x)):
        total += x[i]**2
        
    return total



#------------MAIN----------------------------------------#

class Particle:
    def __init__(self, x0):
        self.position_i       = []      # particle position
        self.velocity_i       = []      # particle velocity
        self.pos_best_i       = []      # best position individual
        self.error_best_i     = -1      # best error individual
        self.error_i          = -1      # error individual
        
        
        for i in range(0, ndims):
            self.velocity_i.append(random.uniform(-1,1))
            self.position_i.append(x0[i])
    
    # evaluate current fitness
    def evaluate_fitness(self, costFunc):
        self.error_i = costFunc(self.position_i)
        
        # Check to see if the current position is an individual best
        if self.error_i < self.error_best_i or self.error_best_i == -1:
            self.pos_best_i     = self.position_i
            self.error_best_i   = self.error_i
            
            
    # update new particle velocity
    def update_velocity(self, pos_best_g):
        w   =  0.5         # constant inertia weight (how much to weigh the previous velocity)
        c1  = 1            # cognitive constant 
        c2  = 2            # social constant
        
        for i in range(0, ndims):
            r1 = random.random()
            r2 = random.random()
            
            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social    = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social
            
            
    # update the particle position based off new velocity updates
    def update_position(self, bounds):
        
        for i in range(0, ndims):
            self.position_i[i]   += self.velocity_i[i]
            
            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]
                
                
            # adjust minimum position if necessary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = bounds[i][0]
                
                
class PSO():
    def __init__(self, costFunc, x0, bounds, nparticles, maxiter):
        global ndims
        
        ndims = len(x0)
        error_best_g = -1               # best error for group
        pos_best_g   = []               # best position for group
        
        # establish the swarm
        swarm = []
        for i in range(0, nparticles):
            swarm.append(Particle(x0))
          
        # Find the time it takes to find the solution
        
        t0 = time.clock()
        # Begin optimization loop
        i = 0
        while i < maxiter:
            
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, nparticles):
                swarm[j].evaluate_fitness(costFunc)
                
                # Determine if current particle is globally the best
                if swarm[j].error_i < error_best_g or error_best_g == -1:
                    pos_best_g     = list(swarm[j].position_i)
                    error_best_g   = float(swarm[j].error_i)
                    
                    
            # cycle through swarm and update velocities and positions
            for j in range(0, nparticles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
                
            i+= 1
        t1 = time.clock()
        
        # Final Results
        print("---Optimal solution found in {:.3f} secs for {} particles\n".format(t1 - t0, nparticles))
        print("Best position : {}".format(pos_best_g))
        print("Best Error    :  {}".format(error_best_g))
        print("-------------------------------------------------------")
            
            
if __name__ == "__main__":
    
    initial = [5, 5]
    bounds  = [(-10, 10), (-10, 10)]
    PSO(cost_func, initial, bounds, nparticles=1000, maxiter=100)
            
            