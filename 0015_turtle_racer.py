import turtle
import random



screen = turtle.Screen()
screen.setup(width=500, height=400)
turtle.hideturtle()
turtle.penup()

turtle_colors = ['red', 'blue', 'purple', 'orange', 'green', 'brown', 'navy', 'gold', ]
turtle_racers = []
FONT = 'ariel', 12, 'bold'


def check_winner(winner):
    if winner == player_choice.title():
        turtle.goto(-100, -150)
        turtle.color(winner)
        turtle.write(f'{winner} won! You won the bet! ', font=FONT)
    else:
        turtle.goto(-135, -150)
        turtle.color(winner)
        turtle.write(f' You lost betting on {player_choice.title()}. {winner} won! ', font=FONT)


def speed_boost(current_racer):
    if random.randint(0, 5) == 3:
        if random.randint(0, 7) == 5:
            if random.randint(0, 10) == 7:
                current_racer.write('               Brrrrrrrrrrrrrrrrrrrrrrrrrrrr!!!')
                return 75
            current_racer.write('               Suupeeer!!')
            return 35
        current_racer.write('           Great!')
        return 15
    else:
        return 0


def race_start():
    race_going = True
    winner = ""
    while race_going:
        for current_racer in turtle_racers:
            current_racer.clear()
            current_racer.forward(random.randint(1, 10))
            current_racer.forward(speed_boost(current_racer))
            if current_racer.xcor() > 230 and winner == "":
                race_going = False
                winner = current_racer.pencolor().title()
    check_winner(winner)


def create_racers(racers):
    for number in range(0, racers):
        new_racer = turtle.Turtle(shape='turtle')
        new_racer.penup()
        new_racer.color(turtle_colors[number])
        new_racer.goto(-220, -100 + (number * 40))
        new_racer.write(f'      {turtle_colors[number].title()}')
        turtle_racers.append(new_racer)


racers = int(turtle.textinput('Choose number of participants.', 'How many turtles want to race? (Min 2 and Max 8)'))
if racers > 8 or racers < 2:
    racers = 6
create_racers(racers)
player_choice = turtle.textinput('Choose your Turtle!', 'Which color turtle do you want to bet on?')
if player_choice.lower() not in turtle_colors:
    player_choice = "None"
race_start()



screen.exitonclick()
