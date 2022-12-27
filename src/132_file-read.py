txt_file = open("sample.txt", "r")

# txt = txt_file.readline()
# print(txt)
# txt = txt_file.readline()
# print(txt)
# txt = txt_file.readline()
# print(txt)


for txt_line in txt_file.readlines():
    print(txt_line)
    # print(txt_line, end="")


txt_file.close()
