with open('Pyfile.txt','w') as file :
	file.write("hi my name is Apoorve ")
	file.close()

with open('Pyfile.txt','r') as file :
    f= file.read()
    print(f)
    file.close()
