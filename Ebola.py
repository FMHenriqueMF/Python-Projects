from turtle     import*
from random import*
from time      import*

 ## -- chamar tela do Turtle -- ##
def a_primeira():                                                     #esconde a tartaruga inicial, para nao haver encomodo.
    ht()
    pu()
    goto(tamanhox + 20,tamanhoy + 20)
    
 ## -- limite do mapa -- ##
def anda_no_seu_quadrado():                                  #nao deixa as pessoas ultrapassarem o limite estipulado do mapa.
    for i in total:
        i.seth( randint(0,360) )                                      # faz cada um andar de forma randomica
        i.fd(10)
        x, y = i.pos()
        if x < -tamanhox or x > tamanhox or y < -tamanhoy or y > tamanhoy:
            i.goto (randint(-tamanhox,tamanhox),randint(-tamanhoy,tamanhoy))
            
 ## -- turtle faz quando nasce -- ##
def primeiros_passos(x, w):
    w.pu()
    w.ht()
    w.goto(randint(-tamanhox,tamanhox),randint(-tamanhoy,tamanhoy))
    w.st()
    w.color(x)
    w.shape("circle")
    w.speed(0)

print(" Bem vindo ao simulador de ebola. \n  Criado por: \n   ~Gustavo Trentin \n   ~Henrique Missel")

 ## -- variaveis -- ##
tamanhox = 370
tamanhoy = 270
graficox = tamanhox + 5
graficoy = tamanhoy - 400
a_primeira()
saudaveis_iniciais   =  int(input("Quantas pessoas serão saudáveis?\n"))
doentes_iniciais     =  int(input("Quantas pessoas terão a doença inicialmente?\n"))
contagio                =  int(input("Qual a porcentagem de contagio?(0, 100)\n"))
mortalidade           =  int(input("Qual a porcentagem da mortalidade da infecção?(0, 100)\n"))
durabilidade          =  int(input("Por quantas semanas a infecção dura?(até a pessoas adquirir imunidade)\n"))
tempoDaSemana = time()       #variavel criada para a semana passar apenas apos um tempo real determinado.
semana = 0                             #semana total, desde o comeco da simulacao.
semana_do_ano = 0                #semana do ano, ate 52 semanas depois volta ao comeco.

 ## -- listas --  ##
total               = []                #lista onde estao todas as pessoas vivas
saudaveis       = []                #lista onde estao as pessoas saudaveis
ebolas            = []                #lista onde estao as pessoas doentes
imunes           = []                #lista onde serao adicionadas pessoas que adquiriram imunidade a doenca
apagados       = []                #lista onde serao adicionadas as pessoas que morreram e serao apagadas
devem_nascer= []                #lista onde serao adicionadas as pessoas que deverao nascer pela procriacao
idade              = []                #diz a idade que a pessoa tem 
idade_imunes = []                #diz quando a pessoa virou imune, para depois serem feitas comparacoes
idade_ebolas  = []                #diz quando a pessoa ficou doente, para depois serem feitas comparacoes
birth               = []                #lista para ver quando a pessoa faz aniversario
graficos = []
 ## -- dicionarios -- ##
ebolasBirth  = {}                   #guardar o dia em que pegou a doenca, para depois ficar imune
imunesBirth = {}                   #guardar o dia em que virou imune, para depis ficar saudavel
plpBirth        = {}                  #aniversario dos saudaveis
plpAge         = {}                  #idade das pessoas

 ## -- grafico -- ##
def turtle_graficas():
    for t in range(4):
        graficos.append( Turtle() )
        graficos[t].pu()
        graficos[t].ht()
        graficos[t].goto(graficox,graficoy)
        graficos[t].st()
        graficos[t].shapesize(0.5)
        graficos[t].pd()

def criacao_grafico():
    constroi_grafico = Turtle()
    constroi_grafico.ht()
    constroi_grafico.pu()
    constroi_grafico.goto(graficox,graficoy)
    constroi_grafico.pd()
    constroi_grafico.goto(graficox + 100,    graficoy)
    constroi_grafico.goto(graficox,          graficoy)
    constroi_grafico.goto(graficox,          graficoy + 100)
    constroi_grafico.goto(graficox,          graficoy)
    graficos[0].color("blue")
    graficos[1].color("red")
    graficos[2].color("green")
    graficos[3].color("grey")
    
def atualiza_grafico(n, a):
    global graficox
    graficos[n].goto(graficox,graficoy + a)
    graficox = graficox + 1
    if graficox > tamanhox + 205:
        graficox = tamanhox + 5
        for i in graficos:
            i.clear()
            i.pu()
            i.goto(tamanhox + 5,graficoy + a)
            i.pd()
        

 ## -- criação dos doentes, saudaveis e lsita onde contem todos -- ##
delay(0)
for i in range(saudaveis_iniciais):            #cria a lista dos saudaveis.
    saudaveis.append( Turtle() )
for i in saudaveis:
    primeiros_passos("green", i)               #torna as pessoas verdes e as direciona a uma certa posicao randomica.

for j in range(doentes_iniciais):               #cria a lista dos doentes.
    ebolas.append( Turtle() )
for j in ebolas:
    primeiros_passos("red", j)                   #cria pessoas vermelha e as direciona a uma certa posicao randomica.
    idade_ebolas.append( 0 )                  
    ebolasBirth = dict(zip(ebolas, idade_ebolas))
    
total = saudaveis + ebolas                     #como ninguem nasce imune, no comeco o total sao as pessoas saudaveis + as infectadas

 ## -- idade populacional -- ##
