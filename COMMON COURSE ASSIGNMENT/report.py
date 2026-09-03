from dataclasses import dataclass
from typing import List, Optional
from backend.tac_gen import TACInstruction

@dataclass
class Quadruple:
    op: str
    arg1: str
    arg2: Optional[str]
    result: str

    def __str__(self):
        a2 = self.arg2 if self.arg2 is not None else ''
        return f"({self.op}, {self.arg1}, {a2}, {self.result})"
    
    def copy(self):
        return Quadruple(self.op, self.arg1, self.arg2, self.result)

@dataclass
class Triple:
    op: str
    arg1: str
    arg2: Optional[str]

    def __str__(self):
        a2 = self.arg2 if self.arg2 is not None else ''
        return f"({self.op}, {self.arg1}, {a2})"

def tac_to_quadruples(tac: List[TACInstruction]) -> List[Quadruple]:
    return [Quadruple(inst.op, inst.arg1, inst.arg2, inst.result) for inst in tac]

def tac_to_triples(tac: List[TACInstruction]) -> List[Triple]:
    triples = []
    # Map a result temporary to its zero-based index in the triples list
    temp_to_index = {}
    
    for i, inst in enumerate(tac):
        arg1 = inst.arg1
        if arg1 in temp_to_index:
            arg1 = f"({temp_to_index[arg1]})"
            
        arg2 = inst.arg2
        if arg2 is not None and arg2 in temp_to_index:
            arg2 = f"({temp_to_index[arg2]})"
            
        if inst.op == '=':
            # For assignment, triple conventionally puts target in arg1, source in arg2
            triples.append(Triple(inst.op, inst.result, arg1))
        else:
            triples.append(Triple(inst.op, arg1, arg2))
            temp_to_index[inst.result] = i
            
    return triples
