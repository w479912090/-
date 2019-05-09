'''
    f(n)        Name
     1          Constant        常量
     logn       Logarithmic     对数
     n          Linear          线性
     nlogn      Log Linear      线性对数
     n^2        Quadratic       平方
     n^3        Cubic           立方
     2^n        Exponential     指数

     @增长速度
     2^n > n^3 > n^2 > nlogn > n > logn > 1
'''

#1
a = 5
b = 6
c = 10
#2
for i in range(n):
    for j in range(n):
        x = i * i
        y = i * j
        z = j * j
#3
for k in range(n):
    w = a * k + 45
    v = b * b
#4
d = 33
'''
第一个项是常数 3, 表示片段开始的三个赋值语句
第二项是 3n^2,因为由于嵌套迭代，有三个语句执行 n^2次。
第三项是 2n, 两个语句迭代 n 次
第四项是常数 1
最后得出 T(n)=3+3n^2+2n+1=3n^2+2n+4
我们可以看到 n^2项是显性的，因此这个代码段是 O(n^2)
'''