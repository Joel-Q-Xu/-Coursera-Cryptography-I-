import requests
url='http://crypto-class.appspot.com/po?er='
def xor(a, b):
    if len(a) > len(b):
        return ''.join([chr(ord(x)^ord(y)) for x, y in zip(a[:len(b)], b)])
    else:
        return ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, b[:len(a)])])
    
def strtochr(guess_m,i,char):
	guess_m= list(guess_m)
	guess_m[i] = char
	return ''.join(guess_m)
    
def query(c):
        req = requests.get(url + c.encode('hex'))    
        if req.status_code == 404:
            return True
        else:
            return False
        
def main():
    charac=[chr(i) for i in range(256)]
    cipher='f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'.decode('hex')

    block=[]
    for ix in range(len(cipher)/16):
        block.append(cipher[ix*16:(ix+1)*16])

    m=''
    iv=cipher[:16]
    bloc=block[1:]

    for i in range(-1,len(bloc)-1):
        if i==-1:
            old_iv=iv
        else:
            old_iv=bloc[i]

        guess_m="\x00"*16

        for j in range(1,len(iv)+1):
            pad="\x00"*(16-j)+chr(j)*j
            for char in charac:
                if char=='\x01'and i==len(bloc)-2:
                    continue
                guess_m=strtochr(guess_m,16-j,char)
                new_iv=xor(xor(guess_m,pad),old_iv)
                if i==-1:
                    iv=new_iv
                else:
                    bloc[i]=new_iv
                print "test:",(iv+''.join(bloc[:i+2])).encode('hex')
                result=query(iv+''.join(bloc[:i+2]))
                if result:
                    break
        m+=guess_m
        print 'm:',m
    return m

if __name__ == '__main__':
	main()
