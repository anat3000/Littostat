a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open("3lettres.txt", "w")

for i1 in a:
    for i2 in a:
        for i3 in a:
            print(i1+i2+i3+"-", file=f, sep="", end="")

f.close()