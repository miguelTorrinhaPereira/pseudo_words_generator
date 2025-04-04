from random import choices


# bom
def tratamento(s):
    # separa em carácteres para poder ser feito o tratamento
    letras = list(s)

    # retira carácteres não letras
    i = 0
    while i < len(letras) - 1:
        if 'a' <= letras[i] <= 'z' or 'à' <= letras[i] <= 'ú' or (letras[i] == ' ' and letras[i + 1] != ' '):
            i += 1
        else:
            if 'A' <= letras[i] <= 'Z' or 'À' <= letras[i] <= 'Ú':
                letras[i] = chr(ord(letras[i]) + 32)
                i += 1
            else:
                del [letras[i]]

    # passa as letras para uma lista de palavras
    palavras = []
    indexAtual = 0
    for i in range(len(letras)):
        if letras[i] == ' ':
            palavras += ['']
            for j in range(i - indexAtual):
                palavras[-1] += letras[indexAtual + j]
            indexAtual = i + 1


    i,j = 0,0
    while i < len(palavras):
        if palavras[i].lower() == 'maias':
            del(palavras[i])
            j+=1
        i+=1
    print(j)
    return palavras

# bom
def silabas(palavras):
    # tira as sílabas e cria uma lista com elas
    silabas = []
    silabas_iniciais = []
    for i in palavras:
        if len(i) < 4: # evita palavra menores que 4, sendo que estás ou dão erro na função ou influência negativamente os resultados do gerador
            continue
        silabas_iniciais += [i[:3]]
        for j in range(1,len(i) - 2):
            silabas += [i[j:j+3]]

    return silabas,silabas_iniciais

# bom
def frequencias(silabas_lista):
    # cria um dicionário da frequência das sílabas
    frequencias = {}
    for silaba in silabas_lista:
        if silaba in frequencias.keys():
           frequencias[silaba] += 1 # caso a silaba já esteija no dicionário, acrescenta um
        else :
            frequencias[silaba] = 1 # caso não esteija, acrejenta a silaba ao dicionário

    return frequencias

# bom
def ligações(silabas_lista):
    # cria um dicionário com as ligações

    liga = {}
    for i in silabas_lista:
        liga[i] = []
        fim = i[1:]
        for j in silabas_lista:
            if fim == j[:2]:
                liga[i] += [j]

    # é necessário passar silabas_lista porque silabas_lista da função não comtêm repetidos
    return liga , silabas_lista

# bom
def tamanho_palavras(palavras):
    # conta a quantidade de palavras para cada tamanho
    tamanhos = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    quantidade = 0

    for i in palavras:
        tamanho = len(i)
        if 3 < tamanho < 17 :
            tamanhos[tamanho - 4] += 1
            quantidade += 1

    # calcula as percentagens
    for i in range(len(tamanhos)):
        tamanhos[i] = (tamanhos[i] / quantidade ) * 100

    return tamanhos

#bom
def processar(s):
    print ('tratamento\n')
    palavras = tratamento(s)

    print('silabas\n')
    silabas_l,silabas_i_l = silabas(palavras)

    print('frequencias\n')
    frequencias_d = frequencias(silabas_l)
    frequencias_i_d = frequencias(silabas_i_l)

    print('ligações\n')
    ligações_d , silabas_l  = ligações(list(set(silabas_l)))
    ligações_i_d, silabas_i_l = ligações(list(set(silabas_i_l)))

    print('tamanho\n')
    tamanhos = tamanho_palavras(palavras)

    return [silabas_i_l, frequencias_i_d, ligações_i_d, frequencias_d, ligações_d, tamanhos]




# bom
def contem(palavra,l):
    for char in l:
        if char in palavra:
         return True
    return False
def duplicado(palavra,l):
    j = 0
    for i in palavra:
        if i in l:
            j += 1
    if j > 1:
        return True
    return False

#bom
def filtrar(escrever):

    file = open('pseudo_palavras.txt', 'r')
    palavras = file.readline()

    palavras = palavras.split(' ')

    t1 = len(palavras) # regista o tamanho inicial

    # filtra
    i = 0
    while i < len(palavras):
        if teste_palavras(palavras[i]):
            print(palavras[i])
            del (palavras[i])
        else:
            i += 1

    t2 = len(palavras) # regista o tamanho final

    print('\n eliminadas', (t1 - t2), 'palavras') # quantas palavras foram eliminadas
    print('de', t1, 'para', t2,'\n') # o tamanho

    if escrever:
        palavras = ' '.join(palavras)

        file = open('pseudo_palavras.txt', 'w')
        file.write(palavras)

    file.close()


