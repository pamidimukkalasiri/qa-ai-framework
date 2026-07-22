import json
from pathlib import Path
from groq import Groq
from core.config import settings
from core.logger import logger


PROMPT = """
You are a Senior QA Engineer with 15 years experience.

Analyze this user story and generate test cases:

{user_story}

Generate test cases covering:
1. Happy path — valid inputs, success
2. Negative — invalid inputs, errors
3. Edge cases — empty fields, boundaries
4. Security — basic security checks

Return ONLY this JSON, nothing else.
No explanation. No markdown. Just JSON:

{{
    "feature": "feature name here",
    "total_count": number,
    "test_cases": [
        {{
            "id": "TC001",
            "title": "test case title",
            "type": "positive/negative/edge/security",
            "priority": "high/medium/low",
            "steps": [
                "Step 1: action here",
                "Step 2: action here"
            ],
            "expected_result": "what should happen"
        }}
    ]
}}
"""


class TestGeneratorAgent:
    """
    AI Agent using Google Gemini API.
    Simple, clean, no async complexity.
    100% Free.
    """

    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model = "llama-3.1-8b-instant"
        logger.info("Groq client ready")

    def generate_from_text(
        self, user_story: str
    ) -> dict:
        """Generate test cases from text"""
        logger.info("Generating from text")
        return self._run(user_story)

    def generate_from_file(
        self, file_path: str
    ) -> dict:
        """Generate test cases from .txt file"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )
        logger.info(f"Reading: {file_path}")
        story = path.read_text(encoding="utf-8")
        return self._run(story)

    def generate_from_all_stories(
        self,
        folder: str = "data/user_stories"
    ) -> list:
        """Generate for all .txt files in folder"""
        folder_path = Path(folder)
        results = []
        files = list(folder_path.glob("*.txt"))
        logger.info(
            f"Found {len(files)} story files"
        )
        for file in files:
            logger.info(
                f"Processing: {file.name}"
            )
            result = self.generate_from_file(
                str(file)
            )
            result["source_file"] = file.name
            results.append(result)
        return results

    def _run(self, user_story: str) -> dict:
        """Call Gemini API"""
        try:
            prompt = PROMPT.format(
                user_story=user_story
            )
            logger.info("Calling Gemini API...")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Return only valid JSON"
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=4096
            )
            result = response.choices[0].message.content

            logger.info("Response received!")
            return self._parse_result(result)

        except Exception as e:
            logger.error(f"API call failed: {e}")
            return {
                "error": str(e),
                "test_cases": [],
                "total_count": 0
            }

    def _parse_result(
        self, result: str
    ) -> dict:
        """Parse JSON from response"""
        try:
            clean = result \
                .replace("```json", "") \
                .replace("```", "") \
                .strip()
            parsed = json.loads(clean)
            logger.info(
                f"Generated "
                f"{parsed.get('total_count', 0)}"
                f" test cases!"
            )
            return parsed
        except json.JSONDecodeError as e:
            logger.error(f"Parse failed: {e}")
            return {
                "error": str(e),
                "raw_output": result,
                "test_cases": [],
                "total_count": 0
            }