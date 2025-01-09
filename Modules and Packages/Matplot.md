```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Plot
plt.plot(x, y)
plt.show()  # Display the plot
```

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Create figure and axes
fig, ax = plt.subplots()

# Plot on the axes
ax.plot(x, y)

# Customize the plot
ax.set_title('My Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Display the plot
plt.show()


```

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Plot with customized line style and color
plt.plot(x, y, linestyle='--', color='r')  # Red dashed line
plt.title('Styled Line Plot')
plt.show()

```

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Scatter plot with customization
plt.scatter(x, y, color='b', marker='o')  # Blue circles
plt.title('Scatter Plot')
plt.show()

```

```python

import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C']
values = [10, 15, 7]

# Bar plot
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title('Bar Plot')
plt.show()

```

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Create subplots (2 rows, 1 column)
fig, axes = plt.subplots(2, 1)

# Plot on first subplot
axes[0].plot(x, y)
axes[0].set_title('Line Plot')

# Plot on second subplot
axes[1].scatter(x, y)
axes[1].set_title('Scatter Plot')

# Display the plot
plt.tight_layout()
plt.show()

```
