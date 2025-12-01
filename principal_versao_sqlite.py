import sqlite3

#define as cores para textos no terminal em  ANSI
cores = {'vermelho':'\033[31m', 'verde':'\033[32m','magenta':'\033[35m',
         'ciano':'\033[36m','finaliza_cor':'\033[0m'} 


class SistemaLivros():
    def __init__(self):

        # Inicia a conexão com o banco de dados SQLite
        self.db_nome = "livros.db"
        self.conn = sqlite3.connect(self.db_nome)
        self.conn.row_factory = sqlite3.Row   # <--- Faz as linhas do sql se comportarem como dicionários
        self.cursor = self.conn.cursor()
        self.cria_table()

        self.inicia_sistema()


    def cria_table(self):
        """Cria a table do sistema se ainda não existir"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                disponibilidade TEXT NOT NULL
            )
        """)

        self.conn.commit()
        

    def cadastrar_item(self):
        '''Adiciona livro com categorias (id,titulo/autor/disponibilidade) à lista de livros. '''

        titulo = input('Digite o título do livro: ').strip().capitalize()
        if self.verificar_nome_vazio('titulo', titulo) == False:
            return
        
        autor = input('Digite o(a) autor(a) do livro: ').strip().capitalize()
        if self.verificar_nome_vazio('titulo', autor) == False:
            return
        
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
        
        # Adiciona livro no banco de dados
        self.cursor.execute('INSERT INTO livros (titulo, autor, disponibilidade) VALUES (?, ?, ?)', (titulo, autor, disponibilidade))
        self.conn.commit()

        print('-------------------------------')
        print(f'{cores['verde']}Cadastro realizado com sucesso!{cores['finaliza_cor']}')

    def verificar_nome_vazio(self,categoria, palavra):
        '''Verifica se o input do usuario é vazio, se for, retorna False'''
        if len(palavra) == 0:
            print('-------------------------------')
            print(f'{cores['ciano']}O {categoria} não pode ser vazio!{cores['finaliza_cor']}')
            print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
            return False

    def listar_livros(self):
        '''Lista todos os livros.'''
        self.cursor.execute('SELECT * FROM livros')  #Busca livros na database
        livros = self.cursor.fetchall()  #Armazena a lista de livros em uma variável
        
        if len(livros) == 0:
            print('-------------------------------')
            print(f'{cores['verde']}Nenhum livro cadastrado.{cores['finaliza_cor']}')

        for livro in livros:
            for categoria in livro.keys():
                print(f'{cores['magenta']}{categoria}{cores['finaliza_cor']} : {cores['ciano']}{livro[categoria]}{cores['finaliza_cor']}')
            print('-------------------------------')
            
        
    def atualizar_item(self):
        '''Atualiza as categorias do livro de acordo com a opção inserida.'''
        try:
            item_id = int(input('Digite o id do livro que deseja atualizar: '))

            self.cursor.execute('SELECT * FROM livros WHERE id = ?', (item_id,))
            livro_selecionado = self.cursor.fetchone()  

            if livro_selecionado == None:
                print('-------------------------------')    
                print(f'{cores['vermelho']}Produto não encontrado. Tente novamente.{cores['finaliza_cor']}')
                return 


            if livro_selecionado:
                categoria_atualizar = input('Que categoria deseja atualizar (titulo/autor/disponibilidade)? ').lower().strip()

                if categoria_atualizar in ['titulo','autor','disponibilidade']:
                    print(f'{categoria_atualizar.capitalize()} Atual : {livro_selecionado[categoria_atualizar]}')

                    valor_atualizado = input('Deseja atualizar para qual valor? ').strip().capitalize()
                    if self.verificar_nome_vazio(categoria_atualizar, valor_atualizado) == False:
                        return
                    
                    if categoria_atualizar == 'disponibilidade':
                        if valor_atualizado == 'S':
                            valor_atualizado = 'Livro Disponível'
                        elif valor_atualizado == 'N':
                            valor_atualizado = 'Livro Indisponível'
                        else:
                            print('-------------------------------')
                            print(f'{cores['ciano']}A resposta deve ser somente "S" ou "N"!{cores['finaliza_cor']}')
                            print(f'{cores['vermelho']}Cadastro Interrompido! Tente Novamente.{cores['finaliza_cor']}')
                            return

                    sql = f'UPDATE livros SET {categoria_atualizar} = ? WHERE id = ?'
                    self.cursor.execute(sql, (valor_atualizado, item_id))

                    self.conn.commit()

                    print('-------------------------------')
                    print(f'{cores['verde']}Atualização realizada com sucesso!{cores['finaliza_cor']}')

                else:
                    print('-------------------------------')
                    print(f'{cores['vermelho']}Categoria inválida no sistema! Tente Novamente.{cores['finaliza_cor']}')
                    return
                

        except ValueError:
            print('-------------------------------')
            print(f'{cores['vermelho']}Valor inserido tem que ser inteiro! Tente Novamente.{cores['finaliza_cor']}')



    def remover_item(self):
        '''Remove o livro da lista de livros a partir do 'id' inserido.'''
        try: 
            item_id = int(input('Digite o id do livro que deseja remover: '))

            self.cursor.execute('SELECT * FROM livros WHERE id = ?', (item_id,))
            livro_selecionado = self.cursor.fetchone()  

            if livro_selecionado == None:
                print('-------------------------------')    
                print(f'{cores['vermelho']}Produto não encontrado. Tente novamente.{cores['finaliza_cor']}')
                return 
            

            if livro_selecionado:
                #deleta o livro selecionado no banco de dados
                self.cursor.execute('DELETE FROM livros WHERE id = ?', (item_id,))
                self.conn.commit()

                print('-------------------------------')
                print(f'{cores['verde']}Livro removido com sucesso!{cores['finaliza_cor']}')

        except ValueError:
            print('-------------------------------')
            print(f'{cores['vermelho']}Valor inserido tem que ser inteiro! Tente Novamente.{cores['finaliza_cor']}')


    def gerar_relatorio(self):
        '''Apresenta o relatório desejado de acordo com o tipo de relatório escolhido.'''
        print("--------- RELATÓRIOS ---------")
        print('Você deseja visualizar:')
        print("1 - Livros cadastrados")
        print("2 - Livros por Autor")
        print("3 - Livros Disponiveis e não disponiveis")
        print("0 - Voltar")
        print('-------------------------------')

        escolha_usuario = input('Escolha uma opção: ').strip()

        self.cursor.execute('SELECT * FROM livros')
        livros = self.cursor.fetchall()

        if escolha_usuario == '1':
            for livro in livros:
                print(f'id-({cores['magenta']}{livro['id']}{cores['finaliza_cor']}) : {cores['ciano']}{livro['titulo']}{cores['finaliza_cor']}')
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



    def menu(self):
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
    
    def inicia_sistema(self):
        while True:
            escolha_usuario = self.menu()
            
            if escolha_usuario == '1':
                self.cadastrar_item()
            elif escolha_usuario == '2':
                self.listar_livros()
            elif escolha_usuario == '3':
                self.atualizar_item()
            elif escolha_usuario == '4':
                self.remover_item()
            elif escolha_usuario == '5':
                self.gerar_relatorio()
            elif escolha_usuario == '6':
                print(f'{cores['verde']}Sistema finalizado!{cores['finaliza_cor']}')
                self.conn.close()
                break
            else:
                print(f'{cores['vermelho']}Não existe essa opção em nosso sistema! Escolha outra. {cores['finaliza_cor']}')

    


if __name__ == '__main__':
    app = SistemaLivros()
