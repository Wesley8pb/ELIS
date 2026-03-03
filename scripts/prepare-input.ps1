param(
    [Parameter(Mandatory = $true)]
    [string]$InputFile,

    [string]$OutputFile
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-DefaultOutputFile {
    param([string]$ResolvedInputPath)
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($ResolvedInputPath)
    $directory = [System.IO.Path]::GetDirectoryName($ResolvedInputPath)
    return [System.IO.Path]::Combine($directory, "$baseName - PROCESSADO.md")
}

function Write-MetadataHeader {
    param(
        [string]$OutPath,
        [string]$Backend,
        [string]$SourcePath,
        [string]$Body
    )

    $sourceName = [System.IO.Path]::GetFileName($SourcePath)
    $header = @(
        "> [EXTRACTION] backend=$Backend",
        "> [SOURCE] $sourceName",
        ""
    ) -join "`r`n"

    $content = "$header$Body"
    Set-Content -Path $OutPath -Value $content -Encoding UTF8
}



$inputLiteral = [System.IO.Path]::GetFullPath($InputFile)
if (-not (Test-Path -LiteralPath $inputLiteral)) {
    throw "Arquivo de entrada nao encontrado: $InputFile"
}
$resolvedInput = (Resolve-Path -LiteralPath $inputLiteral).Path

$extension = [System.IO.Path]::GetExtension($resolvedInput).ToLowerInvariant()
$resolvedOutput = if ($OutputFile) { $OutputFile } else { Get-DefaultOutputFile -ResolvedInputPath $resolvedInput }
$resolvedOutput = [System.IO.Path]::GetFullPath($resolvedOutput)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$docxScript = Join-Path $scriptDir "extract_docx_to_md.py"

# --- Deteccao automatica do interpretador Python ---
# Tenta 'py' (Python Launcher para Windows) primeiro.
# Se nao estiver no PATH, usa o caminho absoluto da instalacao local.
$PYTHON_EXE = $null

if (Get-Command "py" -ErrorAction SilentlyContinue) {
    $PYTHON_EXE = "py"
} elseif (Test-Path "C:\Users\034105571236\AppData\Local\Programs\Python\Python313\python.exe") {
    $PYTHON_EXE = "C:\Users\034105571236\AppData\Local\Programs\Python\Python313\python.exe"
} elseif (Get-Command "python" -ErrorAction SilentlyContinue) {
    $PYTHON_EXE = "python"
} else {
    throw "Python nao encontrado. Certifique-se de que Python esta instalado e disponivel no PATH, ou verifique o caminho em: C:\Users\034105571236\AppData\Local\Programs\Python\Python313\python.exe"
}

switch ($extension) {
    ".docx" {
        & $PYTHON_EXE $docxScript --input $resolvedInput --output $resolvedOutput
        if ($LASTEXITCODE -ne 0) {
            throw "Falha ao converter DOCX para Markdown."
        }
        break
    }
    ".md" {
        $body = Get-Content -LiteralPath $resolvedInput -Raw -Encoding UTF8
        Write-MetadataHeader -OutPath $resolvedOutput -Backend "passthrough-md" -SourcePath $resolvedInput -Body $body
        break
    }
    ".txt" {
        $body = Get-Content -LiteralPath $resolvedInput -Raw
        Write-MetadataHeader -OutPath $resolvedOutput -Backend "passthrough-txt" -SourcePath $resolvedInput -Body $body
        break
    }
    ".pdf" {
        & $PYTHON_EXE scripts/extract_pdf_to_md.py --input $resolvedInput --output $resolvedOutput
        if ($LASTEXITCODE -ne 0) {
            throw "Falha ao extrair PDF com pypdf. Verifique se a biblioteca 'pypdf' esta instalada (pip install pypdf)."
        }
        break
    }
    default {
        throw "Extensao nao suportada: $extension. Use .md, .txt, .docx ou .pdf."
    }
}

Write-Output $resolvedOutput
