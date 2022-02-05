from math import *
from sympy import *
import numpy
#from numpy.linalg import *

#Newton's Method
def Newton(x,fx,fxx,a):
    while fx.subs({x:a})!=0:
        if fxx.subs({x:a})!=0:
            if abs(fx.subs({x:a})/fxx.subs({x:a}))<0.1**5:
                break
            a=round(a-fx.subs({x:a})/fxx.subs({x:a}),10)
        else:
            print("fxx=0!")
            break
    return a

#fixed
def Fixed(func,sel,p0):
    iteration=1
    while abs(func(sel,p0)-p0)>=10**-2:
        print(iteration,p0)
        iteration+=1
        p0=func(sel,p0)
    print("out",p0)

#Newton Nonlinear System
def Newnosys():
    x1,x2,x3 = symbols('x1,x2,x3', real=True)

    #f1=3*x1-cos(x2*x3)-0.5
    #f2=4*x1**2-625*x2**2+2*x2-1
    #f3=e**(-x1*x2)+20*x3+(10*pi-3)/3
    f1=x1**2+x2-37
    f2=x1-x2**2-5
    f3=x1+x2+x3-3
    #f1=3*x1-cos(x2*x3)-0.5
    #f2=x1**2-81*(x2+0.1)**2+sin(x3)+1.06
    #f3=e**(-x1*x2)+20*x3+(10*pi-3)/3
    F=Matrix([[f1],[f2],[f3]])
    J=Matrix([[diff(i,j,1) for j in [x1,x2,x3]] for i in [f1,f2,f3]])
    print(J)
    y=-J.inv()*F
    #Y=solve(array(J),array(F))
    X1,X2,X3=0,0,0
    for i in range(10):
        tp1,tp2,tp3=X1,X2,X3
        assign={x1:tp1,x2:tp2,x3:tp3}
        X1=round(tp1+y[0].subs(assign),10)
        X2=round(tp2+y[1].subs(assign),10)
        X3=round(tp3+y[2].subs(assign),10)
        print(X1,X2,X3)
    print(X1,X2,X3)
    assign={x1:X1,x2:X2,x3:X3}
    print(round(f1.subs(assign)))
    print(round(f2.subs(assign)))
    print(round(f3.subs(assign)))

#Gradent Method
def Grad_Des():
    x1,x2,x3 = symbols('x1,x2,x3', real=True)

    #f1=15*x1+x2**2-4*x3-13
    #f2=x1**2+10*x2-x3-11
    #f3=x2**3-25*x3+22
    #f1=10*x1-2*x2**2+x2-2*x3-5
    #f2=8*x2**2+4*x3**2-9
    #f3=8*x2*x3+4
    f1=3*x1-cos(x2*x3)-0.5
    f2=x1**2-81*(x2+0.1)**2+sin(x3)+1.06
    f3=e**(-x1*x2)+20*x3+(10*pi-3)/3
    g=f1**2+f2**2+f3**2
    g1=diff(g,x1,1)
    g2=diff(g,x2,1)
    g3=diff(g,x3,1)
    X1,X2,X3=0.1,0.1,-0.1
    while 1:
        tp1,tp2,tp3=X1,X2,X3
        assign={x1:tp1,x2:tp2,x3:tp3}
        X1=round(tp1-1e-5*g1.subs(assign),10)
        X2=round(tp2-1e-5*g2.subs(assign),10)
        X3=round(tp3-1e-5*g3.subs(assign),10)
        assign={x1:X1,x2:X2,x3:X3}
        print(X1,X2,X3)
        print(g.subs({x1:X1,x2:X2,x3:X3}))
        if(g.subs(assign)**0.5<0.05):
            break
    print(X1,X2,X3)
    print(g.subs({x1:X1,x2:X2,x3:X3}))

#guassian_elimination
def findnozero(mat,i):
    for m in range(len(mat)):
        if i==-1:
            for n in range(len(mat)-1):
                if mat[m][n]!=0:
                    return 1
        else:
            if mat[m][i]!=0:
                return m
    return -1

def changeloc(mat,i,m):
    if m!=i:
        tmpline=mat[i]
        mat[i]=mat[m]
        mat[m]=tmpline

