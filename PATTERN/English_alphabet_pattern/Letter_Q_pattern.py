# python code to print the English alphabet "Q"...

# Solution:-
def print_Q(n):
    for i in range(n):
        for j in range(n):
            # Draw outer border of Q
            if (
                (i == 0 and 0 < j < n - 1) or  # Top horizontal line
                (i == n - 2 and 0 < j < n - 1) or  # Bottom horizontal line (before tail)
                (j == 0 and 0 < i < n - 2) or  # Left vertical line
                (j == n - 1 and 0 < i < n - 2)  # Right vertical line
            ):
                print("*", end=" ")
            # Tail of Q
            elif i == j and i > n // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
n = int(input())
print_Q(n)
