g = 9.8
size = 0.7
scene = display(title='Ball dropping', width=1200, height=800, background=(1,0.5,0.5), center=vector(0,7,0))
floor = box(length=35, height=0.5, width=4, color=color.green)

dt = 0.003

def balljump(spd):
    ball = sphere(pos=vector(-15.0, 5.0, 0.0), radius=size, color=color.white)
    ball.velocity = vector(spd, -1.0, 0.0)
    
    def jump():
        rate(1000, jump)
    
        previous_x = ball.pos.x
        ball.pos = ball.pos + ball.velocity * dt
    
        if ball.pos.y < size and ball.velocity.y < 0:
            ball.velocity.y = - ball.velocity.y
        else:
            ball.velocity.y = ball.velocity.y - g * dt
    
        if ball.pos.x >= 15.0:
            ball.visible = False
    jump()


for i in range(3, 30):
    balljump(i)
    scene.waitfor('mousedown')