def guassian_elimination(x):
    if findnozero(x,-1)==-1:
        print("All zero!")
        return 0
    for i in range(len(x)-1):
        if x[i][i]==0:
            m=findnozero(x,i)
            if m==-1:
                print("No unique solution")
                return false
            changeloc(x,i,m)
        for m in range(i+1,len(x)):
            if x[m][i]!=0:
                for n in list(reversed(range(i,len(x[i])))):
                    x[m][n]-=x[i][n]*x[m][i]/x[i][i]
    return true

def findmax(mat,i):
    maxloc=0
    for m in range(len(mat)):
        if mat[m][i]>mat[maxloc][i]:
            maxloc=m
    return maxloc

def guassian_pivoting(x):
    for i in range(len(x)-1):
        maxloc=findmax(x,i)
        changeloc(x,i,maxloc)
        if x[i][i]==0:
            print("No unique solution")
            return flase
        for m in range(i+1,len(x)):
            if x[m][i]!=0:
                for n in list(reversed(range(i,len(x[i])))):
                    x[m][n]-=x[i][n]*x[m][i]/x[i][i]
    return true

def solve_gausselm(x):
    answer=[]
    for i in list(reversed(range(len(x)))):
        result=x[i][len(x[i])-1]
        for j in range(len(x[i])-2-i):
            result-=answer[j]*x[i][i+j+1]
        answer=[result/x[i][i]]+answer
    return answer

#Jacob Interation
def Jac_Ite(A,B):
    for i in range(A.shape[0]):
        B[i]/=A[i,i]
        for j in list(reversed(range(A.shape[0]))):
            if j!=i:
                A[i,j]/=A[i,i]
        A[i,i]=1
    D=Matrix([[0 for i in range(i)]+[A[i,i]]+[0 for i in range(i+1,A.shape[1])] for i in range(A.shape[0])])
    L=Matrix([[0 for j in range(i+1)]+[A[i,j] for j in range(i+1,A.shape[1])] for i in range(A.shape[0])])
    U=Matrix([[A[i,j] for j in range(i)]+[0 for j in range(i,A.shape[1])] for i in range(A.shape[0])])
    answer=[0]*A.shape[0]
    while 1:
        answer=-D.inv()*(L+U)*Matrix([[answer[i]] for i in range(A.shape[0])])+D.inv()*B
        for j in range(A.shape[0]):
            print(round(answer[j],10),end=' ')
        print()
        if max(abs(B[m]-(A*Matrix([[answer[i]] for i in range(A.shape[0])]))[m]) for m in range(A.shape[0]))<0.001:
            break

#Guass_Seidel Interation
def Guass_Seidel(A,B):
    for i in range(A.shape[0]):
        B[i]/=A[i,i]
        for j in list(reversed(range(A.shape[0]))):
            if j!=i:
                A[i,j]/=A[i,i]
        A[i,i]=1
    D=Matrix([[0 for i in range(i)]+[A[i,i]]+[0 for i in range(i+1,A.shape[1])] for i in range(A.shape[0])])
    L=Matrix([[0 for j in range(i+1)]+[A[i,j] for j in range(i+1,A.shape[1])] for i in range(A.shape[0])])
    U=Matrix([[A[i,j] for j in range(i)]+[0 for j in range(i,A.shape[1])] for i in range(A.shape[0])])
    answer=[0]*A.shape[0]
    while 1:
        for i in range(A.shape[0]):
            answer[i]=(-D.inv()*(L+U)*Matrix([[answer[i]] for i in range(A.shape[0])])+D.inv()*B)[i]
        for j in range(A.shape[0]):
            print(round(answer[j],10),end=' ')
        print()
        if max(abs(B[m]-(A*Matrix([[answer[i]] for i in range(A.shape[0])]))[m]) for m in range(A.shape[0]))<0.001:
            break

#power_method Interation
def power_method(A,sx):
    for i in range(20):
        for i in range(A.shape[0]):
            if sx[i]!=0:
                print(round((A*sx)[i]/sx[i],10))
                break
        sx=A*sx

#Taylor Polynomial
def Taylor():
    x=symbols("x",real=True)
    f=e**x
    center=0
    df=0
    cal=1
    for i in range(1,10):
        cal=cal*i
        df=df+diff(f,x,i).subs({x:center})*(x-center)**i/cal
    print(df)

