from typing import List, Dict
from backend.ir_repr import Quadruple

def count_metrics(quads: List[Quadruple]) -> Dict[str, int]:
    inst_count = len(quads)
    arith_op_count = sum(1 for q in quads if q.op in ('+', '-', '*', '/', '^'))
    temps = set()
    for q in quads:
        for arg in (q.arg1, q.arg2, q.result):
            if arg and isinstance(arg, str) and arg.startswith('t') and arg[1:].isdigit():
                temps.add(arg)
    
    return {
        'instructions': inst_count,
        'arith_ops': arith_op_count,
        'temps': len(temps)
    }

def generate_report(before: List[Quadruple], after: List[Quadruple]) -> str:
    m_before = count_metrics(before)
    m_after = count_metrics(after)
    
    def reduction(b, a):
        if b == 0: return 0.0
        return ((b - a) / b) * 100.0

    lines = []
    lines.append("Optimization Report")
    lines.append("-" * 65)
    lines.append(f"{'Metric':<20} | {'Before':<10} | {'After':<10} | {'Reduction %':<10}")
    lines.append("-" * 65)
    
    for key in ['instructions', 'arith_ops', 'temps']:
        b = m_before[key]
        a = m_after[key]
        r = reduction(b, a)
        lines.append(f"{key:<20} | {b:<10} | {a:<10} | {r:.1f}%")
        
    return '\n'.join(lines)
