# Escape-AWS-Workspace
Basic Tkinter program that adds an always-on-top button to get out of AWS (back to the host) quickly.

## Introduction
AWS (Amazon WorkSpaces) is a software that allows users to connect to an Amazon-hosted Windows VM installation.

In full screen mode (View > Enter Full Screen), it's very difficult to switch back to the parent/host OS without exiting AWS.

This program adds an "Exit" button that shows in AWS that allows you to jump back to the host OS.

## Instructions
All instructions are completed in the host OS.
* Clone this repo.
* Use `python -m pip install -r requirements.txt` to install requirements.
* Run `EscapeAWS.py` to ensure it runs without errors.
* Press Windows+R to go to the Run dialog.
* Type "shell:startup" and press enter. This takes you to the startup programs for your computer.
* Make a new shortcut to the Python files, like: `C:\Users\<name>\AppData\Local\Microsoft\WindowsApps\pythonw3.exe C:\Users\<name>\<path>\Escape-AWS-Workspace\EscapeAWS.py`

## Alternative Methods
Instead of using this mediocre piece of software to exit AWS, you can instead:
* Move your cursor the very top of the screen, click Support > "About my workspace", click the new window, and press the Windows key on your keyboard.
* Set Task Manager (in the host OS) to be "Always on top" (in the Options menu), size it small, and keep in in a corner of your screen. To exit AWS, click on Task Manager, and press the Windows key on your keyboard.

## Limitations/Known Bugs
* Only works on 1920x1080 screens (hard coded). In the future, update this.
* Only tested on Windows. Likely doesn't work on other host operating systems.

Feel free to submit pull requests to make this tool better!
