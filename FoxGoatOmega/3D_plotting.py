import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import math

def plane():
    Lx=[]
    Ly=[]
    Lz=[]
    x=-1
    while x<=1:
        y=-1
        while y<=1:
            z=math.sqrt(100-x**2-y**2)
            Lx.append(x)
            Ly.append(y)
            Lz.append(z)

            y+=0.1
        x+=0.1


    fig=plt.figure()
    ax=plt.axes(projection='3d')
    ax.scatter(Lx,Ly,Lz,color="red")
    plt.show()

    

    
    

