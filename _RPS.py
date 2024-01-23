from tkinter import *
import random
from functools import partial


class RPS(object):
    def __init__(self, root):
        self.root = root

        self.selectionFrames = []
        self.visualFrames = []
        self.computerFrames = []

    # Clear all frames really fast and resetGame
    def clearFrames(self):
        for x in self.visualFrames:
            x.destroy()
        for x in self.selectionFrames:
            x.destroy()
        for x in self.computerFrames:
            x.destroy()
        self.visualFrames.clear()
        self.selectionFrames.clear()
        self.computerFrames.clear()

    # Start game and verify value that represents rock,paper,scissor
    # 0==ROCK, 1==PAPER, 2==SCISSORS, computers random choice is decided after yours
    def playRPS(self, player):
        main = self.root

        computer = random.randint(0, 2)
        choices = ['Rock', 'Paper', 'Scissors']

        print('Player choose {0}'.format(choices[player]))
        print('Computer choose {0}'.format(choices[computer]))

        # Visual stuff
        self.computerFrames[0].config(text='Computer choice: {0}'.format(choices[computer]))
        self.computerFrames[1].config(text='{0} versus {1}'.format(choices[player], choices[computer]))

        # If you guys both picked the same thing, this fits 3 conditions out of 9
        # There are 6 more to take account of because we have to take into account the player and the computer
        if player == computer:
            print('draw')
            self.computerFrames[1].config(bg='yellow')

        # One higher wins two cases, the last is two higher;
        # 3 conditions for the player have been fit and if we don't run into them the computer did
        elif player + 2 == computer or computer+1 == player:
            print('player: winner')
            self.computerFrames[1].config(bg='green')
        else:
            print('player: loser')
            self.computerFrames[1].config(bg='red')

    # Create this class setting up the game itself
    def createGame(self):
        main = self.root

        sortFrame = Frame(main, width=900, height=450, bg='#aaaaaa')
        sortFrame.place(x=0, y=0)
        self.visualFrames.append(sortFrame)

        computer = Label(main, width=25, font='arial 12 bold', text='Computer choice: {0}'.format('Nan'))
        computer.grid(row=0, column=1)
        self.computerFrames.append(computer)

        choice = Label(main, width=30, font='arial 12 bold', text=' ')
        choice.grid(row=1, column=1)
        self.computerFrames.append(choice)

        rock = Button(main, text="Rock",  font='arial 14 bold',
                      command=lambda: self.playRPS(0)
                      )
        rock.grid(row=3, column=0)
        self.selectionFrames.append(rock)

        paper = Button(main, text="Paper",  font='arial 14 bold',
                       command=lambda: self.playRPS(1)
                       )
        paper.grid(row=3, column=1)
        self.selectionFrames.append(paper)

        scissors = Button(main, text="Scissors",  font='arial 14 bold',
                          command=lambda: self.playRPS(2)
                          )
        scissors.grid(row=3, column=2)
        self.selectionFrames.append(scissors)
