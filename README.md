
# Babai's Algorithm for the Closest Vector Problem (CVP)

This README file provides an overview and explanation of a Python implementation of Babai's Algorithm for the Closest Vector Problem (CVP). This algorithm finds the closest lattice vector to a given target vector.

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Usage](#usage)
4. [Function Explanations](#function-explanations)
5. [Example](#example)

## Introduction
Babai's Algorithm is used to solve the Closest Vector Problem (CVP) in lattice theory. Given a set of basis vectors that define a lattice and a target vector, the algorithm finds the lattice vector closest to the target.

## Prerequisites
- Basic knowledge of Python.
- Basic understanding of vectors and dot products.
- Familiarity with Gram-Schmidt orthogonalization is helpful but not required.

## Usage
Copy and paste the code into a Python file (e.g., `babai_algorithm.py`). To use the algorithm, define the basis vectors and the target vector, and call the `babai_algorithm` function.

## Function Explanations

### `babai_algorithm(basis, target)`
This is the main function that implements Babai's Algorithm.

**Parameters:**
- `basis`: A list of lists where each inner list represents a basis vector of the lattice.
- `target`: A list representing the target vector.

**Returns:**
- A list representing the closest lattice vector to the target vector.

**Steps:**
1. **Gram-Schmidt Orthogonalization:** Converts the basis vectors into an orthogonal basis.
2. **Coordinate Computation:** Computes the coordinates of the target vector in the orthogonalized basis.
3. **Rounding:** Rounds the coordinates to the nearest integer.
4. **Closest Vector Calculation:** Computes the closest lattice vector using the rounded coordinates and the original basis.

### `gram_schmidt(vectors)`
This function performs Gram-Schmidt orthogonalization on a set of vectors.

**Parameters:**
- `vectors`: A list of lists where each inner list represents a vector.

**Returns:**
- A tuple containing two elements:
  - `orthogonalized`: The orthogonalized vectors.
  - `coefficients`: The coefficients used in the orthogonalization process.

### `dot_product(v1, v2)`
This function calculates the dot product of two vectors.

**Parameters:**
- `v1`: A list representing the first vector.
- `v2`: A list representing the second vector.

**Returns:**
- A float representing the dot product of the two vectors.

## Example
Below is an example of how to use the Babai's Algorithm implementation:

```python
# Define the basis vectors
basis = [[1, 1, 1], [0, 1, 0], [0, 0, 1]]

# Define the target vector
target = [2.6, 2.7, 2.8]

# Find the closest lattice vector
closest_vector = babai_algorithm(basis, target)
print("Closest lattice vector:", closest_vector)
```

## Explanation of the Code
- **Imports:**
  - `math` module is imported but not used in this code. It can be removed if not needed.
  
- **`babai_algorithm` function:**
  - Step 1: Uses `gram_schmidt` to orthogonalize the basis.
  - Step 2: Computes coordinates of the target vector in the orthogonalized basis by projecting the target vector onto each orthogonal basis vector.
  - Step 3: Rounds the coordinates to the nearest integer.
  - Step 4: Computes the closest lattice vector by summing the scaled basis vectors.

- **`gram_schmidt` function:**
  - Orthogonalizes a set of vectors and computes the coefficients for each step of orthogonalization.

- **`dot_product` function:**
  - Computes the dot product of two vectors by summing the products of their corresponding components.

## Conclusion
This implementation of Babai's Algorithm provides a method for solving the Closest Vector Problem (CVP) in lattice theory. The provided functions are explained step-by-step to ensure ease of understanding, even for those with basic knowledge of Python and lattice theory.
