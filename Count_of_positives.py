
def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    if len(arr) == 0 or arr == [0,0]:
        return []
    else:
        for values in arr:
            if values >0:
                positive +=1
            elif values <0:
                negative+=values
        return[positive,negative]


    # def count_positives_sum_negatives(arr):
    #     if not arr: return []
    #     pos = 0
    #     neg = 0
    #     for x in arr:
    #         if x > 0:
    #             pos += 1
    #         if x < 0:
    #             neg += x
    #     return [pos, neg]

   
    # def count_positives_sum_negatives(arr):
    #     pos = sum(1 for x in arr if x > 0)
    #     neg = sum(x for x in arr if x < 0)
    #     return [pos, neg] if len(arr) else []