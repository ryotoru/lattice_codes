import math

def babai(basis, target):
    ortho_basis, coefficients = gram_schmidt(basis)  # Gram-Schmidt orthogonalization
    coordinates = [0] * len(basis)
    for i in range(len(basis) - 1, -1, -1):
        coordinates[i] = dot_product(target, ortho_basis[i]) / dot_product(ortho_basis[i], ortho_basis[i])  # Compute the coordinates of the target vector in the orthogonalized basis
        for j in range(len(target)):
            target[j] -= coordinates[i] * basis[i][j]  # Subtract the projection from the target vector
    rounded_coordinates = [round(coordi) for coordi in coordinates]
    # Compute the closest vector in the lattice
    closest_vector = [0] * len(target)
    for i in range(len(basis)):
        for j in range(len(target)):
            closest_vector[j] += rounded_coordinates[i] * basis[i][j]
    return closest_vector

def gram_schmidt(vectors):
    orthogonalized = []
    coefficients = [[0.0 for _ in range(len(vectors))] for _ in range(len(vectors))]

    for i, vector in enumerate(vectors):
        temp_vec = vector.copy()
        for j in range(i):
            coefficients[i][j] = dot_product(temp_vec, orthogonalized[j]) / dot_product(orthogonalized[j], orthogonalized[j])
            for k in range(len(temp_vec)):
                temp_vec[k] -= coefficients[i][j] * orthogonalized[j][k]
        orthogonalized.append(temp_vec)
    return orthogonalized, coefficients

def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

# Example usage
basis = [[1, 5, 1], [0, 1, 0], [0, 0, 1]]
target = [2.6, 3.7, 2.8]

closest_vector = babai(basis, target)
print("Closest lattice vector:", closest_vector)


