key = ["1", "2"]
test = ["1", "2"]
for word in test:
    if word in key:
        test.remove(word)
        print("移除非关键字" + word)
print(test)
print("-----我会分割线-------")
test1 = ["1","2"]
for word in test1:
    if word in key:
        print("移除非关键字" + word)
        word = ""
print(test1)
