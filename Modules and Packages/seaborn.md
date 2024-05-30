# Seaborn


## scatterplot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Lists of values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Creating a scatter plot
sns.scatterplot(x=x, y=y)

# Displaying the plot
plt.show()

```
### histplot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# List of values
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Creating a histogram
sns.histplot(data, kde=True)

# Displaying the plot
plt.show()
```

### Box plot
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Lists of values for multiple categories
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
C = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
D = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Creating a DataFrame from the data
df = pd.DataFrame({'A': A, 'B': B, 'C': C, 'D': D})

# Creating a box plot
sns.boxplot(data=df)

# Displaying the plot
plt.show()
```
### Line Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Lists of values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Creating a line plot
sns.lineplot(x=x, y=y)

# Displaying the plot
plt.show()
```
### Pair plot
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Lists of values
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
C = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
D = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Creating a DataFrame from the data
df = pd.DataFrame({'A': A, 'B': B, 'C': C, 'D': D})

# Creating a pair plot
sns.pairplot(df)

# Displaying the plot
plt.show()


```
