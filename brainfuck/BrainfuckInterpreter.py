#coding : utf-8

import sys
import os

import config

class Interpreter:
    
    def __init__(self, target):
        self.target   = target
        self.code     = ""
        self.tape     = [0 for _ in range(config.TAPE_LENGTH)]
        self.head     = 0
        self.lbMarker = []

    def run(self):
        # return self.target

        self.code = self.target
        c    = "?"

        while len(self.code) > 0 and c != "#":
            # self.showTape()
            c    = self.code[0]
            self.code = self.code[1:] 
            if   c == ">":
                self.LT()
            elif c == "<":
                self.GT()
            elif c == "+":
                self.PL()
            elif c == "-":
                self.MI()
            elif c == "[":
                self.LB()
            elif c == "]":
                self.RB()
            elif c == ".":
                self.DO()
            # elif c == "#":
            #     pass
            else:
                pass

    def LT(self):
        # print("LT, ", end="")
        self.head = min(self.head+1, config.TAPE_LENGTH)
    def GT(self):
        # print("GT, ", end="")
        self.head = max(self.head-1, 0)
    def PL(self):
        # print("PL, ", end="")
        current = self.tape[self.head]
        self.tape[self.head] = min(current+1, config.TAPE_MAX)
    def MI(self):
        # print("MI, ", end="")
        current = self.tape[self.head]
        self.tape[self.head] = max(current-1, config.TAPE_MIN)
    def LB(self):
        # print("LB, ", end="")
        if self.tape[self.head] > 0:
            tmp = len(self.target)-len(self.code)-1
            self.lbMarker.append(tmp)
        else:
            while self.code[0] != "]":
                self.code = self.code[1:]
            self.code = self.code[1:]
    def RB(self):
        # print("RB, ", end="")
        if self.tape[self.head] == 0:
            pass
        else:
            self.code = self.target[self.lbMarker[-1]:]
            self.lbMarker = self.lbMarker[:-1]
    def DO(self):
        # print("DO, ", end="")
        # print(chr(ord("A")+self.tape[self.head]), end="")
        print(chr(self.tape[self.head]), end="")
        # print(self.tape[self.head], end=" ")

    def showTape(self):
        print()
        print(self.code)
        br = ""
        for i in range(self.head):
            br += "   "
        print(br + "v")
        for i in range(10):
            print("{0:02d}".format(self.tape[i]), end="|")

if __name__ == "__main__":

    args    = sys.argv
    srcPath = "samples/"

    if len(args) <= 1:
        print("python BrainfuckInterpreter <src name>")

    elif os.path.exists(srcPath + args[1]) == False:
        print("src '%s' cannot found" % args[1])

    else:
        target = ""
        with open(srcPath + args[1]) as f:
            target = f.read()
        interpreter = Interpreter(target).run()
        print()
        print(target)
