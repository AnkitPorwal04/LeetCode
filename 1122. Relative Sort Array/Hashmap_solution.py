class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Create a dictionary to count the frequency of each element in arr1
        count = {}
        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Create the result array following the order in arr2
        result = []
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]  # Remove the element from the count dictionary once processed
        
        # Sort the remaining elements that are not in arr2 and add them to the result
        remaining = sorted([num for num in count for _ in range(count[num])])
        result.extend(remaining)
        
        return result
