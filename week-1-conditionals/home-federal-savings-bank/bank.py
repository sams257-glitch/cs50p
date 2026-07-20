print("Greeting: ");
x = input().strip().lower();
if(x[0]=='h'):
    if(x[0:5]=='hello'):
        print("$0");
    else:
        print("$20");
else:
    print("$100");