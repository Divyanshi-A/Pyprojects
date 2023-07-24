'''
Author name:Divyanshi Aroa
Project:Coaching Management App
Date:26 December 2021
'''


import time,csv,pickle,random,string,re,os,json
import webbrowser as wbr
import tkinter as tk



def generate(name,file): #generates user_id after reading last record from file
    try:
        with open(file,'rb') as fout:
            while True:
                rec=pickle.load(fout)
    except IOError: #if file not found returns roll no. as 10001
        return name+'_10001'
    except EOFError:
        num=int(rec[0].split('_')[1])
        num+=1
        return name+'_'+str(num)


#verifies user id and pass during login
def verify(user_nm,pswd,p_id):
    #p_id 1->Teacher 2->student 3->Admin in int
    if p_id==1:
        try:
            with open('E:\\Atomic academy\\logs\\teach.bin','rb') as fout:
                while True:
                    lst=pickle.load(fout)
                    if lst[0]==user_nm:
                        if lst[1]==pswd:
                            return 'Verified'
                        else:
                            return 'Invalid password'
        except EOFError:
            return 'Invalid username'
    elif p_id==2:
        try:
            with open('E:\\Atomic academy\\logs\\stud.bin','rb') as fout:
                while True:
                    lst=pickle.load(fout)
                    if lst[0]==user_nm:
                        if lst[1]==pswd:
                            return 'Verified'
                        else:
                            return 'Invalid password'
        except EOFError:
            return 'Invalid username'
    else:
        try:
            with open('E:\\Atomic academy\\Sysfiles\\admin.txt') as fout:
                while True:
                    rec=json.loads((fout.readline()))
                    if rec['Username']==user_nm:
                        if rec['password']==pswd:
                            return 'Verified'
                        else:
                            return 'Invalid password'
        except EOFError:
            return 'Invalid username'
        
        

#login menu    
def login():
    while True:
        user_nm=input('Enter username')
        pswd=input('enter password')
        p_id=int(input('\t\t Choose your identity\n\t\t1.Teacher\n\t\t2.Student\n\t\t3.Administrator\nEnter Choice'))
        ver=verify(user_nm,pswd,p_id)
        if ver.lower()=='verified':
            if p_id==1:
                file='E:\\Atomic academy\\logs\\teach.bin'
                file1='E:\\Atomic academy\\rec\\teach.csv'
                d=display_p(file,file1,user_nm)
                teacher_menu(user_nm,d['Subject'])
                break
            elif p_id==2:
                file='E:\\Atomic academy\\logs\\stud.bin'
                file1='E:\\Atomic academy\\rec\\studrec.csv'
                d=display_p(file,file1,user_nm)
                batch=d['Batch']
                student_menu(batch,user_nm)
                break
            else:
                ver=input('Enter code provided by administrator')
                if ver.lower()=='212j@ss':
                    Admin_menu()
                    break
                else:
                    print('Wrong code recieved')
                    ch=input('Would you like to go back to Main menu?')
                    if ch.lower() in ['y','yes','yeah']:
                        break
                    else:
                        print('You are being redirected to Login menu')
                        time.sleep(2)
        else:
            print(ver)
            ch=input('Would you like to go back to Main menu?')
            if ch.lower() in ['y','yes','yeah']:
                break
            else:
                print('You are being redirected to Login menu')
                time.sleep(2)
                
def check_mail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return email
    else:
        print("Invalid Email")
        email=input('enter email')
        check_mail(email) #use of recursion to make sure correct email format is used
        
    

