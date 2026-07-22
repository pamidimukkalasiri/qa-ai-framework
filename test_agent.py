# test_agent.py
from datetime import datetime
import os

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

# Save to file
os.makedirs("data/generated", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
output_file = (f"data/generated/"
               f"tc_login_{timestamp}.json")

with open(output_file, "w") as f:
    json.dump(result, f, indent=2)

print("\nGenerated test cases:")
print("=" * 50)
print(json.dumps(result, indent=2))
print(f"\nTotal:{result.get('total_count',0)}")
print(f"Saved to:{output_file}")