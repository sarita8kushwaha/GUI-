#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk


# In[1]:


root=tk.Tk()
root.title ('Rectangle')
root.geometry ('500x300')
def area():
    s1=int(e1.get())
    s2=int(e2.get())
    print(f'Area of Rectangle is: {s1*s2}')
    e1.delete(0,tk.END)
    e2.delete(0,tk.End)
    e1.focus()
def parameter():
    s1=int(e1.get())
    s2=int(e2.get())
    print(f'Parameter of Rectangle is: {2*(s1+s2)}')
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e1.focus()
l1=tk.Label(root,text='side1=')
l1.grid(row=0, column=0)
l2=tk.Label(root,text='side2=')
l2.grid(row=1,column=0)
e1=tk.Entry(root)
e1.grid(row=0, column=1)
e2=tk.Entry(root)
e2.grid(row=1, colum=1)
b1=tk.Button(root, text='Area',command=area)
b1.grid(row=2, column=1)
b2=tk.Button(root, text='Parameter',command=parameter)
b2.grid(row=2,colum=1)
b3=tk.Button(root, text='close',command=root.destroy)
b3.grid(row=2,column=2)
root.mainloop()


# In[ ]:




