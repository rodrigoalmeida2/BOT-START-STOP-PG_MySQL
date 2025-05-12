# Service Tray Manager

A lightweight Python application that sits in the Windows system tray and allows you to easily start and stop PostgreSQL and MySQL services with a single click.

## USE

- Clone the project
- Install the dependencies
- look at the name of your postgres and mysql in services.msc, make the changes if necessary

## RUN

```
pyinstaller --onefile --windowed --icon=Rato.ico main.py
```
- Go to dist page after running the pyinstaller and look for main.exe
- Run as administrator and look at the hidden icons in the system tray on Windows
- Give a right click on them and the options appears there and you good to go
