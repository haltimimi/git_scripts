#!/bin/python 

def anti_vowel(text):
	text = "same"
    vowels = ['a','e','o','u','i'] 
    lst = []
    for v in vowels:
        for l in text:
        	if l.lower() != v:
        		lst.append(l)
        		continue

            if i.lower() == l:
            	x = ''
                lst.append(x)
                continue 
            elif i.lower() != l:
            	lst.append(i)
            	continue

    print ''.join(lst)

anti_vowel("WhAAts e sixup")