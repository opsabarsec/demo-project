import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": np.random.randint(20, 40, size=4),
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)

print(df.shape)
print(df.head())
