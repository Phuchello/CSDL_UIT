# PowerShell validation script for IT004 Database Handbook repository

$ErrorActionPreference = "Stop"
$root = (Resolve-Path "$PSScriptRoot\..").Path

function Find-Python {
    if ($env:PYTHON_EXECUTABLE -and (Test-Path $env:PYTHON_EXECUTABLE)) {
        return $env:PYTHON_EXECUTABLE
    }
    
    $candidates = @("python", "python3", "py")
    foreach ($c in $candidates) {
        try {
            $ver = & $c --version 2>$null
            if ($LASTEXITCODE -eq 0 -and $ver -match "Python 3") {
                return $c
            }
        } catch {}
    }

    # Search common Windows Python paths
    $paths = @(
        "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
        "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    )
    foreach ($p in $paths) {
        if (Test-Path $p) {
            return $p
        }
    }
    return "python"
}

$python = Find-Python
Write-Host "Running repository validation suite via $python..."
& $python "$root\scripts\validate.py"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Validation failed with exit code $LASTEXITCODE"
}
