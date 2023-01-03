class BinarySearch:
    def search_iterative(self, arr, x):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return None
