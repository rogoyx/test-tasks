import os
import sys


if __name__ == '__main__':
    directory_name = sys.argv[1]
    file_name1 = os.path.join(directory_name, "Cash1.txt")
    file_name2 = os.path.join(directory_name, "Cash2.txt")
    file_name3 = os.path.join(directory_name, "Cash3.txt")
    file_name4 = os.path.join(directory_name, "Cash4.txt")
    file_name5 = os.path.join(directory_name, "Cash5.txt")

    text1 = []
    with open(file_name1, "rt") as f:
        text1 = [line.strip() for line in f.readlines()]
    if not text1:
        raise Exception("File is empty")
    cash1 = list(map(float, text1))

    text2 = []
    with open(file_name2, "rt") as f:
        text2 = [line.strip() for line in f.readlines()]
    if not text2:
        raise Exception("File is empty")
    cash2 = list(map(float, text2))

    text3 = []
    with open(file_name3, "rt") as f:
        text3 = [line.strip() for line in f.readlines()]
    if not text3:
        raise Exception("File is empty")
    cash3 = list(map(float, text3))

    text4 = []
    with open(file_name4, "rt") as f:
        text4 = [line.strip() for line in f.readlines()]
    if not text4:
        raise Exception("File is empty")
    cash4 = list(map(float, text4))

    text5 = []
    with open(file_name5, "rt") as f:
        text5 = [line.strip() for line in f.readlines()]
    if not text5:
        raise Exception("File is empty")
    cash5 = list(map(float, text5))

    sum_of_lines = []
    for i in range(16):
        sum_of_lines.append((cash1[i]+cash2[i]+cash3[i]+cash4[i]+cash5[i]))
    interval = sum_of_lines.index(max(sum_of_lines))+1
    print(interval)
