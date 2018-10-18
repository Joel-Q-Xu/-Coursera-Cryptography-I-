from hashlib import sha256
"""rb-以二进制格式打开一个文件用于只读，
    文件指针将会放在文件的开头"""
name1='6.1.intro.mp4_download'
name2='6.2.birthday.mp4_download'
with open(name1, "rb") as f:
    blocks=[]
    block=f.read(1024)
    while block:
        blocks.append(block)
        block=f.read(1024)
#从最后一块开始计算
h=sha256(blocks[-1])
for block in reversed(blocks[:-1]):
    h=sha256(block+h.digest())
print(h.hexdigest())