def signup():
    nm=input('Enter Name')
    pswd=input('Enter password')
    email=input('Enter email')
    email=check_mail(email)
    while True:
        p_id=int(input('\t\t Choose identity\n\t\t1.Teacher\n\t\t2.Student\n\t\t\nEnter Choice'))
        if p_id==1:
            s={1:'P',2:'B',3:'M',4:'C'}
            sub=int(input('\t\tChoose Subject:\n\t\t1.Physics\n\t\t2.Biology\n\t\t3.Mathematics\n\t\t4.Chemistry\nEnter Choice'))
            user_nm=generate(nm,'E:\\Atomic academy\\logs\\teach.bin')
            print('Your Username is:',user_nm)
            with open('E:\\Atomic academy\\rec\\teach.csv','a',newline='') as fin:
                rec_writer=csv.writer(fin)
                rec=[user_nm,nm,s[sub],email]
                rec_writer.writerow(rec)
            with open('E:\\Atomic academy\\logs\\teach.bin','ab') as fin:
                rec=[user_nm,pswd]
                pickle.dump(rec,fin)
            
        elif p_id==2:
            sub=input('\t\tChoose subject:\n\t\t1.PCM\n\t\t2.PCB\n\t\tEnter Choice')
            cl=input('\t\tChoose class:\n\t\t1.XI\n\t\t2.XII\n\t\tEnter Choice')
            batch=sub+cl
            d={'11':'PCM_XI','12':'PCM_XII','21':'PCB_XI','22':'PCB_XII'}
            if batch in d:
                batch=d[batch]
                print('Your batch is:',batch)
            else:
                print('Invalid  batch selection made')
                continue
            user_nm=generate(nm,'E:\\Atomic academy\\logs\\stud.bin')
            print('Your username is:',user_nm)
            with open('E:\\Atomic academy\\rec\\studrec.csv','a',newline='') as fin:
                rec_writer=csv.writer(fin)
                rec=[user_nm,nm,batch.split('_')[0],batch.split('_')[1],batch,email]
                rec_writer.writerow(rec)
            with open('E:\\Atomic academy\\logs\\stud.bin','ab') as fin:
                rec=[user_nm,pswd]
                pickle.dump(rec,fin)
        else:
            print('Invalid input made')
            continue
        print('You have been signed up')
        CH=input('Would you like to enter your profile')
        if CH.lower() in ['y','yes']:
            if p_id==1:
                teacher_menu(user_nm,s[sub])
                break
            else:
                student_menu(batch,user_nm)
                break
        else:
            break


#make every csv file newline=''

def display_p(file,file1,user_nm):
    try:
        d={}
        with open (file,'rb') as fout:
            while True:
                l=pickle.load(fout)
                if l[0]==user_nm:
                    d['Username']=l[0]
                    d['pswd']=l[1]
                    break
    except EOFError:
        print('Id not found')
        
    with open(file1,'r') as fout1:
        recreader=csv.reader(fout1)
        c=0
        for i in recreader:
            if c==0:
                lst=i
                c+=1
            if i[0]==user_nm:
                n=0
                for k in lst:
                    d[k]=i[n]
                    n+=1
    return d
           
        
def file_select(SUB):
    lst,lst1,n,m=os.listdir('E:\\Atomic academy\\rec'),[],0,0
    for i in lst:
        n+=1
        if SUB in i.split('_')[-1] or i=='studrec.csv' :
            m+=1
            print(str(m)+'.',i)
            lst1+=[n]
    fn=int(input('Please choose the required file number'))
    file='E:\\Atomic academy\\rec\\'+lst[lst1[fn-1]-1]
    return file

