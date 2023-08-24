f=open('abc.txt','r')
read=f.read()
print(read)

a=open('xyz.txt','w')
write=a.write('hello')
print(write)

a=open('xyz.txt','a')
append=a.write('hi')
print(append)



