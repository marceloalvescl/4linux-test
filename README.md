# 4linux-test

O presente repositório contém as implementações do backend e do frontend do projeto atribuído como teste prático.<br>
Ao final deste README, há uma seção que informa como rodar a aplicação no localhost.<br>
<br>
As linguagens utilizadas no projeto foram Python no backend e JavaScript (NodeJS) no frontend. No banco foi utilizado PostgreSQL<br>
<br>
- Backend<br>
<pre>
Ao analisar o desafio, defini que o framework Flask atenderia as necessidades e utilizei deste microframework para
desenvolver a aplicação.

Flask Blueprint foi utilizado para melhor organização das rotas, visando manter as rotas e a lógica delas apenas em 
um arquivo.
O módulo Flask_Login foi utilizado para gerenciar a autenticação do usuário no backend, o qual provê mecanismos para
logar o usuario, deslogá-lo, verificar se está logado e proibir acesso a rotas que necessitem de autenticação 
(anotação @login_required sobre a definição das rotas).

Com todo esse arcabouço, montei uma API para ser consumida pela aplicação do front-end, definindo as seguintes rotas 
possíveis: /login; /logout e / (rota raiz, onde após autenticação do usuário é feito uma requisição 
para a url https://api.publicapis.org/entries e então retorna um Json contendo as informações de apis públicas)

O Backend foi subdividido em cinco pastas: app, flask_session, models, routes e utils.
 - app
    Contém o arquivo __init__.py responsável por instanciar a classe Flask e fazer as configurações necessárias.
 - flask_session
    Pasta auxiliar onde é armazenado informações de sessões dos usuários, mantendo um registro das sessões válidas 
    e as inativas.
 - models
    Nesta há a classe Account, a qual modela a entidade account do banco Postgres. Esta classe é utilizada também para
    auxiliar na implementação da lógica de autenticação.
 - routes
    Neste subdiretório encontra-se routes.py, arquivo onde encontra-se as rotas da aplicação e toda a lógica dentro delas.
 - utils
    Pasta auxiliar onde encontra-se apenas log.py, o qual utiliza o módulo logging para realizar logs no console.
</pre>
- Frontend<br>
<pre>
No frontend foi utilizado o framework Express do NodeJS para implementação da rota do frontend, onde cada uma realiza 
alguma atividade chave ou retorna um template.
Para consumir a API (backend) foi utilizado o módulo 'node-fetch' para realizar as requisições necessárias.
Utilizei a linguagem de template Embedded JavaScript templating (EJS) para gerar a tabela com as informações da PublicAPIs.
O frontend foi subdividido em duas pastas: public e src.
  - public 
    Contém os templates home.ejs e login.html na raiz da pasta public e mais duas subpastas, sendo elas css e js, para prover 
    os possíveis estilos e scripts necessários. 
  - src
    Nesta pasta econtra-se o arquivo server.js, onde há a instanciação do framework Express e a definição das rotas do frontend.
</pre>
API do python
 ```
 http://127.0.0.1:81/; 
    método POST,
    header Content-Type: application/json e Cookie de sessão,
    caso usuário logado - retorna Json contendo informações da PublicAPIs e statuscode 201,
    caso usuário nao esteja logado - retorna Json informando para fazer login primeiro e statuscode 401.

http://127.0.0.1:81/login; 
    método POST,
    body em formato json contendo os valores de 'username' e 'password',
    caso usuário e senha válidos - retorna Json informando sucesso, statuscode 201 e cookie de sessão,
    caso usuário ou senha inválidos - retorna Json informando erro e statuscode 401,
    (Aqui é feito login_user() o qual ativa a sessão do usuário).

http://127.0.0.1:81/logout; método POST e GET  
    método GET e POST,
    retorna sucesso e 201, mesmo quando usuário ja está deslogado,
    (Aqui é feito logout_user() o qual inativa a sessão do usuário).
 ```

Frontend
 ```
 http://127.0.0.1:80/;
    método GET,
    Cookie de sessão,
    Caso usuário autenticado - retorna o template home.ejs,
    Caso usuário não esteja autenticado - redireciona para a rota /login.
    
 http://127.0.0.1:80/login; 
    método get,
    retorna o template login.html
 
 http://127.0.0.1:80/process-login; 
    método POST,
    body em formato json contendo os valores de 'username' e 'password',
    caso o usuário e senha válidos - adiciona o cookie do usuário e redireciona para a rota /  
    caso o usuário ou senha inválidos - redireciona para a rota /login
    
 http://127.0.0.1:80/logoff;   
    método GET e POST,
    retorna Json informando logout realizado com sucesso e statuscode 201
 ```
<pre>
Dificuldades encontradas:
 - Neste fim de semana tive algumas atividades academicas e não tive condição de implementar algumas funcionalidades 
 extras, como paginação na tabela das apis, logout apenas caso usuário esteja logado, entre outras.
 
 - Ao tentar realizar chamadas para a api do backend via script na página de login (evento de click em botão de login
 realizaria um fetch), me deparei com erro de CSP(Content-Security-Policy), o qual impedia chamadas a referências 
 externas, não consegui desenvolver um workaround e então optei por criar uma rota no frontend '/process-login' 
 para consumir fazer requisição a rota /login do backend.
 
 - Não havia utilizado o módulo Flask-Login anteriormente, passei um tempo lendo a documentação para aprender o básico 
 sobre e percebi que há mais para aprofundar.    
 
 - Tentei subir o projeto utilizando docker-compose porém não obtive sucesso...
</pre>      

Para rodar a aplicacao no localhost: <br>
<pre>
- Tenha este repositório em sua máquina (git clone ou fazendo o download),
- Logo após, instale o Postgres em sua máquina e configure a senha do usuário postgres para root, 
ou então altere a senha configuarada em backend/app/__init__.py linha 7 
(exemplo 'postgresql://postgres:<suaSenha>@localhost/test4linux')
- Com o PostgreSQL rodando, execute os comandos no script presente na raiz do projeto SCRIPT-TEST4LINUX.sql 
para criar o banco, a tabela e inserir o usuário 4linux (para tal pode utilizar o shell psql, como preferir)
- Em seguida abra 2 terminais e navegue até cada uma das pastas: backend e frontend,
  - No terminal onde esteja no diretório backend execute o comando - 'python3 main.py', 
    se necessário - 'pip install -r requirements.txt'
  - No terminal onde esteja no diretório frontend execute o comando - 'npm start', se necessário - 'npm install'
</pre>
