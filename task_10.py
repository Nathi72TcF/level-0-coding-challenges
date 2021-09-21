x = str(input('Enter your words A: ' ))
y = str(input('Enter your words B: ' ))

result = []

def check_common_chars():
    if(x != '' and y != ''): 
	    for i in x: 
		    if(i in y): 
			    result.append(i) 
    else: 
	    for i in y: 
		    if(i in x): 
			    result.append(i) 
    print("Common letters are:", *result) 
check_common_chars()