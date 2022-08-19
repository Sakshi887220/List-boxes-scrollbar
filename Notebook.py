from tkinter import *

root = Tk()
# Create frame and scrollbar
my_frame = Frame(root)


# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED


#configure scrollbar

my_frame.pack()

#Add item to listbox


# Add list of items





def select():
	my_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
	my_listbox.delete(0, END)

def select_all():
	result = ''

	for item in my_listbox.curselection():
		result = result + str(my_listbox.get(item)) + '\n'

	my_label.config(text=result)

def delete_multiple():
	for item in reversed(my_listbox.curselection()):
		my_listbox.delete(item)
		my_label.config(text='')

my_button = Button(root, text="Delete", command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text="Select", command=select)
my_button2.pack(pady=10)

global my_label
my_label = Label(root, text='')
my_label.pack(pady=5)

my_button3 = Button(root, text="Delete All", command=delete_all)
my_button3.pack(pady=10)

my_button4 = Button(root, text="Select All", command=select_all)
my_button4.pack(pady=10)

my_button5 = Button(root, text="Delete Multiple", command=delete_multiple)
my_button5.pack(pady=10)

root.mainloop()
