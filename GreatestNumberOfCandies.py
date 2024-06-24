def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)  # Calculate the maximum number of candies once
        return [candy + extraCandies >= max_candies for candy in candies]

kidsWithCandies("",[2,3,5,1,3],3)