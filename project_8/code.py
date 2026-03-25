# Simple Data Analyzer Program

data = []   # global list


# 1. Input Data
def input_data():
    global data
    values = input("Enter numbers (space-separated): ")
    data = list(map(int, values.split()))
    print("Data stored successfully!\n")


# 2. Display Summary (built-in functions)
def display_summary():
    if not data:
        print("No data available!\n")
        return

    print("\n--- Data Summary ---")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum:", sum(data))
    print("Average:", sum(data) / len(data))
    print()


# 3. Factorial (Recursion)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


# 4. Filter Data (Lambda)
def filter_data():
    if not data:
        print("No data available!\n")
        return

    t = int(input("Enter threshold: "))
    result = list(filter(lambda x: x > t, data))
    print("Filtered Data:", result)
    print()


# 5. Sort Data
def sort_data():
    if not data:
        print("No data available!\n")
        return

    print("1. Ascending")
    print("2. Descending")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Sorted Data:", sorted(data))
    else:
        print("Sorted Data:", sorted(data, reverse=True))
    print()


# 6. Multiple Return Values
def get_stats():
    if not data:
        print("No data available!\n")
        return

    return min(data), max(data), sum(data), sum(data)/len(data)


# 7. Main Menu
def main():
    while True:
        print("=== Data Analyzer ===")
        print("1. Input Data")
        print("2. Display Summary")
        print("3. Factorial")
        print("4. Filter Data")
        print("5. Sort Data")
        print("6. Get Statistics")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            input_data()

        elif choice == 2:
            display_summary()

        elif choice == 3:
            num = int(input("Enter number: "))
            print("Factorial:", factorial(num))
            print()

        elif choice == 4:
            filter_data()

        elif choice == 5:
            sort_data()

        elif choice == 6:
            result = get_stats()
            if result:
                print("Min:", result[0])
                print("Max:", result[1])
                print("Sum:", result[2])
                print("Average:", result[3])
                print()

        elif choice == 7:
            print("Thank you!")
            break

        else:
            print("Invalid choice!\n")


# Run program
main()