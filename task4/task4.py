import sys


def time_to_int(t):
    t1, t2 = t.split(":")
    return int(t1 + t2)


def interval_merging(array):
    intervals = []
    for higher in array:
        if not intervals:
            intervals.append(higher)
        else:
            lower = intervals[-1]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                intervals[-1] = [lower[0], upper_bound]
            else:
                intervals.append(higher)
    return intervals


if __name__ == '__main__':
    file_name = sys.argv[1]
    times = []
    with open(file_name, "rt") as f:
        for line in f.readlines():
            t1, t2 = line.split(" ")
            t1 = time_to_int(t1)
            t2 = time_to_int(t2)
            times.append((t1, "s"))
            times.append((t2, "f"))

    times.sort(key=lambda x: x[0])
    current = 0
    visitors = []
    max_visitors = 0
    for t in times:
        if t[1] == "s":
            current += 1
            visitors.append((t[0], current))
        else:
            current -= 1
            visitors.append((t[0], current))
        if current > max_visitors:
            max_visitors = current

    sections = []
    section = []
    f = False
    for v in visitors:
        if v[1] == max_visitors and not f:
            section.append(v[0])
            f = True
        elif f and v[1] != max_visitors:
            section.append(v[0])
            sections.append(section)
            section = []
            f = False

    merge_sections = interval_merging(sections)

    for i in range(len(merge_sections)):
        for j in range(2):
            merge_sections[i][j] = str(merge_sections[i][j])
            merge_sections[i][j] = merge_sections[i][j][0] + ":" + merge_sections[i][j][1:]

    for row in merge_sections:
        print("{} {}".format(row[0], row[1]))
