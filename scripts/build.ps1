# PowerShell script to compile individual chapter HTML files into book/index.html

$ErrorActionPreference = "Stop"
$root = (Resolve-Path "$PSScriptRoot\..").Path
$chapterDir = "$root\book\chapters"
$output = "$root\book\index.html"

$chapters = @(
    "ch00_intro.html",
    "ch01_overview.html",
    "ch02_er_relational.html",
    "ch03_relational_algebra.html",
    "ch04_sql.html",
    "ch05_constraints.html",
    "ch06_fd_normalization.html",
    "ch07_practical.html",
    "exam_playbook.html",
    "cheat_sheet.html",
    "references.html"
)

$head = @"
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IT004 – Cơ sở dữ liệu: Cẩm nang từ nền tảng đến Exam Mastery</title>
  <meta name="author" content="Võ Trọng Phúc">
  <meta name="description" content="IT004 – Cơ sở dữ liệu – Cẩm nang từ nền tảng đến Exam Mastery – UIT">
  <meta name="keywords" content="IT004, Cơ sở dữ liệu, Database, UIT, SQL Server, Đại số quan hệ, Võ Trọng Phúc">
  <link rel="stylesheet" href="css/book.css">
</head>
<body>
"@

$builder = [System.Text.StringBuilder]::new()
[void]$builder.AppendLine($head)

foreach ($name in $chapters) {
    $chapterPath = "$chapterDir\$name"
    if (-not (Test-Path $chapterPath)) {
        Write-Error "Missing chapter file: $chapterPath"
    }
    
    $content = [System.IO.File]::ReadAllText($chapterPath, [System.Text.Encoding]::UTF8).Trim()
    
    if ($content -match "(?s)<body[^>]*>(.*?)</body>") {
        $content = $matches[1].Trim()
    }
    
    # Ensure details tags have open attribute
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, "<details(?![^>]*\bopen\b)", "<details open")
    
    if ($name -eq "ch05_constraints.html") {
        $content = "<section id=`"ch05`">`n$content`n</section>"
    }
    
    [void]$builder.AppendLine("`n<!-- === $name === -->`n")
    [void]$builder.AppendLine($content)
}

[void]$builder.AppendLine("</body>`n</html>`n")

[System.IO.File]::WriteAllText($output, $builder.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "Successfully compiled $($chapters.Count) chapters into $output"
