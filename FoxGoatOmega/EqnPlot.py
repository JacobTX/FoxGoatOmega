import numpy as np
import matplotlib.pyplot as plt


def eqnplot(fx2,xsol):
   x=np.arange(-100,100,0.001)
   fpro2=""
   np.seterr(divide='ignore',invalid='ignore')

   k=0
   while k < len(fx2):
       
       if fx2[k:k+3]=="sin" and fx2[k-3:k]!="np.":
           fpro2 += "np.sin"
           k=k+3
       elif fx2[k:k+3]=="cos" and fx2[k-3:k]!="np.":
           fpro2 += "np.cos"
           k=k+3
       elif fx2[k:k+3]=="tan" and fx2[k-3:k]!="np.":
           fpro2 += "np.tan"
           k=k+3
       elif fx2[k:k+3]=="log" and fx2[k-3:k]!="np.":
           fpro2 += "np.log"
           k=k+3
       elif fx2[k:k+3]=="exp" and fx2[k-3:k]!="np.":
           fpro2 += "np.exp"
           k=k+3
       else:
           fpro2 += fx2[k:k+1]
           k=k+1

      
   try:       
         plt.plot(x,eval(fpro2))
         plt.plot(x,np.zeros(len(x)),color="green")
         plt.plot(np.zeros(len(x)),x,color="green")
         plt.xlabel("x")
         plt.ylabel("f(x)")
         if xsol!=[]:
              plt.axis([xsol[0]-1,xsol[-1]+1,-10,10])
              plt.scatter(xsol,[0]*len(xsol),marker="o",color="red")
              plt.title("Solution(s) found")
         else:
              plt.xlim([-10,10])
              plt.title("No solutions found")
         plt.show()
         
   except:
         plt.title("No graph available.")
         plt.show()


     
