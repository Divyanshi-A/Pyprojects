import tkinter as tk
import math
import tkinter.messagebox as mbox
#########################DECIMAL#####################
def dec():
    global dc
    global r1
    for z in str(num.get()):
        if val.get()=='1':
            if z not in '1234567890.':
                mbox.showinfo('NOTE','Please enter decimal number\n Review your entries')
        elif val.get()=='2':
            if z not in '10.':
                mbox.showinfo('NOTE','Please enter binary number\n Review your entries')
        elif val.get()=='3':
            if z not in '12345670.':
                mbox.showinfo('NOTE','Please enter octal number\n Review your entries')
        elif val.get()=='4':
            if z not in '1234567890ABCDEFabcdef':
                mbox.showinfo('NOTE','Please enter hexadecimal number\n Review your entries')
    r1=''
    if val.get()=='1':
        r1=num.get()
    elif val.get()=='2':
        n=str(float(num.get()))
        d=4
        m=n.partition('.')
        n,m=int(m[0]),m[2]
        if type(num.get())==int:
            m=0
        j,e=0,0
        l=len(str(n))
        for i in str(n):
            l=l-1
            a=int(i)*(math.pow(2,l))
            j+=a
        for k in str(m):
            l=l-1
            a=int(i)*(math.pow(2,(1/l)))
            e+=a    
        r1=j+e
    elif val.get()=='3':
        n=str(float(num.get()))
        d=4
        m=n.partition('.')
        n,m=int(m[0]),m[2]
        j,e=0,0
        l=len(str(n))
        for i in str(n):
            l=l-1
            a=int(i)*(math.pow(8,l))
            j+=a
        for k in str(m):
            l=l-1
            a=int(k)*(math.pow(8,(1/l)))
            e+=a
        r1=j+e
    elif val.get()=='4':
        n=num.get()
        j,l=0,len(str(n))
        d={'A':10,'a':10,'B':11,'b':11,'C':12,'c':12,'D':13,'d':13,'E':14,'e':14,'f':15,'F':15}
        for i in str(n):
            if i in d:
                    i=d[i]
            l=l-1
            a=int(i)*(math.pow(16,l))
            j+=a
        r1=j
    dc=tk.Label(conv,text=r1,font=('arial',15,),background = "peach puff")
    dc.grid(row=11,column=1)
###################BINARY####################################
def binary():
    for z in str(num.get()):
        if val.get()=='1':
            if z not in '1234567890.':
                mbox.showinfo('NOTE','Please enter decimal number\n Review your entries')
        elif val.get()=='2':
            if z not in '10.':
                mbox.showinfo('NOTE','Please enter binary number\n Review your entries')
        elif val.get()=='3':
            if z not in '12345670':
                mbox.showinfo('NOTE','Please enter octal number\n Review your entries')
        elif val.get()=='4':
            if z not in '1234567890ABCDEFabcdef':
                mbox.showinfo('NOTE','Please enter hexadecimal number\n Review your entries')
    global r2
    global bn
    r2=''
    if val.get()=='1':
        s=''
        n=str(float(num.get()))
        f=''
        d=4
        m=n.partition('.')
        n,m=int(m[0]),float(m[1]+m[2])
        while n!=1:
            if n%2==0:
                s+='0'
            else:
                s+='1'
            n=n//2
        else:
            s+='1'
            s=s[::-1]
        while d!=0:
            m=m*2
            if m>=1:
                f+='1'
                m=m-1
            else:
                f+='0'
            d=d-1
        r2=(s+'.'+f)
    elif val.get()=='2':
        r2=num.get()
    elif val.get()=='3':
        n=num.get()
        m,s=0,''
        l=len(str(n))
        for i in str(n):
            l=l-1
            a=int(i)*(math.pow(8,l))
            m+=a
        n=m
        while n!=1:
                if n%2==0:
                    s+='0'
                else:
                    s+='1'
                n=n//2
        else:
            s+='1'
        r2=s[::-1]
    elif val.get()=='4':
        n=num.get()
        m,l,s=0,len(str(n)),''
        d={'A':10,'a':10,'B':11,'b':11,'C':12,'c':12,'D':13,'d':13,'E':14,'e':14,'f':15,'F':15}
        for  i in str(n):
            if i in d:
                i=d[i]
            l=l-1
            a=int(i)*(math.pow(16,l))
            m+=a
        n=m
        while n!=1:
            if n%2==0:
                s+='0'
            else:
                s+='1'
            n=n//2
        else:
            s+='1'
        r2=s[::-1]
    bn=tk.Label(conv,text=r2,font=('arial',15,),background = "peach puff")
    bn.grid(row=11,column=2)
    
##############################OCTAL#############################################3
def octal():
    global r3
    global ot
    for z in str(num.get()):
        if val.get()=='1':
            if z not in '1234567890':
                mbox.showinfo('NOTE','Please enter decimal number\n Review your entries\ncoversion from fractional decimal is currently unavailable')
        elif val.get()=='2':
            if z not in '10':
                mbox.showinfo('NOTE','Please enter binary number\n Review your entries\ncoversion from fractional binary is currently unavailable')
        elif val.get()=='3':
            if z not in '12345670':
                mbox.showinfo('NOTE','Please enter octal number\n Review your entries')
        elif val.get()=='4':
            if z not in '1234567890ABCDEFabcdef':
                mbox.showinfo('NOTE','Please enter hexadecimal number\n Review your entries')
    
    r3=''
    if val.get()=='1':
        s=''
        n=eval(num.get()) 
        while n!=0:
            s+=str(n%8)
            n=n//8
        r3=s[::-1]
    elif val.get()=='2':
        n=eval(num.get())
        m,s=0,''
        l=len(str(n))
        for i in str(n):
            l=l-1
            a=int(i)*(math.pow(2,l))
            m+=a
        while m!=0:
            s+=str(m%8)
            m=m//8
        r3=s
    elif val.get()=='3':
        r3=num.get()
    elif val.get()=='4':
        n=str(num.get())
        m,l=0,len(str(n))
        d={'A':10,'a':10,'B':11,'b':11,'C':12,'c':12,'D':13,'d':13,'E':14,'e':14,'f':15,'F':15}
        for  i in str(n):
            if i in d:
                i=d[i]
            l=l-1
            a=int(i)*(math.pow(16,l))
            m+=a
        n=int(m)
        s='' 
        while n!=0:
            s+=str(n%8)
            n=n//8
        r3=s[::-1]
    ot=tk.Label(conv,text=r3,font=('arial',15,),background = "peach puff")
    ot.grid(row=11,column=3)
