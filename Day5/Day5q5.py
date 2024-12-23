# 5- Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam.

def check_palindrome(s):
    i,j=0,len(s)-1
    while(i<=j):
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            print("Not a palindrome")
            break
    if i>j:
        print("Palindrome")
s="adam"
check_palindrome(s)