def binary_search(arr, x):
        down = 0
        high = len(arr) - 1
        mid = 0

        while down <= high:

            mid = (high + down) // 2

            # If x is greater, ignore left half
            if arr[mid] < x:
                down = mid + 1

            # If x is smaller, ignore right half
            elif arr[mid] > x:
                high = mid - 1

            # means x is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
        return -1
