from turtle import Screen
import time
import paddle
import ball
import scoreboard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)


player_one = paddle.Paddle((-360, 0))
player_two = paddle.Paddle((360, 0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "s")
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")


screen.listen()

game_is_on = True
time_sleep = 0.1
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    ball.move()

    if max(scoreboard.player_one_score, scoreboard.player_two_score) == 1:
        scoreboard.end_game()
        game_is_on = False

    if ball.xcor() > 360:
        ball.end_round()
        scoreboard.player_one_get_point()
        scoreboard.update_score()
        time_sleep = 0.1

    if ball.xcor() < -360:
        ball.end_round()
        scoreboard.player_two_get_point()
        scoreboard.update_score()
        time_sleep = 0.1

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    if (ball.distance(player_one) < 60 and ball.xcor() < -340) or (ball.distance(player_two) < 60 and ball.xcor() > 340):
        ball.hit()
        time_sleep *= 0.9


screen.exitonclick()
