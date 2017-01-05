# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:26:40 2016

@author: Matthijs
"""
from tkinter import *
from tkinter.filedialog import askopenfilename
from os.path import normpath, basename

def _make_gen(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024*1024)

def rawpycount(filesave):
    f = open(filesave, 'rb')
    f_gen = _make_gen(f.raw.read)
    return sum( buf.count(b'\n') for buf in f_gen )
    f.close()

def find_line(filesave,lookup):
    with open(filesave) as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line:
                break
    myFile.close()
    return num

def file_cutting(amount_of_lines,file_begin,filesave):
    amount_of_files = (amount_of_lines - file_begin)/2500
    a = file_begin
    f = open(filesave)
    lines = f.readlines()
    i = 0; q = 0; c = 0;
    for i in range (0,int(amount_of_files)):
       file_end = file_begin + 2500
       file_ = open(filesave+str(i)+'.prg','w')
       #add the first few lines of codes to every program these lines contain information of the module and standard paramters (tool offset etc)
       for q in range(0,a):
           file_.write(str(lines[q]))
       #add the end of the program
       for c in range(file_begin,file_end):
           file_.write(str(lines[c]))      
       #file_.write(str(lines[amount_of_lines-3]))
       file_.write(str(lines[amount_of_lines-2]))
       file_.write(str(lines[amount_of_lines-1]))
       file_.close()   
       file_begin = file_end
    
    file_ = open(filesave+str(i+1)+'.prg','w')
    file_begin_2 = int(amount_of_files) * 2500 + a
    for q in range(0,a):
        file_.write(str(lines[q]))
    for c in range(file_begin_2,amount_of_lines):
        file_.write(str(lines[c]))
    file_.close()
    return amount_of_files

def create_main(filesave,progname,amount_of_files):
    #create one program that executes all the other programs
    file_ = open(filesave+'mainprogram.prg','w')
    header_begin = '''
%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_Start
    
    !VAR string totalpath;
    ! -------------------------------
    ! Define your variables here
    ! ...
	VAR string totalpath;
    ! -------------------------------
    ! Define your functions here
    ! ...
    PROC Main()
'''
   
    file_.write(header_begin)
    for i in range(0,int(amount_of_files)+1):
        #directory of the mounted disk on your pc should change if it is not the same as pc:/frezen/
        file_.write("    TPerase;\n")
        file_.write("    TPWrite \"start of program"+str(i)+"\""";\n")
        file_.write("    totalpath := \"pc:/"+progname+str(i)+".prg\";\n")
        file_.write("    load\Dynamic, totalpath;\n")
        file_.write("    %\"MOD_Milling:Main\"%;\n")
        file_.write('    Unload totalpath;\n')
        file_.write('    TPErase;')
    header_end = '''
    TPWrite"FINSHED";
    ENDPROC
ENDMODULE
'''
    file_.write(str(header_end))
    file_.close()
    
    
def main():
    filename = askopenfilename()
    print(filename)
    progname = (basename(normpath(filename)))    
    count = rawpycount(filename)
    Move  = find_line(filename,'Move') 
    amount_of_files = file_cutting(count,(Move-1),filename)
    create_main(filename,progname,amount_of_files)
    #print(file_contents)
                    
root = Tk()
thelabel = Label(root, text = "Dripfeed programma")
thelabel.pack()
theButton = Button(root, text = "openfile", command= main)
theButton.pack()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")



root.mainloop()