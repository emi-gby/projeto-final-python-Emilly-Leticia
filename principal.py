
#define as cores para textos no terminal em  ANSI
cores = {'vermelho':'\033[31m', 'verde':'\033[32m','magenta':'\033[35m',
         'ciano':'\033[36m','finaliza_cor':'\033[0m'} 

livros = [
        {"id": 1, "titulo": "O Pequeno Prícipe", "autor": " Antoine de Saint-Exupéry", "disponibilidade": "Livro Disponível"},
        {"id": 2, "titulo": "1984", "autor": "George Orwell", "disponibilidade": "Livro Indisponível"},
        {"id": 3, "titulo": "Fahrenheit 451c", "autor": "Ray Bradburyl", "disponibilidade": "Livro Disponível"},
        {"id": 4, "titulo": "A Morte no Nilo", "autor": "Agatha Christie", "disponibilidade": "Livro Disponível"},
        {"id": 5, "titulo": "Alice no País das Maravilhas", "autor": "Lewis Carroll", "disponibilidade": "Livro Indisponível"},
        {"id": 6, "titulo": "Um Estudo em Vermelho ", "autor": "Arthur Conan Doyle", "disponibilidade": "Livro Indisponível"}
    ]

#set de ids para evitar repetição
id_set = set([item['id'] for item in livros])


def cadastrar_item():
    '''Adiciona livro com categorias (id,titulo/autor/disponibilidade) à lista de livros. '''
    livro = {}
    id = input('Digite o id do livro (número inteiro positivo): ').strip()
        
    id_verificado = verificar_id(id)
    if id_verificado == False:
        return

    livro['id'] = id_verificado

    titulo = input('Digite o título do livro: ').strip().capitalize()
    if verificar_nome_vazio('titulo', titulo) == False:
        return
    livro['titulo'] = titulo

    autor = input('Digite o(a) autor(a) do livro: ').strip().capitalize()
    if verificar_nome_vazio('autor', autor) == False:
        return
    livro['autor'] = autor

    status = input('O livro está disponível (S/N)? ').lower().strip()
    if status == 's':
        disponibilidade = 'Livro Disponível'
    elif status == 'n':
        disponibilidade = 'Livro Indisponível'
    else:
        print('-------------------------------')
        print(f'{cores['ciano']}A resposta deve ser somente "S" ou "N"!{cores['finaliza_cor']}')
        print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
        return
    
    livro['disponibilidade'] = disponibilidade
    livros.append(livro)
    print('-------------------------------')
    print(f'{cores['verde']}Cadastro realizado com sucesso!{cores['finaliza_cor']}')

def verificar_nome_vazio(categoria, palavra):
    '''Verifica se o input do usuario é vazio, se for, retorna False'''
    if len(palavra) == 0:
        print('-------------------------------')
        print(f'{cores['ciano']}O {categoria} não pode ser vazio!{cores['finaliza_cor']}')
        print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
        return False

def verificar_id(id):
    '''Verifica se o id fornecido é único e integer positivo.'''
    try:
        id = int(id)
        if id in id_set:
            print('-------------------------------')
            print(f'{cores['ciano']}Id já utilizado.{cores['finaliza_cor']}')
            print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
            return False
        if id < 0 :
            print('-------------------------------')
            print(f'{cores['ciano']}Id não pode ser negativo.{cores['finaliza_cor']}')
            print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
            return False
        
    except ValueError:
        print('-------------------------------')
        print(f'{cores['ciano']}Id do livro só pode conter números inteiros!{cores['finaliza_cor']}')
        print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
        return False

    
    return id

def listar_livros():
    '''Lista todos os plivros.'''
    for livro in livros:
        for categoria, resultado in livro.items():
            print(f'{cores['magenta']}{categoria}{cores['finaliza_cor']} : {cores['ciano']}{resultado}{cores['finaliza_cor']}')
        print('-------------------------------')

def buscar_livro(item_id):
    '''Busca o id fornecido na lista de livros e retorna o livro se o id corresponder'''

    try:
        item_id = int(item_id)
        #itera sobre a lista de livros e procura em cada item se o valor inserido corresponde ao valor da chave 'id' do dicionario
        for livro in livros:
            if livro['id'] == item_id:
                print('-------------------------------')
                print(f'{cores['verde']}Produto encontrado. \nInformações sobre: {cores['finaliza_cor']}')
                for categoria, resultado in livro.items():
                    print(f'{cores['magenta']}{categoria}{cores['finaliza_cor']} : {cores['ciano']}{resultado}{cores['finaliza_cor']}')
                return livro
            
        print('-------------------------------')    
        print(f'{cores['vermelho']}Produto não encontrado. Tente novamente.{cores['finaliza_cor']}')
        return None

    except ValueError:
        print('-------------------------------')
        print(f'{cores['vermelho']}Valor inserido tem que ser inteiro! Tente Novamente.{cores['finaliza_cor']}')
        return None
    
