a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open("2lettres.txt", "w")
for i1 in a:
	for i2 in a:
		print(i1+i2+"-", file=f, sep="", end="")
f.close()