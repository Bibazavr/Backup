import zipfile
import time
import os

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = 'C:\\Users\lirik\desktop'
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Backup'  # Подставьте тот путь, который вы будете использовать.
# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y_%m_%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H-%M-%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий -->')
if len(comment) == 0:  # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace('', '_') + '.zip'

# Создаём каталог, если его ещё
if not os.path.exists(today):
    os.mkdir(today)  # создание католога
    print('Каталог успешно создан', today)
else:
    print('Каталог уже есть')
# 5. Используем команду "zip" для помещения файлов в zip-фархив

# Запускаем создание резервной копии
z = zipfile.ZipFile(target, mode='w')
for root, dirs, files in os.walk(source):
    for file in files:
        z.write(os.path.join(root, file))

z.close()
