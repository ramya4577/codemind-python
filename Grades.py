a,b,c,d,e=map(int,input().split())
t=a+b+c+d+e
per=t/5
if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per>=70:
    print("Grade C")
elif per>=60:
    print("Grade D")
elif per>=40:
    print("Grade E")
else:
    print("Grade F")