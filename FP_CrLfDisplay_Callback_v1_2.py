# PythonScript that modifies Cr and Lf characters display, reducing their size (Notepad++ CALLBACK)

# Tested with Notepad++ 7.8.2 64 bits, with PythonScript plugin 1.5.2
# on Windows 8.1 64 bits (NOT tested with Notepad++ 32 Bits but should be compatible)
# /!\ this file uses TABS for indent /!\ (better read as 4 chars wide tabs)

# re-run the script to change the CR and LF graphics widths
# change the *options values* (just below) to choose the widths applied on script startup

# *options values* : set values to an INTEGER >= -1
i_start_width_cr	= 1 # width of the CR graphic (carriage return : \r)
i_start_width_lf	= 0 # width of the LF graphic (line feed : \n)
# end of *options values*

# allowed widths values :
	# width = -1	hides CR/LF							: CR/LF will not appear, even with 'Show Symbol End of Line/All Characters'
	# width = 0		makes CR/LF zero char long			: like a small vertical bar |
	# width = 1		makes CR/LF one char long			: as C/L
	# width = 2		makes CR/LF two chars long			: normal Notepad++ display, as CR/LF
	# width > 2		makes CR/LF this width chars long	: as CR/LF with a larger width

# script declarations ******************************************************************************
from Npp import *

s_script_name	= "CrLf Custom Display"
s_callback_name	= "CrLfDisplay Callback"

s_crlf_widthsset		= "CR / LF widths set to : "
s_crlf_widthsrestdef	= "CR / LF widths restored to default : "
s_rerunchangeswidths	= "Re-run the script to change the widths"

s_editorprop_prefix		= "CRLFDISPLAYCB_"
s_editorprop_cb_reg		= s_editorprop_prefix + "CB_REGISTERED"
s_editorprop_cb_on		= s_editorprop_prefix + "CB_ON"
s_editorprop_width_cr	= s_editorprop_prefix + "WIDTH_CR"
s_editorprop_width_lf	= s_editorprop_prefix + "WIDTH_LF"

i_true	= 1
i_false	= 0
i_norm_width	= 2
i_none_width	= -1

class C_CrLfDisplay_CB():
	# class constructor
	def __init__(self, s_script_name, i_none_width, i_norm_width, i_start_width_cr, i_start_width_lf, \
			i_feature_on, s_editorprop_cb_on, s_editorprop_width_cr, s_editorprop_width_lf):
		self.CBDone = False
		self.script_name	= s_script_name
		self.none_width		= i_none_width
		self.norm_width		= i_norm_width
		self.start_width_cr	= i_start_width_cr
		self.start_width_lf	= i_start_width_lf
		self.feature_on		= i_feature_on
		self.editorprop_cb_on		= s_editorprop_cb_on
		self.editorprop_width_cr	= s_editorprop_width_cr
		self.editorprop_width_lf	= s_editorprop_width_lf

	# function to register the callback
	def RegCallBack(self):
		# our CallBack function
		def CB_MyBufferActivated(args):
			if not(console.editor.getProperty(self.editorprop_cb_on) == str(self.feature_on)):
				return

			s_width_cr = console.editor.getProperty(self.editorprop_width_cr)
			s_width_lf = console.editor.getProperty(self.editorprop_width_lf)
			try:
				i_width_cr = int(s_width_cr)
				i_width_lf = int(s_width_lf)
			except:
				return
			self.SetCrLfDisplay(i_width_cr, i_width_lf)
		# end of callback

		if self.CBDone:
			return False

		notepad.callback(CB_MyBufferActivated, [NOTIFICATION.BUFFERACTIVATED])
		self.CBDone = True

	def SetCrLfDisplay(self, i_width_cr, i_width_lf):
		s_cr = "\r"
		s_lf = "\n"
		if i_width_cr >= 0:
			editor1.setRepresentation	(s_cr, " " * i_width_cr)
			editor2.setRepresentation	(s_cr, " " * i_width_cr)
		else:
			editor1.clearRepresentation	(s_cr)
			editor2.clearRepresentation	(s_cr)
		if i_width_lf >= 0:
			editor1.setRepresentation	(s_lf, " " * i_width_lf)
			editor2.setRepresentation	(s_lf, " " * i_width_lf)
		else:
			editor1.clearRepresentation	(s_lf)
			editor2.clearRepresentation	(s_lf)

	def InputCrLfWidth(self, s_cur_width_cr, s_cur_width_lf):
		while True:
			s_response = notepad.prompt( \
				"Enter CR and LF widths (>= " + str(self.none_width) + ") separated by a space (eg. : 2 1), empty for script default" + "\n" + \
				"Special widths : " + \
				str(self.none_width) + " = always invisible, " + \
				str(0) + " = small bar, " + \
				str(self.norm_width) + " = Notepad++ default", \
				self.script_name + " - Enter widths of CR and LF", s_cur_width_cr + " " + s_cur_width_lf)
			if s_response is None:
				return None
			if s_response == "":
				return (self.start_width_cr, self.start_width_lf)

			lst_width = s_response.strip().split()
			if len(lst_width) == 2:
				try:
					i_width_cr = int(lst_width[0])
					i_width_lf = int(lst_width[1])
				except:
					pass
				else:
					if (i_width_cr >= self.none_width and i_width_lf >= self.none_width):
						return (i_width_cr, i_width_lf)
			notepad.messageBox("Invalid input !", self.script_name, MESSAGEBOXFLAGS.ICONEXCLAMATION)
