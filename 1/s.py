import sys
with open(sys.argv[1],'r') as f:
 l = [a.split() for a in f.read().splitlines()]
 [print(a[0] if a[0][0] > a[1][0] else a[1]) for a in l]	
