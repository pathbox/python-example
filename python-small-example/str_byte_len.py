def str_byte_len(mystr):
    return (len(mystr.encode('utf-8')))


print(str_byte_len('i love python'))  # 13(个字节)
print(str_byte_len('字符'))  # 6(个字节)