def Add(ID,Name=None,SUB=None):
    if ID=='t':
        ch=int(input('\t\t1.Add new student profile\n\t\t2.Add student data\n\t\t'))
        if ch==1:
            while True:
                nm=input('Enter Name')
                pswd=input('Enter password')
                email=input('Enter email')
                email=check_mail(email)
                sub=input('\t\tChoose subject:\n\t\t1.PCM\n\t\t2.PCB\n\t\tEnter Choice')
                cl=input('\t\tChoose class:\n\t\t1.XI\n\t\t2.XII\n\t\tEnter Choice')
                batch=sub+cl
                d={'11':'PCM_XI','12':'PCM_XII','21':'PCB_XI','22':'PCB_XII'}
                if batch in d:
                    batch=d[batch]
                    print('Student batch is:',batch)
                else:
                    print('Invalid  batch selection made')
                    continue
                user_nm=generate(nm,'E:\\Atomic academy\\logs\\stud.bin')
                print('Your username is:',user_nm)
                with open('E:\\Atomic academy\\rec\\studrec.csv','a',newline='') as fin:
                    rec_writer=csv.writer(fin)
                    rec=[user_nm,nm,batch.split('_')[0],batch.split('_')[1],batch,email]
                    rec_writer.writerow(rec)
                with open('E:\\Atomic academy\\logs\\stud.bin','ab') as fin:
                    rec=[user_nm,pswd]
                    pickle.dump(rec,fin)
                print('\nStudent record created:\n---------------------','Name: '+nm,'Username: '+user_nm,'Batch: '+batch,sep='\n')
                Ch=input('\nWould you like to create another profile?')
                if Ch.lower() not in ['y','yeah','yes']:
                    Ch=input('Would you like to return to previous menu')
                    if Ch.lower() not in ['y','yeah','yes']:
                        break
                    else:
                        Add(ID,Name,SUB)
        elif ch==2:
            Ch=int(input('Would you like to:\n\t\t1.Create a new file\n\t\t2.Add New test column in marks file\n\t\t3.Add a single record in file'))
            if Ch==1:
                file='E:\\Atomic academy\\rec\\'
                cl=input('\t\tChoose class:\n\t\t1.XI\n\t\t2.XII\n\t\tEnter Choice')
                if cl=='1':
                    cls='XI'
                else:
                    cls='XII'
                fn=input('Enter file name')
                file=file+fn+'_'+'1'+cl+SUB+Name[0]+'.csv'
                while os.path.isfile(file):
                    lst=file.split('.')
                    r=random.choice(string.ascii_letters).lower()
                    file=lst[0]+r+'.'+lst[1]
                print('File path',file,'file name:',file.split('_')[1])
                choice=input('Would you like to auto-fill roll no and name of student in file?\nyes/no')
                if choice.lower() in ['yes','y','yeah']:
                    lst=['Roll_No','Name']
                else:
                    lst=[]
                def field(lst):
                    f=input('Enter name of entry field in file')
                    lst+=[f]
                    ch=input('Would you like to continue?')
                    if ch.lower() in ['y','yes','yeah']:
                        field(lst)
                field(lst)
                with open (file ,'a',newline='') as fh:
                    fin=csv.writer(fh)
                    fin.writerow(lst)
                    if choice.lower() in ['yes','y','yeah']:
                        with open('E:\\Atomic academy\\rec\\studrec.csv' ,'r') as fout:
                            reader=csv.reader(fout) 
                            for i in reader:
                                lst=i[4].split('_')
                                if SUB in lst[0] and cls==lst[1]:
                                    lst1=[i[0].split('_')[1],i[1]]
                                    fin.writerow(lst1)
                        fout.close()
                fh.close()
                print('OPENING FILE...')
                time.sleep(2) 
                os.startfile(file)
            elif Ch==2 or Ch==3:
                file=file_select(SUB)
                os.startfile(file)
    elif ID=='a':
        signup()

def rec_update(file,rol):
    flag=0
    st=[]
    try:
        with open(file,"r") as fin:
            stureader=csv.reader(fin)
            c=1
            for rec in stureader:
                if c==1:
                    lst=rec
                    st.append(rec)
                elif  rec[0]==rol or rec[0].split('_')[-1]== rol:
                    print('\nRECORD FOUND:\n-----------\n',rec)
                    lst1=[]
                    lst1.append(rec[0])
                    print('For Updation:')
                    for i in lst[1:]:
                        print('Enter '+i,end=':')
                        en=input()
                        lst1.append(en)
                    st.append(lst1)
                    flag=1
                else:
                    st.append(rec)
                c=c+1
        fout = open(file,'w',newline='')
        stuwriter= csv.writer(fout)
        stuwriter.writerows(st)
        fout.close()
        if flag==0:
            print("RECORD NOT FOUND")
    except IndexError as e:
        print('Unusual record found please check the file')
    except IOError:
        print('No such file found')
        
