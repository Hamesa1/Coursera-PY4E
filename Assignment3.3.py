s = input("Enter Score: ")
score = float(s)
try:
	if score >= 0.0 and <= 1.0 :
		if score >= .9:
    		print(A)
    	if score >= .8 :
    		print(B)
		if score >= .7 :
    		print(C)
    	if score >= .6 :
    		print(D)
    	if score < .6 :
    		print(F)
except:
    print("Please enter a number between 0.0 and 1.0")
