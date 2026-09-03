<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arithmetic Expression IR Compiler & Optimizer</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #0a0c10;
      --panel-bg: rgba(18, 22, 31, 0.75);
      --panel-border: rgba(255, 255, 255, 0.08);
      --accent-primary: #6366f1;
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --code-bg: #0d1117;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.15) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.12) 0px, transparent 50%);
      background-attachment: fixed;
      padding-bottom: 40px;
    }

    header {
      border-bottom: 1px solid var(--panel-border);
      background: rgba(10, 12, 16, 0.8);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .logo {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .logo-badge {
      background: linear-gradient(135deg, #6366f1, #06b6d4);
      padding: 6px 12px;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.85rem;
      letter-spacing: 1px;
      color: #fff;
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);
    }

    .logo-title {
      font-size: 1.25rem;
      font-weight: 700;
      background: linear-gradient(to right, #ffffff, #9ca3af);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .arch-pipeline {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.8rem;
      font-weight: 600;
      flex-wrap: wrap;
    }

    .arch-step {
      padding: 4px 10px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--panel-border);
    }

    .arch-step.frontend {
      border-color: rgba(99, 102, 241, 0.4);
      color: #818cf8;
    }

    .arch-step.backend {
      border-color: rgba(6, 182, 212, 0.4);
      color: #22d3ee;
    }

    .arch-arrow {
      color: var(--text-muted);
    }

    main {
      max-width: 1280px;
      margin: 32px auto 0;
      padding: 0 24px;
    }

    .card {
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 16px;
      padding: 24px;
      backdrop-filter: blur(16px);
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
      margin-bottom: 24px;
    }

    .section-title {
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .presets-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 12px;
      margin-bottom: 20px;
    }

    .preset-btn {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--panel-border);
      border-radius: 10px;
      padding: 12px 14px;
      color: var(--text-main);
      text-align: left;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .preset-btn:hover {
      background: rgba(99, 102, 241, 0.1);
      border-color: rgba(99, 102, 241, 0.4);
      transform: translateY(-2px);
    }

    .preset-btn .title {
      font-weight: 600;
      font-size: 0.85rem;
      color: var(--accent-cyan);
      margin-bottom: 4px;
    }

    .preset-btn .expr {
      font-family: 'Fira Code', monospace;
      font-size: 0.75rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .input-group {
      display: flex;
      gap: 12px;
    }

    .expr-input {
      flex: 1;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 12px;
      padding: 14px 18px;
      font-family: 'Fira Code', monospace;
      font-size: 0.95rem;
      color: #fff;
      outline: none;
      transition: border-color 0.2s ease;
    }

    .expr-input:focus {
      border-color: var(--accent-primary);
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    }

    .compile-btn {
      background: linear-gradient(135deg, #6366f1, #4f46e5);
      color: white;
      border: none;
      border-radius: 12px;
      padding: 0 28px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .compile-btn:hover {
      opacity: 0.95;
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(99, 102, 241, 0.4);
    }

    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .metric-card {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--panel-border);
      border-radius: 14px;
      padding: 18px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .metric-info .label {
      font-size: 0.8rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 600;
    }

    .metric-info .vals {
      font-size: 1.4rem;
      font-weight: 800;
      margin-top: 4px;
    }

    .metric-badge {
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 6px 12px;
      border-radius: 20px;
      font-weight: 700;
      font-size: 0.85rem;
    }

    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    @media (max-width: 900px) {
      .grid-2col {
        grid-template-columns: 1fr;
      }
    }

    .code-block {
      background: var(--code-bg);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      padding: 16px;
      font-family: 'Fira Code', monospace;
      font-size: 0.85rem;
      line-height: 1.5;
      overflow-x: auto;
      color: #e5e7eb;
      max-height: 380px;
      overflow-y: auto;
    }

    .ir-table {
      width: 100%;
      border-collapse: collapse;
      font-family: 'Fira Code', monospace;
      font-size: 0.85rem;
    }

    .ir-table th, .ir-table td {
      padding: 10px 14px;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .ir-table th {
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.75rem;
      text-transform: uppercase;
      background: rgba(255, 255, 255, 0.02);
    }

    .ir-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    .op-tag {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 600;
      background: rgba(99, 102, 241, 0.15);
      color: #818cf8;
    }

    .temp-tag {
      color: var(--accent-cyan);
    }

    .tree-node {
      margin-left: 18px;
      padding-left: 10px;
      border-left: 2px solid rgba(255, 255, 255, 0.1);
      margin-top: 6px;
    }

    .tree-label {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      margin-bottom: 4px;
    }

    .tree-label.BinOp { background: rgba(99, 102, 241, 0.2); color: #a5b4fc; }
    .tree-label.Assign { background: rgba(16, 185, 129, 0.2); color: #6ee7b7; }
    .tree-label.Var { background: rgba(6, 182, 212, 0.2); color: #67e8f9; }
    .tree-label.Num { background: rgba(245, 158, 11, 0.2); color: #fde047; }

    .trace-item {
      padding: 10px 14px;
      border-left: 3px solid var(--accent-cyan);
      background: rgba(6, 182, 212, 0.05);
      margin-bottom: 8px;
      border-radius: 0 8px 8px 0;
      font-size: 0.85rem;
    }

    .trace-item.iter {
      border-left-color: var(--accent-primary);
      background: rgba(99, 102, 241, 0.1);
      font-weight: 700;
    }

    .trace-item.dce {
      border-left-color: var(--accent-rose);
      background: rgba(244, 63, 94, 0.1);
    }

    .tabs {
      display: flex;
      gap: 8px;
      border-bottom: 1px solid var(--panel-border);
      margin-bottom: 16px;
    }

    .tab-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      padding: 10px 16px;
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.2s;
    }

    .tab-btn.active {
      color: #fff;
      border-bottom-color: var(--accent-primary);
    }
  </style>
</head>
<body>

  <header>
    <div class="header-container">
      <div class="logo">
        <div class="logo-badge">IR COMPILER</div>
        <div class="logo-title">Arithmetic Expression Engine</div>
      </div>
      <div class="arch-pipeline">
        <span class="arch-step frontend">FRONT END (Lexer/Parser)</span>
        <span class="arch-arrow">➔</span>
        <span class="arch-step">AST</span>
        <span class="arch-arrow">➔</span>
        <span class="arch-step backend">BACK END (TAC / IR)</span>
        <span class="arch-arrow">➔</span>
        <span class="arch-step backend">OPTIMIZER</span>
      </div>
    </div>
  </header>

  <main>
    <!-- Expression Input & Presets -->
    <div class="card">
      <div class="section-title">
        <span>⚡ Expression Input & Test Demos</span>
      </div>
      <div class="presets-grid">
        <button class="preset-btn" onclick="setExpression(0)">
          <div class="title">🎯 Finance Expression</div>
          <div class="expr">finalValue = ((principal * rate * time) / 100) + ...</div>
        </button>
        <button class="preset-btn" onclick="setExpression(1)">
          <div class="title">🔥 Constant Folding Demo</div>
          <div class="expr">result = a * (2 + 3) * (10 / 2) + b</div>
        </button>
        <button class="preset-btn" onclick="setExpression(2)">
          <div class="title">🔄 CSE Demo</div>
          <div class="expr">result = (a*b) + (a*b) - (c*d) + (d*c)</div>
        </button>
        <button class="preset-btn" onclick="setExpression(3)">
          <div class="title">💥 Cascading DCE Demo</div>
          <div class="expr">result = (a + b) - (a + b) + c</div>
        </button>
      </div>

      <div class="input-group">
        <input type="text" id="exprInput" class="expr-input" value="finalValue = ((principal * rate * time) / 100) + (principal * (1 + rate/100)^time) - fees" placeholder="Type arithmetic expression...">
        <button class="compile-btn" onclick="compile()">
          <span>Compile & Optimize</span>
          <span>🚀</span>
        </button>
      </div>
    </div>

    <!-- Optimization Report Summary -->
    <div class="metrics-grid" id="metricsGrid"></div>

    <!-- Main Results Layout -->
    <div class="grid-2col">
      <!-- Left Column: Front-End AST & Initial IR -->
      <div>
        <div class="card">
          <div class="section-title">
            <span>🌳 Front-End: Abstract Syntax Tree (AST)</span>
          </div>
          <div id="astContainer" class="code-block"></div>
        </div>

        <div class="card">
          <div class="tabs">
            <button class="tab-btn active" onclick="switchIrTab('tac')">Three-Address Code (TAC)</button>
            <button class="tab-btn" onclick="switchIrTab('quads')">Quadruples IR</button>
            <button class="tab-btn" onclick="switchIrTab('triples')">Triples IR</button>
          </div>
          <div id="irContainer"></div>
        </div>
      </div>

      <!-- Right Column: Optimizer & Optimized Quadruples -->
      <div>
        <div class="card">
          <div class="section-title">
            <span>⚙️ Back-End: Optimization Pass Trace</span>
          </div>
          <div id="traceContainer" class="code-block" style="max-height: 250px;"></div>
        </div>

        <div class="card">
          <div class="section-title">
            <span>✨ Optimized Quadruples IR</span>
          </div>
          <div id="optQuadsContainer"></div>
        </div>
      </div>
    </div>
  </main>

  <script>
    // -------------------------------------------------------------
    // CLIENT-SIDE COMPILER ENGINE (Lexer, Parser, TAC, Optimizer)
    // -------------------------------------------------------------

    // 1. LEXER
    function lex(text) {
      const tokens = [];
      const regex = /\s*(\d+(?:\.\d*)?|[A-Za-z_][A-Za-z0-9_]*|\+|-|\*|\/|\^|\(|\)|=)\s*/g;
      let match;
      let lastIndex = 0;
      while ((match = regex.exec(text)) !== null) {
        const val = match[1];
        let type = 'MISMATCH';
        if (/^\d+(\.\d*)?$/.test(val)) type = 'NUM';
        else if (/^[A-Za-z_][A-Za-z0-9_]*$/.test(val)) type = 'ID';
        else if (val === '=') type = 'ASSIGN';
        else if (val === '+') type = 'PLUS';
        else if (val === '-') type = 'MINUS';
        else if (val === '*') type = 'MUL';
        else if (val === '/') type = 'DIV';
        else if (val === '^') type = 'POW';
        else if (val === '(') type = 'LPAREN';
        else if (val === ')') type = 'RPAREN';
        tokens.push({ type, value: val });
      }
      tokens.push({ type: 'EOF', value: '' });
      return tokens;
    }

    // 2. PARSER
    class Parser {
      constructor(tokens) {
        this.tokens = tokens;
        this.pos = 0;
      }
      current() { return this.tokens[this.pos] || { type: 'EOF', value: '' }; }
      consume(type) {
        const tok = this.current();
        if (tok.type === type) { this.pos++; return tok; }
        throw new Error(`Expected ${type}, got ${tok.type}`);
      }
      parse() {
        const tok = this.current();
        if (tok.type === 'ID' && this.tokens[this.pos + 1] && this.tokens[this.pos + 1].type === 'ASSIGN') {
          this.consume('ID');
          this.consume('ASSIGN');
          const value = this.parseExpr();
          return { type: 'Assign', target: tok.value, value };
        }
        return this.parseExpr();
      }
      parseExpr() {
        let node = this.parseTerm();
        while (['PLUS', 'MINUS'].includes(this.current().type)) {
          const op = this.current().type === 'PLUS' ? '+' : '-';
          this.pos++;
          const right = this.parseTerm();
          node = { type: 'BinOp', op, left: node, right };
        }
        return node;
      }
      parseTerm() {
        let node = this.parseUnary();
        while (['MUL', 'DIV'].includes(this.current().type)) {
          const op = this.current().type === 'MUL' ? '*' : '/';
          this.pos++;
          const right = this.parseUnary();
          node = { type: 'BinOp', op, left: node, right };
        }
        return node;
      }
      parseUnary() {
        if (['PLUS', 'MINUS'].includes(this.current().type)) {
          const op = this.current().type === 'PLUS' ? '+' : '-';
          this.pos++;
          const operand = this.parseUnary();
          return { type: 'UnaryOp', op, operand };
        }
        return this.parsePower();
      }
      parsePower() {
        let node = this.parseAtom();
        if (this.current().type === 'POW') {
          this.pos++;
          const right = this.parseUnary();
          node = { type: 'BinOp', op: '^', left: node, right };
        }
        return node;
      }
      parseAtom() {
        const tok = this.current();
        if (tok.type === 'NUM') { this.pos++; return { type: 'Num', value: parseFloat(tok.value) }; }
        if (tok.type === 'ID') { this.pos++; return { type: 'Var', name: tok.value }; }
        if (tok.type === 'LPAREN') {
          this.pos++;
          const expr = this.parseExpr();
          this.consume('RPAREN');
          return expr;
        }
        throw new Error(`Unexpected token ${tok.type} ('${tok.value}')`);
      }
    }

    // 3. TAC & IR GENERATOR
    class TACGen {
      constructor() {
        this.instructions = [];
        this.tempCount = 0;
      }
      newTemp() {
        this.tempCount++;
        return `t${this.tempCount}`;
      }
      formatNum(val) {
        return Number.isInteger(val) ? String(val) : String(val);
      }
      gen(node) {
        if (node.type === 'Num') return this.formatNum(node.value);
        if (node.type === 'Var') return node.name;
        if (node.type === 'BinOp') {
          const arg1 = this.gen(node.left);
          const arg2 = this.gen(node.right);
          const res = this.newTemp();
          this.instructions.push({ op: node.op, arg1, arg2, result: res });
          return res;
        }
        if (node.type === 'UnaryOp') {
          const arg = this.gen(node.operand);
          const res = this.newTemp();
          this.instructions.push({ op: node.op, arg1: arg, arg2: null, result: res });
          return res;
        }
        if (node.type === 'Assign') {
          const arg = this.gen(node.value);
          this.instructions.push({ op: '=', arg1: arg, arg2: null, result: node.target });
          return node.target;
        }
      }
    }

    // 4. OPTIMIZER PASSES
    function isNum(s) {
      if (s === null || s === undefined) return false;
      return !isNaN(parseFloat(s)) && isFinite(s);
    }

    function evalConst(op, a1, a2) {
      const v1 = parseFloat(a1);
      if (a2 !== null && a2 !== undefined) {
        const v2 = parseFloat(a2);
        if (op === '+') return v1 + v2;
        if (op === '-') return v1 - v2;
        if (op === '*') return v1 * v2;
        if (op === '/') return v1 / v2;
        if (op === '^') return Math.pow(v1, v2);
      } else {
        if (op === '+') return v1;
        if (op === '-') return -v1;
      }
      return null;
    }

    function passConstantFolding(quads) {
      let changed = false;
      quads.forEach(q => {
        if (['+', '-', '*', '/', '^'].includes(q.op) && isNum(q.arg1) && (q.arg2 === null || isNum(q.arg2))) {
          const res = evalConst(q.op, q.arg1, q.arg2);
          if (res !== null && !isNaN(res)) {
            q.op = '=';
            q.arg1 = Number.isInteger(res) ? String(res) : String(res);
            q.arg2 = null;
            changed = true;
          }
        }
      });
      return changed;
    }

    function passCSE(quads) {
      let changed = false;
      const seen = {};
      quads.forEach(q => {
        if (q.op === '=') return;
        const key = `${q.op}|${q.arg1}|${q.arg2}`;
        const keyComm = ['+', '*'].includes(q.op) ? `${q.op}|${q.arg2}|${q.arg1}` : null;
        if (seen[key]) {
          q.op = '=';
          q.arg1 = seen[key];
          q.arg2 = null;
          changed = true;
        } else if (keyComm && seen[keyComm]) {
          q.op = '=';
          q.arg1 = seen[keyComm];
          q.arg2 = null;
          changed = true;
        } else {
          seen[key] = q.result;
        }
      });
      return changed;
    }

    function passAlgebraicSimplification(quads) {
      let changed = false;
      quads.forEach(q => {
        if (q.op === '*') {
          if (q.arg1 === '1') { q.op = '='; q.arg1 = q.arg2; q.arg2 = null; changed = true; }
          else if (q.arg2 === '1') { q.op = '='; q.arg2 = null; changed = true; }
          else if (q.arg1 === '0' || q.arg2 === '0') { q.op = '='; q.arg1 = '0'; q.arg2 = null; changed = true; }
        } else if (q.op === '+') {
          if (q.arg1 === '0') { q.op = '='; q.arg1 = q.arg2; q.arg2 = null; changed = true; }
          else if (q.arg2 === '0') { q.op = '='; q.arg2 = null; changed = true; }
        } else if (q.op === '/') {
          if (q.arg2 === '1') { q.op = '='; q.arg2 = null; changed = true; }
          else if (q.arg1 === q.arg2 && q.arg1 && !isNum(q.arg1)) { q.op = '='; q.arg1 = '1'; q.arg2 = null; changed = true; }
          else if (q.arg1 === '0' && q.arg2 !== '0') { q.op = '='; q.arg1 = '0'; q.arg2 = null; changed = true; }
        } else if (q.op === '-') {
          if (q.arg2 === '0') { q.op = '='; q.arg2 = null; changed = true; }
          else if (q.arg1 === q.arg2 && q.arg1 && !isNum(q.arg1)) { q.op = '='; q.arg1 = '0'; q.arg2 = null; changed = true; }
        } else if (q.op === '^') {
          if (q.arg2 === '1') { q.op = '='; q.arg2 = null; changed = true; }
          else if (q.arg2 === '0') { q.op = '='; q.arg1 = '1'; q.arg2 = null; changed = true; }
        }
      });
      return changed;
    }

    function passCopyPropagation(quads) {
      let changed = false;
      const map = {};
      quads.forEach(q => {
        if (map[q.arg1]) { q.arg1 = map[q.arg1]; changed = true; }
        if (map[q.arg2]) { q.arg2 = map[q.arg2]; changed = true; }
        if (q.op === '=') { map[q.result] = q.arg1; }
      });
      return changed;
    }

    function passDCE(quads, finalTarget) {
      if (!quads.length) return [];
      const tgt = finalTarget || quads[quads.length - 1].result;
      const live = new Set([tgt]);
      const newQuads = [];
      for (let i = quads.length - 1; i >= 0; i--) {
        const q = quads[i];
        if (live.has(q.result)) {
          newQuads.unshift(q);
          if (q.arg1 && !isNum(q.arg1)) live.add(q.arg1);
          if (q.arg2 && !isNum(q.arg2)) live.add(q.arg2);
        }
      }
      return newQuads;
    }

    function optimize(quads) {
      let current = quads.map(q => ({ ...q }));
      const trace = [];
      const finalTgt = current.length ? current[current.length - 1].result : null;
      let changed = true;
      let iter = 1;

      while (changed) {
        changed = false;
        trace.push(`--- Iteration ${iter} ---`);
        const c1 = passConstantFolding(current);
        if (c1) trace.push("Applied Constant Folding");
        changed = changed || c1;

        const c2 = passCSE(current);
        if (c2) trace.push("Applied Common Subexpression Elimination");
        changed = changed || c2;

        const c3 = passAlgebraicSimplification(current);
        if (c3) trace.push("Applied Algebraic Simplification");
        changed = changed || c3;

        const c4 = passCopyPropagation(current);
        if (c4) trace.push("Applied Copy Propagation");
        changed = changed || c4;

        iter++;
      }

      const prevLen = current.length;
      current = passDCE(current, finalTgt);
      if (current.length < prevLen) {
        trace.push("Applied Dead Code Elimination");
      }

      return { optQuads: current, trace };
    }

    function countMetrics(quads) {
      const insts = quads.length;
      const arith = quads.filter(q => ['+', '-', '*', '/', '^'].includes(q.op)).length;
      const temps = new Set();
      quads.forEach(q => {
        [q.arg1, q.arg2, q.result].forEach(arg => {
          if (arg && /^t\d+$/.test(arg)) temps.add(arg);
        });
      });
      return { instructions: insts, arith_ops: arith, temps: temps.size };
    }

    // -------------------------------------------------------------
    // UI CONTROLLER
    // -------------------------------------------------------------
    const presets = [
      "finalValue = ((principal * rate * time) / 100) + (principal * (1 + rate/100)^time) - fees",
      "result = a * (2 + 3) * (10 / 2) + b",
      "result = (a*b) + (a*b) - (c*d) + (d*c)",
      "result = (a + b) - (a + b) + c"
    ];

    let currentIrTab = 'tac';
    let currentData = null;

    function setExpression(idx) {
      document.getElementById('exprInput').value = presets[idx];
      compile();
    }

    function switchIrTab(tab) {
      currentIrTab = tab;
      document.querySelectorAll('.tabs .tab-btn').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
      renderIr();
    }

    function compile() {
      const expr = document.getElementById('exprInput').value;
      try {
        const tokens = lex(expr);
        const parser = new Parser(tokens);
        const ast = parser.parse();
        const tacGen = new TACGen();
        tacGen.gen(ast);
        const quads = tacGen.instructions;
        
        // Build Triples
        const tempToIdx = {};
        const triples = quads.map((q, idx) => {
          let a1 = q.arg1 in tempToIdx ? `(${tempToIdx[q.arg1]})` : q.arg1;
          let a2 = q.arg2 in tempToIdx ? `(${tempToIdx[q.arg2]})` : q.arg2;
          if (q.op === '=') {
            return { index: idx, op: '=', arg1: q.result, arg2: a1 };
          } else {
            tempToIdx[q.result] = idx;
            return { index: idx, op: q.op, arg1: a1, arg2: a2 || '' };
          }
        });

        const { optQuads, trace } = optimize(quads);
        const mBefore = countMetrics(quads);
        const mAfter = countMetrics(optQuads);

        const calcRed = (b, a) => b === 0 ? 0 : Math.round(((b - a) / b) * 1000) / 10;

        currentData = {
          success: true,
          expression: expr,
          ast_dict: ast,
          tac: quads.map(q => q.op === '=' ? `${q.result} = ${q.arg1}` : (q.arg2 ? `${q.result} = ${q.arg1} ${q.op} ${q.arg2}` : `${q.result} = ${q.op} ${q.arg1}`)),
          quads: quads.map(q => ({ op: q.op, arg1: q.arg1, arg2: q.arg2 || '', result: q.result })),
          triples,
          opt_quads: optQuads.map(q => ({ op: q.op, arg1: q.arg1, arg2: q.arg2 || '', result: q.result })),
          opt_trace: trace,
          metrics: {
            before: mBefore,
            after: mAfter,
            reduction: {
              instructions: calcRed(mBefore.instructions, mAfter.instructions),
              arith_ops: calcRed(mBefore.arith_ops, mAfter.arith_ops),
              temps: calcRed(mBefore.temps, mAfter.temps)
            }
          }
        };

        renderAll();
      } catch (err) {
        alert('Compilation Error: ' + err.message);
      }
    }

    function renderAll() {
      if(!currentData) return;
      renderMetrics();
      renderAst();
      renderIr();
      renderTrace();
      renderOptQuads();
    }

    function renderMetrics() {
      const m = currentData.metrics;
      const container = document.getElementById('metricsGrid');
      container.innerHTML = `
        <div class="metric-card">
          <div class="metric-info">
            <div class="label">Instructions</div>
            <div class="vals">${m.before.instructions} ➔ ${m.after.instructions}</div>
          </div>
          <div class="metric-badge">-${m.reduction.instructions}%</div>
        </div>
        <div class="metric-card">
          <div class="metric-info">
            <div class="label">Arithmetic Ops</div>
            <div class="vals">${m.before.arith_ops} ➔ ${m.after.arith_ops}</div>
          </div>
          <div class="metric-badge">-${m.reduction.arith_ops}%</div>
        </div>
        <div class="metric-card">
          <div class="metric-info">
            <div class="label">Temporaries</div>
            <div class="vals">${m.before.temps} ➔ ${m.after.temps}</div>
          </div>
          <div class="metric-badge">-${m.reduction.temps}%</div>
        </div>
      `;
    }

    function renderAstNode(node) {
      if(node.type === 'Num') {
        return `<div class="tree-node"><span class="tree-label Num">Num(${node.value})</span></div>`;
      } else if(node.type === 'Var') {
        return `<div class="tree-node"><span class="tree-label Var">Var(${node.name})</span></div>`;
      } else if(node.type === 'BinOp') {
        return `
          <div class="tree-node">
            <span class="tree-label BinOp">BinOp(${node.op})</span>
            ${renderAstNode(node.left)}
            ${renderAstNode(node.right)}
          </div>
        `;
      } else if(node.type === 'UnaryOp') {
        return `
          <div class="tree-node">
            <span class="tree-label BinOp">UnaryOp(${node.op})</span>
            ${renderAstNode(node.operand)}
          </div>
        `;
      } else if(node.type === 'Assign') {
        return `
          <div class="tree-node">
            <span class="tree-label Assign">Assign(${node.target})</span>
            ${renderAstNode(node.value)}
          </div>
        `;
      }
      return '';
    }

    function renderAst() {
      const container = document.getElementById('astContainer');
      container.innerHTML = renderAstNode(currentData.ast_dict);
    }

    function renderIr() {
      const container = document.getElementById('irContainer');
      if(currentIrTab === 'tac') {
        let lines = currentData.tac.map((t, idx) => `<div><span style="color: #6b7280; width: 28px; display: inline-block;">${idx}:</span> ${t}</div>`).join('');
        container.innerHTML = `<div class="code-block">${lines}</div>`;
      } else if(currentIrTab === 'quads') {
        let rows = currentData.quads.map((q, idx) => `
          <tr>
            <td>${idx}</td>
            <td><span class="op-tag">${q.op}</span></td>
            <td>${q.arg1}</td>
            <td>${q.arg2}</td>
            <td><span class="temp-tag">${q.result}</span></td>
          </tr>
        `).join('');
        container.innerHTML = `
          <table class="ir-table">
            <thead>
              <tr><th>#</th><th>Op</th><th>Arg1</th><th>Arg2</th><th>Result</th></tr>
            </thead>
            <tbody>${rows}</tbody>
          </table>
        `;
      } else if(currentIrTab === 'triples') {
        let rows = currentData.triples.map(t => `
          <tr>
            <td>(${t.index})</td>
            <td><span class="op-tag">${t.op}</span></td>
            <td>${t.arg1}</td>
            <td>${t.arg2}</td>
          </tr>
        `).join('');
        container.innerHTML = `
          <table class="ir-table">
            <thead>
              <tr><th>Triple #</th><th>Op</th><th>Arg1</th><th>Arg2</th></tr>
            </thead>
            <tbody>${rows}</tbody>
          </table>
        `;
      }
    }

    function renderTrace() {
      const container = document.getElementById('traceContainer');
      if(!currentData.opt_trace || currentData.opt_trace.length === 0) {
        container.innerHTML = `<div class="trace-item">No optimization changes required.</div>`;
        return;
      }
      let html = currentData.opt_trace.map(t => {
        let cls = 'trace-item';
        if(t.includes('Iteration')) cls += ' iter';
        if(t.includes('Dead Code')) cls += ' dce';
        return `<div class="${cls}">${t}</div>`;
      }).join('');
      container.innerHTML = html;
    }

    function renderOptQuads() {
      const container = document.getElementById('optQuadsContainer');
      if(!currentData.opt_quads || currentData.opt_quads.length === 0) {
        container.innerHTML = `<div class="code-block">Empty (All dead code eliminated)</div>`;
        return;
      }
      let rows = currentData.opt_quads.map((q, idx) => `
        <tr>
          <td>${idx}</td>
          <td><span class="op-tag">${q.op}</span></td>
          <td>${q.arg1}</td>
          <td>${q.arg2}</td>
          <td><span class="temp-tag">${q.result}</span></td>
        </tr>
      `).join('');
      container.innerHTML = `
        <table class="ir-table">
          <thead>
            <tr><th>#</th><th>Op</th><th>Arg1</th><th>Arg2</th><th>Result</th></tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>
      `;
    }

    // Initial compile on load
    compile();
  </script>
</body>
</html>
