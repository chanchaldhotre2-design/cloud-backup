import os
import shutil

SOURCE = "my_files"
BACKUP = "backup"

def create_backup():
    if not os.path.exists(SOURCE):
        os.makedirs(SOURCE)
        print("Created my_files folder. Add files and try again.")
        return

    if not os.listdir(SOURCE):
        print("my_files folder is empty. Add a file first.")
        return

    shutil.copytree(SOURCE, BACKUP, dirs_exist_ok=True)
    print("Backup created successfully!")

def restore_backup():
    if not os.path.exists(BACKUP):
        print("No backup found!")
        return

    shutil.copytree(BACKUP, SOURCE, dirs_exist_ok=True)
    print("Files restored successfully!")

while True:
    print("\n--- Cloud Backup & Restore ---")
    print("1. Create Backup")
    print("2. Restore Backup")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_backup()
    elif choice == "2":
        restore_backup()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")