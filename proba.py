import tkinter as tk
Name="fds"
window = tk.Tk(className = Name)
def change_className():
  global Name
  Name = "dsfsd"
  window.title(Name)

#bool=True
button=tk.Button(window,command=change_className)
button.pack()
window.mainloop()
