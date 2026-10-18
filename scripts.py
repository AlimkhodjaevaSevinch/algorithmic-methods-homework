# Birthday Cake Candles

def birthdayCakeCandles(candles):
    tallest = max(candles)
    num_tallest = candles.count(tallest)
    return num_tallest
    #return candles.count(max(candles))

# Kangaroo
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
            
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 -v2) >= 0:
        return "YES"
    else:
        return "NO"

  # Strange-advertising
  def viralAdvertising(n):
    shared = 5 
    total = 0
    
    for day in range(n):
        liked = shared // 2
        total = total + liked
        shared = liked * 3
    return total

# Recursive

def superDigit(n, k):
    digit_sum = 0 
    
    for digit in n:
        digit_sum += int(digit)
    digit_sum = digit_sum * k
    
    while digit_sum >= 10:
        new_sum = 0
        for digit in str(digit_sum):
            new_sum += int(digit)
        digit_sum = new_sum
        
    return digit_sum

# Insertion Sort - 1
def insertionSort1(n, arr):
    value = arr[n - 1]
    i = n - 2
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = value
    print(*arr)

# Insertion Sort - 2

def insertionSort2(n, arr):
    for i in range(1, n):
        value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = value
        print(*arr)
