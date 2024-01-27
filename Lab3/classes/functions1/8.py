def spy_game(nums):
    lisz = []
    liss = []
    for x in range(0, len(nums)):
        if nums[x] == 0:
            lisz.append(x)
        if nums[x] == 7:
            liss.append(x)
    if len(lisz) > 1 and len(liss) > 0:
        if liss[0] > lisz[0] and liss[0] > lisz[1]:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))