import shutil

from pathlib import Path
for dest_dir in Path('C:\\SERVER').glob('*/i18n'):
    if dest_dir.is_dir():
        for path in Path('C:\\!_out').glob('*.json'):
            shutil.copy(str(path), str(dest_dir))
input("Готово!")


# если нужно скопировать все файлы (включая "cкрытые": .*)
#for path in Path('/source-dir').iterdir():
#    if path.is_file():
#        shutil.copy(str(path), str(dest_dir))

# Если кроме файлов, вы хотите скопировать и вложенные директории рекурсивно
#for path in Path('/source-dir').iterdir():
#    if path.is_dir():
#        shutil.copytree(str(path), str(dest_dir / path.name),
#        copy_function=shutil.copy) # use the same copy function
#            else:
#                shutil.copy(str(path), str(dest_dir))