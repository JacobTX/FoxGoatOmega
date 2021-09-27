import numpy as np
import scipy.optimize as sp

xsol=[]
crit=[]

def reveqnsolver(fx):
        xsol.clear()
        crit.clear()
        np.seterr(divide='ignore',invalid='ignore')
         #Text box to enter equation 
        fpro="("

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
            elif fx[k:k+1]=="^" and fx[k-3:k]!="np.":
                fpro += "**"
                k=k+1
            else:
                fpro+= fx[k:k+1]
                k=k+1
        fpro+=")"
                

        x = np.arange(-100,100,0.001)
        a=[]  #Pre-Solution set list

        print(fpro)
        def eqn(x):
            return eval(fpro)

        def stfu(f):             
            i=0
            while i<len(f):


                          if ((f[i:i+3] in ['sin','cos','tan'])) and ('Trigonometric' not in crit):
                                  crit.append('Trigonometric')
                          elif ((f[i:i+3] in ['log'])) and ('Logarithmic' not in crit):
                                  crit.append('Logarithmic')
                          elif (((f[i:i+2] == "**" ) and (f[i+2] not in ['0','1','2','3','4','5','6','7','8','9'] and f[i+2:i+4] not in ['(0','(1','(2','(3','(4','(5','(6','(7','(8','(9']))) and ('Exponential' not in crit):
                                  crit.append('Exponential')
                          elif crit==[] and i==len(f)-1:
                                  crit.append('Algebraic')
                          i+=1

            
            if len(crit)>1:
                    crit.clear()
                    crit.append('Misc')
        f=fpro
        stfu(f)

        try:
#Type 0riginal

                     for j in range(len(x)-1):
                        if (eqn(x[j+1]))*(eqn(x[j]))<=0:
                                 a.append((x[j]+x[j+1])/2)
                     
                     for l in a:
                                        b=sp.fsolve(eqn,l)
                                        if  ('Trigonometric' not in crit) and (round(b[0],3) not in xsol):
                                                if round(b[0],3) ==(-0.0):
                                                        xsol.append(0.0)
                                                else:
                                                        xsol.append(round(b[0],3))
                                        elif ('Trigonometric' in crit) and (0<=round(b[0],3)<=2*np.pi) and (round(b[0],3) not in xsol):
                                                if round(b[0],3) ==(-0.0):
                                                        xsol.append(0.0)
                                                else:
                                                        xsol.append(round(b[0],3))
#########################################################################################                                                       
## Type 1
##                for j in range(1,len(x)-2,1):
##                        z=((eqn(x[j+1])-eqn(x[j]))*(eqn(x[j])-eqn(x[j-1])))/((x[j+1]-x[j])*(x[j]-x[j-1]))
##                        if (eqn(x[j+1]))*(eqn(x[j]))<=0 or z<0:
##                                 a.append((x[j]+x[j+1])/2)

##                for l in a:
##                              b=sp.fsolve(eqn,l)
##                              print(b[0])
##                              if  ('Trigonometric' not in crit) and (round(b[0],3) not in xsol):
##                                        if round(b[0],3) ==(-0.0):
##                                                xsol.append(0.0)
##                                        else:
##                                                xsol.append(round(b[0],3))
##                              elif ('Trigonometric' in crit) and (0<=round(b[0],3)<=2*np.pi) and (round(b[0],3) not in xsol):
##                                        if round(b[0],3) ==(-0.0):
##                                                xsol.append(0.0)
##                                        else:
##                                                xsol.append(round(b[0],3))
########################################################################################
## Type 1'
##               for j in range(1,len(x)-2,1):
##                        z=((eqn(x[j+1])-eqn(x[j]))*(eqn(x[j])-eqn(x[j-1])))/((x[j+1]-x[j])*(x[j]-x[j-1]))
##                        if (eqn(x[j+1]))*(eqn(x[j]))<=0 or z<0:
##                                 a.append((x[j]+x[j+1])/2)
                                                                    
##               for l in a:                                                           
##                              b=sp.fsolve(eqn,l)
##                              print(b[0])
##                              if  ('Trigonometric' not in crit) and (eqn(round(b[0],3))==0 or eqn(b[0])==0) and (round(b[0],3) not in xsol):
##                                        if round(b[0],3) ==(-0.0):
##                                                xsol.append(0.0)
##                                        else:
##                                                xsol.append(round(b[0],3))
##                              elif ('Trigonometric' in crit) and (0<=round(b[0],3)<=2*np.pi) and (round(b[0],3) not in xsol):
##                                        if round(b[0],3) ==(-0.0):
##                                                xsol.append(0.0)
##                                        else:
##                                                xsol.append(round(b[0],3))

        except:
             xsol.append("Invalid")
             crit.clear()
             crit.append("Invalid")
        
        





        

        
        





         
         
         

