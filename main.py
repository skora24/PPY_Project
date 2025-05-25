from task import Task
from manager import TaskManager

def main():
    manager = TaskManager()
    manager.load_from_file()

    while True:
        print("\nMENU:")
        print("1. Dodaj zadanie")
        print("2. Edytuj zadanie")
        print("3. Usuń zadanie")
        print("4. Oznacz jako zakończone")
        print("5. Wyświetl listę zadań (bez opisu)")
        print("6. Pokaż szczegóły zadania")
        print("7. Zapisz do pliku")
        print("8. Wczytaj z pliku")
        print("9. Statystyki i wykresy")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        try:
            if choice == "1":
                name = input("Nazwa: ")
                priority = input("Priorytet (UrgentImporant / NotUrgentImporant / UrgentNotImpornant / NotUrgentNotImporant): ")
                status = input("Status (ToDo / InProgress / Finished): ")
                due_date = input("Termin (RRRR-MM-DD): ")
                category = input("Kategoria: ")
                description = input("Opis: ")
                manager.add_task(Task(name, priority, status, due_date, category, description))

            elif choice == "2":
                name = input("Nazwa zadania do edycji: ")
                field = input("Które pole chcesz zmienić (name, priority, status, due_date, category, description): ")
                new_value = input(f"Nowa wartość dla {field}: ")
                manager.edit_task(name, **{field: new_value})

            elif choice == "3":
                name = input("Nazwa zadania do usunięcia: ")
                manager.delete_task(name)

            elif choice == "4":
                name = input("Nazwa zadania do oznaczenia jako zakończone: ")
                manager.mark_finished(name)

            elif choice == "5":
                manager.list_tasks_summary()

            elif choice == "6":
                name = input("Nazwa zadania do podglądu: ")
                manager.show_task_details(name)

            elif choice == "7":
                manager.save_to_file()

            elif choice == "8":
                manager.load_from_file()

            elif choice == "9":
                stats = manager.get_statistics()
                print(f"Zakończone na czas: {stats[0]:.2f}%")
                print(f"Średni czas wykonania: {stats[1]:.2f} dni")
                print(f"Najczęstsza kategoria: {stats[2]}")
                manager.show_charts()

            elif choice == "0":
                print("Zakończono.")
                break

            else:
                print("Niepoprawna opcja.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
