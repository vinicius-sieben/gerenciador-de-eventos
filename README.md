# Gerenciador de Eventos

Sistema de gerenciamento de eventos desenvolvido em Flask para a disciplina de Tópicos Especiais em Engenharia de Software.

## Funcionalidades

- ✅ Sistema de usuários (registro, login, logout)
- ✅ Criação de eventos
- ✅ Visualização de eventos (todos e pessoais)
- ✅ Edição de eventos
- ✅ Exclusão de eventos
- ✅ Dashboard responsivo com Bootstrap
- ✅ Sistema de autenticação seguro

## Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd Metade
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure o banco de dados:**
```bash
python criar_banco.py
```

4. **Execute a aplicação:**
```bash
python main.py
```

5. **Acesse no navegador:**
```
http://localhost:5000
```

## Estrutura do Projeto

```
Metade/
├── main.py              # Aplicação principal Flask
├── models.py            # Modelos do banco de dados
├── config.py            # Configurações do Flask
├── forms.py             # Formulários de autenticação
├── formulario.py        # Formulários de eventos
├── criar_banco.py       # Script de inicialização do banco
├── requirements.txt     # Dependências Python
├── README.md           # Este arquivo
└── template/           # Templates HTML
    ├── base.html       # Template base
    ├── index.html      # Página inicial
    ├── login.html      # Página de login
    ├── register.html   # Página de registro
    ├── dashboard.html  # Dashboard principal
    ├── create_event.html # Criar evento
    └── edit_event.html # Editar evento
```

## Uso

1. **Registre uma nova conta** na página inicial
2. **Faça login** com suas credenciais
3. **Crie eventos** usando o botão "Criar Novo Evento"
4. **Gerencie seus eventos** no dashboard
5. **Visualize todos os eventos** da plataforma

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: SQLite + SQLAlchemy
- **Autenticação**: Flask-Login
- **Frontend**: HTML + Bootstrap 5
- **Formulários**: Flask-WTF + WTForms

## Desenvolvido por

Vinicius Sieben - Tópicos Especiais em Engenharia de Software
