import sys


def getScale(*corners):
    lowerCorners = [tuple(map(float, corner[0])) for corner in corners]
    upperCorners = [tuple(map(float, corner[1])) for corner in corners]
    result = (max([upperCorner[0] for upperCorner in upperCorners]) - min([lowerCorner[0] for lowerCorner in lowerCorners]),
              max([upperCorner[1] for upperCorner in upperCorners]) - min([lowerCorner[1] for lowerCorner in lowerCorners]))
    return result


def main():
    try:
        data = sys.argv[1:]
        coords = [tuple([float(data[i]), float(data[i + 1])]) for i in range(0, len(data), 2)]
        coords = [[coords[i], coords[i + 1]] for i in range(0, len(coords), 2)]
        print(', '.join(map(str, getScale(*coords))))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
