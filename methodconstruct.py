def pair(x,y):
    def get(index):
        if index == 0:
            return x
        else :
            return y
    return get

def select(p , index):
    return p(index)

p = pair(1,12)

print(select(p,0))