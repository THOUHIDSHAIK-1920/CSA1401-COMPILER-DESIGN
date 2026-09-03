import re
from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int

class LexerError(Exception):
    pass

def lex(text: str) -> List[Token]:
    token_specification = [
        ('NUM',    r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN', r'='),            # Assignment operator
        ('ID',     r'[A-Za-z_][A-Za-z0-9_]*'), # Identifiers
        ('PLUS',   r'\+'),           # Addition
        ('MINUS',  r'-'),            # Subtraction
        ('MUL',    r'\*'),           # Multiplication
        ('DIV',    r'/'),            # Division
        ('POW',    r'\^'),           # Exponentiation
        ('LPAREN', r'\('),           # Left Parenthesis
        ('RPAREN', r'\)'),           # Right Parenthesis
        ('SKIP',   r'[ \t]+'),       # Skip over spaces and tabs
        ('NEWLINE',r'\n'),           # Line endings
        ('MISMATCH',r'.'),           # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    tokens = []
    
    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUM':
            tokens.append(Token(kind, value, line_num, column))
        elif kind == 'ID':
            tokens.append(Token(kind, value, line_num, column))
        elif kind in ('PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'LPAREN', 'RPAREN', 'ASSIGN'):
            tokens.append(Token(kind, value, line_num, column))
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise LexerError(f"Unexpected character {value!r} on line {line_num}")
    tokens.append(Token('EOF', '', line_num, len(text) - line_start))
    return tokens
