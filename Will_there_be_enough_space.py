def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    else:
        return (abs(cap - (on + wait)))


# def enough(cap, on, wait):
#     return max(0, wait - (cap - on))





