from omurbek_21_1_hw4.file_executor.create import create_file
from omurbek_21_1_hw4.file_executor.delete import delete_file
from omurbek_21_1_hw4.file_executor.write import write_to_file


print(create_file("apple", 'txt'))
write_to_file("melon.txt", "дереыо это дерево")
print(delete_file("apple.txt"))