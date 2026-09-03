# scripts/agent/verify.ps1 - Phuchello Agent Workflow v2 Verification Entry Point
param(
    [ValidateSet("Fast", "Full")]
    [string]$Mode = "Fast"
)

$ErrorActionPreference = "Continue"
$repoRoot = (Resolve-Path "$PSScriptRoot\..\..").Path
Set-Location $repoRoot

function Find-Python {
    if ($env:PYTHON_EXECUTABLE -and (Test-Path $env:PYTHON_EXECUTABLE)) {
        return $env:PYTHON_EXECUTABLE
    }
    $paths = @(
        "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"
    )
    foreach ($p in $paths) {
        if (Test-Path $p) { return $p }
    }
    $candidates = @("python", "python3", "py")
    foreach ($c in $candidates) {
        try {
            $ver = & $c --version 2>$null
            if ($LASTEXITCODE -eq 0 -and $ver -match "Python 3") { return $c }
        } catch {}
    }
    return "python"
}

$python = Find-Python
$results = [ordered]@{}
$overallStatus = "PASS"

Write-Host "=================================================="
Write-Host " Phuchello Agent Workflow v2 -- Verification ($Mode)"
Write-Host "=================================================="

# Check 1: STATE.yaml and task-contract.json validation
Write-Host ""
Write-Host "[1/4] Validating .agent state files..."
$stateValidator = Join-Path $repoRoot "scripts\agent\validate_state.py"
if (Test-Path $stateValidator) {
    $out = & $python $stateValidator 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [PASS] .agent/STATE.yaml and .agent/task-contract.json verified" -ForegroundColor Green
        $results["agent_state"] = "PASS"
    } else {
        Write-Host "  [FAIL] State validation reported errors:" -ForegroundColor Red
        Write-Host $out
        $results["agent_state"] = "FAIL"
        $overallStatus = "FAIL"
    }
} else {
    Write-Host "  [FAIL] scripts/agent/validate_state.py not found" -ForegroundColor Red
    $results["agent_state"] = "FAIL"
    $overallStatus = "FAIL"
}

# Check 2: Git diff clean & formatting check
Write-Host ""
Write-Host "[2/4] Running git diff --check..."
$diffCheck = git diff --check 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "  [PASS] No trailing whitespace or merge conflict markers" -ForegroundColor Green
    $results["git_diff"] = "PASS"
} else {
    Write-Host "  [FAIL] git diff --check reported issues:" -ForegroundColor Red
    Write-Host $diffCheck
    $results["git_diff"] = "FAIL"
    $overallStatus = "FAIL"
}

# Check 3: Deterministic core repository validator
Write-Host ""
Write-Host "[3/4] Running core repository validator (scripts/validate.py)..."
$valScript = Join-Path $repoRoot "scripts\validate.py"
if (Test-Path $valScript) {
    $valOut = & $python $valScript 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [PASS] Core repository validation passed" -ForegroundColor Green
        $results["core_validate"] = "PASS"
    } else {
        Write-Host "  [FAIL] Core repository validation failed:" -ForegroundColor Red
        Write-Host $valOut
        $results["core_validate"] = "FAIL"
        $overallStatus = "FAIL"
    }
} else {
    Write-Host "  [SKIP] scripts/validate.py not found" -ForegroundColor Yellow
    $results["core_validate"] = "PARTIAL"
    if ($overallStatus -ne "FAIL") { $overallStatus = "PARTIAL" }
}

# Check 4: Garden D2 validator
Write-Host ""
Write-Host "[4/4] Running Garden D2 validator (scripts/validate_garden_d2.py)..."
$gardenVal = Join-Path $repoRoot "scripts\validate_garden_d2.py"
if (Test-Path $gardenVal) {
    $gOut = & $python $gardenVal 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [PASS] Garden D2 validation passed" -ForegroundColor Green
        $results["garden_d2"] = "PASS"
    } else {
        Write-Host "  [FAIL] Garden D2 validation reported errors:" -ForegroundColor Red
        Write-Host $gOut
        $results["garden_d2"] = "FAIL"
        $overallStatus = "FAIL"
    }
} else {
    Write-Host "  [SKIP] scripts/validate_garden_d2.py not found" -ForegroundColor Yellow
    $results["garden_d2"] = "PARTIAL"
    if ($overallStatus -ne "FAIL") { $overallStatus = "PARTIAL" }
}

# Full mode extra check: Quartz build
if ($Mode -eq "Full") {
    Write-Host ""
    Write-Host "[Extra/Full] Checking Quartz build capability..."
    $quartzDir = Join-Path $repoRoot "garden"
    if (Test-Path $quartzDir) {
        $nodeModules = Join-Path $quartzDir "node_modules"
        if (Test-Path $nodeModules) {
            Write-Host "  [INFO] Quartz dependencies present. Running build test..."
            $qBuild = & npx --prefix "$quartzDir" quartz build 2>&1
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  [PASS] Quartz build succeeded" -ForegroundColor Green
                $results["quartz_build"] = "PASS"
            } else {
                Write-Host "  [FAIL] Quartz build failed:" -ForegroundColor Red
                Write-Host $qBuild
                $results["quartz_build"] = "FAIL"
                $overallStatus = "FAIL"
            }
        } else {
            Write-Host "  [PARTIAL] garden/node_modules not installed; Quartz build skipped" -ForegroundColor Yellow
            $results["quartz_build"] = "PARTIAL"
            if ($overallStatus -ne "FAIL") { $overallStatus = "PARTIAL" }
        }
    }
}

Write-Host ""
Write-Host "=================================================="
Write-Host " VERIFICATION SUMMARY: $overallStatus"
Write-Host "=================================================="
foreach ($key in $results.Keys) {
    Write-Host "  $key : $($results[$key])"
}
Write-Host "=================================================="

if ($overallStatus -eq "FAIL") {
    exit 1
} elseif ($overallStatus -eq "PARTIAL") {
    exit 2
} else {
    exit 0
}
