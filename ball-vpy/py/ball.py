from visual import *


g = 9.8
size = 0.7
#scene = display(title='Ball dropping', width=1200, height=800, background=(1,0.5,0.5), center=(0,7,0))
floor = box(length=35, height=0.5, width=4, color=color.green)

def balljump(spd):
    ball = sphere(pos=vector(-15.0, 5.0, 0.0), radius=size, color=color.white)
    ball.velocity = vector(spd, -1.0, 0.0)
    dt = 0.003
    while 1 and ball.pos.x < 15:
        rate(1000)
        previous_x=ball.pos.x
        ball.pos = ball.pos + ball.velocity*dt
        if previous_x == ball.pos.x:
            break
        if ball.y < size and ball.velocity.y < 0:
            ball.velocity.y = - ball.velocity.y
        else:
            ball.velocity.y = ball.velocity.y -  g*dt
    ball.visible = False
    del ball


while 1:
    for i in range(3,30):
        balljump(i)
        sleep(1)
        #scene.waitfor('keydown')
