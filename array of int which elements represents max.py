def jump(a):
    jump, currEnd, nextEnd = 0, 0, 0
    for i in range(len(a)-1):
        nextEnd = max(nextEnd, i + a[i])
        if currEnd == i:
            currEnd = nextEnd
            jump += 1
    return jump
