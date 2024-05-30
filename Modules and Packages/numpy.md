## Numpay

### Basic Operation
```python
# Importing the hypothetical numpay library
import numpay as npy

# Creating a sample array
array = npy.array([1, 2, 3, 4, 5])

# Performing basic operations
sum_array = npy.sum(array)
mean_array = npy.mean(array)
std_array = npy.std(array)

print("Original Array:", array)
print("Sum:", sum_array)
print("Mean:", mean_array)
print("Standard Deviation:", std_array)
```

## Element-wise Operations

```python
# Assuming array is already created
# Performing element-wise operations
squared_array = npy.square(array)

print("Original Array:", array)
print("Squared Array:", squared_array)
```

# Creating a sample matrix
```python
matrix = npy.array([[1, 2], [3, 4]])

# Transposing the matrix
transposed_matrix = npy.transpose(matrix)

print("Original Matrix:\n", matrix)
print("Transposed Matrix:\n", transposed_matrix)
```
