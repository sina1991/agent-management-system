# ALPHA-TEST-002 / Technical Agent 2
# Intended behavior: multiply(3, 4) returns 12.
# Intentional defect for the cycle test: uses addition instead of multiplication.
def multiply(a, b):
    return a + b

if __name__ == "__main__":
    print(multiply(3, 4))
