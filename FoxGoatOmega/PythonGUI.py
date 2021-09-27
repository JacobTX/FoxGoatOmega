from guizero import *
import warnings
import datetime as dt

warnings.filterwarnings("ignore")

def rules():
        Rule=Window(UI,title="Guidelines",bg="gold",layout="grid")
        T1=Text(Rule,text="Format of entry:",size=18,font="Cambria",grid=[200,0,50,2])
        S1='''0) The following symbols must be used for the following operators/functions-

                a) Addition (+)
                b) Subtraction(-)
                c) Multiplication(*)
                d) Division(/)
                e) Exponentiation(**)
                f) Sine( sin() )
                g) Cosine( cos())
                h) Tangent ( tan())
                i) Natural Log( log() )
                j) Exponential( exp() )
                Ex- (x**2)+(3*x)+2 [correct] 
                (x^2)+(3x)+2  [incorrect]
                
             1) Only LHS of the equation must be written and all the constants must be present on LHS with 0 on RHS.
                Ex- To solve x**2+3*x+2=0 , enter x**2+3*x+2

             2) Do not input symbols of functions like square root.
                Ex- For square root, one must enter x**(0.5) not √x.

             3) For sin, cos, tan, log and exp , they can also be entered in the form of their respective numpy functions ( np.sin,np.cos , etc).
                Ex- sin(2*x+3) can be written as np.sin(2*x+3) as well.

             4) Only variable x must be used in the expression. Other symbols cannot be used as variables.
                Ex- x**2+3*x+2 is accepted but not y**2+3*y+2

                '''
        I1=Text(Rule,text=S1,font="Calibri",size=15,grid=[200,5,50,50])
        T2=Text(Rule,text="Common mistakes:",size=18,font="Cambria",grid=[400,0,50,2])
        S2='''0) Writing = in expression
                 Ex- x**2+3*x-2 [correct]
                     x**2+3*x=2 [incorrect]
                     
              1) Using ^ instead of **
                 Ex- x**2 [correct]
                     x^2 [incorrect]
                     
              2) Ignoring multiplication symbol
                 Ex - 3*x [correct]
                      3x [incorrect]
                      
              3) Not writing input of sin, cos,etc in brackets
                 Ex- log(x) [correct]
                     logx [incorrect]

              4)Using X or any other letter as variable
                Ex- x**2+3*x+2 [correct]
                    X**2+3*X+2 [incorrect]

              5)Writing square of trigonometric fucntions as **2(x)
                Ex- (sin(x))**2 [correct]
                    sin**2(x)[incorrect].

        '''
        I2=Text(Rule,text=S2,font="Calibri",size=15,grid=[400,5,50,50])

        def xit():
            c=Rule.yesno("Exit","Do you wish to exit?")
            if c==True:
                Rule.hide()
            else:
                Rule.show()
        Exit=PushButton(Rule,command=xit,text="Exit",grid=[300,200,5,5])
        
def REQS():
    from RevEqnSolver import reveqnsolver,xsol,crit
    from EqnPlot import eqnplot
    from EqnStore import eqnstore,D,DF,DFout
    REQS = Window(UI,title="RevEQS")
    Entertxt = Text(REQS,text="Enter equation in variable x")
    txt = TextBox(REQS,width=45)              #Text box to enter equation
    def findfn():
        def sendplot():
                rep=REQS.yesno("Graphical Solution","Do you wish to plot it?")
                if rep==True:
                       eqnplot(fx,xsol)
        def retcontr1():
                 RetButton.disable()
        def retcontr2():       
                RetButton.enable()
        def enable():
                StoreButton.enable()
        def txtdisable():
                txt.disable()
        fx=txt.value
        reveqnsolver(fx)
        calmsg=REQS.info("RevEQS","Calculating...")
        SollistTxt.value=str(xsol)
        CritlistTxt.value=str(crit)
        SolveButton.disable()
        SollistTxt.after(1,retcontr1)  #To prevent a human from crashing the app by pressing return when send plot message will be displayed"
        SollistTxt.after(1000,sendplot)
        SollistTxt.after(1500,retcontr2)
        SollistTxt.after(2000,txtdisable)
        SollistTxt.after(3000,enable)

    def reset():
        txt.clear()
        SollistTxt.clear()
        CritlistTxt.clear()
        txt.enable()
        SolveButton.enable()
        StoreButton.disable()
    def Return():
            c=REQS.yesno("Exit","Do you wish to exit?")
            if c==True:
                REQS.hide()
            else:
                REQS.show()
    def store():
            if SollistTxt.value==str(['Invalid']):
                    warnmsg=REQS.warn("Warning!!!","Invalid equations cannot be stored!!")
            else:
                    eqnstore(user,txt.value,xsol,crit)
            StoreButton.disable()
        
    SolTxt=Text(REQS,text="Solution set:")
    SollistTxt=Text(REQS)
    CritTest=Text(REQS,text="Class:")
    CritlistTxt=Text(REQS)
    SolveButton=PushButton(REQS,command=findfn,text="Solve")
    ResetButton=PushButton(REQS,command=reset,text="Reset")
    RetButton=PushButton(REQS,command=Return,text="Return")
    StoreButton = PushButton(REQS,command=store,text="Store in Directory")
    StoreButton.disable()


