@echo off

set SRC=main.py
set EXTRACTPATH=.\dist
mkdir %EXTRACTPATH%

pyinstaller.exe -F --specpath %EXTRACTPATH% --distpath %EXTRACTPATH% --workpath %EXTRACTPATH% %SRC%