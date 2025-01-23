import os
import pdb

import pyverilog
from pyverilog.vparser.parser import VerilogCodeParser

def flist_gen(path):
    filelist = []
    for file in path:
        if file.endswith(".v"):
            filelist.append (f"{path}/{file}")

    return filelist

def v2num(s):
    if "'" in s:
        tmp   = s.split("'")
        bw    = int(tmp[0], 10)
        radix = tmp[1][0]
        val   = tmp[1][1:]

        if radix == "h":
            dgt = int(val, 16)
        elif radix == "d":
            dgt = int(val, 10)
        elif radix == "o":
            dgt = int(val, 8)
        elif radix == "b":
            dgt = int(val, 2)
        else:
            print (f"ERROR! Found illegal value {s}!")
    else:
        bw  = 32
        dgt = int(s, 10)

    return bw, dgt
        
def ASTproc(object)
    def __init__ (self, path):
        self.filelist = flist_gen(path)
        self.ast      = self.get_ast(self.filelist)

    def get_ast (self, filelist):
        codeparser = VerilogCodeParser(filelist, ['RD=0.1'])
        ast = codeparser.parse()
        return ast

    def debug_ast_chain (self, filelist):
        for file in filelist:
            codeparser = VerilogCodeParser([file], ['RD=0.1'])
            codeparser.parse()

    def debug_ast(self, filename):
        codeparser = VerilogCodeParser([filename], ['RD=0.1'])
        ast = codeparser.parse()
        pdb.set_trace()

    def pre_scan_lineno(self):
        pass


def AutoGatingChecker(ASTproc):
    def __init__ (self, path):
        super().__init__(self, path)

    



        
