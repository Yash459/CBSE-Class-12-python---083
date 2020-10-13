"""
[+] Singleplayer
-Fix the inconsistency
-Scoring
-New game set option
-Scoring se winner
-Save game option
-Load Game
-New Main Menu
-Settings
-Add more sound tracks
-Admin controls
-Convert to .exe

[+] Multiplayer
-Multiplayer and singleplayer option
-Server code
-Clinet code
-Advanced internet options

[+] Mobile
"""


import turtle
import winsound
import pickle
import os
import threading


win = turtle.Screen()
win.screensize(300, 300)
win.bgcolor("black")
win.title("Tic Tak Toe")
win.update()
pen = turtle.Turtle()
pen.color("white")
pen.turtlesize(5)
size = 210
x, y = -size, -size
msg = None
win_boxes = []
screens = ["MainScreen", "SinglePlayerScreen"]
init_screen = screens[0]
MSButtons = {"singleplayer": {"x": [90, 50], "y": [120, -120]},
             "multiplayer": {"x": [0, -40], "y": [120, -120]},
             "setting": {"x": [-90, -130], "y": [120, -120]}}


def mainScreen():
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 160)
    pen.write("Tic Tak Toe", align = "center", font = ("Arial", 70, "normal"))
    pointsList = [[(120, 90), (120, 50), (-120, 50), (-120, 90), (120, 90)],
         [(120, 0), (120, -40), (-120, -40), (-120, 0), (120, 0)],
         [(120, -90), (120, -130), (-120, -130), (-120, -90), (120, -90)]]
    l = {(120, 50): "SINGLE PLAYER", (120, -40): "MUTLI PLAYER", (120, -130): "SETTINGS"}
    for points in pointsList:
        pen.penup()
        pen.goto(points[0])
        pen.pendown()
        pen.goto(points[1])
        pen.goto(points[2])
        pen.goto(points[3])
        pen.goto(points[4])
        pen.penup()
        pen.goto(0, points[1][1] + 5)
        pen.write(l[points[1]], align = "center", font = ("Arial", 20, "normal"))



def board(size, x, y, showturtle, animate = False):
    pen.hideturtle()
    if showturtle:
        pen.speed(3)
        pen.showturtle()
    pen.clear()
    if not(animate):
        for i in range(2):
            pen.penup()
            x += (2 * size)//3
            y += (2 * size)//3
            pen.goto(x,-size)
            pen.pendown()
            pen.goto(x, size)
            pen.penup()
            pen.goto(-size, y)
            pen.pendown()
            pen.goto(size, y)
            pen.penup()
    elif animate:
        pen1 = turtle.Turtle()
        pen2 = turtle.Turtle()
        pen3 = turtle.Turtle()
        pen4 = turtle.Turtle()
        pen1.penup()
        pen2.penup()
        pen3.penup()
        pen4.penup()
        x += (2 * size)//3
        y += (2 * size)//3
        pen1.goto(x,-size)
        pen1.pendown()
        pen1.goto(x, size)
        pen1.penup()
        pen1.hideturtle()
        pen2.goto(-size, y)
        pen2.pendown()
        pen2.goto(size, y)
        pen2.penup()
        pen2.hideturtle()
        x += (2 * size)//3
        y += (2 * size)//3
        pen3.goto(x,-size)
        pen3.pendown()
        pen3.goto(x, size)
        pen3.penup()
        pen3.hideturtle()
        pen4.goto(-size, y)
        pen4.pendown()
        pen4.goto(size, y)
        pen4.penup()
        pen4.hideturtle()


    pen.penup()
    pen.pensize(10)
    x, y = -size, -size
    pen.color("green")
    pen.goto(- size, -size)
    pen.pendown()
    pen.goto(-size, size)
    pen.goto(size, size)
    pen.goto(size, - size)
    pen.goto(-size, -size)
    pen.penup()
    pen.color("white")
    pen.pensize(2)
    pen.speed(0)
    pen.goto(-100, -230)
    pen.pendown()
    pen.goto(100, -230)
    pen.goto(100, -260)
    pen.goto(-100, -260)
    pen.goto(-100, -230)
    pen.penup()
    pen.goto(0, -255)
    pen.write("NEW GAME", align = "center", font = ("Arial", 15, "normal"))
    pen.penup()
    pen.hideturtle()

