from frontend.parser import parse, ast_to_text
from backend.tac_gen import generate_tac
from backend.ir_repr import tac_to_quadruples, tac_to_triples
from backend.optimizer import optimize
from backend.report import generate_report

class CompileResult:
    def __init__(self, ast, ast_text, tac, quads, triples, opt_quads, opt_trace, report):
        self.ast = ast
        self.ast_text = ast_text
        self.tac = tac
        self.quads = quads
        self.triples = triples
        self.opt_quads = opt_quads
        self.opt_trace = opt_trace
        self.report = report

def compile_expression(source: str) -> CompileResult:
    ast = parse(source)
    ast_text = ast_to_text(ast)
    tac = generate_tac(ast)
    quads = tac_to_quadruples(tac)
    triples = tac_to_triples(tac)
    opt_quads, opt_trace = optimize(quads, trace=True)
    report = generate_report(quads, opt_quads)
    
    return CompileResult(ast, ast_text, tac, quads, triples, opt_quads, opt_trace, report)
