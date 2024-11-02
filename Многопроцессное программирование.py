import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # добавляем строку в список, убирая пробелы
    return all_data

if __name__ == '__main__':
    # Список названий файлов
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    # Линейный вызов
    start_time = time.time()
    for file_name in file_names:
        read_info(file_name)
    end_time = time.time()
    print(f"Время выполнения линейного вызова: {end_time - start_time:.4f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        results = pool.map(read_info, file_names)
    end_time = time.time()
    print(f"Время выполнения многопроцессного вызова: {end_time - start_time:.4f} секунд")
