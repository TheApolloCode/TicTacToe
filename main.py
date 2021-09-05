import random

# EN:Tic Tac Toe
# RO:X si 0

tie=0

v = ["*", "*", "*",
     "*", "*", "*",
     "*", "*", "*"]


def printBoard():
    print(v[0], v[1], v[2])
    print(v[3], v[4], v[5])
    print(v[6], v[7], v[8], "\n")


printBoard()
# EN:The Game Table
# RO:Tabla de joc
condition = True
'''
   EN:Condition that verifies if x or 0 were selected or anything else entirely and reacts accordingly
   RO:Conditie ce verifica daca s-a selectat x sau 0 sau altceva si reactioneaza corespunzator
'''

while condition:
    print("Choose x or 0:")
    playerChoice = str(input())
    if playerChoice == "x":
        computerChoice = "0"
        player = True
        condition = False
    elif playerChoice == "0":
        computerChoice = "x"
        player = False
        condition = False

while True:
    if (v[0] == v[4] == v[8] == "x" or v[0] == v[4] == v[8] == "0"):
        print(v[0] + " wins")
        break
    elif (v[2] == v[4] == v[6] == "x" or v[2] == v[4] == v[6] == "0"):
        print(v[2] + " wins")
        break
    else:
         straightLine=False

    # RO:Linie orizontala,EN:Horizontal line
    if (v[0] == v[1] == v[2] == "x" or v[0] == v[1] == v[2] == "0"):
        print(v[0] + " wins")
        break
    elif (v[3] == v[4] == v[5] == "x" or v[3] == v[4] == v[5] == "0"):
        print(v[3] + " wins")
        break
    elif (v[6] == v[7] == v[8] == "x" or v[6] == v[7] == v[8] == "0"):
        print(v[6] + " wins")
        break
    else:
        horizontalLine=False


    # RO:Linie verticala,EN:Vertical line
    if (v[0] == v[3] == v[6] == "x" or [0] == v[3] == v[6] == "0"):
        print(v[0] + " wins")
        break
    elif (v[1] == v[4] == v[7] == "x" or v[1] == v[4] == v[7] == "0"):
        print(v[1] + " wins")
        break
    elif (v[2] == v[5] == v[8] == "x" or v[2] == v[5] == v[8] == "0"):
        print(v[2] + " wins")
        break
    else:
        verticalLine=False


    while player:
            print("Input the desired position(0-8):")
            position = int(input())
            if v[position]!=playerChoice and v[position]!=computerChoice:
             v[position] = playerChoice
             player = False
             printBoard()
             for i in range(0, 9):
                 if v[i] == "x" or v[i] == "0":
                     tie += 1
    if tie == 9 and verticalLine==False and horizontalLine==False and straightLine==False:
                 print("It's a tie")
                 break
    else:
        tie=0

    '''
    EN:Player turn,the if statement verifies if the position can be occupied(x!=x,x!=0,x!=*)
    RO:Tura jucatorului,conditionala if verifica daca pozitia poate fi ocupata(x!=x,x!=0,x!=*)
    '''

    while player==False:
         position = random.randint(0, 8)
         if v[position]!=computerChoice and v[position]!=playerChoice:
          v[position] = computerChoice
          player = True
          printBoard()
          for i in range(0, 9):
              if v[i] == "x" or v[i] == "0":
                  tie += 1
    if tie == 9 and verticalLine==False and horizontalLine==False and straightLine==False:
              print("It's a tie")
              break
    else:
        tie=0
'''
EN:Computer random turn(can be improved with the implementation of the minimax AI algorithm)
Does the same if check that happens above to verifiy if the move is possible 
RO:Tura aleatorie a calculatorului(poate fi imbunatatita cu implementarea algoritmului de 
   inteligenta artificiala minimax)
   Face aceeasi verificare care se intampla si mai sus,pentru a verifica daca mutarea este posibila
'''

'''
5.09.2021 V:1.01
EN:Updates i did to my code after the first version I published:Added a tie checker,and a print command 
to correctly show it.Game no longer runs in an infinite loop when there's a tie.
RO:Actualizare pe care am facut-o codului meu dupa prima versiune:Am adauga un verificator de remiza si o
comanda pentru a o afisa corect.Jocul nu mai merge intr-o bucla infinita cand este remiza.
'''