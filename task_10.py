result = []

def check_common_chars(x, y):
	x_word = x.lower()
	y_word = y.lower()
	if(x != '' and y != ''): 
	    for i in x_word: 
		    if(i in y_word): 
			    result.append(i) 
	else: 
	    for i in y_word: 
		    if(i in x_word): 
			    result.append(i)
		
	print(f"Common letters are: {', '.join(letter for letter in result)}")
check_common_chars('Ear', 'Dear')