###############################HEXADECIMAL###################################################
def hexa():
    global hx
    global r4
    for z in str(num.get()):
        if val.get()=='1':
            if z not in '1234567890':
                mbox.showinfo('NOTE','Please enter decimal number\nReview your entries\n coversion from fractional decimal is currently unavailable')
        elif val.get()=='2':
            if z not in '10.':
                mbox.showinfo('NOTE','Please enter binary number\n Review your entries\ncoversion from fractional binary is currently unavailable')
        elif val.get()=='3':
            if z not in '12345670':
                mbox.showinfo('NOTE','Please enter octal number\n Review your entries')
        elif val.get()=='4':
            if z not in '1234567890ABCDEFabcdef':
                mbox.showinfo('NOTE','Please enter hexadecimal number\n Review your entries')
    r4=''
    if val.get()=='1':
        s=''
        n=int(num.get())
        a={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while n!=0:
               if n%16<10:
                   s+=str(n%16)
               else:
                   s+=a[n%16]
               n=n//16
        r4=s[::-1]
    elif val.get()=='2':    
        n=eval(num.get())
        m,s=0,''
        l=len(str(n))
        for i in str(n):
            l=l-1
            a=int(i)*(math.pow(2,l))
            m+=a
        n=int(m)
        a={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while n!=0:
               if n%16<10:
                   s+=str(n%16)
               else:
                   s+=a[n%16]
               n=n//16
        r4=s[::-1]
    elif val.get()=='3':
        n=eval(num.get())
        m,s=0,''
        l=len(str(n))
        for i in str(n):
            l=l-1
            a=int(i)*(math.pow(8,l))
            m+=a
        n=int(m)
        s=''
        b={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while n!=0:
               if (n%16)<10:
                   s+=str(n%16)
               else:
                   s+=b[n%16]
               n=n//16
        r4=s[::-1]
    elif val.get()=='4':
        r4=num.get()
    hx=tk.Label(conv,text=r4,font=('arial',15,),background = "peach puff")
    hx.grid(row=11,column=4)

def clear():
    global dc
    global bn
    global ot
    global hx
    dc.destroy()
    bn.destroy()
    ot.destroy()
    hx.destroy()
#=========================MAIN WINDOW========================================   
conv=tk.Tk()
conv['background']='peach puff'
#========================ENTRY===============================================
num=tk.Entry(conv,font=('Helvetica',15),foreground = "Blue")
num.grid(row=3,column=1,columnspan=5)

#============BUTTON_DICT=====================================================
b={'DEC':'1','BIN':'2','OCT':'3','HEX':'4'}

#=======================VARIABLES============================================
result=tk.StringVar
val=tk.StringVar(conv,1)
r1,r2,r3,r4,='','','',''
#===========================BUTTONS==========================================
    
for (t, v) in b.items(): 
    tk.Radiobutton(conv, text = t,font=('Helvetica',15),  
                value = v,variable=val,
                background = "LightBlue1").grid(row=4,column=v)
    tk.Label(conv,background = "lavender",font=('Helvetica',15),text=t).grid(row=10,column=v,padx=5)

#===========================================================================
tk.Button(conv,bd=8, text ='DECIMAL',font=('arial',15),
                background = "light blue",command=dec).grid(row=5,column=1)
tk.Button(conv,bd=8, text ='BINARY',font=('arial',15),
                background = "light blue",command=binary).grid(row=5,column=2)
tk.Button(conv,bd=8, text ='OCTAL',font=('arial',15),
                background = "light blue",command=octal).grid(row=5,column=3)
tk.Button(conv,bd=8, text ='HEXADECIMAL',font=('arial',15),
                background = "light blue",command=hexa).grid(row=5,column=4)

tk.Button(conv,bd=8, text ='CLEAR',font=('arial',15,),
                background = "RED",command=clear).grid(row=4,column=7)

#========================RESULT=========================================
tk.Label(conv,text=r1).grid(row=5,column=7)
tk.Label(conv,text=r2).grid(row=5,column=8)
tk.Label(conv,text=r3).grid(row=5,column=9)
tk.Label(conv,text=r4).grid(row=5,column=10)

#=========================HEADINGS AND NAMES=============================
tk.Label(conv,text='CONVERTOR',font=('Times',25,'underline','italic')).grid(row=0,column=3,rowspan=1,sticky='N')
tk.Label(conv,text='Enter Number',font=('arial',15)).grid(row=3,column=0)
tk.Label(conv,text='Which number is this?',font=('arial',15)).grid(row=4,column=0)
tk.Label(conv,text='Convert this to:',font=('arial',15)).grid(row=5,column=0)
tk.Label(conv,text='Result',font=('arial',20,'underline')).grid(row=7,column=2,rowspan=1,columnspan=2)


conv.mainloop()
