def retUniq(lis):
    dic = []
    for x in lis:
        if lis.count(x) == 1:
            dic.append(x)
    return dic
            
car = ["some", "text", "with", "strings", "some"]
print(retUniq(car))