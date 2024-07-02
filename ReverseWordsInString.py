import timeit

def reverseWords_method1(s: str) -> str:
    x = s.split()
    return " ".join(x[::-1])

def reverseWords_method2(s: str) -> str:
    return " ".join(s.split()[::-1])

def time_trial(method, s: str, number: int = 100000):
    timer = timeit.Timer(lambda: method(s))
    time_taken = timer.timeit(number=number)
    return time_taken / number

s = "the sky is  blue"

# Timing method 1
time1 = time_trial(reverseWords_method1, s)
print(f"Method 1 average time: {time1:.10f} seconds")

# Timing method 2
time2 = time_trial(reverseWords_method2, s)
print(f"Method 2 average time: {time2:.10f} seconds")
