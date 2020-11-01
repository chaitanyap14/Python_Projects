# tic_tac_toe v1.1 by Chaitanya P.
# Now using numpad form of input
# The board uses a dictionary
# v2.0 coming soon with single player mode

global ttt
ttt = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}


def display_board():
    print("")
    print(ttt[7] + "|" + ttt[8] + "|" + ttt[9])
    print("-+-+-")
    print(ttt[4] + "|" + ttt[5] + "|" + ttt[6])
    print("-+-+-")
    print(ttt[1] + "|" + ttt[2] + "|" + ttt[3])


def shape_select():
    print("\n---  Choose O or X  ---")
    global m
    global n
    m = input()
    if(m in ["O", "X"]):
        if(m == "O"):
            n = "X"
            print("Player 1 has chosen {}".format(m))
            print("Player 2 gets {}".format(n))
        elif(m == "X"):
            n = "O"
            print("Player 1 has chosen {}".format(m))
            print("Player 2 gets {}".format(n))
    else:
        print("[-] INVALID INPUT --> Only O and X are accepted.....haven't you ever played tic tac toe ???")
        print("Now you have to restart the program as punishment")
        quit()


def winner():
    if(ttt[1] == ttt[2] == ttt[3]):
        if(ttt[1] == ttt[2] == ttt[3] == m):
            print("\n Player 1 WINS!!!")
        elif(ttt[1] == ttt[2] == ttt[3] == n):
            print("\nPlayer 2 WINS!!!")
        restart()
    elif(ttt[4] == ttt[5] == ttt[6]):
        if(ttt[4] == ttt[5] == ttt[6] == m):
            print("\n Player 1 WINS!!!")
        elif(ttt[4] == ttt[5] == ttt[6] == n):
            print("\nPlayer 2 WINS!!!")
        restart()
    elif(ttt[7] == ttt[8] == ttt[9]):
        if(ttt[7] == ttt[8] == ttt[9] == m):
            print("\nPlayer 1 WINS!!!")
        elif(ttt[7] == ttt[8] == ttt[9] == n):
            print("\nPlayer 2 WINS!!!")
        restart()
    elif(ttt[7] == ttt[4] == ttt[1]):
        if(ttt[7] == ttt[4] == ttt[1] == m):
            print("\nPlayer 1 WINS!!!")
        elif(ttt[7] == ttt[4] == ttt[1] == n):
            print("\nPlayer 2 WINS!!!")
        restart()
    elif(ttt[8] == ttt[5] == ttt[2]):
        if(ttt[8] == ttt[5] == ttt[2] == m):
            print("\nPlayer 1 WINS!!!")
        elif(ttt[8] == ttt[5] == ttt[2] == n):
            print("\nPlayer 2 WINS!!!")
        restart()
    elif(ttt[9] == ttt[6] == ttt[3]):
        if(ttt[9] == ttt[6] == ttt[3] == m):
            print("\nPlayer 1 WINS!!!")
        elif(ttt[9] == ttt[6] == ttt[3] == n):
            print("\nPlayer 2 WINS!!!")
        restart()
    elif(ttt[1] == ttt[5] == ttt[9]):
        if(ttt[1] == ttt[5] == ttt[9] == m):
            print("\nPlayer 1 WINS!!!")
        elif(ttt[1] == ttt[5] == ttt[9] == n):
            print("\nPlayer 2 WINS!!!")
        restart()
    elif(ttt[7] == ttt[5] == ttt[3]):
        if(ttt[7] == ttt[5] == ttt[3] == m):
            print("\nPlayer 1 WINS!!!")
        elif(ttt[7] == ttt[5] == ttt[3] == n):
            print("\nPlayer 2 WINS!!!")
        restart()


def tic_tac_toe():
    display_board()
    shape_select()
    counter = 1
    while(counter < 9):
        print("\n Player 1:")
        a = int(input("Enter cell number: "))
        if(ttt[a] == " "):
            counter = counter + 1
            ttt[a] = m
            display_board()
        else:
            print("[-] INVALID INPUT --> Entry already exists")
            continue

        print("\nPlayer 2:")
        b = int(input("Enter cell number: "))
        if(ttt[b] == " "):
            counter = counter + 1
            ttt[b] = n
            display_board()
        else:
            print("[-] INVALID INPUT --> Entry already exists")
            continue

        if(counter > 4):
            if(ttt[7] == ttt[8] == ttt[9] != " " or ttt[4] == ttt[5] == ttt[6] != " " or ttt[1] == ttt[2] == ttt[3] != " "):
                winner()
            elif(ttt[7] == ttt[4] == ttt[1] != " " or ttt[8] == ttt[5] == ttt[2] != " " or ttt[9] == ttt[6] == ttt[3] != " "):
                winner()
            elif(ttt[7] == ttt[5] == ttt[3] != " " or ttt[1] == ttt[5] == ttt[9] != " "):
                winner()
            elif(counter == 8):
                break

    print("\nDRAW!!!")
    restart()


def restart():
    print("\nWell that ends this round.")
    u = input("Care to go another round ??? (Y/N) or (y/n): ")
    if(u in ["Y", "y", "N", "n"]):
        if(u in ["Y", "y"]):
            global ttt
            ttt = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
            tic_tac_toe()
        elif(u in ["N", "n"]):
            print("\nI knew you'd back out you coward")
            quit()
    else:
        print("\n[-] INVALID INPUT --> Only Y or y or N or n are accepted")


tic_tac_toe()
