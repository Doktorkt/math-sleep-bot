import sys
import subprocess
import os

# Проверяем, передали ли нам аргументы (sys.argv[0] — это имя самого скрипта, а sys.argv[1] — наше слово)
if len(sys.argv) > 1:
    word = sys.argv[1]       # Берём именно чистую строку текста
    reversed_text = word[::-1] # Переворачиваем буквы в строке
    
    # Переходим в домашнюю папку к Java
    home_dir = '/data/data/com.termux/files/home'
    os.chdir(home_dir)
    
    # Запускаем Java
    result = subprocess.run(['java', '-cp', '.', 'Processor', reversed_text], 
                            capture_output=True, text=True)
    
    output = result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
    print(f"Python перевернул, а Java обработала: {output}")
else:
    print("Python не получил текст!")