def pswd_update(file,rol):
    finout=open(file,"r+b")
    p=input("Enter new Password")
    flag=0
    rec=[]
    try:
        while True:
            rpos=finout.tell()
            r=pickle.load(finout)
            if r[0].split('_')[1]==rol:
                rec=[r[0],p]
                finout.seek(rpos)
                pickle.dump(rec,finout)
                flag=1
    except:
        if flag==0:
            print(rol,"Not found")
        else:
            print("Updated")
        finout.close()

def Modify(ID,SUB=None):
    if ID=='t':
        file=file_select(SUB)
        choice=input('Would you like to update:\n\t1.A single record\n\t2.Multiple records')
        if choice=='1':
            rol=input('Enter Roll no.')
            rec_update(file,rol)
        elif choice=='2':
            os.startfile(file)
        else:
            print('Invalid entry recieved')
    elif ID=='a':
        ch=input('Would you like to update:\n\t1.Teacher records\n\t2.Student records')
        Ch=input('Would you like to update:\n\t1.Records\n\t2.Password')
        if ch=='1':
            if Ch=='1':
                choice=input('Would you like to update:\n\t1.A single record\n\t2.Multiple records')
                if choice=='1':
                    rol=input('enter ID')
                    file='E:\\Atomic academy\\rec\\teach.csv'
                    rec_update(file,rol)
                elif choice=='2':
                    print('OPENING FILE')
                    time.sleep(2)
                    os.startfile('E:\\Atomic academy\\rec\\teach.csv')
            elif Ch=='2':
                rol = input("Enter roll to update")
                file='E:\\Atomic academy\\logs\\teach.bin'
                pswd_update(file,rol)
        elif ch=='2':
            if Ch=='1':
                lst,m=os.listdir('E:\\Atomic academy\\rec'),0
                for i in lst:
                    m+=1
                    print(str(m)+'.',i)
                m=int(input('Please choose the required file'))
                file='E:\\Atomic academy\\rec\\'+lst[m-1]
                choice=input('Would you like to update:\n\t1.A single record\n\t2.Multiple records')
                if choice=='1':
                    rol=input('enter roll no.')
                    rec_update(file,rol)
                elif choice=='2':
                    print('OPENING FILE')
                    time.sleep(2)
                    os.startfile(file)
            elif Ch=='2':
                rol = input("Enter roll to update")
                file='E:\\Atomic academy\\logs\\stud.bin'
                pswd_update(file,rol)
            else:
                print('Invalid entry recieved')
    ch=input('\nWould you like to Update again?')
    if ch.lower() in ['y','yes','yeah']:
            Modify(ID,SUB)



def Delete(ID,SUB=None):
    try:
        if ID=='t':
            ch=input('Would you like to delete:\n\t1.A single record\n\t2.Multiple records')
            if ch=='1':
                flag=0
                file=file_select(SUB)
                rol=input('enter roll number')
                lst=[]
                c=1
                with open(file,"r") as fout:
                    recreader = csv.reader(fout)
                    for rec in recreader:
                        if c!=1:
                            if rec[0]!=rol and rec[0].split('_')[-1]!= rol :
                                lst+=[rec]
                            else:
                                flag+=1
                        else:
                            lst+=[rec]
                        c+=1
                with open(file,'w',newline='') as fin:
                    recw = csv.writer(fin)
                    recw.writerows(lst)
                print(flag,'Record deleted')
            elif ch=='2':
                file=file_select(SUB)
                print('OPENING FILE')
                time.sleep(2)
                os.startfile(file)
        elif ID=='a':
            ch=input('Would you like to delete:\n\t1.A single record\n\t2.Multiple records\n\t3.Delete file')
            lst,m=os.listdir('E:\\Atomic academy\\rec'),0
            for i in lst:
                m+=1
                print(str(m)+'.',i)
            m=int(input('Please choose the required file'))
            file='E:\\Atomic academy\\rec\\'+lst[m-1]
            if ch=="1":
                rol=input('Enter roll number')
                fout=open("E:\\Atomic academy\\rec\\temp.csv","w",newline='')
                recwriter= csv.writer(fout)
                flag=0
                with open(file,"r") as fin:
                    recreader = csv.reader(fin)
                    c=1
                    for rec in recreader:
                        if c!=1:
                            if rec[0]!=rol and rec[0].split('_')[1]!= rol:
                                recwriter.writerow(rec) 
                            else:
                                flag+=1
                        else:
                            recwriter.writerow(rec)
                        c+=1
                fin.close()
                fout.close()
                os.remove(file)
                os.rename("E:\\Atomic academy\\rec\\temp.csv",file)
                print(flag,'Record deleted')
            elif ch=='2':
                print('OPENING FILE')
                time.sleep(2)
                os.startfile(file)
            elif ch=='3':
                Ch=input('Please confirm to Delete '+file+'\n1.Yes\n2.No')
                if ch=='1':
                    os.remove(file)
                    print('File Deleted')
    except PermissionError:
       print('Please close the files from background')
       Delete(ID,SUB)             
