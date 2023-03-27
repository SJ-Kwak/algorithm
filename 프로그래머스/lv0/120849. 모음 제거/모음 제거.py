def solution(my_string):
    vowel = ['a','e','i','o','u']
    for i in my_string:
        for j in vowel:
            my_string=my_string.replace(j,'')
    return my_string