import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from search import search_prompt

load_dotenv()
for k in ("OPENAI_API_KEY", "OPENAI_EMBEDDING_MODEL", "DATABASE_URL", "PG_VECTOR_COLLECTION_NAME"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

DATABASE_URL = os.getenv("DATABASE_URL")
PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")


def _retrieve_context(store: PGVector, question: str, *, k: int = 10) -> str:
    results = store.similarity_search_with_score(question, k=k)
    pages = [r[0].page_content for r in results]
    return "\n\n".join(pages)


def main():
    embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL, api_key=os.getenv("OPENAI_API_KEY"))

    store = PGVector(
        embeddings=embeddings,
        collection_name=PG_VECTOR_COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )

    print("Chat iniciado. Digite 'sair' para encerrar o chat.")

    while True:
        user_input = input("Você: ")
        if user_input.strip().lower() == "sair":
            print("Chat encerrado.")
            break

        contexto = _retrieve_context(store, user_input)

        resposta = search_prompt(
            question=user_input,
            contexto=contexto
        )

        print(f"Assistente: \n{resposta}")


if __name__ == "__main__":
    main()
