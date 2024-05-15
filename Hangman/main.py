import random

hangman_states=["___\n  |\n  O","\n/","|","\\","\n/\'","\\"]
# for states in hangman_states:
#     print(states,end='')

def movies():
    file=open("Hangman\movies.txt", "r") 
    data=file.read()
    movies_list=data.split("\n")
    file.close()
    movie=random.choice(movies_list)
    movie=movie.upper()
    play(movie)


def display_current(current_state):
    for ch in current_state:
        print(ch, end=" ")
    print("\n")


def play(answer):
    answer_state=[ch for ch in  answer]
    current_state=['_' if ch.isalpha() else ch for ch in answer]
    guessed=[]
    attempts=6
    failed_attempts=0
    while(attempts>0 and '_' in current_state):
        print("Enter your guess (one alphabet): ")
        guess=input()[0]
        if guess.isalpha():
            guess=guess.upper()
        else: 
            print("You can guess only alphabets!")
            continue
        if guess in guessed:
            print("Already guessed!")
            continue
        else:
            guessed.append(guess)
            if guess in answer_state:
                print("That's a correct guess!")
                for i in range(len(answer_state)):
                    if guess==answer_state[i]:
                        current_state[i]=guess
                display_current(current_state)
            else:
                print("That's an incorrect guess!")
                attempts-=1
                failed_attempts+=1
                print(f"\nRemaining attempts: {attempts}")
                display_current(current_state)
                for j in range(failed_attempts):
                    print(hangman_states[j],end='')
                print("\n")
                
        # print(answer_state)
        # print(current_state)
        
    if('_' not in current_state):
        print("Congratulations! You win!")
    else:
        print("Oh no! NT but you lose.")

movies()