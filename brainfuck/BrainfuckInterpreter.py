#coding : utf-8

import sys
import os

class Interpreter:
    
    def __init__(self, target):
        self.target = target

    def run(self):
        # return "hello interpreter!"
        return self.target

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
        interpreter = Interpreter(target)
        print(interpreter.run())
