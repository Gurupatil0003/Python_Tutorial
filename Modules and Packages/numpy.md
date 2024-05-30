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

### Creating a sample matrix
```python
matrix = npy.array([[1, 2], [3, 4]])

# Transposing the matrix
transposed_matrix = npy.transpose(matrix)

print("Original Matrix:\n", matrix)
print("Transposed Matrix:\n", transposed_matrix)
```

### Array Arithmetic Operations

```python
# Creating two sample arrays
array1 = npy.array([1, 2, 3, 4, 5])
array2 = npy.array([5, 4, 3, 2, 1])

# Adding the arrays
sum_arrays = npy.add(array1, array2)

# Subtracting the arrays
diff_arrays = npy.subtract(array1, array2)

# Multiplying the arrays element-wise
product_arrays = npy.multiply(array1, array2)

# Dividing the arrays element-wise
quotient_arrays = npy.divide(array1, array2)

print("Array1:", array1)
print("Array2:", array2)
print("Sum:", sum_arrays)
print("Difference:", diff_arrays)
print("Product:", product_arrays)
print("Quotient:", quotient_arrays)
```
### Reshaping an Array

```python
# Creating a sample array
array = npy.array([1, 2, 3, 4, 5, 6])

# Reshaping the array into a 2x3 matrix
reshaped_array = npy.reshape(array, (2, 3))

print("Original Array:", array)
print("Reshaped Array:\n", reshaped_array)
```
### Finding Maximum and Minimum Values
```python
# Creating a sample array
array = npy.array([1, 3, 2, 5, 4])

# Finding the maximum value
max_value = npy.max(array)

# Finding the minimum value
min_value = npy.min(array)

print("Array:", array)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
```

### Generating a Range of Numbers
```python
# Generating a range of numbers from 0 to 9
range_array = npy.arange(10)

print("Range Array:", range_array)
```

