<#
.SYNOPSIS
    Compile and run a LEX/Flex program.
.DESCRIPTION
    Takes a .l filename, runs Flex to generate lex.yy.c,
    compiles with GCC, and executes the resulting program.
.PARAMETER LexFile
    The path to the .l LEX source file.
.EXAMPLE
    .\run_lex.ps1 test.l
#>

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$LexFile
)

# Resolve full path
$lexPath = Resolve-Path $LexFile -ErrorAction SilentlyContinue
if (-not $lexPath) {
    Write-Host "Error: File '$LexFile' not found." -ForegroundColor Red
    exit 1
}

$baseName = [System.IO.Path]::GetFileNameWithoutExtension($lexPath)
$lexDir = [System.IO.Path]::GetDirectoryName($lexPath)

# Store current directory and switch to LEX file's folder
$originalDir = Get-Location
Set-Location $lexDir

try {
    Write-Host "[1/3] Running Flex on $LexFile ..." -ForegroundColor Cyan
    $flexResult = & flex $LexFile 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Flex failed with exit code $LASTEXITCODE." -ForegroundColor Red
        $flexResult | ForEach-Object { Write-Host $_ -ForegroundColor Red }
        exit $LASTEXITCODE
    }
    Write-Host "      lex.yy.c generated successfully." -ForegroundColor Green

    Write-Host "[2/3] Compiling lex.yy.c with GCC ..." -ForegroundColor Cyan
    $gccResult = & gcc lex.yy.c -o "$baseName.exe" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Compilation failed with exit code $LASTEXITCODE." -ForegroundColor Red
        $gccResult | ForEach-Object { Write-Host $_ -ForegroundColor Red }
        exit $LASTEXITCODE
    }
    Write-Host "      $baseName.exe created successfully." -ForegroundColor Green

    Write-Host "[3/3] Running $baseName.exe ..." -ForegroundColor Cyan
    Write-Host ""
    & ".\$baseName.exe"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Execution failed with exit code $LASTEXITCODE." -ForegroundColor Red
        exit $LASTEXITCODE
    }

    Write-Host ""
    Write-Host "Done." -ForegroundColor Green
}
finally {
    Set-Location $originalDir
}