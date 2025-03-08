import sys

def string_to_long(s):
    try:
        return int(s)  # Python'da 'int' veri tipi, long'u da kapsar
    except ValueError:
        print("Invalid input: Please enter a valid numeric string.")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python string_to_long.py <number_as_string>")
    else:
        result = string_to_long(sys.argv[1])
        if result is not None:
            print(f"Converted long value: {result}")
