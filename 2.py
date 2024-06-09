import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, len, ang, pers, depth):
    if depth ==0:
        return
    xx = x + len* np.cos(np.radians(ang))
    yy = y + len * np.sin(np.radians(ang))
    plt.plot([x, xx], [y, yy], color='green', linewidth=depth)
    
    len_next = len * pers  
    depth_next = depth - 1  
    draw_branch(xx, yy, len_next, ang - 20, pers, depth_next)  
    draw_branch(xx, yy, len_next, ang + 20, pers, depth_next)  




if __name__ == "__main__":

    depth = input ("Enter depth: ")


    plt.figure(figsize=(8,8))
    plt.axis('off')


    draw_branch(0, 0.5, 0.2, 90, 0.9, int(depth))

    plt.show()