if init_screen == screens[0]:
    mainScreen()
elif init_screen == screens[1]:
    pen.showturtle()
    board(size, x, y)
mainScreen()
game_list = [[None, None, None], [None, None, None], [None, None, None]]
game_winner = None
players = ["X", "0"]
player_turn = players[0]
game = True
moves = 9
scores = {"X": 0, "0": 0}
gameState = {"game list": game_list, "moves": moves, "game": game, "turn": player_turn,
             "scores": scores}

def X(pos):
    winsound.PlaySound("touch.wav", winsound.SND_ASYNC)
    x, y = pos
    length = 50
    pen.penup()
    pen.goto(x - length, y - length)
    pen.pendown()
    pen.goto(x + length, y + length)
    pen.penup()
    pen.goto(x - length, y + length)
    pen.pendown()
    pen.goto(x + length, y - length)
    pen.penup()

def O(pos):
    winsound.PlaySound("touch.wav", winsound.SND_ASYNC)
    x, y = pos
    y -= 50
    radius = 50
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(radius)
    pen.penup()

def lines(win_boxes):
    cord = [(-140, 140), (0, 140), (140, 140),(-140, 0), (0, 0), (140, 0),
            (-140, -140), (0, -140), (140, -140)]
    if win_boxes == [0, 4, 8] or win_boxes == [2, 4, 6]:
        slabX = 50
        slabY = 50
    elif win_boxes[0] + 2 == win_boxes[1] + 1 == win_boxes[2]:
        slabX = 50
        slabY = 0
    else :
        slabY = 50
        slabX = 0
    pol_x, pol_y = 1, 1
    start_xy = cord[win_boxes[0]]
    end_xy = cord[win_boxes[2]]
    if start_xy[0] < 0 :
        pol_x = -1
    if start_xy[1] < 0:
        pol_y = -1
    start_xy = start_xy[0]+(pol_x*slabX), start_xy[1]+(pol_y*slabY)
    end_xy = end_xy[0]-(pol_x*slabX), end_xy[1]-(pol_y*slabY)
    pen.penup()
    pen.pencolor("red")
    pen.pensize(5)
    pen.goto(start_xy)
    pen.pendown()
    pen.goto(end_xy)
    pen.penup()
    pen.pensize(2)
    pen.pencolor("white")


def turn(moves, players, pos):
    if moves%2 != 0:
        X(pos)
        return players[1], moves - 1
    else :
        O(pos)
        return players[0], moves - 1


def scoreUpdater(winner, scores):
    if winner == list(scores.keys())[0]:
        scores[winner] += 1
    else :
        scores[winner] += 1
    return scores


def saveGame(gameState, file_number):
    if os.path.exists("./Saves"):
        filename = "savelogs_" + file_number + ".txt"
        f = open(filename, "w")
        pickle.dump(gameState, f)
        f.close()
        return 1
    else :
        return 0


def loadFile(file_number):
    if os.path.exists("./Saves"):
        filename = "savelogs_" + file_number + ".txt"
        path = "./Saves/" + filename
        if os.path.exists(path):
            f = open(filename, "r")
            gameState = pickle.load(gameState, f)
            f.close()
            return gameState
        else :
            return None
    else :
        return None


def loadGame():
    pass


def print_scores():
    pass


def resetScores(scores, gameState):
    scores = {"X": 0, "0": 0}
    gameState["scores"] = scores
    print_scores(scores)
    return scores, gameState


