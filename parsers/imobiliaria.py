from xml.dom.minidom import parse

dom = parse("imobiliaria.xml")


imobiliaria = dom.documentElement


imoveis = imobiliaria.getElementsByTagName("imovel")

id_imovel = 0

for imovel in imoveis:
    id_imovel += 1
    nome = imovel.getElementsByTagName("nome")[0].firstChild.nodeValue.strip()
    print(f'{id_imovel} - {nome}')

id_escolhido = int(input("Digite o número do imóvel que deseja saber mais: "))
imovel = imoveis[id_escolhido-1]    
print("\n")


for imovel in imoveis:
    nome = imovel.getElementsByTagName("nome")[0]
    descricao = imovel.getElementsByTagName("descricao")[0]
    preco = imovel.getElementsByTagName("preco")[0]
    endereco = imovel.getElementsByTagName("endereco")[0]
    tamanho = imovel.getElementsByTagName("tamanho")[0]
    numQuartos = imovel.getElementsByTagName("numquartos")[0]
    numBanheiros = imovel.getElementsByTagName("numbanheiros")[0]