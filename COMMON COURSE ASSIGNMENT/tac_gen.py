from typing import List, Tuple
from backend.ir_repr import Quadruple

def is_num(s: str) -> bool:
    if s is None:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

def eval_const(op: str, arg1: str, arg2: str = None) -> float:
    v1 = float(arg1)
    if arg2 is not None:
        v2 = float(arg2)
        if op == '+': return v1 + v2
        if op == '-': return v1 - v2
        if op == '*': return v1 * v2
        if op == '/': return v1 / v2
        if op == '^': return v1 ** v2
    else:
        if op == '+': return v1
        if op == '-': return -v1
    raise ValueError(f"Unknown op {op}")

def format_num(val: float) -> str:
    if val == int(val):
        return str(int(val))
    return str(val)

def pass_constant_folding(quads: List[Quadruple]) -> Tuple[List[Quadruple], bool]:
    changed = False
    for i, q in enumerate(quads):
        if q.op in ('+', '-', '*', '/', '^') and is_num(q.arg1) and (q.arg2 is None or is_num(q.arg2)):
            try:
                res = eval_const(q.op, q.arg1, q.arg2)
                q.op = '='
                q.arg1 = format_num(res)
                q.arg2 = None
                changed = True
            except ZeroDivisionError:
                pass
    return quads, changed

def pass_cse(quads: List[Quadruple]) -> Tuple[List[Quadruple], bool]:
    changed = False
    # To detect CSE, we map context (op, arg1, arg2) to the result variable of the first occurrence.
    seen = {}
    for q in quads:
        if q.op == '=':
            continue
        key = (q.op, q.arg1, q.arg2)
        key_comm = (q.op, q.arg2, q.arg1) if q.op in ('+', '*') else None
        
        if key in seen:
            q.op = '='
            q.arg1 = seen[key]
            q.arg2 = None
            changed = True
        elif key_comm and key_comm in seen:
            q.op = '='
            q.arg1 = seen[key_comm]
            q.arg2 = None
            changed = True
        else:
            seen[key] = q.result
    return quads, changed

def pass_algebraic_simplification(quads: List[Quadruple]) -> Tuple[List[Quadruple], bool]:
    changed = False
    for q in quads:
        if q.op == '*':
            if q.arg1 == '1' or q.arg1 == '1.0':
                q.op = '='
                q.arg1 = q.arg2
                q.arg2 = None
                changed = True
            elif q.arg2 == '1' or q.arg2 == '1.0':
                q.op = '='
                q.arg2 = None
                changed = True
            elif q.arg1 == '0' or q.arg1 == '0.0' or q.arg2 == '0' or q.arg2 == '0.0':
                q.op = '='
                q.arg1 = '0'
                q.arg2 = None
                changed = True
        elif q.op == '+':
            if q.arg1 == '0' or q.arg1 == '0.0':
                q.op = '='
                q.arg1 = q.arg2
                q.arg2 = None
                changed = True
            elif q.arg2 == '0' or q.arg2 == '0.0':
                q.op = '='
                q.arg2 = None
                changed = True
        elif q.op == '/':
            if q.arg2 == '1' or q.arg2 == '1.0':
                q.op = '='
                q.arg2 = None
                changed = True
            elif q.arg1 == q.arg2 and q.arg1 is not None and not is_num(q.arg1): # x/x -> 1
                q.op = '='
                q.arg1 = '1'
                q.arg2 = None
                changed = True
            elif (q.arg1 == '0' or q.arg1 == '0.0') and q.arg2 != '0' and q.arg2 != '0.0':
                q.op = '='
                q.arg1 = '0'
                q.arg2 = None
                changed = True
        elif q.op == '-':
            if q.arg2 == '0' or q.arg2 == '0.0':
                q.op = '='
                q.arg2 = None
                changed = True
            elif q.arg1 == q.arg2 and q.arg1 is not None and not is_num(q.arg1): # x - x -> 0
                q.op = '='
                q.arg1 = '0'
                q.arg2 = None
                changed = True
        elif q.op == '^':
            if q.arg2 == '1' or q.arg2 == '1.0':
                q.op = '='
                q.arg2 = None
                changed = True
            elif q.arg2 == '0' or q.arg2 == '0.0':
                q.op = '='
                q.arg1 = '1'
                q.arg2 = None
                changed = True
    return quads, changed

def pass_copy_propagation(quads: List[Quadruple]) -> Tuple[List[Quadruple], bool]:
    changed = False
    # Map from variable/temp to its replacement
    replacements = {}
    for q in quads:
        # First, apply any known replacements to RHS
        if q.arg1 in replacements:
            q.arg1 = replacements[q.arg1]
            changed = True
        if q.arg2 in replacements:
            q.arg2 = replacements[q.arg2]
            changed = True
            
        # If this is a copy instruction, register it
        if q.op == '=':
            # Only propagate if we don't redefine things, but in SSA-like TAC, 
            # temporaries are assigned exactly once. 
            # We will propagate both variables and temporaries.
            replacements[q.result] = q.arg1
    return quads, changed

def pass_dead_code_elimination(quads: List[Quadruple], final_target: str = None) -> List[Quadruple]:
    if not quads:
        return quads
    
    # Normally we infer the final target if not provided, assuming it's the result of the last instruction.
    if not final_target:
        final_target = quads[-1].result
        
    live = {final_target}
    new_quads = []
    
    for q in reversed(quads):
        if q.result in live:
            new_quads.append(q)
            if q.arg1 and not is_num(q.arg1):
                live.add(q.arg1)
            if q.arg2 and not is_num(q.arg2):
                live.add(q.arg2)
        else:
            # instruction is dead!
            pass
            
    return list(reversed(new_quads))

def optimize(quads: List[Quadruple], trace: bool = False) -> Tuple[List[Quadruple], List[str]]:
    # Work on a copy
    current = [q.copy() for q in quads]
    logs = []
    
    # We want to know the final target variable for DCE.
    final_tgt = current[-1].result if current else None
    if current and current[-1].op == "=" and not current[-1].result.startswith("t"):
        # Explicit assignment to user variable
        final_tgt = current[-1].result
        
    changed = True
    iteration = 1
    while changed:
        changed = False
        if trace: logs.append(f"--- Iteration {iteration} ---")
        
        current, c = pass_constant_folding(current)
        if c and trace: logs.append("Applied Constant Folding")
        changed = changed or c
        
        current, c = pass_cse(current)
        if c and trace: logs.append("Applied Common Subexpression Elimination")
        changed = changed or c
        
        current, c = pass_algebraic_simplification(current)
        if c and trace: logs.append("Applied Algebraic Simplification")
        changed = changed or c
        
        current, c = pass_copy_propagation(current)
        if c and trace: logs.append("Applied Copy Propagation")
        changed = changed or c
        
        iteration += 1

    current_len = len(current)
    current = pass_dead_code_elimination(current, final_tgt)
    if trace and len(current) < current_len:
         logs.append("Applied Dead Code Elimination")
         
    return current, logs
