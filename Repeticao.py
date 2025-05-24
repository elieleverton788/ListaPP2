"""Questão 12"""

"""
idademenor = 999999999999999999999999999999999999
idademaior = 0
velho = ""
jovem = ""
while True:
    idade = input("Digite a idade de uma pessoa: ")
    idade = int(idade)
    if idade == 0:
        break
    nome = input("Digite o nome dessa pessoa: ")
    if idade < idademenor:
        idademenor = idade
        jovem = nome
    if idade > idademaior:
        idademaior = idade
        velho = nome
    print("A/s maior/es idade/s foi/foram de: "+velho)
    print("A/s menor/es idade/s foi/foram de: "+jovem)
"""

"""Questão 13"""

"""
soma = 0
for x in range(1, 50):
    print(soma)
    if (x%2) == 0:
        soma = x+soma
"""

"""Questão 14"""


"""qtdhomens = 0
qtdmulheres = 0
qtdcrianca = 0
mediahomens = 0
mediaidade = 0
mediamulheres = 0
mnrenda = 99999999999999999999999999999999
nomerenda = ""
qtddesempregados = 0
cont = 0
while True:
    cont = cont+1
    nome = input("Digite seu nome: ")
    nome = nome.upper()
    if nome == "FIM":
        break
    while True:
        idade = input("Digite sua idade caso esteja entre 0 e 100: ")
        idade = int(idade)
        if idade <= 0 or idade > 100:
            print("Digite outra idade")
        else:
            break
    while True:
        sexo = input("Qual o seu sexo, M - Masculino ou F - Feminino: ")
        sexo = sexo.upper()
        sexo = sexo.replace(" ","")
        if sexo != "M" and sexo != "F":
            print("Só aceitam masculino ou feminino")
        else:
            break
    while True:
        trabalha = input("Digite V - Verdadeiro caso trabalhe e F - Falso caso não: ")
        trabalha = trabalha.upper()
        trabalha = trabalha.replace(" ","")
        if trabalha != "V" and trabalha != "F":
            print("Só V ou F")
        else:
            break
    salario = input("Quanto você recebe de salário mínimo: ")
    salario = salario.replace(",",".")
    salario = float(salario)
    if sexo == "M":
        qtdhomens = qtdhomens+1
    if sexo == "F":
        qtdmulheres = qtdmulheres+1
    if idade < 18 and trabalha == "V":
        qtdcrianca = qtdcrianca+1
    if sexo == "M":
        mediahomens = mediahomens+salario
    if sexo == "F":
        mediamulheres = mediamulheres+salario
    if salario < mnrenda:
        mnrenda = salario
        nomerenda = nome
    if trabalha == "F":
        qtddesempregados = qtddesempregados+1
    mediaidade = mediaidade+idade
    print("Digite 'FiM' em nome para não adicionar outra pessoa.")
mediaidade = mediaidade/cont
mediahomens = mediahomens/cont
mediamulheres = mediamulheres/cont
print("O número de homens na pesquisa foi: "+str(qtdhomens))
print("A quantidade de mulheres foi: "+str(qtdmulheres))
print("A quantidade de pessoas menores de 18 que trabalham é: "+str(qtdcrianca))
print("A renda média dos homens é: "+str(mediahomens))
print("A renda média das mulheres é: "+str(mediamulheres))
print("O nome e Renda da pessoa que trabalha e que tem a menor renda é respectivamente: "+str(nomerenda)+", "+str(mnrenda))
print("A Quantidade de pessoas que não trabalham é: "+str(qtddesempregados))
print("A média de idade dos entrevistados é: "+str(mediaidade))


"""Questão 15"


"""fibantt = 0
fibant = 1
fib = 0
for x in range(1,15):
    print(fib)
    fib = fibant+fibantt
    fibantt = fibant
    fibant = fib
"""

"""Questão 16"""

"""
v = input("Digite um valor inteiro")
v = int(v)
z = 1
soma = 0
for x in range(25, 0, -1):
    soma = soma+(v**x/z)
    print(soma)
    z = z+1
"""

"""Questão 17"""

"""
homidade = -99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
mulidade = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
media = 0
qtdclientes = input("Quantos clientes seram analisados? ")
qtdmulher = 0
qtdacesso = 0
qtdclientes = int(qtdclientes)
for x in range(1,qtdclientes+1):
    nome = input("Qual o nome do cliente "+str(x)+"? ")
    while True:
        sexo = input("Qual o sexo do cliente: M - Masculino ou F - Feminino")
        sexo = sexo.upper()
        sexo = sexo.replace(" ","")
        if sexo != "M" and sexo != "F":
            print("Site não inclusivo: M - Masculino ou F - Feminino")
        else:
            break
    idade = input("Qual a idade do cliente "+str(x)+"? ")
    idade = int(idade)
    while True:
        net = input("O cliente "+str(x)+" tem acesso a internet: Digite S - Sim ou N - Não")
        net = net.upper()
        net = net.replace(" ","")
        if net != "S" and net != "N":
            print("Digite apenas: S - Sim ou N - Não ")
        else:
            break
    if sexo == "F":
        qtdmulher = qtdmulher+1
    media = idade+media
    if net == "S":
        qtdacesso = qtdacesso+1
    if idade > homidade and sexo == "M" and net == "S":
        zomem = nome
        homidade = idade
    if idade < mulidade and sexo == "F" and net == "S":
        zuie = nome
        mulidade = idade
media = media/qtdclientes
print("A média das idades dos clientes é: "+str(media))
print("Tem um total de "+str(qtdmulher)+" mulheres")
print("Um total de "+str(qtdacesso)+" tem acesso a internet")
print("Nome do homem mais velho: "+zomem+", Idade: "+str(homidade))
print("Nome da mulher mais nova: "+zuie+", Idade: "+str(mulidade))"""
