import random

start_game_message = """
Welcome to the Hangman Game!

Kirmada, the evil monster, has taken Bheem hostage! Chutki, Bheem's friend, suffers from a special condition called short-term memory loss. She remembers the structure of words but can't recall the alphabets making them up.
Chutki needs to tell Kirmada the correct word(s) to set Bheem free, otherwise, Bheem will be hanged. Each incorrect guess will make the noose tighter for Bheem, and 6 incorrect guesses will mean GAME OVER!

Help Chutki rescue Bheem by guessing the correct letters. Remember, Bheem's fate is in your hands!

Good luck!

"""

incorrect_guess_messages = [
    "That's an incorrect guess.",
    "Oops! That's not right.",
    "Sorry, that's the wrong answer.",
    "Nope, that's not correct.",
    "Try again, that's not it.",
    "Unfortunately, that's wrong.",
    "That's not the right guess.",
    "Incorrect, please try again.",
    "Not quite, give it another shot.",
    "Sorry, that's not the solution.",
    "That's not the correct answer.",
    "Better luck next time, that's wrong.",
    "No, that's not the right one.",
    "Incorrect guess, keep trying!",
    "That's a miss, try again.",
    "Nope, that's incorrect.",
    "Wrong guess, don't give up!",
    "Not the right answer, try again.",
    "That's not it, have another go.",
    "Oops, that's wrong. Keep going!",
    "Incorrect, but don't lose hope!",
    "Not quite right, try again.",
    "Sorry, that's not it. Keep trying!",
    "That's not the right guess, sorry.",
    "Nope, you missed it. Try once more.",
    "That's a wrong guess, keep at it.",
    "Incorrect, try another guess.",
    "Wrong answer, give it another shot.",
    "That's not correct, but keep going!",
    "Sorry, that's not the one.",
    "Not the right guess, try again.",
    "Oops, that's not correct.",
    "Wrong attempt, give it another try.",
    "That's incorrect, try again.",
    "Sorry, that's wrong. Try once more.",
    "Not the right answer, keep trying.",
    "That's a miss, have another go.",
    "Incorrect guess, try again.",
    "Not quite right, have another shot.",
    "Sorry, that's incorrect. Keep at it!",
    "That's not it, try once more.",
    "Oops, wrong guess. Keep going!",
    "Not the correct answer, keep trying.",
    "Wrong guess, have another try."
]

correct_guess_messages = [
    "That's a correct guess!",
    "You've hit the nail on the head!",
    "Absolutely spot on, well done!",
    "That's exactly right, excellent job!",
    "Congratulations, you've got it perfectly!",
    "Your answer is absolutely correct!",
    "You are right on the money!",
    "Bulls-eye! That's the right answer!",
    "You've got it in one, superb!",
    "That is indeed the right solution!",
    "Bravo! You've nailed it precisely!",
    "You've figured it out splendidly!",
    "Right you are! Excellent work!",
    "Fantastic! You've solved it correctly!",
    "Yes, that's the perfect answer!",
    "You've made a perfect guess!",
    "Exactly right! Keep it up!",
    "Correct! You've done it again!",
    "Perfectly accurate, good job!",
    "You've deciphered it exactly!",
    "Spot on! You're doing great!",
    "You are absolutely on target!",
    "That's a bullseye, well done!",
    "You've cracked it, awesome!",
    "That's the right call, fantastic!",
    "You've answered correctly, bravo!",
    "Great job! That's the right guess!",
    "You've got it, that's spot on!",
    "Outstanding! You've guessed it!",
    "That's absolutely correct, excellent!",
    "You've got the right idea, superb!",
    "Exactly the right guess, wonderful!",
    "Your guess is perfectly accurate!",
    "Spot on! You've got it exactly right!",
    "That's a perfect answer, brilliant!",
    "Correct guess! Keep up the good work!",
    "Your answer is right, fantastic job!",
    "That's a flawless guess, well done!",
    "You've nailed it, that's correct!",
    "Great! Your guess is on point!",
    "Absolutely right, that's the one!",
    "Wonderful! You've got it perfectly!",
    "You're absolutely right, congrats!",
    "That's it! You've guessed correctly!",
    "You've got it, well done indeed!",
    "You've hit the mark perfectly!"
]

