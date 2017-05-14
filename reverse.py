#!/bin/python3

def reverse(text) :
    charlist = []
    for i in range(1,len(text) + 1) :
        charlist.append(text[i * -1])
        print (charlist)
    return ''.join(charlist)


print (reverse("Python!"))
