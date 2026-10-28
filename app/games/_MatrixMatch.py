from tkinter import *
import random
from functools import partial


class MatrixMatch(object):
    def __init__(self, root):
        self.root = root
        # Default MatrixLength and attempts
        self.minMatrixLength = 2
        self.maxMatrixLength = 10
        self.minAttemptLength = 3
        self.maxAttemptLength = 6
        # Display and row/col size
        self.selectionFrames = []
        self.visualFrames = []
        self.matrixFrames = []
        self.totalShaded = 0
        self.attemptsLeft = 3

    # Clear all frames really fast and resetGame
    def clearFrames(self):
        for x in self.matrixFrames:
            x[0].destroy()
        for x in self.visualFrames:
            x.destroy()
        for x in self.selectionFrames:
            x.destroy()
        self.visualFrames.clear()
        self.selectionFrames.clear()
        self.matrixFrames.clear()

    # Start game and verify
    def playMatrix(self, row, col, tries):
        main = self.root
        # Remove the selection menu only, start game
        for x in self.selectionFrames:
            x.destroy()

        # Verify the game before starting it
        self.totalShaded = 0
        row = row if self.minMatrixLength <= row <= self.maxMatrixLength else self.minMatrixLength
        col = col if self.minMatrixLength <= col <= self.maxMatrixLength else self.minMatrixLength
        self.attemptsLeft = tries if self.minAttemptLength <= tries <= self.maxAttemptLength else self.minAttemptLength

        matrix = [[[0, 0] for c in range(col + 2)] for r in range(row + 2)]

        # Menu uses the first rows
        for r in range(2, row + 2):
            for c in range(2, col + 2):
                shaded = random.randint(0, 1)
                self.totalShaded += shaded
                matrix[r][c][0] = matrix[r][c - 1][0] + shaded
                matrix[r][c][1] = matrix[r - 1][c][1] + shaded
                block = Button(main, width=5, font='arial 14 bold',
                               command=partial(self.pickBox, shaded, (r - 2) * col + (c - 2))
                               )
                # if shaded:
                #    block.config(bg='black')
                block.grid(row=r, column=c)
                self.matrixFrames.append([block, shaded])

        # Verify how many attempts are left
        block = Label(main, width=20, font='arial 12 bold', text='{0} attempts remaining'.format(self.attemptsLeft))
        block.grid(row=1, column=0)
        self.visualFrames.append(block)

        # Verify how many blocks should be shaded in that row/column
        for r in range(2, row + 2):
            block = Button(main, width=5, text=matrix[r][-1][0])
            block.grid(row=r, column=1)
            self.visualFrames.append(block)

        for c in range(2, col + 2):
            block = Button(main, width=5, text=matrix[-1][c][1])
            block.grid(row=1, column=c)
            self.visualFrames.append(block)

    def pickBox(self, shaded, num):
        # If we already got the winner/loser screen
        if self.attemptsLeft == 0 or self.totalShaded == 0:
            return

        # If this box hasn't been selected, make it green or red
        if self.matrixFrames[num][0].cget('bg') == 'SystemButtonFace':
            if shaded:
                self.matrixFrames[num][0].config(bg='green')
                self.totalShaded -= 1
            else:
                self.matrixFrames[num][0].config(bg='red')
                self.attemptsLeft -= 1
                self.visualFrames[1].config(text='{0} attempts remaining'.format(self.attemptsLeft))

        # Check for win or lose conditions
        if self.attemptsLeft == 0:
            print('Loser')
            loserLabel = Label(self.root, text="Nice try, here is the correct solution!", relief='solid',
                               font="monospace 24 bold")
            loserLabel.place(x=200, y=400)
            for block in self.matrixFrames:
                if block[1]:
                    block[0].config(bg='black')
            self.visualFrames.append(loserLabel)

        elif self.totalShaded == 0:
            print("Winner")
            winnerLabel = Label(self.root, text="Good job! You got them all", relief='solid',
                                font="monospace 24 bold")
            winnerLabel.place(x=200, y=400)
            self.visualFrames.append(winnerLabel)

    # Create this class
    def createGame(self):
        main = self.root

        sortFrame = Frame(main, width=900, height=450, bg='#aaaaaa')
        sortFrame.place(x=0, y=0)
        self.visualFrames.append(sortFrame)

        # Naming it this because later will allow custom input, how long should the word be?
        rowLabel = Label(main, text="How many rows would you like? [{0}-{1}]".format(self.minMatrixLength,
                                                                                     self.maxMatrixLength),
                         font='arial 24')
        rowLabel.grid(row=0, column=0)
        row_length = Entry(main, relief='solid', fg='#000000', bg='#ffffff')
        row_length.grid(row=1, column=0)

        self.selectionFrames.append(rowLabel)
        self.selectionFrames.append(row_length)

        # Naming it this because later will allow custom input, how long should the word be?
        colLabel = Label(main, text="How many columns would you like? [{0}-{1}]".format(self.minMatrixLength,
                                                                                        self.maxMatrixLength),
                         font='arial 24')
        colLabel.grid(row=2, column=0)
        col_length = Entry(main, relief='solid', fg='#000000', bg='#ffffff')
        col_length.grid(row=3, column=0)

        self.selectionFrames.append(colLabel)
        self.selectionFrames.append(col_length)

        # How many tries.. [3-6]
        triesLabel = Label(main, text="How many tries would you like to solve the grid [{0}-{1}]".format(
            self.minAttemptLength, self.maxAttemptLength), font='arial 24')
        triesLabel.grid(row=4, column=0)
        tries_length = Entry(main, relief='solid', fg='#000000', bg='#ffffff')
        tries_length.grid(row=5, column=0)

        self.selectionFrames.append(triesLabel)
        self.selectionFrames.append(tries_length)

        enterButton = Button(main, text="Enter",
                             command=lambda: self.playMatrix(int(row_length.get()), int(col_length.get()),
                                                             int(tries_length.get())))
        enterButton.grid(row=6, column=0)
        self.selectionFrames.append(enterButton)
