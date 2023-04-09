import math

from cvxopt import matrix, solvers

Q = matrix([[0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 2.5, 0.0],
            [0.0, 0.0, 0.0, 5.0]])
p = matrix([1.0, 1.0, 1.0, 1.0])

G = matrix([
            [-1.0, 0.0, 0.0, 0.0],
            [0.0, -1.0, 0.0, 0.0],
            [0.0, 0.0, -1.0, 0.0],
            [0.0, 0.0, 0.0, -1.0]])
h = matrix([0.0, 0.0, 0.0, 0.0])

# sol = solvers.qp(Q, p, G, h, A, b)
def calcul():
    # for r in range(1,5):
    # r=float(input("r= ")
    za = 1000
    r=3
    A = matrix([[1.0,1.0],[1.0,2.0],[1.0,3.0],[1.0,4.0]])
    b = matrix([1.0,float(r)])
    print(r)
    sol = solvers.qp(Q, p, G, h, A, b)
    print(sol['x'], sol['relative gap'], ' ', sol['gap'])
    otkl_right=math.sqrt(sol['x'][0]**2*0+(sol['x'][1]**2+sol['x'][2]**2*2.5+sol['x'][3]**2*5))
    R_t= 100*math.fabs(1-otkl_right)
    print(otkl_right,R_t,type(sol['x'][3]),type(sum))
calcul()

