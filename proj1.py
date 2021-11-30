def  hamming_encode(x3,x5,x6 ,x7):
  x1= (x3+x5+x7) % 2
  x2= (x3+x6+x7) % 2
  x4= (x5+x6+x7) % 2
  return (x1 ,x2,x3 ,x4,x5,x6 ,x7)
def  hamming_decode(y1,y2,y3 ,y4,y5,y6 ,y7):
  b1= (y1+y3+y5+y7) % 2
  b2= (y2+y3+y6+y7) % 2
  b3= (y4+y5+y6+y7) % 2
  b=4*b3+2*b2+b1 # the  integer  value
  if b==0 or b==1 or b==2 or b==4:
    ls = [y3,y5,y6 ,y7]
    return ls
  else:
    y=[y1,y2 ,y3,y4,y5 ,y6,y7]
    y[b-1]=(y[b -1]+1) % 2   # correct  bit b
    ls = [y[2],y[4],y[5],y[6]]
    return (ls)
y = hamming_encode(1,1,0,1)
print(y)
recv = list(y)
recv[4] ^= 1
print(recv)
#recv[3] ^= 1
hamming_decode(*recv)
#y = hamming_encode(*x)
print(y)
recv = list(y)
print(recv)
recv[3] *= -1
print(recv)
#hamming_decode(*recv)
def  eu_encode(x3,x5,x6 ,x7):
  x1= (x3+x5+x7) % 3
  x2= (x3+x6+x7) % 3
  x4= (x5+x6+x7) % 3
  return (x1 ,x2,x3 ,x4,x5,x6 ,x7)
def bin2euc(x):
  for i in range(len(x)):
    if x[i] ==0:
      x[i] = -1
    else:
      x[i] = 1
  return x
x = [0,1,1,1]
print(len(x))
bin2euc(x)
import numpy as np
import random
noise = np.random.random(len(recv))
new_signal = recv + noise
print(new_signal)
def compare(new_signal):
  for i in range(len(new_signal)):
    if new_signal[i] > 0 :
      new_signal[i] = 1
    else:
      new_signal[i] = 0
  return new_signal
z = list(new_signal)
compare(z) 
print(type(z))
lis = hamming_decode(*z)
print(lis)
def conv(j):
  for i in range(len(j)):
    if j[i] == -1:
      j[i] =0
    else:
      j[i] =1
  return(j)
conv(lis)
import random
def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp    
    return(key1)
n = 4
str1 = rand_key(n)
print("Desired length random binary string is: ", str1)
from random import *
randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]
n_max = 0.01
import matplotlib.pyplot as plt
# Eu first HAmminh Second
tt = []
ft = [] 
ff = []
tf = []
while (n_max <1):
  a =0
  b =0
  c =0
  d =0
  for i in range(10000):
    bit = randBinList(4)
    org = bit
    ham = bit
    enc = list(hamming_encode(*bit))
    print(enc)
    y_hm = enc
    y_eu = bin2euc(enc)
    print(y_eu)
    recv_eu = list(y_eu)
    recv_hm = list(y_hm)
    noise = np.random.normal(0,n_max,len(recv_eu))
    new_eu = recv_eu + noise
    print(new_eu)
    new_hm = recv_hm + noise
    print(new_hm)
    z_eu = list(new_eu)
    z_hm = list(new_hm)
    eu = compare(z_eu)
    hm = compare_h(z_hm)
    lis_1 = hamming_decode(*eu)
    lis_2 = hamming_decode(*hm)
    if (lis_1==org) and (lis_2 == org) :
      c = c+1
    elif (lis_2 == org) and (lis_1 != org):
      a = a+1
    elif (lis_2 != org) and (lis_1 != org):
      b = b+1
    elif (lis_2!= org) and (lis_1 == org):
      d = d +1
  tt.append(c)
  ft.append(a)
  ff.append(b)
  tf.append(d)
  n_max = n_max + 0.01
n = np.linspace(0.01, 1, 100)
plt.plot(tt,'g',label=' euclidian and hamming true')
plt.plot(ft,'r',label=' euclidian false and hamming true')
plt.plot(ff,'b',label=' euclidian false and hamming false')
plt.plot(tf,'m',label=' euclidian true and hamming false')
leg = plt.legend();
def compare_h(new_signal):
  for i in range(len(new_signal)):
    if new_signal[i] > 0.5 :
      new_signal[i] = 1
    else:
      new_signal[i] = 0
  return new_signal
z = list(new_signal)
compare_h(z)
bit = randBinList(4)
print(bit)
org = bit
ham = bit
enc = list(hamming_encode(*bit))
print(enc)
y_hm = enc
y_eu = bin2euc(enc)
print(y_eu)
recv_eu = list(y_eu)
recv_hm = list(y_hm)
noise = np.random.random(len(recv_eu))
new_eu = recv_eu + noise
print(new_eu)
new_hm = recv_hm + noise
print(new_hm)
z_eu = list(new_eu)
z_hm = list(new_hm)
compare(z_eu)
compare_h(z_hm)
lis_1 = hamming_decode(*z_eu)
lis_2 = hamming_decode(*z_hm)
conv(lis_1)
print(lis_1)
print(lis_2)
