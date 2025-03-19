import matplotlib.pyplot as plt
import numpy as np


def f_triangular(dom, points, x):

    start=dom[0]
    end=dom[1]
    p1=points[0]
    p2=points[1]
    p3=points[2]

    if start<=x<=p1:
        sol=0
    if p1<x<=p2:
        sol=(x-p1)/(p2-p1)
    if p2<x<=p3:
        sol=1-(x-p2)/(p3-p2)
    if p3<x<=end:
        sol=0

    return sol

def f_trapezoid(dom, points, x):

    start=dom[0]
    end=dom[1]
    p1=points[0]
    p2=points[1]
    p3=points[2]
    p4=points[3]

    if start<=x<=p1:
        sol=0
    if p1<x<=p2:
        sol=(x-p1)/(p2-p1)
    if p2<x<=p3:
        sol=1
    if p3<x<=p4:
        sol=1-(x-p3)/(p4-p3)
    if p4<x<=end:
        sol=0

    return sol

def plot_members(dom,list_points):

    for i in range(0,len(list_points)):
        points=list_points[i]

        if len(points)==3:

            x=np.linspace(dom[0],dom[1],1000)
            y=[f_triangular(dom,points,a) for a in x]
            plt.plot(x, y)

        if len(points)==4:

            x=np.linspace(dom[0],dom[1],1000)
            y=[f_trapezoid(dom,points,a) for a in x]
            plt.plot(x, y)

    plt.show()
    return