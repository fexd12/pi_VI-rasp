@echo off

pyinstaller --noconfirm --log-level=WARN ^
--windowed ^
--hidden-import="tkinter" ^
--name=Application ^
cadastro_tag\Application.py
