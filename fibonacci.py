"""
fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
user input
0: invalid input
1:[0]
2:[0, 1]
3:[0, 1, 1]
4:[0, 1, 1, 2]
5:[0, 1, 1, 2, 3]
10:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""

def get_fibonacci_series(num):
    if not isinstance(num, int):
        print("Invalid input type")
        return False

    if num <= 0:
        return False
    fibonacci_series = [0, 1]

    if num == 1:
        return [0]
    
    for i in range(num - 2):
        next_item = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_item)
    
    return fibonacci_series
#commit pawan