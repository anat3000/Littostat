f = open("2lettres.py")
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i1 in a:
	for i2 in a:
		print(i1+i2+"-", end="", file=f)
