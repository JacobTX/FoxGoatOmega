import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




np.seterr(divide='ignore',invalid='ignore')
D={"Equation":[],"Solution set":[]}  #DataFrame to store equations
DF=pd.DataFrame(D)


class EqnWorld():
    
    def __init__(self,e,f):
        self.fpre=e
        self.fn=f
        self.xsol=[]
        self.chk=1

    def neoeqnsolver(self):
         x = np.arange(-100,100,0.001)
         a=[]                         #Pre-Solution set list
                  
         def eqn(x):
             return eval(self.fn)
                  
         try:
             print("Calculating...")
             for j in range(len(x)-1):
                 if (eqn(x[j]))*(eqn(x[j+1]))<=0:
                                    a.append((x[j]+x[j+1])/2)
             for k in a:
                     b=sp.fsolve(eqn,k)           
                     self.xsol.append(round(b[0],3))
             print("Solution set:",self.xsol)        
         except:
             print("Invalid")
              
    def eqnplot(self):
                     x=np.arange(-100,100,0.001)
##             try:
                     plt.plot(x,eval(self.fn))
                     plt.plot(x,np.zeros(len(x)),color="green")
                     plt.plot(np.zeros(len(x)),x,color="green")
                     plt.xlabel("x")
                     plt.ylabel("f(x)")
                     if self.xsol!=[]:
                          plt.axis([self.xsol[0]-1,self.xsol[-1]+1,-10,10])
                          plt.scatter(self.xsol,[0]*len(self.xsol),marker="o",color="red")
                          plt.title("Solution(s) found")
                     else:
                          plt.xlim([-100,100])
                          plt.title("No solutions found")
                     plt.show()
##             except:
##                 print("No plot available.")
         
    def eqnstore(self):
            c=len(DF.index)
            DF.loc[c,:]=[self.fpre,str(self.xsol)]
            print(DF)

def UI2():
    fx=input("Enter equation in variable x:")
    fpro=""

    k=0
    while k < len(fx):
        
        if fx[k:k+3]=="sin" and fx[k-3:k]!="np.":
            fpro += "np.sin"
            k=k+3
        elif fx[k:k+3]=="cos" and fx[k-3:k]!="np.":
            fpro += "np.cos"
            k=k+3
        elif fx[k:k+3]=="tan" and fx[k-3:k]!="np.":
            fpro += "np.tan"
            k=k+3
        elif fx[k:k+3]=="log" and fx[k-3:k]!="np.":
            fpro += "np.log"
            k=k+3
        elif fx[k:k+3]=="exp" and fx[k-3:k]!="np.":
            fpro += "np.exp"
            k=k+3
        else:
            fpro += fx[k:k+1]
            k=k+1     

    f1=EqnWorld(fx,fpro)
    
    EqnWorld.neoeqnsolver(f1)
    EqnWorld.eqnplot(f1)
    EqnWorld.eqnstore(f1)


import scipy.optimize as sp

np.seterr(divide='ignore',invalid='ignore')

def neoeqnsolver():
        fx=input("Enter equation in variable x:") 
        fpro=""

        k=0
        while k < len(fx):
            
            if fx[k:k+3]=="sin" and fx[k-3:k]!="np.":
                fpro += "np.sin"
                k=k+3
            elif fx[k:k+3]=="cos" and fx[k-3:k]!="np.":
                fpro += "np.cos"
                k=k+3
            elif fx[k:k+3]=="tan" and fx[k-3:k]!="np.":
                fpro += "np.tan"
                k=k+3
            elif fx[k:k+3]=="log" and fx[k-3:k]!="np.":
                fpro += "np.log"
                k=k+3
            elif fx[k:k+3]=="exp" and fx[k-3:k]!="np.":
                fpro += "np.exp"
                k=k+3
            else:
                fpro+= fx[k:k+1]
                k=k+1
                
        x = np.arange(-100,100,0.001)
        a=[]  #Pre-Solution set list
        xsol=[]

                 
        def eqn(x):
            return eval(fpro)
        
        try:
             print("Calculating...")
             for j in range(len(x)-1):
                 if (eqn(x[j]))*(eqn(x[j+1]))<=0:
                         a.append((x[j]+x[j+1])/2)
             for l in a:
                     b=sp.fsolve(eqn,l)           
                     xsol.append(round(b[0],3))
             print("Solution set:",xsol)        
        except:
             print("Invalid")

def stfu(f):             
    crit=[]
    i=0
    while i<len(f):
        if ((f[i:i+3] in ['sin','cos','tan'])) and ('Trigonometric' not in crit):
            crit.append('Trigonometric')
        elif ((f[i:i+3] in ['log'])) and ('Logarithmic' not in crit):
            crit.append('Logarithmic')
        elif (((f[i:i+2] == "**") and (f[i+2] not in ['0','1','2','3','4','5','6','7','8','9'] and f[i+2:i+5] not in ['(0)','(1)','(2)','(3)','(4)','(5)','(6)','(7)','(8)','(9)']))) and ('Exponential' not in crit):
            crit.append('Exponential')
        elif crit==[] and i==len(f)-1:
            crit.append('Algebraic')
        i+=1
    print(crit)





        

        
        





         
         
         

             
           
            
        
        
        

