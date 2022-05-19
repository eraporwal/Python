print("lets play guessing the number game")
print("you have only 9 guesses")
chance_number=1
while(chance_number<=9):
   chance_number=int(input("guess the number:"))
if chance_number<20:
    print("you guessed very small number")
elif chance_number>20:
    print("you guessedvery big number")
else:
    print("you guessed right")
print(chance_number,"no of gusses left:")
chance_number=chance_number+1
if(guess_number>9):
    print("you loose,your guesses are over")
