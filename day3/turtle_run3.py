import turtle as t

wn = t.Screen()
wn.bgcolor("lightgreen")
wn.title("Turtle Run Ver.1")


move = 20

def moveUp():
    global move
    move = move + 10

def moveDown():
    global move
    move = move - 10


def turn_right():
  t.setheading(0)       # 거북이의 머리 방향을 0도로 돌린다.
  t.forward(move)
  trace()
  run()
    
def turn_left():
  t.setheading(180)    # 거북이의 머리 방향을 180도로 돌린다.
  t.forward(move)
  trace()
  run()

def turn_up():
  t.setheading(90)
  t.forward(move)
  trace()
  run()

def turn_down():
  t.setheading(270)
  t.forward(move)
  trace()
  run()

def reset():
  t.clear()          # 화면을 리셋


def run():
  if c.pos()[0] >= 150:
     c.setheading(180)
  elif c.pos()[0] <= -150:
    c.setheading(0)
  c.forward(15)

def trace():
  angle = b.towards(t.pos())
  b.setheading(angle)
  b.forward(20)
  
    
b = t.Turtle() # 악당
c = t.Turtle() # 먹이
b.shape("turtle")
c.shape("circle")
b.color("red")
c.color("green")
b.up()
b.goto(0, 200)
c.up()
c.goto(0, -200)

t.shape("turtle")
t.color("white","black")
t.speed(0)
t.penup()
t.onkeypress(moveUp, "q")
t.onkeypress(moveDown, "w")
t.onkeypress(turn_right, "Right") # 오른쪽 방향키가 눌리면 turn_right 함수 수행
t.onkeypress(turn_left, "Left")   # 윈쪽 방향키가 눌리면 turn_right 함수 수행
t.onkeypress(turn_up, "Up")       # 위쪽 방향키가 눌리면 turn_right 함수 수행
t.onkeypress(turn_down, "Down")   # 아래쪽 방향키가 눌리면 turn_right 함수 수행
t.onkeypress(reset, "r")          # R키가 눌리면 turn_right 함수 수행
t.listen()                        # 입력을 기다림...
