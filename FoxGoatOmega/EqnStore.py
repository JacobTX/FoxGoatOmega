import pandas as pd
import datetime as dt
import mysql.connector as sqltor


D={"User":[],"Equation":[],"Function_Class":[],"Solution_Set":[],"Date_Instant":[],"Time_Instant":[]}  #DataFrame to store equations
DF=pd.DataFrame(D)
##Dout={"User":[],"Equation":[],"Function_Class":[],"Solution_Set":[],"Date_Instant":[],"Time_Instant":[]}
Dout={}
DFout=pd.DataFrame(Dout)

D2={"User":[],"Equation":[],"Function_Class":[],"Solution_Set":[],"Date_Instant":[],"Time_Instant":[]} 
DF2=pd.DataFrame(D2)

def eqnstore(userid,fx,xsol,crit):
            if xsol!=['Invalid']:
                c=len(DF.index)
                DF.loc[c,:]=[userid,fx,str(crit),str(xsol),(dt.datetime.now().strftime("%Y-%m-%d")),(dt.datetime.now().strftime("%H:%M:%S"))]

               
                
            mydb=sqltor.connect(  #connection object
                host="localhost",
                user="root",
                passwd="NateSaber4669",
                database="FoxGoatOmega",
                )

            cursor=mydb.cursor()  #cursor instance

            if c is not None:
                L=tuple(DF.loc[c,:])
                s="INSERT INTO EqnStore (User,Equation,Function_Class,Solution_Set,Date_Instant,Time_Instant) VALUES (%s,%s,%s,%s,%s,%s);"
                cursor.execute(s,L)

                mydb.commit()

def eqnaccess(user,flist,eqn,date,time,sol):
            DF2.drop(DF2.index,inplace=True)
            DFout.drop(DFout.index,inplace=True)
            mydb=sqltor.connect(  #connection object
                host="localhost",
                user="root",
                passwd="NateSaber4669",
                database="FoxGoatOmega",
                )

            cursor=mydb.cursor()  #cursor instance
            
            t_flist=','.join(["%s"]*len(flist)) #Creating flist tuple 
            flistcond=" AND Function_Class IN (" + t_flist + ") "
            eqncond=" AND Equation LIKE %s "
            
            datecond=" AND Date_Instant BETWEEN %s AND %s "
            timecond=" AND Time_Instant BETWEEN %s AND %s "
            p=sol.split(',')
            print(p)
            
            

            s="SELECT User,Equation,Function_Class,Solution_Set,Date_Instant,Time_Instant FROM EqnStore WHERE User IN (%s) " + flistcond + eqncond + datecond + timecond
            T=user + flist + eqn + date + time
            print(T)
            cursor.execute(s,T)

            data=cursor.fetchall()

            Lcol=["User","Equation","Function_Class","Solution_Set","Date_Instant","Time_Instant"]
            
            q=0
            for i in data:
                DF2.loc[q,:]=list(i)
                q+=1
            print(DF2)

            k=0
            for (r,rseries) in DF2.iterrows():
                for solcond in p:
                        if solcond in rseries['Solution_Set']:
                                a=0
                                while a<6:
                                    if (DFout==rseries).any(1).any() is True:
                                        print("Hi")
                                    else:
                                        DFout.loc[k,Lcol[a]]=str(rseries[a])
                                    a+=1
                k+=1
            

            mydb.close()



                

            

            
                
            
