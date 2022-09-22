echo off
if exist c:\Windows\py.exe (
    c:\Windows\py.exe -3.5 .\main.py
) else (
    py -3.5 .\main.py
)