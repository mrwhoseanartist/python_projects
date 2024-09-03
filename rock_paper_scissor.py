import random

def play():
    user=input("Enter Your choice: \nR for Rock | P for Paper | S for Scissor: ").lower()
    computer=random.choice(['r','p','s'])

    if user==computer:
        return 'Tie!'
    if is_win(user,computer):
        return "You Won!"
    return "You Lose!"

    # r > s | s > p | p > r
def is_win(player,opponet):
    if (player=='r' and opponet=='s') or (player=='s' and opponet=='p') or (player=='p' and opponet=='r'):
        return True
    
print(play())