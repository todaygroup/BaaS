# 자격 증명 및 비밀키 (Credentials and Secrets)

## 9.1 모델링
```python
class LLMProviderCredentials(BaseModel):
    id: str
    provider: Literal["openrouter"]
    api_key: str  # 암호화 저장
    default_model: str = "gpt-4o"

class VectorDBCredentials(BaseModel):
    id: str
    provider: Literal["qdrant"]
    api_url: str
    api_key: str
```
- DB에는 암호화하여 저장하고, 런타임에는 ID로 조회하여 사용함.
