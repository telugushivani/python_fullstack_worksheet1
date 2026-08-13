numbers=[1,2,3,4,5,6,7,8,9,10]
Squares=[i*i for i in numbers]
Even_Numbers=list(filter(lambda numbers: numbers%2==0,numbers))
print("Squares:",Squares)
print("Even Numbers:",Even_Numbers)
