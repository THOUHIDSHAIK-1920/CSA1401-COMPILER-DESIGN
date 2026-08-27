@echo off
setlocal enabledelayedexpansion

REM run_lex.bat - Compile and run a LEX/Flex program
REM Usage: run_lex.bat <filename.l>

if "%~1"=="" (
    echo Error: No LEX file specified.
    echo Usage: run_lex.bat ^<filename.l^>
    exit /b 1
)

set LEXFILE=%~1
set BASENAME=%~n1

if not exist "%LEXFILE%" (
    echo Error: File "%LEXFILE%" not found.
    exit /b 1
)

echo [1/3] Running Flex on %LEXFILE%...
flex "%LEXFILE%"
if %ERRORLEVEL% neq 0 (
    echo Error: Flex failed with exit code %ERRORLEVEL%.
    exit /b %ERRORLEVEL%
)
echo       lex.yy.c generated successfully.

echo [2/3] Compiling lex.yy.c with GCC...
gcc lex.yy.c -o "%BASENAME%.exe"
if %ERRORLEVEL% neq 0 (
    echo Error: Compilation failed with exit code %ERRORLEVEL%.
    exit /b %ERRORLEVEL%
)
echo       %BASENAME%.exe created successfully.

echo [3/3] Running %BASENAME%.exe...
echo.
"%BASENAME%.exe"
if %ERRORLEVEL% neq 0 (
    echo Error: Execution failed with exit code %ERRORLEVEL%.
    exit /b %ERRORLEVEL%
)

echo.
echo Done.
endlocal