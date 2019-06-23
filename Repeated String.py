
# Given a lowercase string of english alphabet. An integer n is given, find and print the number of a's in the first
# n letters of the given infinite string


string = input()
rep = int(input())

length = len(string)

repa = string.count("a")
even = rep%length

print(rep//length*repa + string[0:even].count("a"))