for i in range (len(total)):
    idade.append(randint(1,49))                 #da uma idade randomica as pessoas iniciais, pois em uma populacao real a idade das pessoas variam 
    birth.append(randint(0,52))                  #diz quando a pessoas ira completar mais um ano de vida
plpAge = dict(zip(total, idade))                #adiciona ao dicionario a idade de uma pessoa
plpBirth = dict(zip(total, birth))                #adiciona ao dicionario o aniversario de uma pessoa


 ## -- aniversario e morte por idade -- ##
def aniver():
    global semana_do_ano                                                        #semanas do ano, vai ate 52
    aniversariantes = 0
    for i in total:
        semana_do_ano = semana_do_ano + 1
        if semana_do_ano == 53:                                                 #como o ano tem 52 semanas a cada vez que isso passa a semana volta ao inicio
            semana_do_ano = 0
        if (plpAge[i] < 50 and plpBirth[i]==semana_do_ano):        #verifica se a pessoas fez aniversario 
            plpAge[i] = plpAge[i] + 1
            aniversariantes = aniversariantes + 1
        if plpAge[i] >= 50:                                                             #verifica se a pessoas morre
            i.ht()
            i.goto(tamanhox +20,tamanhoy +20)                            #descarta a pessoa para longe
            apagados.append(i)                                                      #adiciona a uma lista pra depois serem apagadas
    ##--##
    if aniversariantes > 0:
        print(aniversariantes,"pessoa(s) comomemoraram(rou) aniversario nessa semana.")
    else:
        print("Ninguém fez aniversario essa semana")
    ##--##

 ## -- morte por ebola -- ##
def nao_ha_cura():
    for f in ebolas:
        if randint(1,100) <= mortalidade:         #ve se a pessoa ira morrer, lembrando que mortalidade e a fatalidade da doenca
            f.ht()
            f.goto(tamanhox + 20,tamanhoy +20)
            apagados.append(f)                       #adiciona as pessoas a uma lista para depois serem apagadas
            
 ## -- remocao das pessoas mortas -- ##
def bateu_as_botas():
    for i in apagados:                                   #a pessoa apagada estara no total, nos resta saber se ela e imune, doente ou saudavel
        if i in ebolas:
            ebolas.remove(i)
        elif i in saudaveis:
            saudaveis.remove(i)
        elif i in imunes:
            imunes.remove(i)
        if i in total:
            total.remove(i)
        apagados.remove(i)
                    
 ## -- cura da doença -- ##
def criou_imunidade(x):
    for t in ebolas:                                           # pega todos os doentes
        if ebolasBirth[t] + durabilidade <= x:
            imunes.append(t)                              # acrescenta no grupo dos imunes
            imunesBirth[t] = x
            t.color("gray")
            ebolas.remove(t)
            
 ## -- fim da imunidade -- ##
def mutacao_do_virus(x):
    for q in imunes:                                # pega todos os imunes
        if imunesBirth[q] + 52 <= x:          # verifica se ainda está imune
            saudaveis.append(q)
            q.color("green")
            imunesBirth.pop(q)
            imunes.remove(q)

 ## -- multiplicação populacional -- ##
def mais_um_no_mundo(x, y):
    if y < 300:                                          # verifica o tamanho da população
        for _ in range (y):                           # pega todo
            if randint(1,100) == 1:   
                devem_nascer.append( Turtle() )
        for i in devem_nascer:
            primeiros_passos("green", i)
            plpAge[i] = 0                              #nasce com 0 anos de idade
            plpBirth[i] = x                             #define a semana de aniversario de acordo com a semana em que nasceu
            total.append(i)
            saudaveis.append(i)
        for i in devem_nascer:
            devem_nascer.remove(i)

 ## - - infecção --  ##
def infectou(tempoDeInfeccao):
    x = 0
    for i in ebolas:                                                                     #pega todos dos ebolas
        for j in saudaveis:                                                            #pega todos dos saudaveis
            if i.distance(j) <  30 and randint (1, 100) <= contagio:  #verifica a distancia para ver se pega a doenca
                x = x + 1                                                                 #quantas pessoas foram infectadas na semana
                j.color("red")                                                          
                ebolas.append(j)
                ebolasBirth[j] = tempoDeInfeccao
                saudaveis.remove(j)
    print("Pessoas contaminadas na semana: ", x)

 ## -- ciclo -- ##
turtle_graficas()
criacao_grafico()
while True:
    delay(0)
    if tempoDaSemana + 1 < time():          # verifica já passou o a próxima semana
        anda_no_seu_quadrado()                 #faz as pessoas andarem sem sairem do espaco estipulado
        tempoDaSemana = time()                #atualiza o tempo
        semana = semana +1                       #se passou uma semana          
        print(" -- -- -- -- -- -- -- -- --")
        print("Semana: ", semana)
        print("Total de pessoas: ",len(total))
        infectou(semana)                                                           #varifica se a pessoa foi infectada
        print("Total de pessoas contagiadas: ",len(ebolas))
        criou_imunidade(semana)                                              #verifica se doença   passou
        mais_um_no_mundo(semana_do_ano, len(total))            #verifica se  nasceu  alguem
        nao_ha_cura()                                                                #verifica se a  doença matou
        bateu_as_botas()                                                            #tira todos os mortos das listas
        mutacao_do_virus(semana)
        aniver()
        atualiza_grafico(0,len(total))
        atualiza_grafico(1,len(ebolas))
        atualiza_grafico(2,len(saudaveis))
        atualiza_grafico(3,len(imunes))
        print(" -- -- -- -- -- -- -- -- -- ")
