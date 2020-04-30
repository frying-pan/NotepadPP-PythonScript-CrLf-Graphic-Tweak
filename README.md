# NotepadPP-PythonScript-CrLf-Graphic-Tweak

Change the graphic of CR and LF for Notepad++ when the script is run from Notepad++ (with PythonScript plugin installed)

via a callback on notepad object (NOTIFICATION.BUFFERACTIVATED) : the graphics can be made smaller, with various sizes

Tested with Notepad++ 7.8.2 64 bits, with PythonScript plugin 1.5.2,

on Windows 8.1 64 bits (NOT tested with Notepad++ 32 Bits but should be compatible)


# Install :

This script can be run at Notepad++ startup (folders below are those of a local installation) : 

* copy the Perso_CrLfDisplay_Callback .py script file in :

C:\Users\[username]\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts

* add "import [Perso_ScintWndProc_Hook py script file name without extension]"

to the startup.py file located, for me, under the Notepad++ install folder :

C:\Program Files\Notepad++\plugins\PythonScript\scripts

(I think I had to take ownership of startup.py before being able to write into it)


# Versions :

Perso_CrLfDisplay_Callback_v1_0.py
