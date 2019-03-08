a=int(input("Digite un numero"))
for i in range(1,a+1,1):
    print(i)
    x=a/i
    print(x)
    if i%i==0 and i%1==0 and i%2!=0:
        print("SI es un numero primo")
    else:
        print("NO")