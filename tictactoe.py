from IPython.display import clear_output
def game():
    clear_output()
    print("Welcome to the Tic Tac Toe Tournament.")
    print("Player 1 will be O and Player 2 will be X. Player 1 starts first.")
    print("Choose 1-9 to take over a spot on the grid. Best of Luck!")
    list_one = [' ',' ',' ']
    list_two = [' ',' ',' ']
    list_three = [' ',' ',' ']
    list_four = []
    status = True
    ct = 1
    while status == True:
        if ct % 2 == 1:
            val = int(input("Enter the position: "))
            if val in list_four:
                print("Position already filled!")
            elif val == 1:
                list_one[0] = "0"
                list_four.append(val)
            elif val == 2:
                list_one[1] = "0"
                list_four.append(val)
            elif val == 3:
                list_one[2] = "0"
                list_four.append(val)
            elif val == 4:
                list_two[0] = "0"
                list_four.append(val)
            elif val == 5:
                list_two[1] = "0"
                list_four.append(val)
            elif val == 6:
                list_two[2] = "0"
                list_four.append(val)
            elif val == 7:
                list_three[0] = "0"
                list_four.append(val)
            elif val == 8:
                list_three[1] = "0"
                list_four.append(val)
            elif val == 9:
                list_three[2] = "0"
                list_four.append(val)
            else:
                print("Please enter a valid number between 1-9 only!")
            print(list_one)
            print(list_two)
            print(list_three)
            ct = ct + 1
        elif ct % 2 == 0:
            val = int(input("Enter the position: "))
            if val in list_four:
                print("Position already filled!")
            elif val == 1:
                list_one[0] = "X"
                list_four.append(val)
            elif val == 2:
                list_one[1] = "X"
                list_four.append(val)
            elif val == 3:
                list_one[2] = "X"
                list_four.append(val)
            elif val == 4:
                list_two[0] = "X"
                list_four.append(val)
            elif val == 5:
                list_two[1] = "X"
                list_four.append(val)
            elif val == 6:
                list_two[2] = "X"
                list_four.append(val)
            elif val == 7:
                list_three[0] = "X"
                list_four.append(val)
            elif val == 8:
                list_three[1] = "X"
                list_four.append(val)
            elif val == 9:
                list_three[2] = "X"
                list_four.append(val)
            else:
                print("Please enter a valid number between 1-9 only!")
            print(list_one)
            print(list_two)
            print(list_three)
            ct = ct + 1
            
        if list_one[0] == "0" and list_one[1] == "0" and list_one[2] == "0":
            print("Player 1 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break   
        elif list_two[0] == "0" and list_two[1] == "0" and list_two[2] == "0":
            print("Player 1 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break 
        elif list_three[0] == "0" and list_three[1] == "0" and list_three[2] == "0":
            print("Player 1 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break  
        elif list_one[0] == "0" and list_two[0] == "0" and list_three[0] == "0":
            print("Player 1 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break  
        elif list_one[1] == "0" and list_two[1] == "0" and list_three[1] == "0":
            print("Player 1 wins!")  
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break   
        elif list_one[2] == "0" and list_two[2] == "0" and list_three[2] == "0":
            print("Player 1 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break 
        elif list_one[0] == "0" and list_two[1] == "0" and list_three[2] == "0":
            print("Player 1 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break  
        elif list_one[2] == "0" and list_two[1] == "0" and list_three[0] == "0":
            print("Player 1 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break 
        elif list_one[0] == "X" and list_one[1] == "X" and list_one[2] == "X":
            print("Player 2 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break   
        elif list_two[0] == "X" and list_two[1] == "X" and list_two[2] == "X":
            print("Player 2 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break   
        elif list_three[0] == "X" and list_three[1] == "X" and list_three[2] == "X":
            print("Player 2 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break  
        elif list_one[0] == "X" and list_two[0] == "X" and list_three[0] == "X":
            print("Player 2 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break   
        elif list_one[1] == "X" and list_two[1] == "X" and list_three[1] == "X":
            print("Player 2 wins!")  
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break  
        elif list_one[2] == "X" and list_two[2] == "X" and list_three[2] == "X":
            print("Player 2 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break  
        elif list_one[0] == "X" and list_two[1] == "X" and list_three[2] == "X":
            print("Player 2 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break   
        elif list_one[2] == "X" and list_two[1] == "X" and list_three[0] == "X":
            print("Player 2 wins!")
            val1 = int(input("Play Again? Type any digit for No and 1 for Yes: "))
            if val1 == 1:
                status = False
                game()
            else:
                break   