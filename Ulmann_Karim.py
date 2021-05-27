from tkinter import *
from time import *
import random

global countlives
countlives = 0


def draw():
    global Lives
    global start
    global countlives
    start = time()
    xpos = random.randint(25, 460)
    ypos = random.randint(100, 360)
    xpos1 = random.randint(25, 460)
    ypos2 = random.randint(100, 360)
    pallet = ['red', 'blue', 'green', 'yellow', 'purple']

    if Lives == 0:
        canvas.delete('all')
        finisher()

    elif Score > 15:
        countlives += 1
        canvas.configure(bg='black')  # pick up from here
        canvas.create_text(250, 50, text='Level 2\nEnter Dark Mode!', font=('Comic Sans MS', 20, 'bold italic'),
                           fill='white')
        lvl2Target = canvas.create_rectangle(xpos1, ypos2, xpos1 + 40, ypos2 + 40,
                                             fill='white')
        canvas.tag_bind(lvl2Target, "<ButtonPress-1>", isClicked)
        if countlives == 1:
            saviour()
        else:
            pass

    else:
        newTarget = canvas.create_rectangle(xpos, ypos, xpos + 40, ypos + 40, fill=random.choice(pallet))
        canvas.tag_bind(newTarget, "<ButtonPress-1>", isClicked)

        decoy = canvas.create_oval(xpos1, ypos2, xpos1 + 40, ypos2 + 40,
                                   fill=random.choice(pallet))  # create a distraction
        canvas.tag_bind(decoy, "<ButtonPress-1>", wrongClick)
        newTarget = canvas.create_rectangle(xpos, ypos, xpos + 40, ypos + 40, fill=random.choice(pallet))
        canvas.tag_bind(newTarget, "<ButtonPress-1>", isClicked)

    presser["state"] = "disabled"  # after user presses start they must press the figure to continue playing


def isClicked(*args):
    global target
    try:
        click = 0
        canvas.delete('all')
        if click == 0 and Score == 0:  # user must see the message when playing for the first round
            canvas.create_text(250, 50, text='You have 2 seconds to click!\n AIM FOR THE SQUARE',
                               font=('Comic Sans MS', 18, 'bold italic'),
                               fill='red')
            click += 1
        else:
            click += 1
        # a little level of more difficulty
        speed = [2, 1.5, 1]
        superspeed = [0.5, 1]
        if Score >= 5:
            target = random.choice(speed)  # vary time to click
            if Score >= 15:
                target = random.choice(superspeed)  # vary time to click after going dark
                if Score >= 20:
                    target = 0.5  # Expect most users to fail here
                # print(target)
        else:
            target = 2
        if time() - start < target:
            updateScore()
            draw()
        else:
            if Score == 0:
                canvas.delete('all')
                finisher()
            else:
                reduceScore()
                draw()
    except:
        draw()


def wrongClick(*args):
    global Score
    global Lives
    try:
        canvas.delete('all')
        if Score == 0:
            canvas.create_text(250, 50, text='Penalty for clicking the \n Wrong Object!\n - 1 life!',
                               font=('Comic Sans MS', 18, 'bold italic'),
                               fill='red')
            Lives -= 1
            lives_text.set(f' LIVES : {Lives}')
            draw()

        elif Score > 2:
            canvas.create_text(250, 50, text='Penalty for clicking the \n Wrong Object!\n -2 POINTS!',
                               font=('Comic Sans MS', 18, 'bold italic'),
                               fill='red')
            wrongClickSore()
            draw()
        else:
            canvas.create_text(250, 50, text='Penalty for clicking the \n Wrong Object!',
                               font=('Comic Sans MS', 18, 'bold italic'),
                               fill='red')
            wrongClickSore()
            draw()
    except:
        draw()


def reduceScore():
    taunts = ['too slow! ', 'Faster! ', 'are you even trying?! ', "huft that's slow ", 'boring.. ', 'BAKA! ',
              'slow and steady wins the race.. ', "Keep Goin'! ", 'Pick it up! ', 'Big Sad :( ', 'Expected better ']
    global Score
    global Lives
    if Lives == 0:
        canvas.delete('all')
        finisher()
    else:

        Lives -= 1
        lives_text.set(f' LIVES : {Lives}')

        canvas.create_text(250, 50, text=random.choice(taunts) + '\n-1 life', font=('Comic Sans MS', 20, 'bold italic'),
                           fill='black')


def wrongClickSore():
    global Score
    global Lives
    if Score <= 0:
        score_variable.set(f' Score : {0}')
        finsher()
    elif Lives <= 0:
        finisher()
    else:
        Score -= 2
        score_variable.set(f' Score : {Score}')
        Lives -= 1
        lives_text.set(f' LIVES : {Lives}')


def updateScore():
    encouragement = ["let's make things faster! ", 'not bad', 'could be better', 'better late than never',
                     'learning fast', "let's go champ!",
                     'quick reflexes :)', 'going faster would be nice..', 'Above Expectations', 'Maybe.. good',
                     'Maybe Impressive ']
    global Score
    canvas.delete('all')
    Score += 1
    score_variable.set(f' Score : {Score}')
    canvas.create_text(250, 50, text=random.choice(encouragement) + '\n+1 Score',
                       font=('Comic Sans MS', 20, 'bold italic'),
                       fill='black')


def saviour():
    global Lives
    global countlives
    countlives += 1
    Lives = 3
    lives_text.set(f' LIVES : {Lives}')
    countlives += 1
    countlives += 1


def finisher():
    global Lives
    global target
    canvas.delete('all')
    Lives = 0
    lives_text.set(f' LIVES : {Lives}')
    canvas.configure(bg='#808080')  # enter dark mode!
    canvas.create_text(260, 50, text="Mission Failed We'll get em' next time",
                       font=('Comic Sans MS', 15, 'bold italic'),
                       fill='white')
    canvas.create_text(250, 75, text="Your Score is " + str(Score), font=('Comic Sans MS', 20, 'bold italic'),
                       fill='white')
    if target != 1:
        canvas.create_text(250, 125,
                           text="You needed to hit the square in\n " + str(target) + " Seconds for that score",
                           font=('Comic Sans MS', 15, 'bold italic'),
                           fill='white')
    else:
        canvas.create_text(250, 125, text="You needed to hit the square in\n " + str(target) + " Second for that score",
                           font=('Comic Sans MS', 15, 'bold italic'),
                           fill='white')


root = Tk()

root.title('How fast can you go?')

canvas = Canvas(root, width=500, height=500)

canvas.pack(side=TOP)

canvas.tag_bind('first', "<ButtonPress-1>", isClicked)

frame = Frame(root)

presser = Button(frame, text="Start!", command=isClicked, font=("Comic Sans MS", 25))
presser.grid(row=1, column=1)

Score = 0
score_variable = StringVar(frame, f' Score! : {Score}')
scoreBoxLabel = Label(frame, textvariable=score_variable, font=("Comic Sans MS", 25))
scoreBoxLabel.grid(row=1, column=3)

Lives = 3
lives_text = StringVar(frame, f' LIVES : {Lives}')
livesLabel = Label(frame, textvariable=lives_text, font=("Comic Sans MS", 25))
livesLabel.grid(row=1, column=0)

frame.pack(side=BOTTOM)

root.mainloop()
