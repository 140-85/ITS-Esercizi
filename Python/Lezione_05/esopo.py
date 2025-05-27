import random

def current_position(tortoise, hare):
    position = ["_"] * 70
    position[tortoise] = "T"
    position[hare] = "H"
    
    if tortoise == hare:
        position = "OUCH!!!"

def tortoise_move():
    squares = random.randint(1, 10)
    if squares >=1 and squares <= 5:
        return 3
    elif squares >= 6 and squares <= 7:
        return -6
    else:
        return 1

def hare_move():
    squares = random.randint(1, 10)
    if squares >= 1 and squares <= 2:
        return 0
    elif squares >= 3 and squares <= 4:
        return 9
    elif squares == 5:
        return -12
    elif squares >= 6 and squares <= 8:
        return 1
    else:
        return -2

print("BANG !!!!! AND THEY'RE OFF !!!!!")

tortoise = 1
hare = 1
    
while tortoise < 70 and hare < 70:
    tortoise = (1, tortoise + tortoise_move())
    hare = (1, hare + hare_move())
        
    current_position(tortoise, hare)
        
    if tortoise >= 70:
        print("TORTOISE WINS! || VAY!!!")
        break
    elif hare >= 70:
        print("HARE WINS || YUCH!!!")
        break
    elif tortoise >= 70 and hare >= 70:
        print("IT'S A TIE.")
        break