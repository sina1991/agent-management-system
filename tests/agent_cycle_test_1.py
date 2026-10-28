# ALPHA-TEST-002 / Technical Agent 1
# Intended behavior: add(2, 3) returns 5.
# Intentional defect for the cycle test: syntax error on the return line.
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))
