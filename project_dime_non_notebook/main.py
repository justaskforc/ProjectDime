import turtle

screen = turtle.Screen()
screen.setup(width=1100, height=1100)
screen.bgcolor("green")
screen.tracer(0, 0)

SELECTED_TOKEN = "w1"
PLAYER_TURN = "w"

VALID_MOVES = {
    "(0,100)": [(-100.00, 100.00), (0.00, 250.00), (100.00, 100.00)],
    "(100,100)": [(0.00, 100.00), (100.00, 0.00)],
    "(100,0)": [(100.00, 100.00), (250.00, 0.00), (100.00, -100.00)],
    "(100,-100)": [(100.00, 0.00), (0.00, -100.00)],
    "(0,-100)": [(100.00, -100.00), (0.00, -250.00), (-100.00, -100.00)],
    "(-100,-100)": [(0.00, -100.00), (-100.00, 0.00)],
    "(-100,0)": [(-100.00, -100.00), (-250.00, 0.00), (-100.00, 100.00)],
    "(-100,100)": [(-100.00, 0.00), (0.00, 100.00)],
    "(0,250)": [(0.00, 100.00), (250.00, 250.00), (-250.00, 250.00)],
    "(250,250)": [(0.00, 250.00), (250.00, 0.00)],
    "(250,0)": [(250.00, 250.00), (100.00, 0.00), (250.00, -250.00)],
    "(250,-250)": [(250.00, 0.00), (0.00, -250.00)],
    "(0,-250)": [(250.00, -250.00), (0.00, -100.00), (-250.00, -250.00)],
    "(-250,-250)": [(0.00, -250.00), (-250.00, 0.00)],
    "(-250,0)": [(-250.00, -250.00), (-100.00, 0.00), (-250.00, 250.00)],
    "(-250,250)": [(-250.00, 0.00), (0.00, 250.00)],
    "(-400,-150)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                    (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                    (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                    (-250.00, 250.00)],
    "(-400,-90)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                   (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                   (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                   (-250.00, 250.00)],
    "(-400,-30)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                   (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                   (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                   (-250.00, 250.00)],
    "(-400,30)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                  (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                  (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                  (-250.00, 250.00)],
    "(-400,90)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                  (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                  (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                  (-250.00, 250.00)],
    "(-400,150)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                   (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                   (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                   (-250.00, 250.00)],
    "(400,-150)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                   (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                   (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                   (-250.00, 250.00)],
    "(400,-90)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                  (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                  (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                  (-250.00, 250.00)],
    "(400,-30)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                  (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                  (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                  (-250.00, 250.00)],
    "(400,30)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                 (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                 (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                 (-250.00, 250.00)],
    "(400,90)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                 (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                 (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                 (-250.00, 250.00)],
    "(400,150)": [(0.00, 100.00), (100.00, 100.00), (100.00, 0.00), (100.00, -100.00), (0.00, -100.00),
                  (-100.00, -100.00), (-100.00, 0.00), (-100.00, 100.00), (0.00, 250.00), (250.00, 250.00),
                  (250.00, 0.00), (250.00, -250.00), (0.00, -250.00), (-250.00, -250.00), (-250.00, 0.00),
                  (-250.00, 250.00)]
}

title = turtle.Turtle()
title.penup()
title.hideturtle()
title.goto(0, 350)
title.write("Six Men's Morris", align="center", font=("arial", 100, "normal"))

announcer = turtle.Turtle()
announcer.penup()
announcer.hideturtle()
announcer.goto(0, -400)
announcer.color("white")
announcer.write("White to move", align="center", font=("arial", 40, "normal"))

announcer2 = turtle.Turtle()
announcer2.penup()
announcer2.hideturtle()
announcer2.goto(0, -440)
announcer2.color("red")


def move_turtle(x, y, where):
    global SELECTED_TOKEN
    global PLAYER_TURN
    if SELECTED_TOKEN[0] == PLAYER_TURN:
        pos = token_turtles[SELECTED_TOKEN].pos()
        key_pos = f"({int(pos[0])},{int(pos[1])})"
        if where in VALID_MOVES[key_pos]:
            token_turtles[SELECTED_TOKEN].goto(where)
            if PLAYER_TURN == "w":
                announcer.clear()
                announcer2.clear()
                PLAYER_TURN = "b"
                announcer.color("black")
                announcer.write("Black to move", align="center", font=("arial", 40, "normal"))
            else:
                announcer.clear()
                announcer2.clear()
                PLAYER_TURN = "w"
                announcer.color("white")
                announcer.write("White to move", align="center", font=("arial", 40, "normal"))
        else:
            announcer2.write("Flying is not allowed!", align="center", font=("arial", 20, "normal"))


# Dictionary of positions
positions = {
    "p1": (0, 100),
    "p2": (100, 100),
    "p3": (100, 0),
    "p4": (100, -100),
    "p5": (0, -100),
    "p6": (-100, -100),
    "p7": (-100, 0),
    "p8": (-100, 100),
    "p9": (0, 250),
    "p10": (250, 250),
    "p11": (250, 0),
    "p12": (250, -250),
    "p13": (0, -250),
    "p14": (-250, -250),
    "p15": (-250, 0),
    "p16": (-250, 250)
}

# Dictionary of position turtles
position_turtles = {}

# Placing the position turtles on the screen
for key, coord in positions.items():
    name = f"{key}"
    position_turtles[name] = turtle.Turtle()
    position_turtles[name].penup()
    position_turtles[name].goto(coord)
    position_turtles[name].color("blue")
    position_turtles[name].shape("circle")
    position_turtles[name].onclick(lambda x, y, curr_pos=position_turtles[name].pos(): move_turtle(x, y, curr_pos))

# Drawing the paths
artist = turtle.Turtle()
artist.pencolor("blue")
artist.penup()
artist.goto(-100, -100)
artist.pendown()
for m in [200, 500]:
    for n in range(4):
        artist.forward(m)
        artist.left(90)
    artist.penup()
    artist.goto(-250, -250)
    artist.pendown()
artist.penup()
for i in [[(0, 100), 90], [(100, 0), 0], [(0, -100), 270], [(-100, 0), 180]]:
    artist.goto(i[0])
    artist.pendown()
    artist.setheading(i[1])
    artist.forward(150)
    artist.penup()
artist.hideturtle()

# Dictionary of white tokens
white_tokens = {
    "w1": (-400, -150),
    "w2": (-400, -90),
    "w3": (-400, -30),
    "w4": (-400, 30),
    "w5": (-400, 90),
    "w6": (-400, 150),
}

# Dictionary of black tokens
black_tokens = {
    "b1": (400, -150),
    "b2": (400, -90),
    "b3": (400, -30),
    "b4": (400, 30),
    "b5": (400, 90),
    "b6": (400, 150),
}

# Dictionary of token turtles
token_turtles = {}

# Placing the token turtles on the screen
for i, e in enumerate([white_tokens, black_tokens]):
    for key, coord in e.items():
        name = f"{key}"
        token_turtles[name] = turtle.Turtle()
        token_turtles[name].shapesize(2)
        token_turtles[name].penup()
        token_turtles[name].goto(coord)
        token_turtles[name].onclick(lambda x, y, label=name: select_token(x, y, label))
        if i == 0:
            token_turtles[name].color("white")
        else:
            token_turtles[name].color("black")
        token_turtles[name].shape("circle")
        screen.update()

screen.tracer(1, 10)


def select_token(x, y, label):
    global SELECTED_TOKEN
    SELECTED_TOKEN = label


screen.update()

screen.mainloop()
