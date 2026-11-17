class Solution:
    def search(self, arr, key):
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == key:
                return mid

            if arr[mid] >= arr[lo]:
                if key >= arr[lo] and key < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if key > arr[mid] and key <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
