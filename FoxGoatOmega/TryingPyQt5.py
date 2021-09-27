##import sys       #Table using QtGui
##from PyQt5 import QtGui
##
##class PrettyWidget(QtGui.QWidget):
##
##    def _init_(self):
##        super(PrettyWidget,self)._init()
##        self.initUI()
##
##    def initUI(self):
##        self.setGeomtery(600,300,400,200)
##        self.setWindowTitle('Table')
##
##        grid=QtGui.QGridLayout()  #Grid Layout
##        self.setLayout(grid)
##
##        data={'Kitty':[1,2,3,4],'Cat':[4,5,6,7],'Meow':[7,8,9,5],'Purr':[4,3,4,8]} #Data
##
##        table = QtGui.QTableWidget(self) #Create Empty 5X5 table
##        
##
##
##        self.show()
##def main():
##    app=QtGui.QApplication(sys.argv)
##    w=PrettyWidget()
##    app.exec_()
##
##if _name_=='_main_':
##    main()

##from guizero import * #Creating waffles
##
##
##tryinghard=App(title="Trying hard",layout="grid")
##waf=Waffle(tryinghard,grid=[200,100])
##wafa=Waffle(tryinghard,grid=[200,150])
##
##tryinghard.display()

def compbreak(fx):
    L=[]
    i=0
    j=len(fx)
    while i<len(fx): #Finding brackets within function to find composing functions
        if fx[i]=="(":
            j-=1
            while j>=0:
                if fx[j]==")":
                    L.append(fx[i+1:j])
                    break
                j-=1
        i+=1
    print(L)
def compbreak2():
    import re
    f=input("Enter a composite function") #Input function
    fx=(re.split('\+|-',f))
    print(fx)
    for k in fx:
        k="("+k+")"
        compbreak(k)
            
    
def bracketcounter():
    f=input("Enter a string:")
    cnt=0
    for i in f:
        if i in ["(",")"]:
            cnt+=1
    
##  Type 1 No restriction on quantity of algebraic terms
##                if ((f[i:i+3] in ['sin','cos','tan'])) and ('Trigonometric' not in crit):
##                    crit.append('Trigonometric')
##                elif ((f[i:i+3] in ['log'])) and ('Logarithmic' not in crit):
##                    crit.append('Logarithmic')
##                elif (((f[i:i+2] == "**") and (f[i+2] not in ['0','1','2','3','4','5','6','7','8','9'] and f[i+2:i+4] not in ['(0','(1','(2','(3','(4','(5','(6','(7','(8','(9']))) and ('Exponential' not in crit):
##                    crit.append('Exponential')
##                else:
##                    crit.append('Algebraic')
##                i+=1
##  Type 2 Lot of restriction on algebraic but not enough 
##                          if ((f[i:i+3] in ['sin','cos','tan'])) and ('Trigonometric' not in crit):
##                                  crit.append('Trigonometric')
##                          elif ((f[i:i+3] in ['log'])) and ('Logarithmic' not in crit):
##                                  crit.append('Logarithmic')
##                          elif (((f[i:i+2] == "**" ) and (f[i+2] not in ['0','1','2','3','4','5','6','7','8','9'] and f[i+2:i+4] not in ['(0','(1','(2','(3','(4','(5','(6','(7','(8','(9']))) and ('Exponential' not in crit):
##                                  crit.append('Exponential')
##                          elif f[i-2:i+1] != "**x" and f[i-1:i+2] != "**x" and f[i:i+3] != "**x" and f[i] not in ['+','-','*','/'] and f[i] not in ['0','1','2','3','4','5','6','7','8','9',")","("] and ('Algebraic' not in crit):
##                                  crit.append('Algebraic')
##                          i+=1


#User filtering in Table
##            t_user=','.join(["%s"]*len(user))
##            usercond=""
##            if user!=('All',):   #Test why All causes expansion of table by changing background colour of DispBox      
##                usercond=(" WHERE User IN (" + (t_user) + ")")
##            else:
##                usercond=""

##            s="SELECT User,Equation,Function_Class,Solution_Set,Date_Instant,Time_Instant FROM EqnStore WHERE "+ usercond + flistcond
            
##            if user!=('All',):
##                cursor.execute(s,user)
##            else:
##                cursor.execute(s)

def wtf():
    import pandas as pd
    D={"A":[1,2,3,4],"B":[[1,2],[2,3],[3,4],[4,1]],"C":["Apple","Ball","Cat","Dog"],"D":[4,3,2,1]}
    DF=pd.DataFrame(D)
    D2={}
    DF2=pd.DataFrame(D2)
    c=0
    for (r,rseries) in DF.iterrows():
            if 1 in rseries['B']:
                    a=0
                    while a<4:
                            DF2.loc[c,a]=str(rseries[a])
                            a+=1
            c+=1
    print(DF)
    print(DF2)
    print(DF['B'])
    print(DF['A'])
    print(DF['C'])
    print(DF2[1])
    
def solvinv():
    import numpy as np
    x=np.arange(-100,100,0.001)
    def eqn(x):
        return(eval("(x-2)**(0.5)"))
    for j in range(len(x)-2):
        z=(((eqn(x[j+1])-eqn(x[j]))*(eqn(x[j+2])-eqn(x[j+1])))/((x[j+1]-x[j])*(x[j+2]-x[j+1])))
        if z>0:
            print(z)
        else:
            print("Stop",z)
            break
                
def wtfscipy():#Core of equation-solving engine
    import scipy.optimize as sp
    import numpy as np
    x=np.arange(-100,100,0.001)
    a=[]
    xsol=[]
    f=input("Enter equation:")
    def eqn(x):
        return(eval(f))
    for j in range(1,len(x)-2,1):
                 z=((eqn(x[j+1])-eqn(x[j]))*(eqn(x[j])-eqn(x[j-1])))/((x[j+1]-x[j])*(x[j]-x[j-1]))
                 if (eqn(x[j]))*(eqn(x[j+1]))<=0 or z<0:
                                    a.append((x[j]+x[j+1])/2)
    for k in a:
         b=sp.fsolve(eqn,k)
##         print(b[0])
         if eqn(round(b[0],3))==0:
             xsol.append(round(b[0],3))
    print("Pro-solution set:",a)
##    for q in a:
##        if eqn(q)==0:
##            print(q,"Yes")
##        else:
##            print(q,"No")
    print("Solution set:",xsol)
##    for r in xsol:
##        if eqn(r)==0:
##            print(r,"Yes")
##        else:
##            print(r,"No")
