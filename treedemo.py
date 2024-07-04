def tree(rootlabel ,branches=[]):
    for branch in branches:
        assert is_tree(branch) ,"branch must be tree"
    return [rootlabel] + list(branches)

def label(tree) :
    return tree[0]

def branches(tree) :
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree) :
        if  not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

print(tree(1,[[1],[2],[3,[4],[5]]]))
b = tree(0,[tree(1),tree(2,[tree(4),tree(5)]),tree(3)])
print(b)
print(is_leaf(branches(b)[0]))
print(is_leaf(branches(b)[1]))
print(is_leaf(branches(b)[2]))
print(branches(b)[1])

# print(is_tree(a))
print(is_leaf(branches(branches(b)[1])[0]))
print(is_leaf(branches(branches(b)[1])[1]))

def fib_tree(n):
    if n == 0 or n ==1:
        return tree(n)
    else:
        left,right = fib_tree(n-2),fib_tree(n-1)
        fib_tree_label = label(left) + label(right)
        return tree(fib_tree_label,[left,right])

def count_leaves(tree):
    if is_leaf(tree):
       return 1
    else :
        branches_count = [count_leaves(b) for b in branches(tree)]
        return sum(branches_count)
       
    
print(fib_tree(5))