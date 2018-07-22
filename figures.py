import numpy as np, matplotlib.pyplot as plt, pandas as pd
from matplotlib import rcParams
from utils import *

params = {
   'axes.labelsize': 16,
    'axes.titlesize': 20,
   'font.size': 20,
   'legend.fontsize': 16,
   'xtick.labelsize': 13,
   'ytick.labelsize': 13,
   'text.usetex': False,
    'font.family':"sans-serif",
   'font.sans-serif':'Arial',
    'figure.facecolor': 'black',
    'savefig.facecolor': 'black',
    'axes.facecolor': 'black',   # axes background color
    
    "figure.edgecolor": "black",
    "savefig.edgecolor": "black",
    
   'text.usetex': False,

   }

plt.style.use(['dark_background'])
rcParams.update(params)

def figure2a():
    f, axs = plt.subplots(1,2,figsize=(8,4), facecolor='black')
    plt.rc("font",family="sans-serif",size=14)

    ax = axs[0]
    ax.axis('off')
    draw_neural_net(ax, .15, .9, .1, .85, [4, 1])
    ax.annotate('Network A', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top', size=15,);

    ax = axs[1]
    ax.axis('off')
    draw_neural_net(ax, .15, .9, .1, .85, [4, 1, 1])
    ax.annotate('Network B', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top', size=15,);    