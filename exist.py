import tkinter as tk
import pandas as pd
import csv

data=pd.read_csv('data.csv')
que=data['DESCRIPTIONACCIDENT'].values.tolist()

root=tk.Tk()
root.geometry('300x400')
root.title('quiz')



main_frame=tk.Frame(root)
main_frame.pack(fill=tk.BOTH,expand=True)

lp=[]
lp.append(que[0])
k=0
def cus_falt():
    global k
    
   
    k=1
    print('customer Fault')
    
    
    
def sys_err():
    global k
    k=2
    print('system error')
   
    
def un_st():
    global k
    k=3
    print('unclear statement')

def s():
    print('skip')
    

pq=2
def b1():
    global pq
    pq=pq+1
    
def dele():
    r=[]
    with open('data.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for row in csv_reader:
            if csv_reader.line_num==pq:
                continue
            else:
                r.append(row)
    with open('data.csv','w',newline='') as csv_file:
        csv_writer=csv.writer(csv_file)
        csv_writer.writerows(r)

def move_next():
    global c
    global lp
    if not c>len(pages)-2:
        for p in pages:
            p.pack_forget()
        c+=1     
        page=pages[c]
        bt1=tk.Button(page,text="Customer Fault",padx=60,command=lambda:[move_next(),cus_falt(),fun(),dele()])
        bt2=tk.Button(page,text="System Error",padx=70,command=lambda:[move_next(),sys_err(),fun(),dele()])
        bt3=tk.Button(page,text="Unclear Statement",padx=60,command=lambda:[move_next(),un_st(),fun(),dele()])
        bt4=tk.Button(page,text="Skip",padx=50,command=lambda:[move_next(),b1(),s()])
        bt1.pack(pady=30)
        bt2.pack(pady=30)
        bt3.pack(pady=30)
        bt4.pack(pady=30)
        page.pack(pady=100)

        


c=0
page=tk.Frame(main_frame)
page.pack(pady=120)
page_label=tk.Label(page,text='Enter the Range',font=('BOLD',20))
page_label.pack()  
nam= tk.Entry(page,font=('calibre',20,'normal'))
nam.pack()
bt=tk.Button(page,text="SUBMIT",padx=60,command=lambda:[sub(),move_next()])
bt.pack(pady=30)

pages=[page]


kk=1
def sub():
    global c
    c=int(nam.get())-1

def fun():
    global lp
    global kk
    if k==1:
       lp.append('customer Fault')
    elif k==2:
           lp.append('system Error')
    elif k==3:
      lp.append('unclear Statement')
    writer1 = open('ecdata.csv', 'a', encoding='UTF8') 


    writer2 = csv.writer(writer1)

    writer2.writerow(lp)
    writer1.close()
    lp=[]
    lp.append(que[kk])
    kk+=1



for i in range(len(que)):
    page=tk.Frame(main_frame)
    page_label=tk.Label(page,text=str(i+1)+str('.')+str(que[i]),font=('BOLD',10))
    page_label.pack()    
    pages.append(page)






bottom_frame=tk.Frame(root)



bottom_frame.pack(side=tk.BOTTOM,pady=10)
