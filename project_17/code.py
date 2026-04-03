
dataset = []
dataset_summary = {}


def input_data():
    global dataset

    choice = input("Enter 1 for 1D list OR 2 for 2D list: ")

    if choice == "1":
        data = input("Enter numbers separated by spaces: ")
        dataset = list(map(int, data.split()))
    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        dataset = []
        for i in range(rows):
            row = list(map(int, input(f"Enter row {i+1}: ").split()))
            dataset.append(row)
    else:
        print("Invalid choice!")
        return

    print("Data stored successfully!\n")


def display_summary():
    global dataset, dataset_summary

    if not dataset:
        print("No data available!\n")
        return

    flat_data = flatten(dataset)

    dataset_summary = {
        "Total elements": len(flat_data),
        "Minimum": min(flat_data),
        "Maximum": max(flat_data),
        "Sum": sum(flat_data),
        "Average": sum(flat_data) / len(flat_data)
    }

    print("\nDataset Summary:")
    for k, v in dataset_summary.items():
        print(f"- {k}: {v}")
    print()


def flatten(data):
    if isinstance(data[0], list):
        return [item for sublist in data for item in sublist]
    return data


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def recursive_operation():
    choice = input("Enter 'f' for factorial or 'fib' for fibonacci: ")

    n = int(input("Enter number: "))

    if choice == "f":
        print("Factorial:", factorial(n))
    elif choice == "fib":
        print("Fibonacci:", fibonacci(n))
    else:
        print("Invalid choice!")
    print()


def filter_data():
    global dataset

    if not dataset:
        print("No data available!\n")
        return

    flat_data = flatten(dataset)

    threshold = int(input("Enter threshold: "))
    filtered = list(filter(lambda x: x > threshold, flat_data))

    print("Filtered values:", filtered, "\n")


def sort_data():
    global dataset

    if not dataset:
        print("No data available!\n")
        return

    choice = input("1. Ascending\n2. Descending\nEnter choice: ")

    reverse = True if choice == "2" else False

    if isinstance(dataset[0], list):
        # Sort each row
        sorted_data = [sorted(row, reverse=reverse) for row in dataset]
    else:
        sorted_data = sorted(dataset, reverse=reverse)

    print("Sorted Data:", sorted_data, "\n")


def dataset_statistics():
    global dataset

    if not dataset:
        print("No data available!\n")
        return

    flat_data = flatten(dataset)

    minimum = min(flat_data)
    maximum = max(flat_data)
    total = sum(flat_data)
    average = total / len(flat_data)

    return minimum, maximum, total, average


def display_statistics():
    stats = dataset_statistics()
    if stats:
        print("\nStatistics:")
        print("Min:", stats[0])
        print("Max:", stats[1])
        print("Sum:", stats[2])
        print("Average:", stats[3])
        print()


def display_info(**kwargs):
    """
    Displays dataset information using kwargs
    """
    print("\nDataset Info:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()


def show_info():
    global dataset_summary
    if dataset_summary:
        display_info(**dataset_summary)
    else:
        print("No summary available!\n")


def main():
    while True:
        print("===== Data Analyzer Menu =====")
        print("1. Input Data")
        print("2. Display Summary (Built-in)")
        print("3. Recursive Operation")
        print("4. Filter Data (Lambda)")
        print("5. Sort Data")
        print("6. Dataset Statistics (Tuple Return)")
        print("7. Display Info (**kwargs)")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            input_data()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            recursive_operation()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            display_statistics()
        elif choice == "7":
            show_info()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")


main()