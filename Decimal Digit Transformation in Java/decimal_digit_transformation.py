class DigitTransformer:
    
    def transform_digit(self, digit):
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError("Input must be a single decimal digit (0-9)")
        
        x = digit
        xx = digit * 10 + digit
        xxx = digit * 100 + digit * 10 + digit
        xxxx = digit * 1000 + digit * 100 + digit * 10 + digit
        
        return x + xx + xxx + xxxx
    
    def transform_digit_optimized(self, digit):
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError("Input must be a single decimal digit (0-9)")
        
        return digit * 1234
    
    def transform_digit_general(self, digit, repetitions):
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError("Digit must be a single decimal digit (0-9)")
        if not isinstance(repetitions, int) or repetitions <= 0:
            raise ValueError("Number of repetitions must be a positive integer")
        
        result = 0
        current_term = 0
        
        for _ in range(repetitions):
            current_term = current_term * 10 + digit
            result += current_term
        
        return result


def main():
    transformer = DigitTransformer()
    
    try:
        result = transformer.transform_digit(3)
        print(f"Result for digit 3: {result}")
        
        optimized_result = transformer.transform_digit_optimized(3)
        print(f"Optimized result for digit 3: {optimized_result}")
        
        general_result = transformer.transform_digit_general(3, 4)
        print(f"General result for digit 3 with 4 repetitions: {general_result}")
        
        try:
            transformer.transform_digit(10)
        except ValueError as e:
            print(f"Error: {e}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()