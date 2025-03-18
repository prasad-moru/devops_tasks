class ArrayIntersection:
    def find(self, a, b):
        i, j, res = 0, 0, []
        while i < len(a) and j < len(b):
            if i and a[i] == a[i-1]: i += 1; continue
            if a[i] < b[j]: i += 1
            elif a[i] > b[j]: j += 1
            else: res.append(a[i]); i += 1; j += 1
        return res

    def find_set(self, a, b): return sorted(set(a) & set(b))

if __name__ == "__main__":
    s = ArrayIntersection()
    a1, a2 = [1,2,2,3,4,5], [2,3,3,5,6,7]
    print("Two-Pointer:", s.find(a1, a2))
    print("HashSet:", s.find_set(a1, a2))
    a3, a4 = [1,3,5,7], [2,4,6,8]
    print("No Intersection:", s.find(a3, a4))