import random
score = 0


def f():
    global score
    a = 1
    b = 10
    n1 = random.randint(a, b)
    n2 = random.randint(a, b)
    a = n1 * n2
    x = int(input('What is ' + str(n1) + ' into ' + str(n2) + ' ?'))
    if a == x:
        score += 1
        print("Whohoo!! You are right. Your score is " + str(score))
    else:
        score -= 1
        print("You Are Wrong. Your score is " + str(score))


f()
f()
f()
f()
f()
f()
f()
f()
f()
f()
if score > 5:
    print("The game is Over. You have Won!!!! with " + str(score) + " points")
else:
    print("The game is Over. You have Lost with " + str(score) +
          " points. Better luck next time!")
