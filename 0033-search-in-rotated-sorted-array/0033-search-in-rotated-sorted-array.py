class Solution:
    def search(self, arr, key):
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # If key found, return the index
            if arr[mid] == key:
                return mid

            # If Left half is sorted
            if arr[mid] >= arr[lo]:

                # If the key lies within this sorted half,
                # move the hi pointer to mid - 1
                if key >= arr[lo] and key < arr[mid]:
                    hi = mid - 1

                # Otherwise, move the lo pointer
                else:
                    lo = mid + 1

            # If Right half is sorted
            else:

                # If key lies within this sorted half
                if key > arr[mid] and key <= arr[hi]:
                    lo = mid + 1

                # Otherwise, move the hi pointer
                else:
                    hi = mid - 1

        return -1
        