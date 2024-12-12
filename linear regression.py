import numpy as np
import pandas as pd
import matplotlib.pyplot as ppl

x_data = []
y_data = []

while True:
    x_data.append(float(input("Enter your data in x: ").strip()))
    y_data.append(float(input("Enter your data in y: ").strip()))
    terminate = input("Do you want to stop: ").lower().strip()
    if terminate == "y":
        break

#table of your data
data = {
    "x": x_data,
    "y": y_data,
    "x*y": [x*y for x,y in zip(x_data,y_data)],
    "x^2": [x*x for x in x_data]
}

# table
data_frame = pd.DataFrame(data)

#sum of element in x, x^2
sum_of_x = sum(x_data)
sum_of_y = sum(y_data)
sum_of_x_squ = sum(i**2 for i in x_data)
sum_of_xy = sum(x*y for x,y in zip(x_data, y_data))
n = len(x_data)


# A matrix
A = np.array([
        [n, sum_of_x],
        [sum_of_x, sum_of_x_squ]
])

# B matrix
B = np.array([
    [sum_of_y],
    [sum_of_xy]
])

#to calulate a, b
X = np.dot(np.linalg.inv(A),B)

a, b = X[1,0], X[0,0]

print("x => ", x_data)
print("y => ", y_data)

print("\nTable:")
print(data_frame)

print("\nData: ")
print(f"Σx = {sum_of_x}")
print(f"Σy = {sum_of_y}")
print(f"Σx*y = {sum_of_xy}")
print(f"Σx^2 = {sum_of_x_squ}")

print(f"\nthe best line is: f(x) = {a:.3f}x {b:+.3f} \n")

ppl.show()
# draw the graph
ppl.scatter(x_data, y_data, color = "blue", label = "DataPoints")
y_predict = [a*x+b for x in x_data]
ppl.plot(x_data, y_predict, color = "red", label = "best fit line")
