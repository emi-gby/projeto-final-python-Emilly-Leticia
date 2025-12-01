# projeto-final-python-Emilly-Leticia


# 📚 **Sistema de Controle de Livros**

Sistema simples e interativo no terminal que tem como objetivo o gerenciamento de livros. O sistema permite cadastrar, visualizar, atualizar e remover livros, de forma que implementa as operações principais de um CRUD (Create, Read, Update, Delete).

--- 

## ⚙️ **Funcionalidades do Sistema**

- **Menu principal**: O sistema mostra um menu com 6 opções.
    
- **Cadastrar livro(1):** Adiciona um novo livro com informações de id, título, autor e disponibilidade (Disponível ou Indisponível) ao sistema.
    
- **Listar livros(2):** Mostra os livros cadastrados e suas respectivas categorias (id, titulo, autor, disponibilidade).
    
- **Atualizar livro(3):** Atualiza informações de um livro escolhido pelo usuário.
    
- **Remover livro(4):** Remove livro escolhido pelo id da lista de livros.
    
- **Gerar Relatório(5):** Oferece três tipos de relatórios automáticos:
    
    1. Livros cadastrados
        
    2. Livros por Autor
        
    3. Livros Disponíveis e Não disponíveis
        
- **Sair(6):** Fecha o programa.


---

## 💡**Funcionamento geral**

O sistema é totalmente interativo e executado diretamente no terminal. Ele garante que cada produto possua um código único, utilizando validações de dados para evitar erros durante o cadastro. A aplicação usa listas para armazenar dinamicamente as informações dos livros e conjuntos (_sets_) para assegurar a exclusividade dos códigos. O código inicial traz uma lista com livros previamente registrados.

---

## 👩🏽‍💻**Detalhes Técnicos**

- **Controle de Cores**: O sistema usa códigos ANSI para colorir o texto no terminal, tornando a interface mais amigável e visualmente agradável.
    
- **Tratamento de Erros**: Há validação para entradas de dados, como verificar se o título ou autor não estão vazios, e garantir que a disponibilidade seja apenas 'S' ou 'N'.

---

## 📋**Exemplo do Menu**

```
-------------------------------
------ Sistema de Livros ------
-------------------------------
Você deseja:
1- Cadrastar Livro
2- Listar Livros
3- Atualizar Livro
4- Remover Livro
5- Gerar Relatório
6- Sair do Programa
-------------------------------
Escolha uma opção: 
```

---

## 💻**Exemplos de Uso**

Exemplo 1: Cadastrar livro.
```
Escolha uma opção: 1
-------------------------------
Digite o id do livro (número inteiro positivo): 10
Digite o título do livro: Assassinato no Expresso Oriente
Digite o(a) autor(a) do livro: Agatha Christie
O livro está disponível (S/N)? s
-------------------------------
Cadastro realizado com sucesso!
-------------------------------
```

Exemplo 2: Gerar Relatório- Livros por Autor

```
Escolha uma opção: 5
-------------------------------
------ RELATÓRIOS ------
Você deseja visualizar:
1 - Livros cadastrados
2 - Livros por Autor
3 - Livros Disponiveis e não disponiveis
0 - Voltar
-------------------------------
Escolha uma opção: 2
id-(1) = O Pequeno Prícipe :  Antoine de Saint-Exupéry
id-(2) = 1984 : George Orwell
id-(3) = Fahrenheit 451 : Ray Bradburyl
id-(4) = A Morte no Nilo : Agatha Christie
id-(5) = Alice no País das Maravilhas : Lewis Carroll
id-(6) = Um Estudo em Vermelho  : Arthur Conan Doyle
id-(10) = Assassinato no expresso oriente : Agatha christie
-------------------------------
```

---

---

## 📚 **Sistema de Controle de Livros - versão Sqlite**

Sistema simples de gerenciamento de livros utilizando Python e SQLite. 

## 💥 **Diferenciais**

- **Banco de Dados SQLite**: O sistema utiliza um banco de dados SQLite chamado `livros.db`. Ele armazena as informações dos livros em uma tabela chamada `livros`, com as colunas `id`, `titulo`, `autor` e `disponibilidade`.


## 💫 **Requisitos**

- **Python 3.x**
    
- **Biblioteca `sqlite3`** (incluída no Python por padrão)


---

## 👥 Contribuidores

|Nome|GitHub|
|---|---|
|Emilly Barbosa|[https://github.com/emi-gby](https://github.com/emi-gby)|
|Letícia Leandro|[https://github.com/MusMus19Leh](https://github.com/MusMus19Leh)|
