from typing import List, Dict, Any, Tuple, Optional
from .schema import ChunkMetadata

class RAGStore:
    def search(self, query: str, filters: Dict[str, Any], k: int) -> List[Tuple[str, ChunkMetadata]]:
        """Search for relevant chunks in the vector store."""
        raise NotImplementedError

    def add_documents(self, docs: List[Tuple[str, ChunkMetadata]]) -> None:
        """Add new chunks to the vector store."""
        raise NotImplementedError

    def reindex(self, new_docs: List[Tuple[str, ChunkMetadata]]) -> None:
        """Reindex existing documents."""
        raise NotImplementedError
