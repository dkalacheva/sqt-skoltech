# This file is not a part of QuTiP toolbox
###############################################################################

import matplotlib.animation as animation
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import display, HTML

def plot_animation(result, sphere, interval=100, repeat=False, engine="jshtml"):
    """Create an animated plot of a Result object, as returned by one of
    the qutip evolution solvers.
    
    Args:
        result (obj): result object returned by qutip evolutionary solver
        sphere (obj): qutip.Bloch instance to plot the result
        interval (int): Delay between frames in milliseconds. Defaults to 100.
        repeat (bool): Indicates whether to loop animation. Defaults to False.
        engine (str): jshtml or html5. Engine to produce animation. Defaults to jshtml.

    """
        
    sphere.points = []
    sphere.point_style = []
    sphere.make_sphere()

    def update_graph(num):
        sphere.points = []
        sphere.point_style = []
        sphere.add_points([result.expect[0][:num+1], result.expect[1][:num+1],
                           result.expect[2][:num+1]], meth='l')
        sphere.make_sphere()
        return sphere.axes.artists

    anim = animation.FuncAnimation(
        sphere.fig, update_graph, frames=len(result.times), blit=True,
        interval=interval, repeat=False)
    
    context_dic = {
        "animation.html": engine,
        "animation.embed_limit": 2**32
    }
    
    if engine == "html5":
        context_dic["animation.writer"] = "ffmpeg"
    
    with plt.rc_context(context_dic):
        if engine == "html5":
            html_obj = HTML(anim.to_html5_video())
        else:
            html_obj = HTML(anim.to_jshtml())
           
        plt.close(anim._fig)
        display(html_obj)
