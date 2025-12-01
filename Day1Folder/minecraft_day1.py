# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def forward(steps):
    agent.move(FORWARD, steps)
def back(steps):
    agent.move(BACK, steps)
def up(steps):
    agent.move(UP, steps)
def down(steps):
    agent.move(DOWN, steps)
def left():
    agent.turn(LEFT)
    # agent.move(LEFT, 1)
def right():
    agent.turn(RIGHT)
    # agent.move(RIGHT, 1)
def teleport():
    agent.teleport_to_player()
player.on_chat("mf1", forward)
player.on_chat("mb1", back)
player.on_chat("mu1", up)
player.on_chat("md1", down)
player.on_chat("tl", left)
player.on_chat("tr", right)
player.on_chat("come", teleport)


def obby1():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 2)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("obby", obby1)









