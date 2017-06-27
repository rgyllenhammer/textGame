'''
a text based game by reese gyllenhammer all in python
'''
import random
import sys

player = 'x'
sinkhole = 'N'
end = 'E'
shot = '|'

minlev = 0
maxlev = 8

minspot = 0
maxspot = 8

curlev = 0
curspot = 0

field = [

    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.',end],

]
def intro():
    print('''

hello there ninja! In this game you will be have darts thrown at you
faster than you can keep up with... are you ready??

OF COURSE YOU ARE!

In this game, you are the x, the enemy ninjas are marked as N, and the katanas they
are throwing at you are the moving lines.

In order to win, you must sneak around and assasinate 10 ninjas, before you finally
get yourself onto the ending block, marked as E.

If you win, you will win 100 reese points...

GOOD LUCK! YOU CAN DO IT!!

    ''')


def win():
    print('''


Congratulations ninja!!!

I knew you could do it. You have been rewarded 100 reese points as promised.
You may cash these in for virtually anything you want in the world. They say
that reese points are the only true international currency, and people will even trade
their entire homes for just a few reese points...

Nah jk my points are virtually meaningless except for the fact that maybe
every reese point is a high five or something or if me and u r like close it could
be a hug for every five points or something idk man just I cant belive you are still reading this
either play again or go get a life seriously.

-Reese



    ''')

def lose():
    print('''

YOU LOSE TRY AGAIN

    ''')


def maingame(curlev, curspot):
    alive = True
    won = False
    sinkholeList = []
    counter = 1
    score = 0

    randSinkLev = random.randint(1,7)
    randSinkSpot = random.randint(1,7)
    shotLev = randSinkLev - 1

    sinkholeList.append([randSinkLev,randSinkSpot,shotLev])

    while (alive) and (not won):

        field[curlev][curspot] = player

        for sink in sinkholeList:
            field[sink[0]][sink[1]] = sinkhole
            field[sink[2]][sink[1]] = shot


        oldlev = curlev
        oldspot = curspot

        print('\n\n')

        for level in field:
            for spot in level:
                print(spot, " ", end="")
            print()

        print('\n\n')

        move = input('\n\nwhat would you like to do, move (l)eft, (r)ight, (u)p, or (d)own? ')
        print('\n\n\n\n')
        curlev, curspot = movePlayer(move, oldlev, oldspot)


        field[oldlev][oldspot] = '.'
        print("current level = {} current spot = {} current score = {}".format(curlev, curspot, score))

        if (curlev == 8 and curspot == 8) and score >= 10:
            won = True
            win()

        for sink in sinkholeList:
            oldShotLev = sink[2]
            sink[2] -= 1

            field[oldShotLev][sink[1]] = '.'

            if (sink[2] == curlev) and (sink[1] == curspot):
                alive = False
                lose()

            if (sink[0] == curlev) and (sink[1] == curspot):
                field[sink[0]][sink[1]] = '.'
                field[sink[2]][sink[1]] = '.'
                score += 1

                sinkholeList.remove(sink)

            elif sink[2] < 0:
                field[sink[0]][sink[1]] = '.'
                field[sink[2]][sink[1]] = '.'

                sinkholeList.remove(sink)

                randSinkLev = random.randint(1,7)
                randSinkSpot = random.randint(1,7)
                shotLev = randSinkLev - 1

                sinkholeList.append([randSinkLev,randSinkSpot,shotLev])

        if counter % 3 == 0:
            randSinkLev = random.randint(1,7)
            randSinkSpot = random.randint(1,7)
            shotLev = randSinkLev - 1

            sinkholeList.append([randSinkLev,randSinkSpot,shotLev])


        counter += 1
        field[8][8] = end






def movePlayer(move, curlev, curspot):
    if move == 'a':
        curspot -= 1
        if curspot < minspot:
            curspot = minspot

    elif move == 'd':
        curspot += 1
        if curspot > maxspot:
            curspot = maxspot

    elif move == 'w':
        curlev -= 1
        if curlev < minlev:
            curlev = minlev

    elif move == 's':
        curlev += 1
        if curlev > maxlev:
            curlev = maxlev

    else:
        print("\nincorrect input. only enter a, s, d, or w")

    return curlev, curspot


intro()
maingame(curlev, curspot)
