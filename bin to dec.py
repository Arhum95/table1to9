a=int(input("Enter a Binary number :"))
i=0
dec=0
while(a>0):
   rem=a%10
   a=int(a/10)
   n=2**i*rem
   dec=dec+n
   i=i+1
print("Decimal equivalent is :",dec)
