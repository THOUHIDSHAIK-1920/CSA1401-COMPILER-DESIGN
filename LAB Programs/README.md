# LEX / Flex Programming on Windows

## Required Software

| Software | Expected Path |
|----------|--------------|
| **Flex (GnuWin32)** | `C:\Program Files (x86)\GnuWin32\bin\flex.exe` |
| **GCC (TDM-GCC-64)** | `C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\bin\gcc.exe` |

## Required PATH Entries

Add these folders to your Windows **User PATH** environment variable:

```
C:\Program Files (x86)\GnuWin32\bin
C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\bin
```

### How to add to PATH (PowerShell - Administrator not required):

```powershell
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
$newEntries = "C:\Program Files (x86)\GnuWin32\bin;C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\bin"
[Environment]::SetEnvironmentVariable("Path", $currentPath + ";" + $newEntries, "User")
```

Restart your terminal after updating PATH for the changes to take effect.

---

## How to Create a LEX File

1. Create a new file with a `.l` extension (e.g., `myprogram.l`).
2. Write your LEX code using this structure:

```lex
%{
#include <stdio.h>
%}

%%
/* Pattern-action rules */
[0-9]+      { printf("Number: %s\n", yytext); }
[a-zA-Z]+   { printf("Word: %s\n", yytext); }
[ \t\n]+    ;                           /* ignore whitespace */
.           { printf("Symbol: %s\n", yytext); }
%%

int yywrap() { return 1; }

int main() {
    yylex();
    return 0;
}
```

### LEX File Structure

- **`%{ ... %}** — C code to include at the top (headers, declarations)
- **`%% ... %%`** — Pattern-action rules (`regex { C code }`)
- **`yywrap()`** — Must return 1 to indicate end of input
- **`main()`** — Calls `yylex()` to start scanning

---

## How to Compile Manually

### Step 1: Generate C source with Flex
```cmd
flex myprogram.l
```
This creates `lex.yy.c` in the current folder.

### Step 2: Compile with GCC
```cmd
gcc lex.yy.c -o myprogram.exe
```

### Step 3: Run the executable
```cmd
myprogram.exe
```

Or pipe input directly:
```cmd
echo hello 123 + | myprogram.exe
```

---

## How to Use `run_lex.bat`

This batch script automates the Flex → GCC → Run workflow.

```cmd
run_lex.bat test.l
```

The script:
1. Runs Flex on the specified `.l` file
2. Compiles `lex.yy.c` into an `.exe` with the same base name
3. Runs the executable
4. Stops with a clear error message if any step fails

---

## How to Use `run_lex.ps1`

PowerShell version with colored output and better error handling.

```powershell
.\run_lex.ps1 test.l
```

Same workflow: Flex → GCC → Run, with coloured status messages.

---

## Common Errors and Solutions

| Error | Likely Cause | Solution |
|-------|-------------|----------|
| `flex : The term 'flex' is not recognized` | Flex not in PATH | Add `C:\Program Files (x86)\GnuWin32\bin` to your User PATH |
| `gcc : The term 'gcc' is not recognized` | GCC not in PATH | Add `C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\bin` to your User PATH |
| `lex.yy.c: No such file or directory` | Flex didn't run / no `.l` file | Check that `flex myfile.l` ran successfully |
| `undefined reference to _yyparse` | Wrong tool used (Yacc/Bison code) | This is a LEX file, not Yacc — ensure `.l` contains LEX syntax |
| `warning: implicit declaration of function 'yylex'` | Missing `%%` section | Ensure your rules are between `%%` markers |
| `test.exe is not recognized` or execution blocked | Windows SmartScreen / App Control | See security note below |
| Permission denied running scripts | PowerShell execution policy | Run: `Set-ExecutionPolicy RemoteScope CurrentUser` |

### Security Note on Execution

If Windows Smart App Control or your organisation's security policy blocks the generated `.exe`:
- **Do not disable security features.**
- Options:
  - Run on a personal (unmanaged) machine
  - Ask your IT administrator to allow the executable
  - Use Windows Subsystem for Linux (WSL) with `sudo apt install flex`