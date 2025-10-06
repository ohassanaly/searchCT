TODO : Persist the ChromaDB embedding model name in config, and pass it on get_collection in query_vector_db

my current collection uses default "all-MiniLM-L6-v2" embedding. Ff using another one, I should provide it when getting the collection : collection = chroma_client.get_collection(name="rct_sections", embedding_function = )
