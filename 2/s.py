from decimal import *
getcontext().prec=999
while 1:a,b=input().split();print('{0:g}'.format(Decimal(a)/10**Decimal(b)))
