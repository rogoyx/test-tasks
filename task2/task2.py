import sys


def position_points(x, y, figure):
    fig_x = figure[::2]
    fig_y = figure[1::2]
    if x in fig_x and y in fig_y:
        return 0
    elif ((x - fig_x[0]) * (fig_y[1] - fig_y[0]) == (y - fig_y[0]) * (fig_x[1] - fig_x[0]) and
          fig_x[0] <= x <= fig_x[1] and fig_y[0] <= y <= fig_y[1]) or \
            ((x - fig_x[1]) * (fig_y[2] - fig_y[1]) == (y - fig_y[1]) * (fig_x[2] - fig_x[1]) and
             fig_x[1] <= x <= fig_x[2] and fig_y[1] <= y <= fig_y[2]) or \
            ((x - fig_x[2]) * (fig_y[3] - fig_y[2]) == (y - fig_y[2]) * (fig_x[3] - fig_x[2]) and
             fig_x[2] <= x <= fig_x[3] and fig_y[2] <= y <= fig_y[3]) or \
            ((x - fig_x[3]) * (fig_y[0] - fig_y[3]) == (y - fig_y[3]) * (fig_x[0] - fig_x[3]) and
             fig_x[3] <= x <= fig_x[0] and fig_y[3] <= y <= fig_y[0]):
        return 1
    elif min(fig_x) < x < max(fig_x) and min(fig_y) < y < max(fig_y):
        return 2
    else:
        return 3


if __name__ == '__main__':
    file_name = sys.argv[1]
    text1 = []
    with open(file_name, "rt") as f:
        text1 = [line.strip() for line in f.readlines()]
    if not text1:
        raise Exception("File is empty")
    figure = [i.split() for i in text1]
    figure = [float(j) for i in figure for j in i]

    file_name = sys.argv[2]
    text2 = []
    with open(file_name, "rt") as f:
        text2 = [line.strip() for line in f.readlines()]
    if not text2:
        raise Exception("File is empty")
    points = [i.split() for i in text2]
    points = [float(j) for i in points for j in i]

    i = 0
    while True:
        try:
            print(position_points(points[i], points[i + 1], figure))
            i += 2
        except:
            break
