import tkinter as tk
from tkinter import ttk
import win32clipboard

class CtrlV:
	def __init__(self, win):
		self.win = win
		win.title("Ctrl+V")
		
		self.frmCtrlv = tk.Frame(win)
		self.frmCtrlv.grid(column=0, row=0)
		self.frmBtn = tk.Frame(win)
		self.frmBtn.grid(column=1, row=1)
		''' Button '''
		self.btnCtrlV = ttk.Button(self.frmBtn, text="Paste",command=self.paste)
		self.btnCtrlV.grid(column=0, row=0)
		self.btnExit = ttk.Button(self.frmBtn, text="X",command=self.exit)
		self.btnExit.grid(column=1, row=0)
		''' '''

	'''
	Function to work with clipboard
	'''
	def paste(self):
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardText('Subodh+77\n')
		win32clipboard.CloseClipboard()
	
	'''
	Exit app
	'''
	def exit(self):
		exit()

'''
## Main 
'''
win = tk.Tk()
CtrlV(win)
win.call('wm', 'attributes', '.', '-topmost', True)
win.mainloop()

