s=str(input("Introduceti un sir"))
s="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
s1=""
s2=s
s3=s
print("Sirul initial: ", s)
for k in s:
    a=chr(ord(k)+1)
    s1+=a
    b=s1.replace('!',' ')
    c=b.replace('[','A')
print("primul sir:",c)
for k in s2:
    e=s2.replace(('Z'),('A'))
print("al doilea sir:",e)
for k in s3:
    f=s3.replace((' '),('-'))
print("al treilea sir:",f)
