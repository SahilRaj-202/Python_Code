# /write a program to evaluate a polynomial of one variable i.e,x if the value od x is 2

def Eval_Poly(P,X):
    sum=0
    for power in P:
        sum=sum+P[power]*X**power
    print('The Value of Polynomail after Evaluation:',sum)

P={0:-2,2:1,3:3}
Eval_Poly(P,2)