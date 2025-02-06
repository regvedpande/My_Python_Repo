def findIntersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # Convert the first list to a set for O(1) lookup
    set1 = set(nums1)
    # Create result list to store intersection
    result = []
    
    # Check each element from nums2
    for num in nums2:
        # If number exists in set1 and not already in result
        if num in set1 and num not in result:
            result.append(num)
    
    return result

# Test the function
if __name__ == "__main__":
    # Example test cases
    array1 = [1, 2, 2, 1]
    array2 = [2, 2]
    print(f"Intersection of {array1} and {array2}:", findIntersection(array1, array2))
    
    array3 = [4, 9, 5]
    array4 = [9, 4, 9, 8, 4]
    print(f"Intersection of {array3} and {array4}:", findIntersection(array3, array4))