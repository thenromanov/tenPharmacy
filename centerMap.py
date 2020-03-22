import sys


def getCenter(*coords):
    xs = [float(coord[0]) for coord in coords]
    ys = [float(coord[1]) for coord in coords]
    return [sum(xs) / len(xs), sum(ys) / len(ys)]


def main():
    try:
        data = sys.argv[1:]
        coords = [tuple([data[i], data[i + 1]]) for i in range(0, len(data), 2)]
        print(', '.join(map(str, getCenter(*coords))))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
