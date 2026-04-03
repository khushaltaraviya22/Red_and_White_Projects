class JournalManager:

    def create_file(self):
        filename = input("Enter file name (with .txt): ")

        if not filename.endswith(".txt"):
            print("Error: Only .txt files are allowed.\n")
            return

        try:
            with open(filename, "x"):
                print(f"File '{filename}' created successfully!\n")

        except FileExistsError:
            print(f"File '{filename}' already exists.\n")

        except Exception as e:
            print("Error creating file:", e)

    def get_filename(self):
        filename = input("Enter file name (with .txt): ")

        if not filename.endswith(".txt"):
            print("Error: Only .txt files are allowed.\n")
            return None

        return filename

    def add_entry(self):
        filename = self.get_filename()
        if not filename:
            return

        try:
            date = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
            entry = input("Enter your journal entry:\n")

            with open(filename, "a") as file:
                file.write(f"[{date}]\n{entry}\n\n")

            print("Entry added successfully!\n")

        except Exception as e:
            print("Error while adding entry:", e)

    def view_entries(self):
        filename = self.get_filename()
        if not filename:
            return

        try:
            with open(filename, "r") as file:
                content = file.read()

                if content.strip() == "":
                    print("No journal entries found.\n")
                else:
                    print("\nYour Journal Entries:")
                    print("-" * 40)
                    print(content)

        except FileNotFoundError:
            print("Error: File does not exist.\n")

    def search_entry(self):
        filename = self.get_filename()
        if not filename:
            return

        try:
            keyword = input("Enter keyword or date to search: ")

            with open(filename, "r") as file:
                lines = file.readlines()

            found = False
            print("\nMatching Entries:")
            print("-" * 40)

            for line in lines:
                if keyword.lower() in line.lower():
                    print(line)
                    found = True

            if not found:
                print(f"No entries found for: {keyword}\n")

        except FileNotFoundError:
            print("Error: File not found.\n")

    def delete_entries(self):
        filename = self.get_filename()
        if not filename:
            return

        try:
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")

            if confirm.lower() == "yes":
                with open(filename, "w"):
                    pass
                print("All entries deleted (file cleared).\n")
            else:
                print("Deletion cancelled.\n")

        except Exception as e:
            print("Error while deleting:", e)


def main():
    jm = JournalManager()

    while True:
        print("\n===== Personal Journal Manager =====")
        print("1. Create File")
        print("2. Add a New Entry")
        print("3. View All Entries")
        print("4. Search for an Entry")
        print("5. Delete All Entries")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            jm.create_file()
        elif choice == "2":
            jm.add_entry()
        elif choice == "3":
            jm.view_entries()
        elif choice == "4":
            jm.search_entry()
        elif choice == "5":
            jm.delete_entries()
        elif choice == "6":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.\n")


main()