def search(file):
        Ch=input('Would you like to view:\n\t\t1.Single record\n\t\t2.Multiple records\n\t\t3.All records')
        if Ch=='1':
            rol=input('Enter roll')
            c=1
            with open (file,newline='') as fout:
                recreader = csv.reader(fout)
                for i in recreader:
                    if c==1 or i[0].split('_')[-1]==rol or i[0]==rol:
                        for k in i:
                            print(k,end='\t')
                        print('\n')
                        c+=1
        elif Ch=='2':
            l,r=[],0
            def k(l,obj):
                rol=input('Enter '+obj)
                l+=[rol]
                c=input('Would you like to Continue')
                if c.lower() in ['y','yes','yeah']:
                    k(l,obj)
            c,n=1,1
            with open (file) as fout:
                recreader = csv.reader(fout)
                for i in recreader:
                    if c==1:
                        lst=i
                        for j in i:
                            print(n,j)
                            n+=1
                        opt=int(input('Enter criteria for searching'))
                        k(l,lst[opt-1])
                        c+=1
                        for k in lst:
                            print(k,end='\t')
                        print('\n')
                    elif i[opt-1] in l:
                        for k in i:
                            print(k,end='\t')
                            r+=1
                        print('\n')
            print('Total Records found:',r)
        elif Ch=='3':
            with open (file) as fout:
                recreader = csv.reader(fout)
                for rec in recreader:
                    for k in rec:
                            print(k,end='\t')
                    print('\n')

def View(ID,SUB=None,user_nm=None):
    if ID=='t':
        ch=input('\t\t1.View student record\n\t\t2.View Quiz results\n\t\t3.View your profile')
        if ch=='1':
            file=file_select(SUB)
            search(file)
        elif ch=='2':
            d={'1':'XI','2':'XII'}
            cl=input('\t\tChoose class:\n\t\t1.XI\n\t\t2.XII\n\t\tEnter Choice')
            cl=d[cl]
            num=input('\t\tEnter Quiz no:')
            nm=input('Enter Quiz name')
            q=nm.upper()+'_'+num
            file='E:\\Atomic academy\\Sysfiles\\quiz_'+SUB.upper()+'.bin'
            print('file name =',file)
            if os.path.isfile(file)==False:
                print('\nNo quiz file found.Please check file in system')
                return
            
            try:
                with open(file,'rb') as f:
                    while True:
                        rec=pickle.load(f)
                        if rec[0]==q:
                            if rec[1]==cl:
                                chrome.open(rec[3])
                                break
            except EOFError:
                print('\nQuiz not found')

        elif ch=='3':
            file='E:\\Atomic academy\\logs\\teach.bin'
            file1='E:\\Atomic academy\\rec\\teach.csv'
            d=display_p(file,file1,user_nm)
            print('\n\n\t\t*****USER PROFILE*****')
            for key,value in d.items():
                print('\t\t',key,':',value)
    elif ID=='a':
        ch=int(input('\t\t1.View student record\n\t\t2.View Teacher Records\n\t\t3.View profile'))
        if ch==1:
            lst,m=os.listdir('E:\\Atomic academy\\rec'),0
            for i in lst:
                m+=1
                print(str(m)+'.',i)
            m=input('Please choose the required file')
            file='E:\\Atomic academy\\rec\\'+lst[int(m)-1]
            search(file)
        elif ch==2:
            search('E:\\Atomic academy\\rec\\teach.csv')
        elif ch==3:
            with open('E:\\Atomic academy\\Sysfiles\\admin.txt') as fout:
                d=json.loads((fout.readline()))
                print('\n\n\t####ADMIN PROFILE####')
                for key,value in d.items():
                    print('\t\t',key,':',value)

