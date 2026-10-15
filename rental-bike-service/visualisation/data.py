
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline



# Download the dataset of UCI Bike Rental
import requests
import zipfile
import io

url = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"

response = requests.get(url)

with zipfile.ZipFile(io.BytesIO(response.content)) as z:
  z.extractall()


print("Dataset downloaded and extracted successfully!.")



# View dataset
df = pd.read_csv("day.csv")
df.head()
