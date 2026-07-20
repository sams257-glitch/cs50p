x,y,z=input("Expression: ").split(" ");
x,z=int(x),int(z);
if(y=='+'):
    print(x+z);
elif(y=='-'):
    print(x-z);
elif(y=='*'):
    print(x*z);
elif(y=='/'):
    print(f"{x/z:.2f}");
else:
    print(x%z);