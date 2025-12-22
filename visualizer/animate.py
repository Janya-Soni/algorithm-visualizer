import matplotlib.pyplot as plt
def draw_array(ar, highlight_indices=None):
    plt.clf()
    colour=["blue"]*len(ar)
    if highlight_indices:
        for i in highlight_indices:
            colour[i]="red"
    plt.bar(range(len(ar)),ar, color=colour)
    plt.pause(0.1)