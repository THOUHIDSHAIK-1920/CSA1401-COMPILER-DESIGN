# Arithmetic Expression Compiler

This project implements a compiler front end and back end for arithmetic expressions.

## Architecture

*   **FRONT END:** Parses source code text into an Abstract Syntax Tree (AST). Completely independent from the back end.
*   **BACK END:** Lowers the AST into Three-Address Code (TAC), translates it to Quadruples and Triples, and applies optimization passes to the Quadruple IR to reduce execution cost.

## Intermediate Representation (IR) Formats

The Back End translates the AST into Three Address Code (TAC), which generates instructions sequentially using fresh temporaries. These instructions are typically represented as **Quadruples** or **Triples**.

*   **Quadruples:** A quadruple is a tuple of the form `(op, arg1, arg2, result)`. Each temporary generated during TAC is explicitly named as a target. Both source operands can be variables, numeric literals, or explicit temporaries.
*   **Triples:** A triple is a tuple of the form `(op, arg1, arg2)`. There is no explicit `result` field. Instead, when a later instruction needs to refer to the computation from a previous instruction, it refers to it directly by its *position* or index in the triple array, for example `(3)`, meaning the value produced by the 4th instruction.

### Why Optimization Operates on Quadruples (not Triples)

The optimization passes in this project operate exclusively on **Quadruples**. Why?

Because the passes (like Common Subexpression Elimination and Dead Code Elimination) routinely require **deleting** and **reordering** instructions. If we used Triples, where instructions refer to arguments by their array index, deleting a single dead instruction would invalidate all downstream position indices and require updating the entire remainder of the program! Quadruples give each result a firm identity (temp name), making the instructions order-independent and safely updatable in place.

## Optimization Passes

### Constant Folding
Evaluating instructions at compile-time when both of its operands are numeric constants. This prevents the runtime from doing repetitive calculations.
*   *Before:* `t1 = 2 + 3`
*   *After:*  `t1 = 5`

### Common Subexpression Elimination (CSE)
If a computation identically matches a previously executed computation, we do not emit a new calculation. Instead, we insert a copy instruction, reusing the original temporary.
*   *Before:* `t1 = a * b`, `t2 = a * b`
*   *After:* `t1 = a * b`, `t2 = t1`

### Copy Propagation
Often as a result of CSE or Algebraic Simplification, we end up with simple copy instructions (`t2 = t1`). Copy propagation replaces all later uses of the target (`t2`) with the source (`t1`), allowing the copy instruction itself to be eliminated.
*   *Before:* `t2 = t1`, `t3 = t2 + c`
*   *After:* `t2 = t1`, `t3 = t1 + c`

### Algebraic Simplification
Applying basic mathematical rules to simplify expressions that involve variables and identities (like multiplying by 1 or adding 0) or expressions that cancel themselves out (like `x - x`).
*   *Before:* `t3 = t1 - t1`
*   *After:* `t3 = 0`

### Dead Code Elimination (DCE)
By running a backward liveness analysis starting from the final assigned result variable, we can determine which temporaries are never used. Dead Code Elimination removes instructions computing those ignored temporaries.
*   *Before:* `t1 = a + b`, `result = c` (where `t1` is never read)
*   *After:* `result = c`
