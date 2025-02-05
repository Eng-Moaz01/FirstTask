degree = int(input("enter your degree :-> "))


def g_degree (values):
    password=""
    for i in range(0,100) :
        password =password+ str(password.join(random.choices(values,k=1)))
    return password

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