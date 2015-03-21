from colorz import Color
import colorz

def letThemGo():
    return [
        Color(41, 33, 82),
        Color(20, 86, 99),
        Color(220, 42, 94),
        Color(249, 146, 79),
        Color(245, 243, 202)
    ]


def ulquiorra():
    return [
        Color(238, 241, 232),
        Color(167, 193, 170),
        Color(78, 131, 85),
        Color(57, 88, 82),
        Color(34, 51, 59)
    ]


def vivacious():
    [
        Color(204, 12, 57),
        Color(230, 120, 30),
        Color(200, 207, 2),
        Color(248, 252, 193),
        Color(22, 147, 167),
    ]


def randpallette(num):
    output = []
    for i in range(0, num):
        output.append(colorz.randcolor())
    return output


def main():
    print randpallette(7)

if __name__ == '__main__':
    main()
