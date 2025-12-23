# 데이터 및 RAG 인프라 (Data and RAG Infrastructure)

## 9.1 벡터 스토어 설계
- **Provider**: Qdrant.
- **Metadata**: source_id, page, section, topic, language 포함.
- **Embeddings**: `text-embedding-3-large`.

## 9.2 인덱싱 파이프라인
- PDF → Chunking (고정 크기 + 겹침) → Embedding → Upsearch.
- 저자별/워크스페이스별 컬렉션 분리를 통한 멀티테넌시 지원.
