#coding : utf-8

import sys
import os

import config

class Interpreter:
    
    def __init__(self, target):
        self.target = target
        self.tape = [0 for _ in range(config.TAPE_LENGTH)]
        self.head = 0

    def run(self):
        # return self.target

        code = self.target
        c    = "?"

        while len(code) > 0 and c != "#":
            c    = code[0]
            code = code[1:] 
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
        print("LT, ", end="")
    def GT(self):
        print("GT, ", end="")
    def PL(self):
        print("PL, ", end="")
    def MI(self):
        print("MI, ", end="")
    def LB(self):
        print("LB, ", end="")
    def RB(self):
        print("RB, ", end="")
    def DO(self):
        print("DO, ", end="")

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
