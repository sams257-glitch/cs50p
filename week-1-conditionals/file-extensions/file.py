x=input("File Name: ");
if '.' in x:
    p1,p2=x.split('.');
    if(p2=='gif'or'jpg'or'txt'or'jpeg'or'png'or'pdf'or'zip'):
        print("image/"+p2);
else:
    print("application/octet-stream");