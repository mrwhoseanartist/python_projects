import random 
def guess():
    guess=0
    attempt=0
    random_number=random.randint(1,100)
    while guess!=random_number:
        guess=int(input("Enter ur guess: "))
        if guess>random_number:
            print("It's too high")
            attempt+=1
        elif guess<random_number:
            print("Tt's too low")
            attempt+=1
    print(f"congrats u have guessed the number {random_number} correctly in {attempt} attempts!")
guess()
