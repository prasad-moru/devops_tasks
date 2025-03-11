class ArrayIntersection:

    def find_intersection(self, array1, array2):
        if not array1 or not array2:
            return []
        
        result = []
        i = j = 0
        while i < len(array1) and j < len(array2):
            if i > 0 and array1[i] == array1[i-1]:
                i += 1
                continue
            
            if array1[i] < array2[j]:
                i += 1
            elif array1[i] > array2[j]:
                j += 1
            else:
                result.append(array1[i])
                i += 1
                j += 1
        
        return result
    
    def find_intersection_using_set(self, array1, array2):
        if not array1 or not array2:
            return []
        set1 = set(array1)
        intersection = set1.intersection(array2)
        
        return sorted(list(intersection))


def main():
    solution = ArrayIntersection()
    arr1 = [1, 2, 2, 3, 4, 5]
    arr2 = [2, 3, 3, 5, 6, 7]
    
    print("Input Arrays:")
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    
    result = solution.find_intersection(arr1, arr2)
    print(f"\nIntersection (Two-Pointer Method): {result}")
    
    result_set = solution.find_intersection_using_set(arr1, arr2)
    print(f"Intersection (HashSet Method): {result_set}")
    arr3 = [1, 3, 5, 7]
    arr4 = [2, 4, 6, 8]
    print("\nTest case with no intersection:")
    print(f"Array 1: {arr3}")
    print(f"Array 2: {arr4}")
    
    result2 = solution.find_intersection(arr3, arr4)
    print(f"Intersection: {result2}")


if __name__ == "__main__":
    main()