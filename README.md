# DadosSaúde

## Sobre

DadosSaúde é um pequeno site desenvolvido em um projeto apenas para fins de apresentação de alguns dos dados coletados durante a disciplina de quarto período INF1032, Introdução à Ciência dos Dados, da PUC-RJ, ministrada pelo professor Helio Cortes Vieira Lopes.

O tema escolhido para o trabalho foi a investigação da existência de predisposição de doenças crônicas por região do Brasil. Para cada subcategoria de doenças crônicas, o site apresenta gráficos e uma linha do tempo interativa que mostra em um mapa do Brasil, em cada ano relevante de nossa pesquisa, como as ocorrências dessas doenças variou nessas regiões.

O projeto foi feito em Django usando também partes do template de layout fornecido pelo projeto didático [StudyBuddy](https://github.com/divanov11/StudyBud/).

## Instalando o Projeto

### Criar uma venv

Clone o repositório ou extraia o zip baixado e abra a pasta do projeto na sua IDE. Em seguida abra o terminal e navegue até a pasta correta.

Crie um ambiente virtual Python (venv) usando o comando:  
  
```bash
python -m venv venv
```

Não esqueça de baixar a versão mais recente do Python se já não a tiver. Apos a criação da venv, será possivel ativa-la.

### Ativar a venv

No Windows:
```bash
venv\Scripts\activate
```
No macOS/Linux:
```bash
source venv/bin/activate
```
Para desativar a venv basta usar o comando:
```bash
deactivate
```

A utilização da venv é opcional, porém aconselhável para isolar as dependências do projeto, evitando conflitos entre diferentes projetos e facilitando a distribuição.

### Instalar as dependências

Com a venv ativada, use o seguinte comando para instalar as dependências do projeto:
```bash
pip install -r requirements.txt
```
Todos os pacotes usados no projeto serão instalados.

## Executando o Projeto

Com o diretório do projeto aberto na IDE e a venv ativada, para iniciar o projeto, execute:

```bash
python manage.py runserver
```

O acesso ao site estará disponível em seu navegador na porta padrão: http://127.0.0.1:8000/.

## Preview do Site

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Página Inicial
</p>
<img src="https://github.com/user-attachments/assets/b19750ee-4921-47cf-aa4c-fe6542fe78af">
</td> 
<td width="50%">
<br>
<p align="center">
  Página de dados
</p>
<img src="https://github.com/user-attachments/assets/682da93c-23bd-4b3b-bf9e-42bb43fbc323">  
</td>
</table>
