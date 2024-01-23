import sys

def knapsack(v, w, n, W):
    if W == 0:
        return -sys.maxsize
    
    if n < 0 or W == 0:
        return 0
    
    include = v[n] + knapsack(v, w, n - 1, W - w[n])
    
    exclude = knapsack(v, w, n - 1, W)
    
    return max(include, exclude)


if __name__ == '__main__':
    v = [20, 5, 10, 40, 15, 25]
    w = [1, 2, 3, 8, 7, 4]

    W = 5
    
    print('Knapsack value is:', knapsack(v, w, len(v) - 1, W))

