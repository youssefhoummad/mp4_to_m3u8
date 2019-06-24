#!/usr/bin/env python3
#
# Copyright 2019 youssef hoummad (youssef.hoummad@outlook.com)
#

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter import messagebox

from main import *


class Program:
    def __init__(self):

        # paths
        self.dst = None
        self.src = None

        # GUI stafs
        self.gui_init()

   
    def gui_init(self):
        root = tk.Tk()
        root.configure(background='white')
        root.title('mp4 to hls')
        root.geometry('420x400')

        mainFrame = tk.Frame(root, bg='white')

        tk.Label(root, text="MP4 to HLS", bg='white', fg='#9581BD', font=('Consolas',20)).grid(row=0, column=0, padx=10, pady=10)

        self.entry1 = ttk.Entry(mainFrame, width=50)
        self.entry2 = ttk.Entry(mainFrame, width=50)

        self.src_button = ttk.Button(mainFrame, text="Chose file", command=self.get_src)
        self.dst_button = ttk.Button(mainFrame, text="Select folder", command=self.get_dst)
        self.submitButton = ttk.Button(mainFrame, text="convert", command=self.convert)
        self.result = tk.Label(mainFrame, text="", bg='white', fg='#2E982E', font=('Consolas',20))

        # bootstrap :)
        self.entry1.grid(row=0,column=0, padx=5, pady=5, sticky='we', columnspan=3)
        self.entry2.grid(row=1,column=0, padx=5, pady=5, sticky='we', columnspan=3)
        self.src_button.grid(row=0, column=3, padx=5, pady=5)
        self.dst_button.grid(row=1, column=3, padx=5, pady=5)
        self.submitButton.grid(row=2, column=0, padx=5, pady=20, columnspan=4)
        self.result.grid(row=3, column=0, padx=5, pady=20, columnspan=4)
        mainFrame.grid(row=1, column=0, padx=10, pady=10)

        root.mainloop()


    def get_src(self):
        self.re_init()

        self.src = askopenfilename(initialdir = "/",title = "Select file", filetypes = (("video files","*.mp4"),("all files","*.*")))
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, self.src)


    def get_dst(self):
        self.re_init()

        self.dst = askdirectory(initialdir="%desktop%", title='Select folder to save hls')
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, self.dst)


    def re_init(self):
        "refresh interface"
        self.submitButton.config(state=tk.NORMAL)
        self.result.config(text="")
        self.submitButton.grid(row=2, column=0, padx=5, pady=20, columnspan=4)


    def convert(self):
        if self.src is None or self.dst is None:
            return messagebox.showerror("error", "Need to chose file and folder")

        self.result.config(text="just wait...")
        self.submitButton.config(state=tk.DISABLED)


        for q in ('SD', 'HD', 'FHD'):
            result = mp4_to_m3u8(self.src, self.dst, resolution=q)
        if result==0:
            self.result.config(text="DONE.", fg='#2E982E')
            return # sys.exit(0)
        else:
            self.result.config(text="field...", fg='#f4425c')
            return # os.system('exit')



if __name__ == '__main__':
    Program()
