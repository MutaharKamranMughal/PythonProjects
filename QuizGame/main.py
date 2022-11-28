# Quiz Game

print('Welcome to my Computer Quiz!!')

playing = input("Do you want to play? ")
if playing.lower() != 'yes':
     quit()
else:
    print('Okay!! Lets play :)')

score = 0

answer = input("1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("CORRECT! Lets move forward.")
    score += 1
else:
    print('Wrong answer!!')

answer = input("2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("CORRECT! Pretty smart you are ;). Next!")
    score += 1
else:
    print('Wrong answer!!')

answer = input("3. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("CORRECT! Almost there.")
    score += 1
else:
    print('Wrong answer!!')

answer = input("4. What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("CORRECT! Genius!! All done, congrats :))")
    score +=1
else:
    print('Wrong answer!! So close...')

percentage = score/4 * 100

print(f'Your total score is {score}. You got {score} questions correct.')
print(f"That makes {percentage}%.")
