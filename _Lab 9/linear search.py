def linear_search(listy, x):
    for i in listy:
        if x==i:
            return listy.index(i)
    
    return -1

def test():
    print(linear_search([1,2,4,5],4))
test()
    
