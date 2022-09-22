echo off
if exist c:\Windows\py.exe (
    c:\Windows\py.exe .\main.py
) else (
    python .\main.py
)