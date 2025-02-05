isRun=True

while isRun:
    degree = int(input("enter your degree for exit enter -1 :-> "))

    if degree == -1:
        isRun=False
        break


    if 100 >= degree >= 85:
        print("Excellent")
    elif 85 > degree >= 75:
        print("VEry Good")
    elif 75 > degree >= 65:
        print("good")
    elif 65 > degree >= 50:
        print("acceptable")
    else:
        print("fail")