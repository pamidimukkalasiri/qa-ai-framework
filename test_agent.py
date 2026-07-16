# test_agent.py
from ai_agents.test_generator.agent import (
    TestGeneratorAgent
)
import json

print("=" * 50)
print("AI Test Case Generator")
print("Powered by Google Gemini")
print("=" * 50)

agent = TestGeneratorAgent()

print("\nGenerating test cases...")

result = agent.generate_from_file(
    "data/user_stories/us001_login.txt"
)

print("\nRESULT:")
print("=" * 50)
print(json.dumps(result, indent=2))

total = result.get("total_count", 0)
if total > 0:
    print(f"\n✅ {total} test cases generated!")
else:
    print("\n❌ Check error above")