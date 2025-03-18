class EvenFib:
    def __init__(self): self.a, self.b, self.s, self.c = 2, 8, 2, 1
    def next(self): self.a, self.b, self.s, self.c = self.b, 4*self.b+self.a, self.s+self.a, self.c+1; return self.a
    def sum(self, n): [self.next() for _ in range(n-1)]; return self.s

if __name__ == "__main__":
    e = EvenFib()
    print(f"Sum of first 100 even Fibonacci numbers: {e.sum(100)}")
    print("\nFirst 10 even Fibonacci numbers:", 2, *[EvenFib().next() for _ in range(9)])