def Quiz(batch):
    file='E:\\Atomic academy\\Sysfiles\\quiz_'
    sub=int(input('\t\tPlease select subject:\n\t\tEnter:\n\t\t1 for Physics\n\t\t2 for Chemistry\n\t\t3 for Mathematics\Biology'))
    num=input('\t\tEnter Quiz no:')
    nm=input('Enter Quiz name')
    q=nm.upper()+'_'+num
    if sub==1 :
        file+='P'
    elif sub==2:
        file+='C'
    elif sub==3:
        file+=batch.split('_')[0][2].upper()
    else:
        print('Invalid input recieved')
        return
    file+='.bin'
    print('file name =',file)
    if os.path.isfile(file)==False:
        print('\nNo quiz file found.Please check in with your sbject teacher')
        return
    
    try:
        with open(file,'rb') as f:
            while True:
                rec=pickle.load(f)
                if rec[0]==q:
                    if rec[1]==batch.split('_')[1]:
                        chrome.open(rec[2])
                        break
    except EOFError:
        print('\nQuiz not found')

                        
                

def Assignment(batch):
    if batch=='PCM_XII':
        chrome.open('https://drive.google.com/drive/folders/1zlz-v42UMnJGphcotssKj1b6YCiTqjCi?usp=sharing')
    elif batch=='PCM_XI':
        chrome.open('https://drive.google.com/drive/folders/1KSPiNCm7MasPhvsoickQn9X6EVfJOtc6?usp=sharing')
    elif batch=='PCB_XI':
        chrome.open('https://drive.google.com/drive/folders/1jHKbJHdllZzBn_rp08rpEAs4PHHn4OKM?usp=sharing')
    elif batch=='PCB_XII':
        chrome.open('https://drive.google.com/drive/folders/1uTDy5cTGlGDnY7HPXyJ5H6jE87B8RfSH?usp=sharing')
    else:
        print('INVALID BATCH RECIEVED')
        
def quiz_m(SUB):
    d={'1':'XI','2':'XII'}
    chrome.open('https://docs.google.com/forms/u/0/')
    nm=input('\nEnter Quiz name')
    cl=input('\t\tChoose class:\n\t\t1.XI\n\t\t2.XII\n\t\tEnter Choice')
    cl=d[cl]
    link=input('Insert link for students here')
    link1=input('Insert link for Evaluation here')
    file='E:\\Atomic academy\\Sysfiles\\quiz_'+SUB.upper()+'.bin'
    try:
        with open(file,'rb') as fout:
            while True:
                rec=pickle.load(fout)
    except IOError:
        q=nm.upper()+'_'+'1'
    except EOFError:
        num=int(rec[0].split('_')[1])
        num+=1
        q=nm.upper()+'_'+str(num)
    print('Quiz name:',q)
    with open(file,'ab') as f:
        rec=[q,cl,link,link1]
        pickle.dump(rec,f)
    
def student_menu(batch,user_nm):
    print('\t\tWelcome to student section')
    while True:
        choice=int(input('\t\tWould you like to:\n\t1.Take a Test\n\t2.Access Assignment\n\t3.View Profile\n\t4.Exit'))
        if choice==1:
            Quiz(batch)
        elif choice==2:
            Assignment(batch)
        elif choice==3:
            file='E:\\Atomic academy\\logs\\stud.bin'
            file1='E:\\Atomic academy\\rec\\studrec.csv'
            d=display_p(file,file1,user_nm)
            print('\t\t\tUSER PROFILE')
            for key,value in d.items():
                print('\t\t',key,':',value)
        elif choice==4:
          print('You are being logged out')
          time.sleep(2)
          break
          
