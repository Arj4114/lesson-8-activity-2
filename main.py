print("enter a number (numerator): ")
numn = int(input())
print("enter a number (denominator): ")
numd = int(input())
if numn%numd ==0:
    print("\n" +str(numn)+ "is divisivle by " + str(numd))
else:
    print("\n" +str(numn)+ "is not divisivle by " + str(numd))