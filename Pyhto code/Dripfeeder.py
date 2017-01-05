# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:57:44 2016

@author: Matthijs
"""

from tkinter import *
from tkinter.filedialog import askopenfilename


def find_line(filename,lookup):
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line:
                break
    myFile.close()
    return num
    


def _make_gen(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024*1024)

def rawpycount(filename):
    f = open(filename, 'rb')
    f_gen = _make_gen(f.raw.read)
    return sum( buf.count(b'\n') for buf in f_gen )
    f.close()
#count = number of lines in the file
#line= where the setup of the file ends and other the slicing should take part
def file_cutting(count,file_begin,filename):
    amount_of_files = (count - file_begin)/2500
    #store the file_begin parameter in variable a
    a = file_begin
    q=0
    c=0
    f = open(filename)
    lines = f.readlines()
    #opens the file form line ... to line ...
    for i in range (0,int(amount_of_files)):
       file_end = file_begin + 2500
       print (file_begin, file_end)       
       file_ = open('C:/Users/Matthijs/Documents/HSS/Stage_RDM/program'+str(i)+'.prg','w')
       #add the first few lines of codes to every program these lines contain information of the module and standard paramters (tool offset etc)
       for q in range(0,a):
           file_.write(str(lines[q]))
       #add the subprogram with all the info off the path of the robotarm to the program
       for c in range(file_begin,file_end):
           file_.write(str(lines[c]))      
       file_.write(str(lines[count-3]))
       file_.write(str(lines[count-2]))
       file_.write(str(lines[count-1]))
       file_.close()   
       file_begin = file_end
    
    file_ = open('C:/Users/Matthijs/Documents/HSS/Stage_RDM/program'+str(i+1)+'.prg','w')
    file_begin_2 = int(amount_of_files) * 2500 + a
    print("File begin line foor the last program = ",file_begin_2)
    for q in range(0,a):
        file_.write(str(lines[q]))
    for c in range(file_begin_2,count):
        file_.write(str(lines[c]))
    file_.close()
       
        
def main():
    filename = askopenfilename()
    print(filename)
    count = rawpycount(filename)
    MoveL  = find_line(filename,'MoveL')
    Proc_Milling = find_line(filename,'Proc Milling')
    file_cutting(count,MoveL,filename)
    print ("line = ", line)
    print ("MoveL found at line" ,MoveL)
    print ("Proc Milling found at line")
    #print(file_contents)
                    
root = Tk()
thelabel = Label(root, text = "Dripfeed programma")
thelabel.pack()

theButton = Button(root, text = "openfile", command= main)
theButton.pack()



root.mainloop()