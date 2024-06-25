import timeit

class Flowerbed:
    def canPlaceFlowers_v1(self, flowerbed: list[int], n: int) -> bool:
        newPlants = 0
        le = len(flowerbed)
        i = 0
        while i < le:
            if flowerbed[i] == 0:
                lEmpty = i == 0 or flowerbed[i - 1] == 0
                fEmpty = i + 1 == le or flowerbed[i + 1] == 0

                if lEmpty and fEmpty:
                    newPlants += 1
                    i += 1
                if newPlants >= n:
                    return True
            i += 1
        return False

    def canPlaceFlowers_v2(self, flowerbed: list[int], n: int) -> bool:
        newPlants = 0
        last = 0
        lP = 0
        for i in flowerbed:
            if lP == 1:
                if i == 0:
                    newPlants += 1
                lP = 0
            elif last == 0 and i == 0:
                lP = 1
            last = i
        if lP == 1:
            newPlants += 1
        return newPlants >= n

    def canPlaceFlowers_v3(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)

        # Handle edge cases for the first and last elements
        if length == 1:
            return flowerbed[0] == 0 and n <= 1

        # Plant at the first position if possible
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        # Plant at the last position if possible
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

        if n <= 0:
            return True

        # Check for three consecutive zeros in the middle of the array
        for i in range(1, length - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

                if n <= 0:
                    return True

        return n <= 0

    def canPlaceFlowers_combined(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)
        newPlants = 0

        # Loop through the flowerbed
        i = 0
        while i < length:
            if flowerbed[i] == 0:
                # Check if the previous plot is empty or it is the first plot
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the next plot is empty or it is the last plot
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Plant a flower here for logical purposes
                    newPlants += 1
                    if newPlants >= n:
                        return True
                    i += 1  # Skip the next spot to avoid adjacent planting
            i += 1

        return newPlants >= n

# Create a large test dataset
large_flowerbed = [0, 1] * 5000 + [0] * 10000  # Large flowerbed with 15000 plots
n = 5000  # Number of flowers to plant

# Test the functions with timeit
flowerbed_instance = Flowerbed()

def test_v1():
    return flowerbed_instance.canPlaceFlowers_v1(large_flowerbed.copy(), n)

def test_v2():
    return flowerbed_instance.canPlaceFlowers_v2(large_flowerbed.copy(), n)

def test_v3():
    return flowerbed_instance.canPlaceFlowers_v3(large_flowerbed.copy(), n)

def test_combined():
    return flowerbed_instance.canPlaceFlowers_combined(large_flowerbed.copy(), n)

# Measure the execution time
time_v1 = timeit.timeit(test_v1, number=10)
time_v2 = timeit.timeit(test_v2, number=10)
time_v3 = timeit.timeit(test_v3, number=10)
time_combined = timeit.timeit(test_combined, number=10)

print(f"v1 execution time: {time_v1} seconds")
print(f"v2 execution time: {time_v2} seconds")
print(f"v3 execution time: {time_v3} seconds")
print(f"Combined execution time: {time_combined} seconds")
