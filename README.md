# Cinema Ticket Reservation API

API REST para gerenciamento de reservas e compras de ingressos de cinema, desenvolvida baseada nos requisitos de software do processo seletivo para estagiário back-end da B2Bit.

## Funcionalidades

* Autenticação via JWT
* Listagem de filmes
* Listagem de sessões por filme
* Visualização de assentos por sessão
* Reserva temporária de assentos (com expiração)
* Compra de ingressos
* Listagem de ingressos do usuário

## Arquitetura

O sistema foi projetado com foco em **consistência e concorrência**, utilizando:

* **Django + Django REST Framework** para a API
* **PostgreSQL** como banco de dados
* **Redis** para controle de locks (reservas temporárias)
* **Celery** para fallback de expiração

## Autenticação

A API utiliza JWT.

### Obter token:

```
POST /api/token/
```

### Refresh:

```
POST /api/token/refresh/
```

## Instalação

### 1. Clonar o projeto

```bash
git clone <repo>
cd <repo>
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
```

---

### 3. Instalar dependências

```bash
poetry install
```

### 4. Configurar variáveis de ambiente

Exemplo:

```
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5. Rodar migrações

```bash
python manage.py migrate
```

### 7. Rodar servidor

```bash
python manage.py runserver
```

## Redis

Certifique-se de ter o Redis rodando:

```bash
redis-server
```

## 📄 Modelagem

Principais entidades:

* User
* Movie
* Room
* Seat
* Session
* Ticket

## Decisões de projeto

* O estado de "comprado" é definido pela existência de um `Ticket`
* Reservas são mantidas apenas no Redis
* Redis é a fonte de verdade para locks temporários

## Autor

Desenvolvido por Yuri Teixeira
