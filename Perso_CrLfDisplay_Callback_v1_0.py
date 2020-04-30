# PythonScript that modifies Cr and Lf characters display, reducing their size (Notepad++ CALLBACK)
# Tested with Notepad++ 7.8.2 64 bits, with PythonScript plugin 1.5.2
# on Windows 8.1 64 bits (NOT tested with Notepad++ 32 Bits but should be compatible)
# /!\ this file uses TABS for indent /!\ (better read as 4 chars wide tabs)

# re-run the script to cycle through modes or de-activate the callback

# general declarations *****************************************************************************
from Npp import *

# script declarations ******************************************************************************
s_script_name	= "CrLf Custom Display"
s_callback_name	= "CrLfDisplay Callback"

s_crlfmode			= "Cr and Lf mode"
s_reruncyclemodes	= "Re-run script to cycle the modes. *Normal* mode disable the CallBack"

s_editorprop_cb_reg		= "CRLFDISPLAYCALLBACK_REGISTERED"
s_editorprop_cb_mode	= "CRLFDISPLAYCALLBACK_MODE"
i_true					= 1
i_start_mode			= 3 # choose a start mode between 0 and i_normal_mode
i_normal_mode			= 8

class C_CrLfDisplay_CB():
	# class constructor
	def __init__(self, i_base_mode, s_editorprop_cb_mode):
		self.CBDone = False
		self.base_mode			= i_base_mode
		self.editorprop_cb_mode	= s_editorprop_cb_mode

	# function to register the callback
	def RegCallBack(self):
		# our CallBack function
		def CB_MyBufferActivated(args):
			s_mode = console.editor.getProperty(self.editorprop_cb_mode)
			try:
				i_mode = int(s_mode)
			except:
				return
			if i_mode == self.base_mode: # if callback de-activated : abort
				return

			self.SetCrLfDisplay(i_mode)

		if self.CBDone:
			return False

		notepad.callback(CB_MyBufferActivated, [NOTIFICATION.BUFFERACTIVATED])
		self.CBDone = True

	def SetCrLfDisplay(self, i_mode):
		if i_mode == self.base_mode:
			editor.setRepresentation("\r", "  ")	# "  " makes CR two chars long : normal as a CR
			editor.setRepresentation("\n", "  ")	# "  " makes LF two chars long : normal as a LF
		elif i_mode == self.base_mode - 1:
			editor.setRepresentation("\r", "  ")
			editor.setRepresentation("\n", " ")
		elif i_mode == self.base_mode - 2:
			editor.setRepresentation("\r", " ")
			editor.setRepresentation("\n", "  ")
		elif i_mode == self.base_mode - 3:
			editor.setRepresentation("\r", "  ")
			editor.setRepresentation("\n", "")
		elif i_mode == self.base_mode - 4:
			editor.setRepresentation("\r", "")
			editor.setRepresentation("\n", "  ")

		elif i_mode == self.base_mode - 5:
			editor.setRepresentation("\r", " ")		# " " makes CR one char long : as a C
			editor.setRepresentation("\n", " ")		# " " makes LF one char long : as a L
		elif i_mode == self.base_mode - 6:
			editor.setRepresentation("\r", " ")
			editor.setRepresentation("\n", "")
		elif i_mode == self.base_mode - 7:
			editor.setRepresentation("\r", "")
			editor.setRepresentation("\n", " ")

		elif i_mode == self.base_mode - 8:
			editor.setRepresentation("\r", "")		# "" makes CR zero char long : appears like a small vertical bar
			editor.setRepresentation("\n", "")		# "" makes LF zero char long : appears like a small vertical bar
# end of class

print "[" + s_script_name + " starts]"

# create an instance of the callback class, and populate object properties with variables which are also needed globally
o_crlfdisplay_cb = C_CrLfDisplay_CB(i_normal_mode, s_editorprop_cb_mode)

if console.editor.getProperty(s_editorprop_cb_reg) != str(i_true):
	console.editor.setProperty(s_editorprop_cb_reg, str(i_true))
	console.editor.setProperty(s_editorprop_cb_mode, str(i_start_mode))

	# register the callback on NOTIFICATION.BUFFERACTIVATED
	o_crlfdisplay_cb.RegCallBack()
	o_crlfdisplay_cb.SetCrLfDisplay(i_start_mode)
	notepad.activateBufferID(notepad.getCurrentBufferID())

	print "\t" + s_callback_name + " registered and ACTIVATED, " + \
		s_crlfmode + " = " + str(i_start_mode) + " (" + s_reruncyclemodes + ")"
else:
	s_mode = console.editor.getProperty(s_editorprop_cb_mode)
	try:
		i_mode = int(s_mode)
	except:
		i_mode = i_normal_mode
	if i_mode > 0:
		i_mode = i_mode - 1
	else:
		i_mode = i_normal_mode
	console.editor.setProperty(s_editorprop_cb_mode, str(i_mode))

	o_crlfdisplay_cb.SetCrLfDisplay(i_mode)
	notepad.activateBufferID(notepad.getCurrentBufferID())

	if i_mode == i_normal_mode:
		print "\t" + s_callback_name + " de-activated, " + \
			s_crlfmode + " = " + str(i_mode) + " [normal] (" + s_reruncyclemodes + ")"
	else:
		print "\t" + s_callback_name + " ACTIVATED, " + \
			s_crlfmode + " = " + str(i_mode) + " (" + s_reruncyclemodes + ")"
