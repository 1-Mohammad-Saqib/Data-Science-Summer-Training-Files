📘 NumPy Day 3 Notes
1. ndim

Returns the number of dimensions of an array.

arr.ndim

Example:

arr = np.array([[1,2],[3,4]])
print(arr.ndim)

Output:

2
2. shape

Returns the shape of an array.

arr.shape

Example:

arr = np.array([[1,2,3],
                [4,5,6]])

Output:

(2,3)

Meaning:

2 Rows
3 Columns
3. size

Returns the total number of elements.

arr.size

Example:

6
4. dtype

Returns the data type of array elements.

arr.dtype

Example:

int64
float64
5. reshape()

Changes the shape of an array without changing its data.

arr.reshape(2,3)

Rule:

Total elements before = Total elements after.

6. flatten()

Converts a multidimensional array into a 1D array.

arr.flatten()
7. Transpose (T)

Converts rows into columns and columns into rows.

arr.T
8. reshape(-1)

Automatically calculates one dimension.

arr.reshape(2,-1)
arr.reshape(-1,2)
Important Properties
Property	Purpose
ndim	Number of dimensions
shape	Rows and columns
size	Total elements
dtype	Data type
Important Methods
Method	Purpose
reshape()	Change array shape
flatten()	Convert to 1D
T	Transpose matrix
Important Rule
Elements Before = Elements After

Example:

6 elements

2×3 ✅
3×2 ✅
1×6 ✅
6×1 ✅
2×4 ❌
📚 Word of the Day
Dimension

A dimension is the number of axes an array has.

Examples:

1D → [1, 2, 3]

2D →

[[1,2,3],
 [4,5,6]]
3D → Multiple 2D arrays stacked together.
🎓 Mentor Tip ⭐

Always remember these four properties:

arr.ndim   # Dimensions
arr.shape  # Shape
arr.size   # Total elements
arr.dtype  # Data type

These are among the most frequently used NumPy properties in Data Science, Pandas, and Machine Learning.