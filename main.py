import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

for turtle_index in range(0,6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.color(colors[turtle_index])
  new_turtle.goto(x=-230, y=y_positions[turtle_index])
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      if user_bet == turtle.pencolor():
        print(f"You won! The {turtle.pencolor()} is the winner!")
      else:
        print(f"You lost! The {turtle.pencolor()} is the winner!")
    else:
      rand_distance = random.randint(0,10)
      turtle.forward(rand_distance)

screen.exitonclick()