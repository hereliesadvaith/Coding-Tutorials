# sorted list
numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
# number to find
query = 15


class BinarySearch:
    def __init__(self, numbers, query) -> None:
        self.numbers = numbers
        self.query = query

    # if there's more than one 15 we need to find the smallest index
    def location(self, mid):
        if self.numbers[mid] == self.query:
            if mid - 1 >= 0 and self.numbers[mid - 1] == self.query:
                return "left"
            else:
                return "found"
        elif self.numbers[mid] < self.query:
            return "right"
        else:
            return "left"

    def locate_index(self):
        lo, hi = 0, len(self.numbers) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            print(mid)
            result = self.location(mid)
            if result == "found":
                return mid
            elif result == "left":
                hi = mid - 1
            elif result == "right":
                lo = mid + 1
        return -1


q1 = BinarySearch(numbers, query)
print(q1.locate_index())
