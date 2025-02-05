degree = int(input("enter your degree :-> "))


def g_degree (values):
    degree=""
    for i in range(0,100) :
        degree =degree + str(degree.join(random.choices(values,k=1)))
    return degree

if(degree<=100 and degree >=85):
    print("Excellent")
elif(degree<85 and degree>= 75):
    print("VEry Good")
elif(degree<75 and degree >= 65):
    print("good")
elif(degree<65 and degree>=50):
    print("acceptable")
else :
    print("fail")       