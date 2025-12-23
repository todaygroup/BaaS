import pytest
from packages.core.src.domain.book import Book
from datetime import datetime

def test_book_model_validation():
    # Test valid book creation
    book_data = {
        "id": "book-123",
        "project_id": "proj-456",
        "title": "Agentic AI 101",
        "target_audience": "Tech Leaders",
        "tone": "Professional",
        "language": "ko",
        "status": "outline",
        "created_at": datetime.now()
    }
    book = Book(**book_data)
    assert book.id == "book-123"
    assert book.status == "outline"

def test_book_status_enum():
    # Test invalid status
    with pytest.raises(ValueError):
        Book(
            id="book-123",
            project_id="proj-456",
            title="Title",
            target_audience="Audience",
            tone="Tone",
            status="invalid-status", # Must be outline, drafting, editing, or completed
            created_at=datetime.now()
        )
