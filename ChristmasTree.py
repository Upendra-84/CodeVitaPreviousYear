n = int(input())
for i in range(n):
	print(" "*(n-i),"*"*(2*i - 1))
	print("\n")
for j in range(1,n):
	print(" "*(n-j),"*"*(2*j + 1))
	print("\n")
print(" "*7, "*")
print(" "*7,"*")