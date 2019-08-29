# Falola Yusuf, Github: falfat
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:51:29 2019

@author: falol
"""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111)
ax1.margins(0.1)

x = np.linspace(100, 500, 9)
square = np.array([0.0136627197265625, 0.017855834960937501, 
                   0.021271514892578124, 0.027868652343750001, 0.049776458740234376, 
                   0.059987640380859374, 0.067276763916015628, 0.075751495361328122, 
                   0.084228515625])
pentagon = np.array([0.014463043212890625, 0.024922180175781249,
                     0.038410186767578125, 0.053911590576171876, 0.057305145263671878, 
                     0.063529205322265622, 0.084172821044921881, 0.083993530273437506,
                     0.093072509765625006])
hexagon = np.array([0.018543243408203125, 0.024989318847656251, 
                     0.026175689697265626, 0.028702545166015624, 0.061986541748046874,
                     0.076688385009765631, 0.081553649902343747, 0.09069061279296875,
                     0.103717041015625])
heptagon = np.array([0.013310241699218749, 0.024720001220703124,
                      0.031475067138671875, 0.054514312744140626, 0.065634155273437494, 
                      0.076533508300781247, 0.089128112792968756, 0.096347045898437497,
                      0.10726242065429688])
circle = np.array([0.012801361083984376, 0.017919921875000001,
                    0.021068572998046875, 0.026520538330078124, 0.030735015869140625,
                    0.036123657226562501, 0.041535186767578128, 0.046557617187499997,
                    0.04956817626953125])
ellipse = np.array([0.020505523681640624, 0.027030181884765626, 
                    0.027912902832031249, 0.032617187499999999, 0.037120056152343747, 
                    0.049967193603515626, 0.051202392578124999, 0.058380889892578128, 
                    0.080847930908203122])
ax1.plot(x, square*1000, 'bo-', label='square')
ax1.plot(x, pentagon*1000, 'ro-', label='pentagon')
ax1.plot(x, hexagon*1000, 'go-', label='hexagon')
ax1.plot(x, heptagon*1000, 'mo-', label='heptagon')
ax1.plot(x, circle*1000, 'ko-', label='circle')
ax1.plot(x, ellipse*1000, 'yo-', label='ellipse')

plt.xlabel("number of fractures")
plt.ylabel("time (milli seconds)")
plt.title("average times for generating fracture network of different shapes")
# Add a legend
ax1.legend(loc='best', fontsize=14);
plt.savefig('timings')
plt.show()
