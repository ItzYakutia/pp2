def solve(numheads, numlegs):
    chickk = 0
    rabbitk = 0
    for chickk in range(numheads + 1):
        rabbitk = numheads - chickk
        total_legs = (chickk * 2) + (rabbitk * 4)
        if total_legs == numlegs:
            return chickk, rabbitk
    return None, None
chickens, rabbits = solve(35, 94)
if chickens is not None and rabbits is not None:
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution")
