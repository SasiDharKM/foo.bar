def recurse_find(h,q_element,adjustment):
    root = 2**h -1
    root_half = root // 2
    
    if (q_element == root_half + adjustment) or (q_element == root_half*2 + adjustment):
        return root + adjustment
    if q_element > root_half + adjustment:
        adjustment = adjustment + root_half
    
    return recurse_find(h-1, q_element, adjustment)
    
def answer(h, q):
    # your code here
    p = [None]*len(q)
    root = 2**h - 1
    
    for index, element in enumerate(q):
        if root == element:
            p[index] = -1
        else:
            p[index] = recurse_find(h,element,0)
    return p