# end of class

# script code **************************************************************************************
print "[" + s_script_name + " starts]"

if i_start_width_cr < i_none_width: i_start_width_cr = i_norm_width
if i_start_width_lf < i_none_width: i_start_width_lf = i_norm_width

# create an instance of the callback class, and populate object properties with script and Notepad variables
o_crlfdisplay_cb = C_CrLfDisplay_CB(s_script_name, i_none_width, i_norm_width, i_start_width_cr, i_start_width_lf, \
						i_true, s_editorprop_cb_on, s_editorprop_width_cr, s_editorprop_width_lf)

if console.editor.getProperty(s_editorprop_cb_reg) != str(i_true):
	console.editor.setProperty(s_editorprop_cb_reg, str(i_true))
	console.editor.setProperty(s_editorprop_width_cr, str(i_start_width_cr))
	console.editor.setProperty(s_editorprop_width_lf, str(i_start_width_lf))

	# register the callback on NOTIFICATION.BUFFERACTIVATED
	o_crlfdisplay_cb.RegCallBack()

	if (i_start_width_cr == i_norm_width and i_start_width_lf == i_norm_width):
		console.editor.setProperty(s_editorprop_cb_on, str(i_false))
		print "\t" + s_callback_name + " registered and DE-ACTIVATED /!\\, " + \
			s_crlf_widthsrestdef + str(i_start_width_cr) + " / " + str(i_start_width_lf) + " (" + s_rerunchangeswidths + ")"
	else:
		console.editor.setProperty(s_editorprop_cb_on, str(i_true))
		print "\t" + s_callback_name + " registered and activated, " + \
			s_crlf_widthsset + str(i_start_width_cr) + " / " + str(i_start_width_lf) + " (" + s_rerunchangeswidths + ")"

	o_crlfdisplay_cb.SetCrLfDisplay(i_start_width_cr, i_start_width_lf)
	notepad.activateBufferID(notepad.getCurrentBufferID())
else:
	s_width_cr = console.editor.getProperty(s_editorprop_width_cr)
	s_width_lf = console.editor.getProperty(s_editorprop_width_lf)

	t_width = o_crlfdisplay_cb.InputCrLfWidth(s_width_cr, s_width_lf)
	if t_width is None:
		print "\t" + s_callback_name + " no change"
	else:
		i_width_cr = t_width[0]
		i_width_lf = t_width[1]
		console.editor.setProperty(s_editorprop_width_cr, str(i_width_cr))
		console.editor.setProperty(s_editorprop_width_lf, str(i_width_lf))
		if (i_width_cr == i_norm_width and i_width_lf == i_norm_width):
			console.editor.setProperty(s_editorprop_cb_on, str(i_false))
			print "\t" + s_callback_name + " DE-ACTIVATED /!\\, " + \
				s_crlf_widthsrestdef + str(i_width_cr) + " / " + str(i_width_lf) + " (" + s_rerunchangeswidths + ")"
		else:
			console.editor.setProperty(s_editorprop_cb_on, str(i_true))
			print "\t" + s_callback_name + " activated, " + \
				s_crlf_widthsset + str(i_width_cr) + " / " + str(i_width_lf) + " (" + s_rerunchangeswidths + ")"

		o_crlfdisplay_cb.SetCrLfDisplay(i_width_cr, i_width_lf)
		notepad.activateBufferID(notepad.getCurrentBufferID())
