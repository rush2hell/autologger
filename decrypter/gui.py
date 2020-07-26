import tkinter as tk
from tkinter import filedialog
import pyAesCrypt

bufferSize = 64 * 1024
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

#heading 
label1 = tk.Label(root, text='File Decrypter Tool')
label1.config(font=('helvetica', 16))
canvas1.create_window(200, 25, window=label1)

#choose image label
label2 = tk.Label(root, text='Choose Image path :')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label2)

#for image upload input
entry1 = tk.Entry(root) 
canvas1.create_window(200, 75, window=entry1)


#choose log label
label3 = tk.Label(root, text='Choose Log path :')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label3)

#for log upload input
entry2 = tk.Entry(root) 
canvas1.create_window(200, 125, window=entry2)

#password label
label4 = tk.Label(root, text='Enter password :')
label4.config(font=('helvetica', 10))
canvas1.create_window(200, 150, window=label4)

#password input
entry3 = tk.Entry(root) 
canvas1.create_window(200, 175, window=entry3)

def getFiles():
	#decryption process
	path_image = entry1.get()
	path_log = entry2.get() 
	file_pass = entry3.get()
	pyAesCrypt.decryptFile(path_image, "data_image.jpg", file_pass, bufferSize)
	pyAesCrypt.decryptFile(path_log, "data_log.txt", file_pass, bufferSize)
	label5 = tk.Label(root, text= 'Files Decrypted ' ,font=('helvetica', 12))
	canvas1.create_window(200, 240, window=label5)

def getImage():
	root.filename = filedialog.askopenfilename(initialdir="c:/", title="Select Image File", filetypes=(("Encrypted image files", "*.enc_img"),("all files", "*.*")))
	entry1.insert(0,root.filename)

def getLog():
	root.filename = filedialog.askopenfilename(initialdir="c:/", title="Select Image File", filetypes=(("Encrypted log files", "*.enc_log"),("all files", "*.*")))
	entry2.insert(0,root.filename)

#button for image path
button1 = tk.Button(text='Choose Image', command=getImage, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas1.create_window(320, 75, window=button1)

#button for log path
button2 = tk.Button(text='Choose Log File', command=getLog, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas1.create_window(320, 125, window=button2)

#decrypt button
button3 = tk.Button(text='Decrypt File', command=getFiles, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 210, window=button3)

root.mainloop()