def win(l):
    global win_boxes
    if l[0][0] == l[0][1] == l[0][2] != None:
        win_boxes = [0, 3, 6]
        lines(win_boxes)
        return l[0][0], False
    elif l[1][0] == l[1][1] == l[1][2] != None:
        win_boxes = [1, 4, 7]
        lines(win_boxes)
        return l[1][0], False
    elif l[2][0] == l[2][1] == l[2][2] != None:
        win_boxes = [2, 5, 8]
        lines(win_boxes)
        return l[2][0], False
    elif l[0][2] == l[1][2] == l[2][2] != None:
        win_boxes = [0, 1, 2]
        lines(win_boxes)
        return l[0][2], False
    elif l[0][1] == l[1][1] == l[2][1] != None:
        win_boxes = [3, 4, 5]
        lines(win_boxes)
        return l[0][1], False
    elif l[0][0] == l[1][0] == l[2][0] != None:
        win_boxes = [6, 7, 8]
        lines(win_boxes)
        return l[0][0], False
    elif l[0][2] == l[1][1] == l[2][0] != None:
        win_boxes = [0, 4, 8]
        lines(win_boxes)
        return l[0][2], False
    elif l[0][0] == l[1][1] == l[2][2] != None:
        win_boxes = [2, 4, 6]
        lines(win_boxes)
        return l[0][0], False
    else :
        return None, True

def displayUpdate(player):
    global msg
    pen.penup()
    pen.goto(0, 230)
    pen.color("black")
    pen.write(msg, align = "center", font = ("Arial", 20, "normal"))
    pen.pencolor("white")
    msg = player + "'s Turn"
    pen.write(msg, align = "center", font = ("Arial", 20, "normal"))
    

def gameEnd(game_winner):
    winsound.PlaySound("win.wav", winsound.SND_ASYNC)
    global msg
    pen.penup()
    pen.goto(0, 230)
    pen.color("black")
    pen.write(msg, align = "center", font = ("Arial", 20, "normal"))
    pen.color("white")
    if game_winner == "Tie":
        msg = "Game is " + game_winner
    else : msg = game_winner + " is Winner"
    pen.write(msg, align = "center", font = ("Arial", 20, "normal"))
    

def move(pos, box):
    global game_list, game_winner, player_turn, players, game, moves
    if not game_list[box[0]][box[1]] and game:
        game_list[box[0]][box[1]] = player_turn
        player_turn, moves = turn(moves, players, pos)
        game_winner, game = win(game_list)
        if game:
            if moves == 0:
                gameEnd("Tie")
                game = False
            else :
                displayUpdate(player_turn)
        else :
            gameEnd(game_winner)

def reset(showturtle = False):
    global game_list, game_winner, player_turn, players, game, moves, msg, win_boxes, scores, gameState
    board(size, x, y, showturtle)
    game_list = [[None, None, None], [None, None, None], [None, None, None]]
    game_winner = None
    players = ["X", "0"]
    player_turn = players[0]
    game = True
    moves = 9
    msg = None
    win_boxes = []
    displayUpdate(players[0])
    gameState = {"game list": game_list, "moves": moves, "game": game, "turn": player_turn,
             "scores": scores}
    
                
def pos_calculator(xcor, ycor):
    box_pos = [-210, -70, 70, 210]
    x_box, y_box = None, None
    pos_y = [-140, 0, 140]
    pos_x = [-140, 0, 140]
    for i in range(len(box_pos)-1):
        if xcor > box_pos[i] and xcor < box_pos[i+1]:
            x_box = i
        if ycor > box_pos[i] and ycor < box_pos[i+1]:
            y_box = i
    if x_box != None and y_box != None:
        xcor = pos_x[x_box]
        ycor = pos_y[y_box]
        move((xcor, ycor), (x_box, y_box))
    elif xcor >= -100 and xcor <= 100 and ycor >= -260 and ycor <= -230:
        winsound.PlaySound("touch.wav", winsound.SND_ASYNC)
        reset()


def MainScreenCheck(xcor, ycor, MSButtons):
    global screens, init_screen
    if xcor <= MSButtons["singleplayer"]["x"][0] and xcor >= MSButtons["singleplayer"]["x"][1] and ycor <= MSButtons["singleplayer"]["y"][0] and ycor >= MSButtons["singleplayer"]["y"][1]:
        init_screen = screens[1]
        reset(showturtle = True)


def screen(xcor, ycor):
    global screens, init_screen, MSButtons
    if init_screen == screens[0]:
        MainScreenCheck(xcor, ycor, MSButtons)
    elif init_screen == screens[1]:
        pos_calculator(xcor, ycor)



turtle.onscreenclick(screen)
turtle.mainloop()

