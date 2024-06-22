if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    order = list(arr)
    order.sort(reverse=True)
    
    for i in range(1, n):
        if order[i] == order[0]:
            continue
        else:
            print(order[i])
            break