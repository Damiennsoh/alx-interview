def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return [num for row in triangle for num in row]

        # Example usage of the pascal_triangle function
n = int(input("Enter a number: "))
result = pascal_triangle(n)
print(f"The Pascal's triangle of level {n} is: {result}")

