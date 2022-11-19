import random
def hangman():
    list=["apple","bat","cap","dog","egg"]
    word=random.choice(list)
    print(word)
    turns=10
    guessmade=""
    available=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=""
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("you won")
            break
        print("guess the words",main_word)
        guess=input()
        if guess in available:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print("--------------")
            if turns==8:
                print("8 turns left")
                print("------------")
                print("      o      ")
            if turns==7:
                print("7 turns left")
                print("------------")
                print("      o      ")
                print("      |      ")
            if turns==6:
                print("6 turns left")
                print("------------")
                print("      o      ")
                print("      |      ")
                print("     /        ")
            if turns==5:
                print("5 turns left")
                print("------------")
                print("      o      ")
                print("      |      ")
                print("     / \      ")
            if turns==4:
                print("4 turns left")
                print("------------")
                print("      o      ")
                print("     /|      ")
                print("     / \      ")
            if turns==3:
                print("3 turns left")
                print("------------")
                print("      o      ")
                print("     /|\      ")
                print("     / \      ")
            if turns==2:
                print("2 turns left")
                print("------------")
                print("      o  |  ")
                print("     /|\      ")
                print("     / \     ")
            if turns==1:
                print("omly 1 turns left")
                print("------------")
                print("      o ---|")
                print("     /|\   |  ")
                print("     / \   |  ")
            if turns==0:
                print("you lose")
                break
            else:
                hint=input("enter 1.yes/2.no")
                if hint=="1":
                    print(word[-1])        
name=input("enter your name-->>")
print("welcome",name)
print("---------------------")
print("try to guess the word in less than 10 attempt")
hangman()

