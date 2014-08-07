import Tkinter as tk
from Tkinter import *
# m1 = tk.PanedWindow()
# m1.pack(fill=BOTH, expand=3)

button_list=[];
root = Tk(  )
no_rows=3;
no_cols=4;
for r in range(no_rows):
    for c in range(no_cols):
        button_list.append(Button(root, text ="Hello").grid(row=r,column=c));
print button_list[0]
# can_list=[];
# for can_no in range(len(button_list)):
	# c=Canvas(button_list[can_no],bg="blue",height=);
	# can_list.append(c);
		
		
root.mainloop(  )

# left = Label(m1, text="left pane")
# m1.add(left)

# m2 = PanedWindow(m1, orient=VERTICAL)
# m1.add(m2)

# top = Label(m2, text="top pane")
# m2.add(top)

# bottom = Label(m2, text="bottom pane")
# m2.add(bottom)
# tk.mainloop()
