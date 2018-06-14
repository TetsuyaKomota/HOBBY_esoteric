# coding = utf-8
import sys
import os

"""
できるようにすること
    ・PRINT A -> A を出力 (空白は文字と認識)
    ・VAR A B -> A という変数に B という値を代入して保持
    ・+ A B   -> A に   B を加算して A に保持
    ・- A B   -> A から B を減算して A に保持
    ・* A B   -> A に   B を積算して A に保持
    ・/ A B   -> A を   B で割算して A に保持
    ・FOR A   -> 直後の ROF までを A 回繰り返す
    ・ROF     -> FOR 文の終わり
    ・IF A    -> A = 0 なら直後の FI までスキップ
    ・FI      -> IF 文の終わり
    ・END     -> ソースコードの終わり
"""

class ReverseCompiler:

    def __init__(self, target):
        self.target = target

    def run(self):
        code = [line.split(" ") for line in self.target.split("\n")]
        # remove null char 
        for i in range(len(code)):
            code[i] = [ci for ci in code[i] if len(ci) != 0]
        code = [c for c in code if len(c) != 0]
        for c in code:
            print(c)
        
if __name__ == "__main__":

    args    = sys.argv
    srcPath = "samples/"

    if len(args) <= 1:
        print("python BrainfuckReverseCompiler.py <src name>")

    elif os.path.exists(srcPath + args[1]) == False:
        print("src '%s' cannot found" % args[1])

    else:
        target = ""
        with open(srcPath + args[1]) as f:
            target = f.read()
        print(target)
        ReverseCompiler(target).run()
        print()
