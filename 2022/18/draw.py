
def savefig(cubes, serial=0):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import os
    import glob
    
    
    # remove plot if it exists already    
    try:
        fl = glob.glob("plot"+"{:04d}".format(serial)+".png")
                       
        for fp in fl:
            try:
                os.remove(fp)
            except:
                pass
    except:
        pass
    c=0

    ax = plt.figure().add_subplot(projection='3d')
    plt.xlabel("x")
    plt.ylabel("y")
    #        plt.zlabel("x")
    
    ax.voxels(cubes)
    plt.savefig("plot"+"{:04d}".format(serial)+".png")
        
        
