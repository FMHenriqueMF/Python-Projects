from random import*

print("Bem vindo ao TrucoPython v2")

#####   criação das cartas    ##### 
nro_cartas = ["4","5","6","7","10","11","12","1","2","3"]
naipe_cartas= ["moles","espada","copas","paus"]
cartas1 = []
cartas2 = []
cartas3 = []
cartas4 = []
contador = 0
cartas = []
cartas_rodada = []
valor_rodada = []
valor_rodada_sort = []
jogada_permitida = False
jogada1 =0
escolha = -1
qm_ganhador = 0
for i in nro_cartas:
    for k in naipe_cartas:
        cartas.append(i+" "+"de"+" "+k)

#####   valorização das cartas  #####
valor_cartas = []
for i in range(1,41):
    valor_cartas.append(i)
    
#####   distribuição de cartas  #####
def distribui(c,x):
    global contador
    for i in range(3):
        c.append(x[contador])
        contador += 1
def dar_cartas():
    cartas_escolhidas = sample(cartas,16)
    distribui(cartas1,cartas_escolhidas)
    distribui(cartas2,cartas_escolhidas)
    distribui(cartas3,cartas_escolhidas)
    distribui(cartas4,cartas_escolhidas)
    vira = cartas_escolhidas[15]
    print("O vira é: ",vira) 
    valor_vira(vira)
 
#####   valorização do vira     #####
def valor_vira(v):
    count = 0
    for i in cartas:
        count += 1
        if i == v:
            break
    while ((count % 4)!=0):
        count += 1
    for i in valor_cartas:
        if count == i:
            for j in range(4):
                if count >= 40:
                    count = 0
                valor_cartas[count] = count + 50
                count +=1
dar_cartas()
bara = dict(zip(cartas,valor_cartas))

#####   mostra na tela as cartas e jogada    #####
def sua_jogada1():
    global jogada1
    print("Suas cartas são: ")
    for x in range(len(cartas1)):
        print("Digite",x+1,"para jogar:")
        print("      ",cartas1[x])
    jogada1 = int(input("Você jogará: - "))
    verifica_carta(jogada1)

#####   retirar carta da mão    #####
def retira_carta(card,j):
    for x in range(len(card)):
        if x == j:
            cartas_rodada.append(card[j-1])
            del card[j-1]
            break


#####   verificação da jogada com o numero de cartas    #####             
def verifica_carta(j):
    global jogada_permitida
    for x in range(len(cartas1)):
        if x+1 == j:
            jogada_permitida = True

#####   Decisão de que carta jogar  #####              
def jogada_bot(card):
    global escolha
    escolha = randint(0,len(card) -1)
    
#####   Mostra na tela  #####
def prints(nome,card,jogada):
    print("...........................")  
    print( nome, " jogou : ", card[jogada-1])
    retira_carta(card,jogada)
    escolha = -1

#####   Verificação de ganhador     #####
def declara_campeao():
    print(qm_ganhador)
    if qm_ganhador == 2:
        print("A dupla vencedora da rodada é: adversários!")
    if qm_ganhador == 4:
        print("A dupla vencedora da rodada é: adversários!")
    if qm_ganhador == 1:
        print("A dupla vencedora da rodada é: Sua!")
    if qm_ganhador == 3:
        print("A dupla vencedora da rodada é: Sua!")

def ganhador():
    global qm_ganhador
    for x in cartas_rodada:
        for i in cartas:
            if x == i:
                valor_rodada.append(bara[x])
                valor_rodada_sort.append(bara[x])
    valor_rodada_sort.sort()
    for k in valor_rodada:
        qm_ganhador += 1
        if valor_rodada_sort[-1] == k:
            break
    declara_campeao()

#####   Rodada 1    #####
        #Jogada1#
sua_jogada1()
if jogada_permitida:
    prints("Você",cartas1,jogada1)
    jogada_bot(cartas2)
    prints("Oponente 1",cartas2, escolha)
    jogada_bot(cartas3)
    prints("Seu aliado",cartas3, escolha)
    jogada_bot(cartas4)
    prints("Oponente 2",cartas4, escolha)
    print("...........................")
    ganhador()
    

    
    


        
        











    
