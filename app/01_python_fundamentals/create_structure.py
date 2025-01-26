
import os

# Definisci la struttura delle directory
structure = {
  "01_python_basics": [
    "01_variables_and_data_types",
    "02_strings_and_basic_operations",
    "03_input_output",
    "04_operators"
  ],
  "02_control_structures": [
    "01_if_else",
    "02_loops"
  ],
  "03_functions": [
    "01_function_basics",
    "02_arguments_and_return",
    "03_lambda_functions",
    "04_recursion",
    "05_scope_and_globals_usage"
  ],
  "04_data_structures": [
    "01_lists",
    "02_tuples",
    "03_dictionaries",
    "04_sets"
  ],
  "05_object_oriented_programming": [
    "01_classes_and_objects",
    "02_inheritance",
    "03_polymorphism",
    "04_encapsulation",
    "05_class_and_static_methods"
  ],
  "06_modules_and_packages": [
    "01_creating_modules",
    "02_importing_modules",
    "03_python_packages",
    "04_package_management_with_pip"
  ],
  "07_exceptions_and_error_handling": [
    "01_try_except",
    "02_custom_exceptions",
    "03_debugging_basics"
  ],
  "08_file_handling": [
    "01_reading_files",
    "02_writing_files",
    "03_json_handling",
    "04_csv_handling"
  ],
  "09_standard_libraries": [
    "01_os_module",
    "02_sys_module",
    "03_math_module",
    "04_datetime_module",
    "05_random_module",
    "06_re_module",
    "07_logging_module"
  ],
  "10_advanced_topics": [
    "01_decorators",
    "02_generators",
    "03_context_managers",
    "04_metaclasses",
    "05_threading_and_multiprocessing",
    "06_asyncio"
  ],
  "11_example_projects": [
    "01_command_line_tools",
    "02_simple_web_scraper",
    "03_mini_game_guess_number",
    "04_todo_list_in_file"
  ]
}



# Funzione per creare la struttura
def create_structure(structure):
    # Ottiene il percorso della cartella dove risiede il file corrente
    base_path = os.path.dirname(os.path.abspath(__file__))

    for main_folder, subfolders in structure.items():
        main_folder_path = os.path.join(base_path, main_folder)
        os.makedirs(main_folder_path, exist_ok=True)  # Crea la cartella principale

        for subfolder in subfolders:
            subfolder_path = os.path.join(main_folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)  # Crea la sottocartella

            # Crea la cartella "exercises" nella sottocartella
            exercises_path = os.path.join(subfolder_path, "exercises")
            os.makedirs(exercises_path, exist_ok=True)

            # Crea un file Python con il nome della sottocartella
            python_file_path = os.path.join(subfolder_path, f"{subfolder}.py")
            with open(python_file_path, "w") as python_file:
                python_file.write(f"# File per {subfolder}\n")
                python_file.write("# Aggiungi il tuo codice qui\n")

# Creazione della struttura
create_structure(structure)

print("Struttura creata con successo con file Python!")

