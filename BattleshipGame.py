#File: BattleshipGame.py

from random import random, randrange

def main():
    my_fleet = [["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7]
    my_hits = [["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7]
    com_fleet = [["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7]
    com_hits = [["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7,["*"]*7]
    intro()
    my_place(my_fleet)
    com_place(com_fleet)
    myhits = 0
    comhits = 0
    while myhits < 10 and comhits < 10:
        myhits = my_attack(my_hits,com_fleet,myhits)
        comhits = com_attack(com_hits,my_fleet,comhits)
    if myhits == 10: return "You are the winner"
    elif comhits == 10: return "You lose"

def intro():
    print("This program simulates a game of battleship you and the computer")
    print("Enter coordinates in the form (x, y) when defining position of a ship")
    print("Enter direction as either horizontal, from left to right")
    print("or vertical, from top to bottom, from the starting position")
    print("Aircarrier size = 5 units")
    print("Cruiser size = 3 units")
    print("Destroyer size = 2 units")
    print("The board size is 7*7 units")
    print("The letters that appear when facing the computer, represents which ships got hit")
    print("The letter M represents a missed shot")
    print("If you want to exit the game, press enter instead of entering coordinates at any stage in the game")
    print()
    

def my_place(fleet):
    print("**Ships will be placed going from left to right or top to bottom\n"
          "of starting coordinate!!!**")
    run = 0
    ships = ("Aircarrier","Cruiser","Destroyer")
    slen = (5, 3, 2)
    while run < 3:
        x = eval(input("Insert starting x coordinate for {0}: ".format(ships[run])))
        y = eval(input("Insert starting y coordinate for {0}: ".format(ships[run])))
        direc = input("Insert direction (vertical or horizontal): ")
        if direc[0] == "h":
            if (x-1+slen[run])<=7 and fleet[y-1][(x-1):(x-1+slen[run])]==["*"]*slen[run]:
                for i in range(x-1,x+slen[run]-1):
                    fleet[y-1][i] =ships[run][0]
                run+=1
                output(fleet)
            else:
                print("Overlapping with other ship or not enough space horizontally")
                output(fleet)
        elif direc[0] == "v":
            if (y-1+slen[run])<=7 and [fleet[y-1+i][x-1] for i in range(slen[run])] == ["*"]*slen[run]:
                for i in range(y-1,y+slen[run]-1):
                    fleet[i][x-1] = ships[run][0]
                run+=1
                output(fleet)
            else:
                print("Overlappng with other ship or not enough space vertically")
                output(fleet)
        else: print("Needs to be either 'horizontal or vertical'!")

def com_place(fleet):
    run = 0
    ships = ("Aircarrier","Cruiser","Destroyer")
    slen = (5, 3, 2)
    while run < 3:
        x = randrange(1,8)
        y = randrange(1,8)
        direc = randrange(2)
        if direc == 0:
            if (x-1+slen[run])<=7 and fleet[y-1][(x-1):(x-1+slen[run])]==["*"]*slen[run]:
                for i in range(x-1,x+slen[run]-1):
                    fleet[y-1][i] =ships[run][0]
                run+=1
        elif direc == 1:
            if (y-1+slen[run])<=7 and [fleet[y-1+i][x-1] for i in range(slen[run])] == ["*"]*slen[run]:
                for i in range(y-1,y+slen[run]-1):
                    fleet[i][x-1] = ships[run][0]
                run+=1

def my_attack(hits,com,score):
    print("Your turn")
    x = eval(input("Insert x coordinate to hit: "))
    y = eval(input("Insert y coordinate to hit: "))
    if x<=7 and x>=0 and y>=0 and y<=7:
        if hits[y-1][x-1] == "A" or hits[y-1][x-1] == "C" or hits[y-1][x-1] == "D" or hits[y-1][x-1] == "M" :
            print("Already guessed!Try another!")
            return my_attack(hits,com,score)
        elif com[y-1][x-1] != "*":
            hits[y-1][x-1] = com[y-1][x-1]
            output(hits)
            return score+1
        else:
            hits[y-1][x-1] = "M"
            print("You miss")
            output(hits)
            return score
    else:
        print("Numbers must be in range starting from 1 to 7")
        return my_attack(hits,com,score)

def com_attack(hits,my,score):
    print("Computer turn")
    x = randrange(1,8)
    y = randrange(1,8)
    if x<=7 and x>=0 and y>=0 and y<=7:
        if hits[y-1][x-1] == "A" or hits[y-1][x-1] == "C" or hits[y-1][x-1] == "D" or hits[y-1][x-1] == "M" :
            return com_attack(hits,my,score)
        if my[y-1][x-1] != "*":
            hits[y-1][x-1] = my[y-1][x-1]
            output(hits)
            return score+1
        else:
            hits[y-1][x-1] = "M"
            output(hits)
            return score
    else:
        return com_attack(hits,my,score)

def output(fleet):
    matrix = ""
    for i in fleet:
        for j in i:
            matrix += "{0:5}".format(j)
        matrix+="\n"
    print(matrix)

main()
                     
    