def atualizar_item():
    '''Atualiza as categorias do livro de acordo com a opção inserida.'''
    item_id = input('Digite o id do livro que deseja atualizar: ').strip()
    livro = buscar_livro(item_id)

    if livro == None:
        return
    
    categoria_atualizar = input('Que categoria deseja atualizar (id,titulo/autor/disponibilidade)? ').lower().strip() 

    if categoria_atualizar in ['id','titulo','autor','disponibilidade']:
        print(f'{categoria_atualizar.capitalize()} Atual : {livro[categoria_atualizar]}')

    else:
        print('-------------------------------')
        print(f'{cores['vermelho']}Categoria inválida no sistema! Tente Novamente.{cores['finaliza_cor']}')
        return

    valor_atualizado = input('Deseja atualizar para qual valor? ').strip().capitalize()

    if categoria_atualizar == 'id':
        id_verificado = verificar_id(valor_atualizado)
        if id_verificado == False:
            return
        print(f'{categoria_atualizar.capitalize()} Atual : {livro[categoria_atualizar]}')
        livro[categoria_atualizar] = id_verificado

    elif categoria_atualizar == 'disponibilidade':
        if valor_atualizado == 'S':
            disponibilidade = 'Livro Disponível'
        elif valor_atualizado == 'N':
            disponibilidade = 'Livro Indisponível'
        else:
            print('-------------------------------')
            print(f'{cores['ciano']}A resposta deve ser somente "S" ou "N"!{cores['finaliza_cor']}')
            print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
            return
        
        livro['disponibilidade'] = disponibilidade

    else:
        if verificar_nome_vazio(categoria_atualizar, valor_atualizado) == False:
            return
        livro[categoria_atualizar] = valor_atualizado
        
    print('-------------------------------')
    print(f'{cores['verde']}Atualização realizada com sucesso!{cores['finaliza_cor']}')



def remover_item():
    '''Remove o livro da lista de livros a partir do 'id' inserido.'''
    item_id = input('Digite o id do livro que deseja remover: ').strip()
    livro = buscar_livro(item_id)

    if livro == None:
        return

    livros.remove(livro)
    print('-------------------------------')
    print(f'{cores['verde']}Livro removido com sucesso!{cores['finaliza_cor']}')


def gerar_relatorio():
    '''Apresenta o relatório desejado de acordo com o tipo de relatório escolhido.'''
    print("------ RELATÓRIOS ------")
    print('Você deseja visualizar:')
    print("1 - Livros cadastrados")
    print("2 - Livros por Autor")
    print("3 - Livros Disponiveis e não disponiveis")
    print("0 - Voltar")
    print('-------------------------------')

    escolha_usuario = input('Escolha uma opção: ').strip()

    if escolha_usuario == '1':
        for livro in livros:
            print(f'id-{cores['magenta']}{livro['id']}{cores['finaliza_cor']} : {cores['ciano']}{livro['titulo']}{cores['finaliza_cor']}')
    elif escolha_usuario == '2':
        for livro in livros:
            print(f'id-{cores['magenta']}({livro['id']}) = {livro['titulo']}{cores['finaliza_cor']} : {cores['ciano']}{livro['autor']}{cores['finaliza_cor']}')
    elif escolha_usuario == '3':
        for livro in livros:
            print(f'id-{cores['magenta']}({livro['id']}) = {livro['titulo']}{cores['finaliza_cor']} : {cores['ciano']}{livro['disponibilidade']}{cores['finaliza_cor']}')
    elif escolha_usuario == '0':
        return
    
    else:
        print(f'{cores['vermelho']}Não existe essa opção em nosso sistema! Escolha outra. {cores['finaliza_cor']}')



def menu():
    '''Printa o menu principal do sistema e retorna a opção escolhida.'''
    print('-------------------------------')
    print('------ Sistema de Livros ------')
    print('-------------------------------')
    print('Você deseja:')
    print('1- Cadrastar Livro')
    print('2- Listar Livros')
    print('3- Atualizar Livro')
    print('4- Remover Livro')
    print('5- Gerar Relatório')
    print('6- Sair do Programa')
    print('-------------------------------')

    opcao = input('Escolha uma opção: ').strip()

    print('-------------------------------')

    return opcao    

while True:
    escolha_usuario = menu()
    
    if escolha_usuario == '1':
        cadastrar_item()
    elif escolha_usuario == '2':
        listar_livros()
    elif escolha_usuario == '3':
        atualizar_item()
    elif escolha_usuario == '4':
        remover_item()
    elif escolha_usuario == '5':
        gerar_relatorio()
    elif escolha_usuario == '6':
        print(f'{cores['verde']}Sistema finalizado!{cores['finaliza_cor']}')
        break
    else:
        print(f'{cores['vermelho']}Não existe essa opção em nosso sistema! Escolha outra. {cores['finaliza_cor']}')