def teste_palavras(p):
    lista_final = ['q','w','t','y','p','d','f','g','h','j','k','ç','z','x','c','v','b','n','r','s','l','m']

    if      p[-1] in ['â', 'ô', 'ê', 'ã', 'õ', 'é', 'è', 'ú', 'ù', 'û','p','q','w','b','t','y','d','f','g','h','j','k','ç','x','c','v','n'] \
        or (p[-2:] not in ['ns'] and p[-1] in lista_final and p[-2] in lista_final) \
        or contem(p, ['th', 'zs', 'zm', 'dm', 'dn', 'w', 'k', 'gd', 'gh', 'qe', 'quê', 'ps', 'pn','qu','mn','nm'
                        ,'rm','sh','çae','tm','mt','ms','não','qué','bm','ãa','bs','bd','y','mf','mv','cb','cx','pt'
                        ,'tã','dj','à','pb','ft','tf','ft''xv','vx','df','ée','eé','ôo','oô']) \
        or duplicado(p, ['ç']) \
        or duplicado(p, ['á', 'à', 'â', 'é', 'è', 'ê', 'ó', 'ò', 'í', 'ì', 'î', 'ú', 'ù', 'û', 'ã', 'õ'])\
        or p[:2] == 'lh':
        return True

    # confirma se não tem letras repetidas pegadas exeto ss e rr
    for i in range(len(p) - 1):
        if p[i] == p[i + 1] and p[i] not in ['s', 'r']:
            return True
    # evita qualquer h com uma letra antes que não seja c,n,l
    for i in range(1,len(p)):
        if p[i] == 'h' and p[i-1] not in ['c','n','l']:
            return True
    # evita palavras com quatro vogas de seguida
    v = ['a','e','i','o','u','á', 'à', 'â', 'é', 'è', 'ê', 'ó', 'ò', 'í', 'ì', 'î', 'ú', 'ù', 'û', 'ã', 'õ']
    for i in range(len(p)-2):
        if p[i] in v and p[i+1] in v and p[i+2] in v:
            return True
    # remove palavras que tem ção ou çõe no meio da palavra
    if 'ção' in p[:-1] or 'ções' in p[:-1]:
        return True
    return False

# bom
def gerar_pseudo_palavras(quantidade):

    def inicia_variaveis():
        fich = open('info_gerador_de_palavras.txt','r',encoding='UTF-16')
        vars = fich.read()
        fich.close()

        vars = vars.split('\n')
        silabas_i_l2 = eval(vars[0])
        frequencias_i_d2 = eval(vars[1])
        ligações_i_d2 = eval(vars[2])
        frequencias_d2 = eval(vars[3])
        ligações_d2 = eval(vars[4])
        tamanhos2 = eval(vars[5])

        return silabas_i_l2,frequencias_i_d2,ligações_i_d2,frequencias_d2,ligações_d2,tamanhos2

    #bom
    def calc_probabilidades(silabas, frequencias_dicionário):
        # função que calcula as probabilidads

        #calcula a soma das frequencias
        total = 0
        for i in silabas:
            total += frequencias_dicionário[i]

        # calculas probabilidades
        probabilidades = []
        for i in range(len(silabas)):
            probabilidades += [(frequencias_dicionário[silabas[i]] / total) * 100]

        return probabilidades

    #bom
    def nova_silaba(ligações_d,frequencias_d,ultima_silaba):
        if ligações_d.get(ultima_silaba):
            vizinhos = ligações_d[ultima_silaba]
            probrabilidades_vizinhos = calc_probabilidades(vizinhos,frequencias_d)
            return choices(vizinhos,weights=probrabilidades_vizinhos)[0]
        else:
            return 0

    #bom
    def nova_palavra(tamanho):

        #começa a palavra
        palavra = choices(silabas_i_l, weights=probabilidades_i)[0]
        ultima_silaba = palavra

        # segunda silaba
        ultima_silaba = nova_silaba(ligações_i_d,frequencias_i_d,ultima_silaba)
        if ultima_silaba == 0:
            return nova_palavra(tamanho)
        palavra += ultima_silaba[2:]

        # cria o resto da palavra
        for j in range(tamanho-4):

            ultima_silaba = nova_silaba(ligações_d, frequencias_d, ultima_silaba)
            if ultima_silaba == 0:
                return nova_palavra(tamanho)
            palavra += ultima_silaba[2:]


        return palavra

    #bom
    def tratamento_final(palavras):

        print('\n a remover multiplos')
        t1 = len(palavras)
        palavras = list(set(palavras))
        t2 = len(palavras)
        print('iliminadas', (t1 - t2), 'palavras')  # quantas palavras foram eliminadas
        print('de', t1, 'para', t2, '\n')  # o tamanho

        print('a ordenar\n')
        palavras.sort()

        print('a converter para string\n')
        palavras = ' '.join(palavras)

        return palavras




    print('A gerar palavras \n')
    g = 0

    silabas_i_l, frequencias_i_d, ligações_i_d, frequencias_d, ligações_d, tamanhos = inicia_variaveis()

    probabilidades_i = calc_probabilidades(silabas_i_l,frequencias_i_d)

    palavras = []

    # gerar palavras
    for i in range(quantidade):

        # escolhe o tamalho da palavra
        tamanho = choices(range(4,17), tamanhos)[0]

        # adiciona uma palavra á lista
        palavra = nova_palavra(tamanho)
        while teste_palavras(palavra):
            palavra = nova_palavra(tamanho)

        palavras += [palavra]

        #escreve a palavra
        g += 1
        #print(g)

    # tratamento final
    palavras = tratamento_final(palavras)

    # guardar palavras
    f = open('peseudo_palavras.txt', 'w', encoding='UTF-16')
    f.write(palavras)
    f.close()

def analisar():
    fich = open('livro_peseudo_palavras.txt','r',encoding='UTF-16')
    text = fich.read()
    fich.close()

    vars = processar(text)

    fich = open('info_gerador_de_palavras.txt','w',encoding='UTF-16')
    for var in vars:
        fich.write(var.__repr__()+'\n')
    fich.close()

gerar_pseudo_palavras(200)
