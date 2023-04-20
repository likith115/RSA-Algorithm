import math
from tkinter import *
import tkinter.messagebox
import random
root=Tk()
root.title("Encrypt & Decrypt")
primes=[]
for num in range(11,100):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        primes.append(num)
print(primes)
x=random.randint(0,len(primes))
p=primes[x]
primes.remove(p)
y=random.randint(0,len(primes))
q=primes[y]
e=2
N=p*q
phi=(p-1)*(q-1)
def gcd(a,b):
    if(b==0):
        return a
    else:
        return(gcd(b,a%b))
while(e<phi):
    if(gcd(e,phi)==1):
        break
    else:
        e=e+1
def get_d(e,phi):
    n11=1
    while(phi*n11+1)%e!=0:
        n11=n11+1
    d1=(n11*phi+1)/e
    return d1
d=int(get_d(e,phi))
print("e :",e)
print("d: ",d)
my_font=('calibre',10, 'bold')
Label(root,text="").grid(row=1,column=0)
Label(root,text="ENTER THE TEXT",borderwidth=2,width=15,height=4,font=my_font).grid(row=2,column=0,columnspan=10)
text=Text(root,borderwidth=2,width=30,height=8)
text.grid(row=3,column=0,padx=70,pady=10,columnspan=10)
global en
en=[]
def encrypt():
    plain_text=text.get(1.0,END)
    ascii=[]
    for i in plain_text:
        ascii.append(ord(i))
    print(ascii)
    for j in ascii:
        C=pow(j,e)
        C=C%N
        en.append(C)
    print(en)
    Label(root,text="Encrypted Message",font=my_font).grid(row=6,column=0)
    texten = Text(root,width=20,height=5)
    texten.grid(row=7, column=0,padx=50,pady=10)
    for i in en:
        texten.insert(END,str(i)+" ")
def decrypt():
    de = []
    plain_text = text.get(1.0, END)
    plain_text = plain_text.split()
    plain_text = [int(x) for x in plain_text]
    print(plain_text)
    for k in plain_text:
        M=pow(k,d)
        M=int(M%N)
        de.append(M)
    print(de)
    org = ''.join(chr(val) for val in de)
    print(str(org))
    Label(root, text="decrypted Message",font=my_font).grid(row=6, column=2)
    textdn = Text(root, width=20, height=5)
    textdn.grid(row=7, column=2, padx=50, pady=10)
    textdn.insert(END,str(org))
encry=Button(root,text="ENCRYPT",command=encrypt)
encry.grid(row=5,column=0,pady=10,padx=80)
decry=Button(root,text="DECRYPT",command=decrypt)
decry.grid(row=5,column=2,pady=10,padx=80)
root.mainloop()








