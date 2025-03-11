class EvenFibonacciCalculator:
    
    def __init__(self):
        self.previous_odd1 = 1 
        self.previous_odd2 = 1 
        self.current_even = 2 
        self.count = 1
        self.sum = 2
    
    def generate_next_even(self):
        next_even = 4 * self.current_even + self.previous_odd2
        self.previous_odd2 = self.previous_odd1
        self.previous_odd1 = self.current_even
        self.current_even = next_even
        
        self.count += 1
        self.sum += next_even
        
        return next_even
    
    def calculate_sum_of_even_fibonacci(self, n):
        self.__init__()
        while self.count < n:
            self.generate_next_even()
        
        return self.sum


def main():
    """Main function to demonstrate the calculator."""
    calculator = EvenFibonacciCalculator()
    
    TARGET_COUNT = 100
    sum_value = calculator.calculate_sum_of_even_fibonacci(TARGET_COUNT)
    
    print(f"The sum of the first {TARGET_COUNT} even Fibonacci numbers is: {sum_value}")
    
    # Print some intermediate values for verification
    calculator = EvenFibonacciCalculator()
    print("\nFirst 10 even Fibonacci numbers:")
    print(f"1: {calculator.current_even}")
    for i in range(2, 11):
        print(f"{i}: {calculator.generate_next_even()}")


if __name__ == "__main__":
    main()