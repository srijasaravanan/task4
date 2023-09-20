mark1=90
mark2=87
mark3=95
mark4=85
mark5=79
max_mark=100
if(mark1>mark2 and mark1>mark3 and mark1>mark4 and mark1>mark4 and mark1>mark5):
 max_mark=mark1
elif(mark2>mark3 and mark2>mark4 and mark2>mark5):
 max_mark=mark2
elif(mark3>mark4 and mark3>mark5):
 max_mark=mark3
elif(mark4>mark5):
 max_mark=mark4
else:
 max_mark=mark5
print("Maximum mark=",max_mark);

if(mark1<mark2 and mark1<mark3 and mark1<mark4 and mark1<mark4 and mark1<mark5):
 max_mark=mark1
elif(mark2<mark3 and mark2<mark4 and mark2<mark5):
 max_mark=mark2
elif(mark3<mark4 and mark3<mark5):
 max_mark=mark3
elif(mark4<mark5):
 max_mark=mark4
else:
 max_mark=mark5
print("Minimum mark=",max_mark);
