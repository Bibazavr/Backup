import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ["C:\\Users\lirik\Desktop", "C:\\Users\lirik\Desktop\Programs"]
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Backup'  # Подставьте тот путь, который вы будете использовать.
# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')
# Создаём каталог, если его ещё
if not os.path.exists(today):
    os.mkdir(today)  # создание католога
print('Каталог успешно создан', today)
# Имя zip-файла
target = today + os.sep + now + '.zip'
# 5. Используем команду "zip" для помещения файлов в zip-фархив
zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной компии НЕ УДАЛОСЬ')