def EQP():
        from EqnPlot import eqnplot
        from RevEqnSolver import reveqnsolver,xsol,crit
        from EqnStore import eqnstore,D,DF,DFout
        EQP=Window(UI,title="EqnPlot")
        EnterTxt2 = Text(EQP,text="Enter equation to plot:")
        txt2=TextBox(EQP,width=45)
                
        def plot():
                fx2=txt2.value
                reveqnsolver(fx2)
                xsol2=xsol
                plotmsg=EQP.info("EqnPlot","Plotting...")
                eqnplot(fx2,xsol2)
                def enable2():
                        StoreButton2.enable()
                        ResetButton2.enable()
                def txtdisable2():
                        txt2.disable()
                PlotButton.disable()
                EnterTxt2.after(1000,txtdisable2)
                EnterTxt2.after(10,enable2)
        def reset2():
                txt2.clear()
                PlotButton.enable()
                txt2.enable()
                StoreButton2.disable()
        def Return():
            c=EQP.yesno("Exit","Do you wish to exit?")
            if c==True:
                EQP.hide()
            else:
                EQP.show()
        def store2():
                if xsol==['Invalid']:
                       warnmsg2=EQP.warn("Warning!!!","Invalid equations cannot be stored!!") 
                eqnstore(user,txt2.value,xsol,crit)
                StoreButton2.disable()
        PlotButton=PushButton(EQP,command=plot,text="Plot")
        ResetButton2=PushButton(EQP,command=reset2,text="Reset")
        Retbutton=PushButton(EQP,command=Return,text="Return")
        StoreButton2=PushButton(EQP,command=store2,text="Store in Directory")
        ResetButton2.disable()
        StoreButton2.disable()

def Logforth():
        if LogButton.text=="Logout":
                LogButton.text="Login"
                LoginTxt.value="Inactive"
                leavmsg=UI.info("Farewell","Thank you for using FGO !!!")
                REQSButton.disable()
                EQPButton.disable()
                EQDBButton.disable()
        elif LogButton.text=="Login":
                global user
                user=UI.question("Login","Enter User Name:")
                if user!="" and user is not None :
                        LogButton.text="Logout"
                        LoginTxt.value="Hello "+user
                        REQSButton.enable()
                        EQPButton.enable()
                        EQDBButton.enable()
def history():
        from EqnStore import eqnaccess,DFout
        import pandas as pd
        def showrows():
                nr=0
                nc=0
                try:
                        nr=int(RowBox.value)
                        nc=int(ColBox.value)
                except:
                        Warn0=arch.warn("Warning!!","Row/Column parameter invalid!!")
                u=tuple(user.split(','))
                s=EqnBox.value     #Creating a eqntuple with only one value out of string
                L=s.split(',')
                a='%'.join(L)
                b="%"+a+"%"
                c=tuple(b.split(','))
                eqn=c
                if InitDateBox.value=="":
                        InitDateBox.value="000-00-00"
                if FinDateBox.value=="":
                        FinDateBox.value=dt.datetime.now().strftime("%Y-%m-%d")
                if InitTimeBox.value=="":
                        InitTimeBox.value="00:00:00"
                if FinTimeBox.value=="":
                        FinTimeBox.value="24:00:00"
                        
                d=InitDateBox.value+","+FinDateBox.value
                t=InitTimeBox.value+","+FinTimeBox.value
                date=tuple(d.split(','))
                time=tuple(t.split(','))
                flist=[]
                if TrigCheck.value ==True:
                        flist.append("['Trigonometric']")
                if LogCheck.value ==True:
                        flist.append("['Logarithmic']")
                if ExpCheck.value == True:
                        flist.append("['Exponential']")
                if AlgebCheck.value == True:
                        flist.append("['Algebraic']")
                if MiscCheck.value == True:
                        flist.append("['Misc']")
                sol=SolBox.value
