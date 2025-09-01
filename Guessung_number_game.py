import random
print("                               Welcome to the Number Guessing Game!                                 ")
print("I am thinking of a number between 1 and 100.")
t=1
n=random.randint(1,101)
while True:
    try:
        s=int(input("Take a guess:"))
        if(s==n):
            print(f"Congratulation! You guessed it in {t} attempts.")
            p=input("Do you want to play again? (yes/no):")
            if(p.lower()=='yes'):
                n=random.randint(1,101)
                t=0
                continue
            else:
                break
        elif(s>n):
            print("Too high! Try again.") 
            t=t+1
        elif(s<n):
            print("Too low! Try again.")
            t=t+1
    except ValueError as e:
        print("Error",e)         
print("Thanks for playing! Goodbye!")
    

