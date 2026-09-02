
#if

a=int(input("enter age:"))
if a>18:
    print("vote")
#if-else

a=int(input("enter age:"))
if a>18:
    print("vote")
else:
    print("cant vote")


#last digit of the number
a=123
b=a%10
print(b)

#remove the last digit

a=123
b=a//10
print(b)

#check whether
#even or odd

a=int(input("enter a:"))
if a%2!=0:
    print("odd")
else:
    print("even")

a=int(input("enter a:"))
if a%2==0:
    print("even")
else:
    print("odd")

#check the username and the password

u=input("enter username:")
p=int(input("enter pass:"))
if u=="Livewire" and p== 123098:
    print("login")
else:
    print("unsuccessfull")
    
#3 and 5

a=int(input("enter a:"))
if a%3==0 and a%5==0:
    print("login")
else:
    print("unsuccessfull")
    