##                try:
##                        eqnaccess(u,tuple(flist),eqn,date,time,sol)
##                except:
##                         Warn1=arch.warn("Warning!!","Parameters invalid/incomplete!!")
                eqnaccess(u,tuple(flist),eqn,date,time,sol)
                        
                
                l=0
                while l<len((DFout.iloc[0:nr,0:nc]).columns): #Important to use iloc for column headings especially
                        DispBox=Text(arch,grid=[6+l,0],size=20,width="fill")  #flexible column headings
                        DispBox.value=((DFout.iloc[0:nr,0:nc]).columns[l])
                        l+=1 
                k=0
                while k<len((DFout.iloc[0:nr,0:nc]).index):
                        DispBox=Text(arch,grid=[5,1+k],size=20,width="fill")
                        DispBox.value=((DFout.iloc[0:nr,0:nc]).index[k]+1)
                        k+=1
                i=0
                while i<len((DFout.iloc[0:nr,0:nc]).columns):
                        j=0
                        while j<len((DFout.iloc[0:nr,0:nc]).index):
                                DispBox=Text(arch,grid=[6+i,1+j],size=15,width="fill") #flexible number of columns which DF cannot acheive
                                DispBox.value=((DFout.iloc[0:nr,0:nc]).iloc[j,i])
                                j+=1
                        i+=1
                RowBox.disable()
                ColBox.disable()
                EqnBox.disable()
                InitDateBox.disable()
                FinDateBox.disable()
                InitTimeBox.disable()
                FinTimeBox.disable()
                SolBox.disable()
        def clear():
                nr=0
                nc=0
                try:
                        nr=int(RowBox.value)
                        nc=int(ColBox.value)
                except:
                        Warn0=arch.warn("Warning!!","Row/Column parameter invalid!!")
                l=0
                while l<len((DFout.iloc[0:nr,0:nc]).columns): #Important to use iloc for column headings especially
                        DispBox=Text(arch,grid=[6+l,0],size=20,width="fill")  #flexible column headings
                        DispBox.value=("  "*len(str((DFout.iloc[0:nr,0:nc]).columns[l])))
                        l+=1 
                k=0
                while k<len((DFout.iloc[0:nr,0:nc]).index):
                        DispBox=Text(arch,grid=[5,1+k],size=20,width="fill") 
                        DispBox.value=("  "*len(str((DFout.iloc[0:nr,0:nc]).index[k]+1)))
                        k+=1
                i=0
                while i<len((DFout.iloc[0:nr,0:nc]).columns):
                        j=0
                        while j<len((DFout.iloc[0:nr,0:nc]).index):
                                DispBox=Text(arch,grid=[6+i,1+j],size=15,width="fill") #flexible number of columns which DF cannot acheive
                                DispBox.value=("  "*len(str((DFout.iloc[0:nr,0:nc]).iloc[j,i])))
                                j+=1
                        i+=1
                        
                RowBox.clear()
                ColBox.clear()
                EqnBox.clear()
                SolBox.clear()
                InitDateBox.clear()
                FinDateBox.clear()
                InitTimeBox.clear()
                FinTimeBox.clear()
                RowBox.enable()
                ColBox.enable()
                EqnBox.enable()
                SolBox.enable()
                InitDateBox.enable()
                FinDateBox.enable()
                InitTimeBox.enable()
                FinTimeBox.enable()
                TrigCheck.value=0
                LogCheck.value=0
                ExpCheck.value=0
                AlgebCheck.value=0
                MiscCheck.value=0
        def ret():
                y=arch.yesno("Exit","Do you wish to exit?")
                if y==True:
                        arch.hide()

        arch=Window(UI,title="Archive",layout="grid",bg="red")
        arch.show(wait=True)
        UserText=Text(arch,text="User: "+ user,grid=[0,0],size=20,font="Cambria",bg="gold")
        RowText=Text(arch,text="Enter number of rows (<=25)?",grid=[0,1])
        RowBox=TextBox(arch,text=25,grid=[0,2])
        RowBox.bg="white"
        ColText=Text(arch,text="Enter number of columns (<=6)?",grid=[0,3])
        ColBox=TextBox(arch,text=6,grid=[0,4])
        ColBox.bg="white"
        Functext=Text(arch,text="Function Class:",grid=[0,5])
        TrigCheck=CheckBox(arch,text="['Trigonometric']",grid=[0,6])
        LogCheck=CheckBox(arch,text="['Logarithmic']",grid=[0,7])
        ExpCheck=CheckBox(arch,text="['Exponential']",grid=[0,8])
        AlgebCheck=CheckBox(arch,text="['Algebraic']",grid=[0,9])
        MiscCheck=CheckBox(arch,text="['Misc']",grid=[0,10])
        EqnText=Text(arch,text="Equation Term(s)",grid=[0,11])
        EqnBox=TextBox(arch,grid=[1,11])
        EqnBox.bg="white"
        DateTimeText=Text(arch,text="Date and Time",grid=[0,12])
        InitDate=Text(arch,text="Initial Date (Year-Month-Date):",grid=[0,13])
        InitDateBox=TextBox(arch,grid=[1,13])
        InitDateBox.bg="white"
        FinDate=Text(arch,text="Final Date (Year-Month-Date):",grid=[0,14])
        FinDateBox=TextBox(arch,grid=[1,14])
        FinDateBox.bg="white"
        InitTime=Text(arch,text="Initial Time (Hour:Minutes:Seconds):",grid=[0,15])
        InitTimeBox=TextBox(arch,grid=[1,15])
        InitTimeBox.bg="white"
        FinTime=Text(arch,text="Final Time (Hour:Minutes:Seconds):",grid=[0,16])
        FinTimeBox=TextBox(arch,grid=[1,16])
        FinTimeBox.bg="white"
        SolText=Text(arch,text="Common Solution(s)",grid=[0,17])
        SolBox=TextBox(arch,grid=[1,17])
        SolBox.bg="white"
        ShowButton=PushButton(arch,command=showrows,text="Display",grid=[0,18])
        ClearButton=PushButton(arch,command=clear,text="Clear",grid=[0,19])
        RetButton=PushButton(arch,command=ret,text="Return",grid=[0,20])        
        
         
