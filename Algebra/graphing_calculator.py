import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sympy import symbols, sympify, lambdify, linsolve
import sys

x, y = symbols('x y')

# ---------------- MAIN MENU ---------------- #
def main():
    while True:
        print("\n====== MATHEMATICAL VISUALIZER ======")
        print("1. Graph an equation + table of values")
        print("2. Solve two equations (symbolically)")
        print("3. Graph two linear equations & intersection")
        print("4. Plot quadratic roots & vertex")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == '1':
                graph_and_table()
            elif choice == '2':
                solve_equations()
            elif choice == '3':
                graph_intersection()
            elif choice == '4':
                quadratic_plot()
            elif choice == '5':
                print("Exiting program. Bye 👋")
                sys.exit()
            else:
                print("❌ Invalid choice")
        except Exception as e:
            print("⚠️ Error:", e)


# ---------------- OPTION 1 ---------------- #
def graph_and_table():
    expr = input("Enter equation in x (example: x**2 + 3*x): ")
    f = lambdify(x, sympify(expr), "numpy")

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals)
    plt.title(f"y = {expr}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

    # Table
    table_x = np.arange(-5, 6)
    table_y = f(table_x)
    df = pd.DataFrame({"x": table_x, "y": table_y})
    print("\nTable of Values:")
    print(df)


# ---------------- OPTION 2 ---------------- #
def solve_equations():
    print("Enter equations in terms of x and y (example: 2*x + y - 5)")
    eq1 = sympify(input("Equation 1 = 0: "))
    eq2 = sympify(input("Equation 2 = 0: "))

    solution = linsolve([eq1, eq2], (x, y))
    print("Solution:", solution)


# ---------------- OPTION 3 ---------------- #
def graph_intersection():
    print("Line 1: y = m1*x + b1")
    m1, b1 = map(float, input("Enter m1,b1: ").split(","))

    print("Line 2: y = m2*x + b2")
    m2, b2 = map(float, input("Enter m2,b2: ").split(","))

    x_vals = np.linspace(-10, 10, 400)
    y1 = m1 * x_vals + b1
    y2 = m2 * x_vals + b2

    # Solve intersection
    sol = linsolve(
        [m1*x + b1 - y, m2*x + b2 - y],
        (x, y)
    )

    xi, yi = sol.args[0]

    plt.plot(x_vals, y1, label="Line 1")
    plt.plot(x_vals, y2, label="Line 2")
    plt.scatter(float(xi), float(yi))
    plt.text(float(xi), float(yi), f"({xi:.2f}, {yi:.2f})")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Intersection Point:", sol)


# ---------------- OPTION 4 ---------------- #
def quadratic_plot():
    print("y = ax² + bx + c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    x_vals = np.linspace(-10, 10, 400)
    y_vals = a*x_vals**2 + b*x_vals + c

    plt.plot(x_vals, y_vals, label="Quadratic")
    plt.axhline(0)
    plt.grid(True)

    # Roots
    disc = b**2 - 4*a*c
    if disc >= 0:
        r1 = (-b + np.sqrt(disc)) / (2*a)
        r2 = (-b - np.sqrt(disc)) / (2*a)
        plt.scatter([r1, r2], [0, 0], label="Roots")

    # Vertex
    vx = -b / (2*a)
    vy = a*vx**2 + b*vx + c
    plt.scatter(vx, vy, label="Vertex")

    plt.legend()
    plt.show()


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    main()
