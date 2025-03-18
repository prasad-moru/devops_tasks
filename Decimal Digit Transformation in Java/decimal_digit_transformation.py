class DigitTransformer:
    def transform(self, d, r=4):
        if not (0 <= d <= 9): raise ValueError("Input must be a digit (0-9)")
        return sum(d * (10**i - 1) // 9 for i in range(1, r + 1))

if __name__ == "__main__":
    dt = DigitTransformer()
    print("Result:", dt.transform(3))
    print("Optimized:", 3 * 1234)
    print("General:", dt.transform(3, 4))
