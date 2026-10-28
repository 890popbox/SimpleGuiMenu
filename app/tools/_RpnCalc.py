# Let's try this without stack, just using list.
from tkinter import *


class RPNCalc(object):
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.visualStack = []
        self.visualFrames = []
        self.helpFrames = []
        self.decimalCount = 0
        self.cacheEntry = '0'

    # Make sure stack always has 4 zero's
    def checkStack(self):
        while len(self.stack) < 4:
            self.stack.append('0')

    # Show the stack, do the last 3, replace the 4th with the peek of the list, to retain interactive view.
    def showStack(self, top='0'):
        for i, j in zip(range(len(self.stack) - 3, len(self.stack)), range(len(self.visualStack) - 1)):
            self.visualStack[j].config(text=self.stack[i])
        self.visualStack[3].delete(0, END)
        self.visualStack[3].insert(END, top)

    # Clear stack (AC)
    def clearStack(self):
        self.stack.clear()
        self.checkStack()
        self.showStack()
        self.clearLine()

    # Clear line
    def clearLine(self):
        self.visualStack[3].delete(0, END)
        self.visualStack[3].insert(END, '0')

    # Negative/Positive
    def switchNegaPos(self):
        data = float(self.visualStack[3].get()) * -1
        self.visualStack[3].delete(0, END)
        self.visualStack[3].insert(END, str(data))

    # Clear frames
    def clearFrames(self):
        # Function to clear frames
        if len(self.visualStack) >= 4:
            self.cacheEntry = self.visualStack[3].get()
        for a in self.visualFrames:
            a.destroy()
        self.visualFrames.clear()
        for b in self.visualStack:
            b.destroy()
        self.visualStack.clear()
        self.thankYou()

    # Set the line
    def setOperand(self, num):
        curr = self.visualStack[3].get()
        if curr == '0' and num != '.':
            self.visualStack[3].delete(0, END)
            self.visualStack[3].insert(END, num)
        elif (self.decimalCount == 0 and num == '.'):
            self.visualStack[3].insert(END, num)
            self.decimalCount += 1
        else:
            if (num != '.'):
                self.visualStack[3].insert(END, num)

    # Do the math
    def doOperator(self, op):
        rOperand = float(self.visualStack[3].get())
        lOperand = float(self.stack.pop())
        result = 0
        if (op == '%'):
            result = lOperand % rOperand
        elif (op == '*'):
            result = lOperand * rOperand
        elif (op == '/'):
            if (rOperand != 0):
                result = lOperand / rOperand
            else:
                result = 0
        elif (op == '-'):
            result = lOperand - rOperand
        elif (op == '+'):
            result = lOperand + rOperand
        else:  # Make sure they are back on if the operator doesn't exist
            self.stack.append(str(lOperand))
            self.stack.append(str(rOperand))
            return
        self.checkStack()
        self.showStack()
        self.setOperand(str(result))

    # Help page..
    def helpMe(self):
        main = self.root
        helpFRAME = Frame(main, width=530, height=265, bg='#2c2f33')
        helpFRAME.place(x=350, y=225)  # a93226
        self.helpFrames.append(helpFRAME)
        info1 = Label(main, text='C - Clear current line (Sets bottom line to zero)\n'
                                 + 'AC - Clear the whole Stack (Everything gets cleared to zero)\n'
                                 + 'POP - Pops the last thing off the stack (Will put it in the last line)\n'
                                 + 'Enter - Pushes in the number you enter in the bottom line\n\n'
                                 + 'Calculator works as a Simple Reverse Polish Notation Calculator\n'
                                 + 'All Operands are pushed to the stack (Last is mututable)\n' + 'Operators are preformed after Operands are entered\n\n'
                                 + 'Calculator uses simple builtin cache for Stack and Last Entry\n'
                                 + 'Frames are cleared if they exist, Stack is only cleared with AC'
                      , fg='#bbbbbb', bg='#2c2f33', font='arial 12 bold')
        info1.place(x=360, y=230)
        self.helpFrames.append(info1)
        thanks_ = Button(main, text="Click to close Help Menu", width=30, command=self.thankYou)
        thanks_.place(x=500, y=450)
        self.helpFrames.append(thanks_)

    def thankYou(self):
        for t in self.helpFrames:
            t.destroy()
        self.helpFrames.clear()

    # Create the stack
    def createStack(self):
        main = self.root
        rpnFRAME = Frame(main, width=800, height=400, bg='#cccccc')
        rpnFRAME.place(x=0, y=0)
        self.visualFrames.append(rpnFRAME)
        # Stack spots
        stackPos4 = Label(main, width=20, fg='#000000', bg='#ffffff')
        stackPos4.grid(row=1, column=0, pady=5)
        self.visualStack.append(stackPos4)
        stackPos3 = Label(main, width=20, fg='#000000', bg='#ffffff')
        stackPos3.grid(row=2, column=0, pady=5)
        self.visualStack.append(stackPos3)
        stackPos2 = Label(main, width=20, fg='#000000', bg='#ffffff')
        stackPos2.grid(row=3, column=0, pady=5)
        self.visualStack.append(stackPos2)
        stackPos1 = Entry(main, width=25, justify='center', fg='#000000', bg='#ffffff')
        stackPos1.grid(row=4, column=0, pady=5)
        self.visualStack.append(stackPos1)
        myTitle = Label(main, text='Simple RPN Calc', fg='#bbbbbb', bg='#2c2f33', font='arial 24 bold')
        myTitle.grid(row=0, column=0, pady=5, padx=5)
        self.visualFrames.append(myTitle)
        help_ = Button(main, text="Click for help using RPN Calc", width=30, command=self.helpMe)
        help_.place(x=650, y=500)
        self.visualFrames.append(help_)
        self.checkStack()
        self.showStack(self.cacheEntry)

    # Push data..
    def pushCalc(self):
        data = self.visualStack[3].get()
        self.stack.append(data)
        self.showStack(data)

    def popCalc(self):
        tmp = self.stack.pop()
        self.showStack(tmp)
        return tmp

    # Create the calc
    def createCalc(self):
        main = self.root
        equal_ = Button(main, text="Enter", width=20, command=lambda: self.pushCalc())
        equal_.grid(row=5, column=3, columnspan=2)
        self.visualFrames.append(equal_)
        ac_ = Button(main, text="AC", width=10, command=lambda: self.clearStack())
        ac_.grid(row=0, column=2)
        self.visualFrames.append(ac_)
        c_ = Button(main, text="C", width=10, command=lambda: self.clearLine())
        c_.grid(row=0, column=1)
        self.visualFrames.append(c_)
        pop_ = Button(main, text="POP", width=10, command=lambda: self.popCalc())
        pop_.grid(row=0, column=3)
        self.visualFrames.append(pop_)
        more_ = Button(main, text="More labels here ???", width=20)
        more_.grid(row=1, column=1, columnspan=2)
        self.visualFrames.append(more_)
        switcher_ = Button(main, text="-/+", width=10, command=lambda: self.switchNegaPos())
        switcher_.grid(row=1, column=3)
        self.visualFrames.append(switcher_)

        plus_ = Button(main, text="+", width=10, command=lambda: self.doOperator('+'))
        plus_.grid(row=4, column=4)
        self.visualFrames.append(plus_)
        times_ = Button(main, text="x", width=10, command=lambda: self.doOperator('*'))
        times_.grid(row=2, column=4)
        self.visualFrames.append(times_)
        sub_ = Button(main, text="-", width=10, command=lambda: self.doOperator('-'))
        sub_.grid(row=3, column=4)
        self.visualFrames.append(sub_)
        div_ = Button(main, text="/", width=10, command=lambda: self.doOperator('/'))
        div_.grid(row=1, column=4)
        self.visualFrames.append(div_)
        mod_ = Button(main, text="%", width=10, command=lambda: self.doOperator('%'))
        mod_.grid(row=0, column=4)
        self.visualFrames.append(mod_)

        seven_ = Button(main, text="7", width=10, command=lambda: self.setOperand('7'))
        seven_.grid(row=2, column=1)
        self.visualFrames.append(seven_)
        eight_ = Button(main, text="8", width=10, command=lambda: self.setOperand('8'))
        eight_.grid(row=2, column=2)
        self.visualFrames.append(eight_)
        nine_ = Button(main, text="9", width=10, command=lambda: self.setOperand('9'))
        nine_.grid(row=2, column=3)
        self.visualFrames.append(nine_)
        four_ = Button(main, text="4", width=10, command=lambda: self.setOperand('4'))
        four_.grid(row=3, column=1)
        self.visualFrames.append(four_)
        five_ = Button(main, text="5", width=10, command=lambda: self.setOperand('5'))
        five_.grid(row=3, column=2)
        self.visualFrames.append(five_)
        six_ = Button(main, text="6", width=10, command=lambda: self.setOperand('6'))
        six_.grid(row=3, column=3)
        self.visualFrames.append(six_)
        one_ = Button(main, text="1", width=10, command=lambda: self.setOperand('1'))
        one_.grid(row=4, column=1)
        self.visualFrames.append(one_)
        two_ = Button(main, text="2", width=10, command=lambda: self.setOperand('2'))
        two_.grid(row=4, column=2)
        self.visualFrames.append(two_)
        three_ = Button(main, text="3", width=10, command=lambda: self.setOperand('3'))
        three_.grid(row=4, column=3)
        self.visualFrames.append(three_)
        zero_ = Button(main, text="0", width=10, command=lambda: self.setOperand('0'))
        zero_.grid(row=5, column=1)
        self.visualFrames.append(zero_)
        dot_ = Button(main, text=".", width=10, command=lambda: self.setOperand('.'))
        dot_.grid(row=5, column=2)
        self.visualFrames.append(dot_)
