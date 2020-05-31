hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
def computepay(h,r):
    if h > 40:
        pay = r* 40 + ((h - 40) * (1.5* r ))
        return pay
    else:
        pay = h * r
        return pay


p = computepay(h,r)
print("Pay",p)
