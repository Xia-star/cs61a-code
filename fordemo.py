# p = [[1,2],[3,3],[6,7],[8,8],[4,4],[2,2]]
# same_count = 0
# for x,y in p:
#     if x == y :
#         same_count += 1
# print(same_count)
# print([[element1,element2]*2 for [element1,element2] in p if element1 == element2] )
# s = [1,2,3,4,5]
# print([x for x in s if 25 % x == 0])
# 
def divisor(n):
    return [1] + [x for x in range(2,n) if n % x == 0]
print(divisor(12))

print([x for x in range(1,100) if sum(divisor(x)) == x])

def apply_to_all(make_fun,s):
    return [make_fun(x) for x in s]
def keep_if(filter ,s):
    return [x for x in s if filter(x)]

def divisor2(n):
    filter = lambda x : n % x == 0
    return [1] + keep_if(filter,range(2,n))
print(divisor2(12))