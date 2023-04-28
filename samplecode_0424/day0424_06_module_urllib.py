from urllib import request
import bs4 as bs

target = request.urlopen("https://google.com")
print(target)
print("-----------------------------------------------------")
output = target.read()

print(output)