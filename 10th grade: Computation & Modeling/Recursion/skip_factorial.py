# part a (nonrecursive)
def skip_factorial_nonrecursive(n):
    
    ans = 1
    
    if n%2 == 0:
        for half_num in range(int(n/2)):
            ans *= n - (2 * half_num)
    else:
        for half_num in range(int(n/2 + 1)):
            ans *= n - (2 * half_num)
    
    return ans

print("Testing skip_factorial_nonrecursive(6)...")
assert skip_factorial_nonrecursive(6) == 48, skip_factorial_nonrecursive(6)
print("PASSED")

print("Testing skip_factorial_nonrecursive(7)...")
assert skip_factorial_nonrecursive(7) == 105, skip_factorial_nonrecursive(7)
print("PASSED")

# part b (recursive)
def skip_factorial_recursive(n):
    
    if n%2 == 0: # if n is even    
        if n == 0:
            return 1
        else:
            return n * skip_factorial_recursive(n - 2)
        
    else: # if n is odd
        if n == 1:
            return 1
        else:
            return n * skip_factorial_recursive(n - 2)

print("Testing skip_factorial_recursive(6)...")
assert skip_factorial_recursive(6) == 48, skip_factorial_recursive(6)
print("PASSED")

print("Testing skip_factorial_recursive(7)...")
assert skip_factorial_recursive(7) == 105, skip_factorial_recursive(7)
print("PASSED")