user=""
#Main UI
UI=App(title="FoxGoat Omega",layout="grid",bg="silver")
FoxGoatImg1=Picture(UI,image="NineTails.gif",grid=[500,10,5,5])
WelcBox=Box(UI,grid=[500,1,5,1],border=True)
Welctext=Text(WelcBox,text="FoxGoat Omega",grid=[400,20,500,500],color="red",font="Cambria",size=25)
ButtonBox=Box(UI,grid=[500,300,3,1],border=True)
AboutButton=PushButton(ButtonBox,command=rules,text="About FGO",grid=[300,3,1,1],width=20,height=2)
RulesButton=PushButton(ButtonBox,command=rules,text="Guidelines for users",grid=[300,3,1,1],width=20,height=2)
REQSButton=PushButton(ButtonBox,command=REQS,text="Solve equations",grid=[400,3,1,1],width=20,height=2)
EQPButton=PushButton(ButtonBox,command=EQP,text="Plot graphs",grid=[500,3,1,1],width=20,height=2)
EQDBButton=PushButton(ButtonBox,command=history,text="Usage History",grid=[600,3,1,1],width=20,height=2)
#Logforth
LogBox=Box(UI,grid=[600,1,5,1],border=True)
LogButton = PushButton(LogBox,command=Logforth,text="Login",grid=[500,300,1,1],width=20,height=2)
LoginTxt=Text(LogBox,grid=[400,300,1,1],width=20,height=2,bg="yellow")
REQSButton.disable()
EQPButton.disable()
EQDBButton.disable()

UI.display()
