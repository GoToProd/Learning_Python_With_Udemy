import os

# Переходим во вторую папку
os.chdir('./test')

# Получаем текущую директорию (теперь это вторая папка)
current_directory = os.getcwd()

# Создаем полный путь к файлу text.txt в текущей директории
file_path = os.path.join(current_directory, "text.txt")

# Создаем файл text.txt
with open(file_path, 'w') as file:
    file.write("Привет, мир!")

print(f"Файл {file_path} успешно создан во второй папке.")
