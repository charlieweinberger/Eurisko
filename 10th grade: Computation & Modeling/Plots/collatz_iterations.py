# part a
def collatz_iterations(number):
    num_iterations = 0
    while number != 1:
        num_iterations += 1
        if number % 2 == 0:  
            number = number // 2
        else:
            number = 3*number + 1
    return num_iterations

print("\nPart A:")
print("Testing collatz_iterations(13)...")
assert collatz_iterations(13) == 9, collatz_iterations(13)
print("PASSED")

# part b
print("\nPart B:")
max_collatz_iterations = max([collatz_iterations(num) for num in range(1, 1001)])
print("Of the numbers from 1 to 1000, the number {} has the highest number of Collatz iterations.".format(max_collatz_iterations))

# part c
import matplotlib.pyplot as plt
plt.style.use('bmh')

x_coords = [num for num in range(1, 1001)]
y_coords = [collatz_iterations(num) for num in range(1, 1001)]

plt.plot(x_coords, y_coords)
plt.xlabel('Number')
plt.ylabel('Number of Collatz Iterations')
plt.title('Collatz Iterations for each number from 1 to 1000')
plt.savefig('collatz_iterations_png.png')