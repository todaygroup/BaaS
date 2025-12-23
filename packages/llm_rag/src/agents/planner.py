from typing import Any, Dict
from packages.llm_rag.src.llm.layer import llm_layer
from packages.llm_rag.src.llm.router import Role

class BookPlannerAgent:
    def __init__(self):
        self.role = Role.PLANNER

    async def plan_outline(self, topic: str, audience: str, tone: str) -> Dict[str, Any]:
        """
        Plans a book outline based on topic, audience, and tone.
        """
        system_prompt = f"""
        You are a World-Class Book Planner. Your mission is to create a structured outline for a professional book.
        Target Audience: {audience}
        Writing Tone: {tone}
        """
        
        user_prompt = f"""
        Create a detailed outline for a book about: {topic}.
        The outline should include:
        1. Book Title and Subtitle
        2. 5-7 Chapters with titles and a brief purpose for each.
        Format the output as valid JSON.
        """

        response = await llm_layer.call_llm(
            role=self.role,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=None # In real implementation, use a Pydantic model for structured output
        )
        
        # In a real scenario, we would parse the JSON from response.content
        return {
            "title": topic,
            "outline": response.get("content", "Failed to generate outline")
        }

planner_agent = BookPlannerAgent()
