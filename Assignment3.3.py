s = input("Enter Score: ")
score = float(s)
if score >= .9:
    print("A")
elif score >= .8:
    print("B")
elif score >= .7:
    print("C")
elif score >= .6:
    print("D")
elif score < .6 and score >= 0:
    print("F")
else:
    print("Please enter a number between 0.0 and 1.0")
# Instead of using the try and except blocks, I used the if, elif, and else functions. The only drawback is that number greater than 1 will result in an and not in the 
#error message