def teacher_menu(user_nm,sub):
    print('\t\tWelcome to Teacher section')
    while True:
        choice=int(input('\t\tWould you like to:\n\t1.Update&View\n\t2.Assign Assignment\n\t3.Insert Quiz/Test\n\t4.Exit'))
        if choice==1:
            while True:
                ch=int(input('\t\tWould you like to:\n\t1.Add Records\n\t2.Update student data \n\t3.Delete record\n\t4.View\n\t5.Exit'))
                if ch==1:
                    Add('t',user_nm.split('_')[0],sub)
                elif ch==2:
                    Modify('t',sub)
                elif ch==3:
                    Delete('t',sub)
                elif ch==4:
                    View('t',sub,user_nm)
                elif ch==5:
                    print('You are being redirected to teacher main menu')
                    time.sleep(3)
                    break
                else:
                    print('Invalid Input')
        elif choice==2:
            chrome.open('https://drive.google.com/drive/folders/1IyHj2Fn7-RDOl20dWJ_pUHtT6l0MIEDS?usp=sharing')
        elif choice==3:
            quiz_m(sub)
        elif choice==4:
            print('You are being logged out')
            time.sleep(3)
            break
        else:
            print('Invalid input recieved')

def Admin_menu():
    print('Welcome to Admin Section')
    while True:
            ch=int(input('\t\tWould you like to:\n\t1.Add record\n\t2.Update record \n\t3.Delete record\n\t4.View\n\t5.Exit'))
            if ch==1:
                Add('a')
            elif ch==2:
                Modify('a')
            elif ch==3:
                Delete('a')
            elif ch==4:
                View('a')
            elif ch==5:
                print('You are being redirected to main menu')
                time.sleep(3)
                break
            else:
                print('Invalid Input')
        
           
            
    
#__main__



chrome=wbr.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")



m=tk.Tk()
l=tk.Label(m,bg='LightBlue1',text='WELCOME TO:',font=('Calisto MT',50))
l.pack(anchor='center',fill='both')
l1=tk.Label(m,bg='LightBlue1',text='        ',font=('bold',50))
l1.pack(anchor='center',fill='both')
l2=tk.Label(m,bg='LightBlue1',text='ATOMIC ACADEMY',font=('Castellar',50))
l2.pack(anchor='center',fill='both')
l1=tk.Label(m,bg='LightBlue1',text='        ',font=('italic',50))
l1.pack(anchor='center',fill='both')
l2=tk.Label(m,bg='LightBlue1',text='"A place where dreams come true"',font=('Californian Fb',40))
l2.pack(anchor='center',fill='both')
l1=tk.Label(m,bg='LightBlue1',text='------------',font=('italic',50))
l1.pack(anchor='center',fill='both')
l1=tk.Label(m,bg='LightBlue1',text='________________________________________________________',font=('italic',100))
l1.pack(anchor='center',fill='both')
l1=tk.Label(m,bg='Light pink',text='Author:Divyanshi Arora\t\t Class:12 A',font=('French Script MT',40))
l1.pack(anchor='center',fill='both')
l1=tk.Label(m,bg='Light pink',text='Topic:COACHING MANAGEMENT APP',font=('Californian Fb',30))
l1.pack(anchor='center',fill='both')
l1=tk.Label(m,bg='Light pink',text='        ',font=('italic',50))
l1.pack(anchor='center',fill='both')
m.mainloop()

while True:
    print('\t\t\tATOMIC ACADEMY\n\n\n\t\tLogin/Signup Window')
    path=input('\t\tWould you like to:\n\t\t\ta) LOGIN b)SIGN UP c)EXIT\nEnter Choice')
    if path.lower()=='a':
        login()
    elif path.lower()=='b':
        signup()
    else:
        ch=input('invalid choice\n\t\tWould you like to exit?')
        if ch.lower() in ['yes','y','yeah']:
            print('We hope you visit soon!')
            break
        else:
            print('You are being redirected to main menu again')
            time.sleep(2)
            continue

