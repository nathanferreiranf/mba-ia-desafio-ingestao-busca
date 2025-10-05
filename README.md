# Desafio MBA Engenharia de Software com IA - Full Cycle

Descreva abaixo como executar a sua solução.

## Requisitos
- Python 3.8+
- PostgreSQL com extensão pgvector instalada
- Conta na OpenAI com acesso à API
- Variáveis de ambiente configuradas:
  - `OPENAI_API_KEY`: Sua chave de API da OpenAI
  - `OPENAI_EMBEDDING_MODEL`: Modelo de embedding, ex: text-embedding-3-small
  - `DATABASE_URL`: URL de conexão com o banco PostgreSQL (ex: postgresql+psycopg://postgres:postgres@localhost:5432/rag)
  - `PDF_PATH`: document.pdf
  - `PG_VECTOR_COLLECTION_NAME`: Nomde da collection Ex: documents

## Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/nathanferreiranf/mba-ia-desafio-ingestao-busca.git
    cd mba-ia-desafio-ingestao-busca
    ```
2. Crie o ambiente virutal (VirtualEnv) para Python:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    ```
3. Ordem de execução
    1. Subir o banco de dados:
        ```bash
        docker-compose up -d
        ```
    2. Executar ingestão do PDF:
        ```bash
        python src/ingest.py
        ```
    3. Iniciar o chat:
        ```bash
        python src/chat.py
        ```