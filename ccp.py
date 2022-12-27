#新バージョン
#参考：食玩問題　http://aquarius10.cse.kyutech.ac.jp/~otabe/shokugan/
from math import log
import matplotlib.pyplot as plt
import numpy as np
N = 28 #おまけの種類
L = 300 #試行回数
UnitCost = 120 #単価
Tax = 1.1 #消費税
Data = np.full((N+1,N+1,L+1),-1.0)
def f(n,m,l):
    if Data[n,m,l] >= 0:
        return Data[n,m,l]
    if n - m > l:
        return 0
    if n== m:
        return 1
    Data[n,m,l] = f(n,m+1,l-1)*(n-m)/n+f(n,m,l-1)*m/n
    return Data[n,m,l]
def H(n):
    #コピペ：調和級数を計算するPythonプログラム　https://python5.com/q/jsmpamdk
    gamma = 0.57721566490153286060651209008240243104215933593992
    return gamma + log(n) + 0.5/n - 1./(12*n**2) + 1./(120*n**4)
print("期待値\t"+chr(165)+"{:,.2f}".format(N*H(N)*UnitCost*Tax))
for l in range(1,L):
    plt.plot(l*UnitCost*Tax,f(N,0,l),marker=".",color="red")
plt.vlines(N*H(N)*UnitCost*Tax, 0, 1, "blue") 
plt.show()
for l in range(2,L):
    plt.plot(l*UnitCost*Tax,f(N,0,l)-f(N,0,l-1),marker=".",color="red")
plt.show()
