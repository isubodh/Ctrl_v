import tkinter as tk
from tkinter import ttk
import win32clipboard as cb

'''
'''
class CtrlV:
	def __init__(self, win):
		self.win = win
		win.title("Ctrl+V")
		## User should not rezie the app
		win.resizable(False, False)
		## Don't want to see any control buttons
		win.overrideredirect(True)
		
		## Loc need to be set manually as we disabled control
		width = int(win.winfo_screenwidth()/10)
		height = int(win.winfo_screenheight()/25)
		xcorr = int(win.winfo_screenwidth() *0.9 )
		ycorr = int(win.winfo_screenheight() * 0.9 )
		win.geometry("{0}x{1}+{2}+{3}".format(width, height, xcorr, ycorr))
		
		self.frmCtrlv = tk.Frame(win)
		self.frmCtrlv.grid(column=0, row=0)
		self.frmBtn = tk.Frame(win)
		self.frmBtn.grid(column=1, row=1)
		''' Button '''
		self.btnCtrlV = ttk.Button(self.frmBtn, text="Paste",command=self.paste)
		self.btnCtrlV.grid(column=0, row=0)
		self.btnCtrlV.bind('<Double-3>', quit) 
		self.btnRestore = ttk.Button(self.frmBtn, text="X",command=self.restore)
		self.btnRestore.grid(column=1, row=0)
		
		self.data = ''
		self.myKeyWord = 'Subodh+77\n'

	'''
	Function to work with clipboard
	'''
	def paste(self):
		#with 
		cb.OpenClipboard()
		current = cb.GetClipboardData(cb.CF_TEXT)
		if current != self.myKeyWord :
			self.data = current
		cb.EmptyClipboard()
		cb.SetClipboardText(self.myKeyWord)
		cb.CloseClipboard()
	
	'''
	To restore the last value
	'''
	def restore(self):
		cb.OpenClipboard()
		current = cb.GetClipboardData()
		if current == self.myKeyWord :
			cb.EmptyClipboard()
			cb.SetClipboardText(self.data)
		cb.CloseClipboard()			
			
			
			
	'''
	Exit app
	'''
	def quit(self):
		print("Exiting...")
		exit()

'''
## Main 
'''
win = tk.Tk()
CtrlV(win)
win.call('wm', 'attributes', '.', '-topmost', True)
win.mainloop()

