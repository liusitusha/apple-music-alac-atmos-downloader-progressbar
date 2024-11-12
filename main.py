import os

# 提示用户输入URL
url = input("请输入URL: ")

# 构造命令
command = f"go run main.go {url}"

# 执行命令
os.system(command)