# Load environment variables
from hw2 import load_env, get_key
import numpy as np

# Load .env
load_env()

# Check API_KEY
api_key = get_key("API_KEY")
print("API_KEY exists:", api_key is not None)

print("\n=== Array Creation ===")
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1)

arr2 = np.zeros((2, 3))
print("2x3 zeros array:\n", arr2)

arr3 = np.ones((3, 2))
print("3x2 ones array:\n", arr3)

arr4 = np.arange(0, 10, 2)
print("Array with arange 0-10 step 2:", arr4)

arr5 = np.linspace(0, 1, 5)
print("5 values evenly spaced between 0 and 1:", arr5)

print("\n=== Basic Array Operations ===")
print("Max of arr1:", arr1.max())
print("Min of arr1:", arr1.min())
