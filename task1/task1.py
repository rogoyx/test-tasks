import functools
import math
import sys


def get_percentile(array, percent):
    if not array:
        return None
    k = (len(array)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return array[int(k)]
    d0 = array[int(f)] * (c-k)
    d1 = array[int(c)] * (k-f)
    return d0+d1


def get_median(array):
    median = 0.0
    if len(array) % 2 == 0:
        median = array[int(((len(array) / 2) + ((len(array) + 1) / 2)) / 2)]
    else:
        median = array[int((len(array) + 1) / 2)]
    return median


def get_average(array):
    average = 0.0
    for i in array:
        average += i
    return average/len(array)


if __name__ == '__main__':
    file_name = sys.argv[1]
    text = []
    with open(file_name, 'rt') as f:
        text = [line.strip() for line in f.readlines()]
    if not text:
        raise Exception("File is empty")
    array = list(map(float, text))
    array.sort()
    percentile = get_percentile(array, 0.9)
    print(format(percentile, '.2f'))
    median = get_median(array)
    print(format(median, '.2f'))
    maximum = max(array)
    minimum = min(array)
    print(format(maximum, '.2f'))
    print(format(minimum, '.2f'))
    average = get_average(array)
    print(format(average, '.2f'))
