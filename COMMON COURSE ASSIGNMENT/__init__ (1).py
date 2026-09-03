import re
import os
from dataclasses import dataclass
from typing import List, Optional, Any

@dataclass
class TACInstruction:
    op: str
    arg1: str
    arg2: Optional[str]
    result: str

    def __str__(self):
        if self.op == '=':
            return f"{self.result} = {self.arg1}"
        if self.arg2:
            return f"{self.result} = {self.arg1} {self.op} {self.arg2}"
        else:
            return f"{self.result} = {self.op} {self.arg1}"

class TACGenerator:
    def __init__(self):
        self.instructions: List[TACInstruction] = []
        self.temp_count = 0

    def new_temp(self) -> str:
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node: Any) -> str:
        name = node.__class__.__name__
        if name == 'Num':
            # ensure float formatting uses integers if decimals are 0 for cleaner IR
            val = node.value
            if val == int(val):
                return str(int(val))
            return str(val)
        elif name == 'Var':
            return node.name
        elif name == 'BinOp':
            arg1 = self.generate(node.left)
            arg2 = self.generate(node.right)
            res = self.new_temp()
            self.instructions.append(TACInstruction(node.op, arg1, arg2, res))
            return res
        elif name == 'UnaryOp':
            arg = self.generate(node.operand)
            res = self.new_temp()
            # We use 'unary-' or 'unary+' for clarity, but standard TAC might just use op.
            self.instructions.append(TACInstruction(f"{node.op}", arg, None, res))
            return res
        elif name == 'Assign':
            arg = self.generate(node.value)
            res = node.target
            self.instructions.append(TACInstruction('=', arg, None, res))
            return res
        else:
            raise Exception(f"Unknown AST node type in TAC generator: {name}")

def generate_tac(ast: Any) -> List[TACInstruction]:
    gen = TACGenerator()
    gen.generate(ast)
    return gen.instructions
