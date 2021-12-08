#incomplete

ccomputer = ["", "rock", "paper", "scissors"]

uuser = ["", "rock", "paper", "scissors"]


def playGround():
    choice = int(input(
        " 1 for rock \n 2 for paper \n 3 for scissors \n Your Choice?: "))
    for i in ccomputer:
        if i == choice:
            print("It is draw. ")
        elif ccomputer[1] and choice:
            print("User Wins. ")
        elif ccomputer[2] and uuser[choice]:
            print("Computer Wins. ")
        elif ccomputer[3] and uuser[choice]:
            print("User Wins. ")


def main():
    while True:
        playGround()
        isExit = input(
            "Do You Want to Contiue? Write 'continue' if you 'exit'")
        if isExit.lower == "continue":
            pass
        elif isExit.lower == "exit":
            break


main()
