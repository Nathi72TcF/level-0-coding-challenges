result = []

def check_common_chars(x, y):
    if(x != '' and y != ''): 
	    for i in x: 
		    if(i in y): 
			    result.append(i) 
    else: 
	    for i in y: 
		    if(i in x): 
			    result.append(i)

    print(f"Common letters are: {', '.join(letter for letter in result)}")
check_common_chars('house', 'computers')