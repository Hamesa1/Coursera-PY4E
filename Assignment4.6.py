def computepay(h, r):
    return (h*r)
def computeovertimepay(h, r):
    reg = 40*r
    overtime = (h-40)*1.5*r
    return(reg+overtime)
h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
if h <= 40:
   p = computepay(h, r)
else:
    p = computeovertimepay(h, r)
print("Pay", p)
