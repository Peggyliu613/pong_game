from turtle import Turtle, Screen
import paddle
import ball
import score


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)


player_one = paddle.Paddle((-360, 0))
player_two = paddle.Paddle((360, 0))
ball = ball.Ball()


screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "s")
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")


screen.listen()

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
