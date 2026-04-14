number1=float(input("enter first number"))
number2=float(input("enter second number"))
operation=input("enter the operation you wantt to perform(+,-,/,*,%,//,**)")
dict={"+":number1+number2,"-":number1-number2,"/":number1/number2,"*":number1*number2,"%":number1%number2,"//":number1//number2,"**":number1**number2}
print("result: ",(dict.get(operation)))