#Neville's Method
def Nevilles():
    sample=[1,2,3,4,6]

def Lag_Inter_Poly():
    pass

#Bisection
def Bisection(x,func,start,end):
    while (end-start)/2>=10**-10 and func.subs({x:(start+end)/2})!=0:
        if func.subs({x:(start+end)/2})*func.subs({x:start})>0:
            start=(start+end)/2
        elif func.subs({x:(start+end)/2})*func.subs({x:start})<0:
            end=(start+end)/2
    return (start+end)/2

def lagr_Inter_poly():
    x=symbols("x",real=true)
    origin=e**(2*x)*cos(3*x)
    f=50/9*(x-0.3)*(x-0.6)-100/9*e**0.6*cos(0.9)*x*(x-0.6)+50/9*e**1.2*cos(1.8)*x*(x-0.3)
    f=simplify(f)
    for i in range(101):
        if  diff(f-origin,x,1).subs({x:0.6*i/100})*diff(f-origin,x,1).subs({x:0.6*(i+1)/100})<0:
            zeropoint=Bisection(x,diff(f-origin,x,1),0.6*i/100,0.6*(i+1)/100)
            print(zeropoint,end=' ')
            print(round(diff(f-origin,x,1).subs({x:zeropoint}),10),end=' ')
            print(round((f-origin).subs({x:zeropoint}),10))
'''
    x=symbols("x",real=true)
    origin=sin(ln(x))
    f=sin(ln(2.0))*(x-2.4)*(x-2.6)/0.4/0.6-sin(ln(2.4))*(x-2.0)*(x-2.6)/0.4/0.2+sin(ln(2.6))*(x-2.0)*(x-2.4)/0.6/0.2
    f=simplify(f)
    for i in range(200,261):
        if  diff(f-origin,x,1).subs({x:i/100})*diff(f-origin,x,1).subs({x:(i+1)/100})<0:
            zeropoint=Bisection(x,diff(f-origin,x,1),i/100,(i+1)/100)
            print(zeropoint,end=' ')
            print(round(diff(f-origin,x,1).subs({x:zeropoint}),10),end=' ')
            print(round((f-origin).subs({x:zeropoint}),10))
'''

def Romberg_Method(fun,x,start,end,R1,R2):
    if R2==1:
        result=0
        for i in range(0,2**(R1-1)):
            result+=(end-start)/2**R1*(fun.subs({x:start+(end-start)*i/2**(R1-1)})+fun.subs({x:start+(end-start)*(i+1)/2**(R1-1)}))
        return result
    else:
        return Romberg_Method(fun,x,start,end,R1,R2-1)+1/(4**(R2-1)-1)*(Romberg_Method(fun,x,start,end,R1,R2-1)-Romberg_Method(fun,x,start,end,R1-1,R2-1))

def Euler_method(fun,x,yf,yl,start,end,step):
    for i in range(int((end-start)/step)):
        yl=yl+step*(fun.subs({x:start+i*step,yf:yl}))
    print(yl)

def pade():
    A=Matrix([[diff(f,x,i+j+1).subs({x:0})/factorial(i+j+1) for j in range(6)] for i in range(6)])
    B=Matrix([[-diff(f,x,7+i).subs({x:0})/factorial(i+7)] for i in range(6)])
    q=A.inv()*B
    p=[diff(f,x,j).subs({x:0})/factorial(j)+sum([q[6-j+i,0]*diff(f,x,i).subs({x:0})/factorial(i) for i in range(0,j)]) for j in range(7)]
    for i in range(6):
        print(p[i],end=' ')
    print("\n1",end=' ')
    for i in range(6):
        print(q[5-i,0],end=' ')


if __name__=='__main__':
    x=symbols("x",real=true)
    f1=(x-2363/18183*x**3+12671/4363920*x**5)/(1+445/12122*x**2+601/872784*x**4+121/16662240*x**6)
    f2=x-x**3/6+x**5/120-x**7/5040+x**9/362880-x**11/39916800
    for i in range(100):
        print(round((f1-f2).subs({x:i/100*}),10))
    pass
