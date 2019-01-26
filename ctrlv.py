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
		
		## Button for Ctrl+V
		self.btnCtrlV = ttk.Button(self.frmBtn, text="Paste",command=self.paste)
		self.btnCtrlV.grid(column=0, row=0)
		
		##Button for restoring back value
		self.btnRestore = ttk.Button(self.frmBtn, text="X",command=self.restore)
		self.btnRestore.grid(column=1, row=0)
		
		#Popup menu
		self.rclick = RightClick(self.win)
		self.btnCtrlV.bind('<Button-3>', self.rclick.popup)
		
		
		data = ''
		self.myKeyWord = 'Subodh+77\n'

	## Add the keyword ready to paste
	def paste(self):
		global myKeyWord
		cb.OpenClipboard()
		current = cb.GetClipboardData(cb.CF_TEXT)
		if current != self.myKeyWord :
			self.data = current
		cb.EmptyClipboard()
		cb.SetClipboardText(self.myKeyWord)
		cb.CloseClipboard()
	
	## We are restoring back to what it was
	def restore(self):
		global myKeyWord		
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

class RightClick:
    def __init__(self, win):

        # create a popup menu
        self.aMenu = tk.Menu(win, tearoff=0)
        self.aMenu.add_command(label='Exit', command=self.quit)
        self.aMenu.add_command(label='About', command=self.about)

        self.tree_item = ''

    def quit(self):
        exit()

    def about(self):
        print ('This is for ease of typing!')

    def popup(self, event):
        self.aMenu.post(event.x_root, event.y_root)
        self.btnCtrlV = app.btnCtrlV.focus()
'''
## Main 
'''
win = tk.Tk()
app=CtrlV(win)
win.call('wm', 'attributes', '.', '-topmost', True)
win.mainloop()

