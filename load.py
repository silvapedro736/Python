from graphics import *

def loadingCallBack(p, red, green, size, game):

    while True:

                              
            for i in range(len(p) / 10):
                point = Rectangle(p[i][0], p[i][1])
                if p[i][2] == 0:
                    point.setFill(red)
                if p[i][2] == 1:
                    point.setFill(green)

                point2 = Rectangle(p[i + size][0], p[i + size][1])
                if p[i + size][2] == 0:
                    point.setFill(red)
                if p[i + size][2] == 1:
                    point.setFill(green)

                point3 = Rectangle(p[i + (2 * size)][0], p[i + (2 * size)][1])
                if p[i + (2 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (2 * size)][2] == 1:
                    point.setFill(green)

                point4 = Rectangle(p[i + (3 * size)][0], p[i + (3 * size)][1])
                if p[i + (3 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (3 * size)][2] == 1:
                    point.setFill(green)

                point5 = Rectangle(p[i + (4 * size)][0], p[i + (4 * size)][1])
                if p[i + (4 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (4 * size)][2] == 1:
                    point.setFill(green)

                point6 = Rectangle(p[i + (5 * size)][0], p[i + (5 * size)][1])
                if p[i + (5 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (5 * size)][2] == 1:
                    point.setFill(green)

                point7 = Rectangle(p[i + (6 * size)][0], p[i + (6 * size)][1])
                if p[i + (6 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (6 * size)][2] == 1:
                    point.setFill(green)

                point8 = Rectangle(p[i + (7 * size)][0], p[i + (7 * size)][1])
                if p[i + (7 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (7 * size)][2] == 1:
                    point.setFill(green)

                point9 = Rectangle(p[i + (8 * size)][0], p[i + (8 * size)][1])
                if p[i + (8 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (8 * size)][2] == 1:
                    point.setFill(green)

                point10 = Rectangle(p[i + (9 * size)][0], p[i + (9 * size)][1])
                if p[i + (9 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (9 * size)][2] == 1:
                    point.setFill(green)

                point11 = Rectangle(p[i + (10 * size)][0], p[i + (10 * size)][1])
                if p[i + (10 * size)][2] == 0:
                    point.setFill(red)
                if p[i + (10 * size)][2] == 1:
                    point.setFill(green)

                    
                point.draw(game)
                point2.draw(game)
                point3.draw(game)
                point4.draw(game)
                point5.draw(game)
                point6.draw(game)
                point7.draw(game)
                point8.draw(game)
                point9.draw(game)
                point10.draw(game)
                point11.draw(game)