winning_messages = [
    "Congratulations, you've won!",
    "You're the winner, great job!",
    "Victory is yours, well done!",
    "You did it, you won!",
    "Fantastic, you've emerged victorious!",
    "Hooray! You've claimed the win!",
    "Bravo! You are the champion!",
    "Excellent work, you are the winner!",
    "You’ve triumphed, congratulations!",
    "You nailed it, you’re the winner!",
    "Outstanding! You've won the game!",
    "You're the best, you've won!",
    "Impressive! You've secured the victory!",
    "You’ve won, amazing job!",
    "Way to go! You’re the champion!",
    "You’re victorious, well played!",
    "Hats off to you, you've won!",
    "Superb! You've conquered the game!",
    "You’ve done it, you’re the winner!",
    "You’ve come out on top, congrats!",
    "Victory! You’ve won the challenge!",
    "You’ve achieved victory, great job!",
    "You’re the winner, outstanding work!",
    "Hurrah! You’ve taken the win!",
    "You’ve won, excellent performance!",
    "Champion! You've won the game!",
    "You’ve got the victory, fantastic!",
    "Amazing! You've won the match!",
    "You’re the winner, great effort!",
    "You’ve prevailed, congratulations!",
    "You’re triumphant, well done!",
    "You’ve clinched the win, superb!",
    "Victory is yours, outstanding job!",
    "You’ve won, brilliant performance!",
    "You're the top player, well done!",
    "You’ve outplayed everyone, you won!",
    "Congratulations, you’re the best!",
    "You’ve won, incredible job!",
    "You’re the victor, excellent work!",
    "You’ve succeeded, great job!",
    "Well played, you’ve won!",
    "You’ve done it, you’re victorious!",
    "Champion! Excellent performance!",
    "You’ve come out ahead, congrats!",
    "You’ve taken the prize, great job!",
    "You’ve earned the win, fantastic!"
]

losing_messages = [
    "Better luck next time!",
    "Don't worry, you'll get it next time.",
    "Sorry, you lost this time.",
    "Keep trying, you’ll do better next time.",
    "Unfortunately, you've lost this round.",
    "That was a tough one, try again!",
    "Don't give up, keep practicing!",
    "Chin up, you can win the next one!",
    "Not your day, but don't lose hope.",
    "You did your best, try again!",
    "Sorry, that's a loss.",
    "It was a hard-fought game, better luck next time.",
    "You were close, keep at it!",
    "Don't be discouraged, try again soon.",
    "You gave it a good effort!",
    "Next time will be your time!",
    "You can't win them all, keep trying!",
    "Take heart, and try again.",
    "A loss this time, but you can do it!",
    "Stay positive, you’ll win the next one!",
    "It’s a setback, but not the end!",
    "Keep going, you’re improving!",
    "It was a tough match, but don't give up.",
    "You tried hard, better luck next time.",
    "Every loss is a step towards winning.",
    "You’re getting better, keep it up!",
    "A tough break, but you’ll bounce back!",
    "Perseverance is key, keep trying.",
    "Don't let this loss get you down.",
    "You can learn from this and improve!",
    "You’ve got the spirit, keep playing!",
    "Sorry about the loss, but keep at it.",
    "Defeat is just a stepping stone to victory.",
    "You played well, just not your day.",
    "Take this as a challenge for next time.",
    "You’re on the right track, don't stop!",
    "You’ll get there with persistence!",
    "Another try and you’ll make it!",
    "A loss can be a learning experience.",
    "Don't worry, success is on the horizon.",
    "You’re doing great, keep practicing.",
    "Each game is a chance to improve.",
    "It was a close game, keep trying!",
    "You’ve got what it takes, try again.",
    "Losing is part of the journey to success.",
    "You’ll get them next time, don’t worry.",
    "Stay determined, and you'll succeed."
]


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
    print(start_game_message)
    display_current(current_state)
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
                # print("That's a correct guess!")
                print(random.choice(correct_guess_messages))
                for i in range(len(answer_state)):
                    if guess==answer_state[i]:
                        current_state[i]=guess
                display_current(current_state)
            else:
                #print("That's an incorrect guess!")
                print(random.choice(incorrect_guess_messages))
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
        # print("Congratulations! You win!")
        print(random.choice(winning_messages))
    else:
        # print("Oh no! NT but you lose.")
        print(random.choice(losing_messages))
        display_current(answer_state)

movies()