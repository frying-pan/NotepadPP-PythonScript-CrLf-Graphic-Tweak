# CrLf_Display

Change the graphic of CR and LF for Notepad++ when the script is run from Notepad++ (with PythonScript plugin installed)

via a callback on notepad object (NOTIFICATION.BUFFERACTIVATED) : the graphics can be made smaller, with various sizes

Tested with Notepad++ 7.8.2 64 bits, on Windows 8.1 64 bits (NOT tested with Notepad++ 32 Bits but should be compatible)

using PythonScript plugin 1.5.2 from https://github.com/bruderstein/PythonScript/releases/ (based on python 2.7).

Features :
  * set up the options inside the script : i_start_width_cr, i_start_width_lf
  * or re-run the script to make CR and LF appear as just C, F, or a small vertical bar | graphic

# Install :

This script can be run at Notepad++ startup (folders below are those of a local installation) : 

* copy the FP_CrLfDisplay_Callback .py script file in :

C:\Users\[username]\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts

* add "import [FP_CrLfDisplay_Callback (py) script file name without extension]"

to the startup.py file located, for me, under the Notepad++ install folder :

C:\Program Files\Notepad++\plugins\PythonScript\scripts

(I think I had to take ownership of startup.py before being able to write into it)

# Versions :

FP_CrLfDisplay_Callback_v1_0.py

FP_CrLfDisplay_Callback_v1_1.py
changes :
  * handling both Notepad++ views
  * more flexible configuration

FP_CrLfDisplay_Callback_v1_2.py
changes :
  * minor update

FP_CrLfDisplay_Callback_v1_3.py
changes :
  * script name changed from Perso_CrLfDisplay_Callback to FP_CrLfDisplay_Callback for easier identification
  * minor update

