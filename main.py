# Открываем файл для чтения
with open('text.txt', 'r', encoding='utf-8') as input_file:
    # Читаем все строки из файла
    lines = input_file.readlines()

# Фильтруем строки, содержащие более 5 символов
filtered_lines = [line for line in lines if len(line.strip()) > 5]

# Открываем новый файл для записи
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Записываем отфильтрованные строки в новый файл
    output_file.writelines(filtered_lines)

print("Фильтрация завершена. Проверьте файл output.txt.")
