import tkinter as tk
from tkinter import ttk,messagebox,PhotoImage
import googletrans as gtr
from translate import Translator
from PyMultiDictionary import MultiDictionary
import pyttsx3

win=tk.Tk()
win.title("my project")
win.geometry("1080x500")
win.resizable(0,0)
win.configure(background="Lavender")


def open_dictionary_window():
    def dict1():
        dictionary=MultiDictionary()
        meaning.config(text=dictionary.meaning('en', word.get())[1])
        synonym.config(text=dictionary.synonym('en', word.get()))
        antonym.config(text=dictionary.antonym('en', word.get()))

    def speaknow():
        engine = pyttsx3.init()
        engine.say(meaning.cget("text")+"  "+synonym.cget("text")+"  "+antonym.cget("text"))
        engine.runAndWait()
    
    root=tk.Toplevel(win)
    root.title("Dictionary")
    root.geometry("1250x750")
    root.configure(bg="lavender")

    tk.Label(root, text="Search Here", font=("Arial 36 bold"), fg="darkslateblue").pack(pady=10)

    frame =tk.Frame(root)
    tk.Label(frame, text="Type Word:", font=("Arial 28 bold")).pack(side=tk.LEFT)
    word = tk.Entry(frame, font=("Arial 23 bold"))
    word.pack()
    frame.pack(pady=10)

    frame1 =tk.Frame(root)
    tk.Label(frame1, text="Meaning: ", font=("Arial 18 bold")).pack(side=tk.LEFT)
    meaning =tk.Label(frame1, text="", font=("Arial 18"), wraplength=1000)
    meaning.pack()
    frame1.pack(pady=15)

    frame2 =tk.Frame(root)
    tk.Label(frame2, text="Synonym: ", font=("Arial 18 bold")).pack(side=tk.LEFT)
    synonym =tk.Label(frame2, text="", font=("Arial 18"), wraplength=1000)
    synonym.pack()
    frame2.pack(pady=15)

    frame3 =tk.Frame(root)
    tk.Label(frame3, text="Antonym: ", font=("Arial 18 bold")).pack(side=tk.LEFT)
    antonym=tk.Label(frame3, text="", font=("Arial 18"), wraplength=1000)
    antonym.pack(side=tk.LEFT)
    frame3.pack(pady=20)

    tk.Button(root, text="Submit", font=("Arial 18 bold"), command=dict1).pack()
    tk.Button(root, text="Speak", font=("Arial 18 bold"), command=speaknow).pack()
    root.mainloop()

def label_change():
    c1=combo1.get()
    c2=combo2.get()
    lbl1.configure(text=c1)
    lbl2.configure(text=c2)
    win.after(10,label_change)


def translate_fn():
    txt=text1.get(1.0, tk.END)
    src_lang=combo1.get()
    dest_lang=combo2.get()

    translator=Translator(from_lang=src_lang, to_lang=dest_lang)
    trans_text=translator.translate(txt)

    text2.delete(1.0, tk.END)
    text2.insert(tk.END, trans_text)
    
#icon

image_icon=tk.PhotoImage(file="icon.png")
win.iconphoto(False,image_icon)
#arrow
arrow_image=tk.PhotoImage(file="arrow.png")
image_lbl=tk.Label(win,image=arrow_image,width=128)
image_lbl.place(x=465,y=80)

language=gtr.LANGUAGES
languageV=list(language.values())
lang1=language.keys()



#combobox1
combo1=ttk.Combobox(win,values=languageV,state="r")
combo1.place(x=110,y=20)
combo1.set("English")
  
lbl1=tk.Label(win,text="ENGLISH",width=18,bd=5,font="seoge 30 bold",relief=tk.GROOVE)
lbl1.place(x=10,y=50)
#combobox2
combo2=ttk.Combobox(win,values=languageV,state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT")
  
lbl2=tk.Label(win,text="SELECT",width=18,bd=5,font="seoge 30 bold", relief=tk.GROOVE)
lbl2.place(x=620,y=50)

#frame1
f1=tk.Frame(win,bg="Black",bd=5)
f1.place(x=10,y=118,width=440,height=210)

text1=tk.Text(f1,font="Robote 20",bg="white",relief=tk.GROOVE,wrap=tk.WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=tk.Scrollbar(f1)
scrollbar1.pack(side="right",fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#frame2
f2=tk.Frame(win,bg="Black",bd=5)
f2.place(x=620,y=118,width=440,height=210)

text2=tk.Text(f2,font="Robote 20",bg="white",relief=tk.GROOVE,wrap=tk.WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=tk.Scrollbar(f2)
scrollbar2.pack(side="right",fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button
tr_button=tk.Button(win,text="Translate",font=("Roboto",15),activebackground="white",cursor="hand2",
                    bd=1,width=10,height=2,bg="black",fg="white",command=translate_fn)

tr_button.place(x=476,y=250)



button3 =tk.Button(win, text="ENGLISH DICTIONARY", font=("Roboto", 15), activebackground="white", cursor="hand2",
                 bd=1, width=20, height=2, bg="black", fg="white", command=open_dictionary_window)
button3.place(x=426, y=400)


label_change()

win.mainloop()
