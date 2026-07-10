# 📚 NumPy - Day 1

## Concepts

- NumPy = Numerical Python
- NumPy Array (`ndarray`)
- Indexing
- Slicing
- Array Properties
- Vectorization

---

## ⭐ Important Points

- Import using:
  ```python
  import numpy as np
  ```

- Create array:
  ```python
  np.array()
  ```

- Array properties:
  - `ndim`
  - `shape`
  - `size`
  - `dtype`

- NumPy stores data in **contiguous memory**.
- NumPy performs **element-wise operations**.
- Vectorization allows operations on the whole array without writing loops.

---

## ❌ My Mistakes

- Forgot `print()` needs parentheses.
- Confused changing a loop variable with changing the array.
- Made small multiplication/calculation mistakes while predicting output.

---

## ✅ Improvements

- Think element by element for NumPy operations.
- Remember that changing `value` does not change the array.
- Double-check arithmetic before answering.
- Compare NumPy behavior with Python lists to understand the differences.

---

## 🎯 Interview Questions

✔ What is NumPy?

✔ Why is NumPy faster than Python lists?

✔ Difference between Python List and NumPy Array?

✔ What is vectorization?

✔ Why does `arr * 2` work without a loop?

---

## 💡 Data Science Connection

- NumPy is the foundation of Pandas.
- Used for fast numerical computations.
- Most machine learning libraries (TensorFlow, PyTorch, Scikit-learn) rely on NumPy arrays.

## 🏅 Word of the Day

### Vectorization

**Definition:**
Vectorization means performing an operation on an entire NumPy array at once without writing an explicit loop.

### Example

```python
import numpy as np

arr = np.array([1, 2, 3])

arr = arr * 2

print(arr)
```

**Output**

```
[2 4 6]
```

### Why it matters

- Faster than Python loops.
- Uses optimized C code internally.
- One of the main reasons NumPy is so efficient.
- Widely used in Data Science and Machine Learning.