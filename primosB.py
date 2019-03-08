x=0
a=int(input("Digite un numero"))
while a>0:
    x+=1
    print(x)
    if x%x==0 and x%1==0 and x%2!=0:
        print("SI es un numero primo")
    else:
        print("NO")
    if x==a:
        break
