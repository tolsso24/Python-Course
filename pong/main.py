# Copyright 2021 Timmy Olsson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from turtle import Screen, onkey
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000000")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((350, 0))
sec_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(sec_paddle.go_up, "w")
screen.onkey(sec_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(sec_paddle) < 50 and ball.xcor() < -320 or ball.distance(paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        scoreboard.increase_left()
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.increase_right()
        ball.reset_position()


screen.exitonclick()
