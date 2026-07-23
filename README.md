# QA AI Framework 🤖
[![QA AI Framework Pipeline](https://github.com/pamidimukkalasiri/qa-ai-framework/actions/workflows/test-pipeline.yml/badge.svg)](https://github.com/pamidimukkalasiri/qa-ai-framework/actions/workflows/test-pipeline.yml)

> AI-powered test automation framework built with
> **Python + Playwright + Groq AI**
> under active development — CI/CD enabled

---

## Current Status

```
✅ Core + Playwright Layer
✅ Advanced Playwright Features
✅ AI Test Case Generator
✅ CI/CD Pipeline
🔄 Docker (in progress)
```

---

## What This Framework Does

| Feature | Description | Status |
|---------|-------------|--------|
| AI Test Generator | Generates test cases from user stories using Groq + Llama | ✅ |
| UI Automation | Full e-commerce flow using Playwright | ✅ |
| Smart Reporting | Allure reports with screenshots on failure | ✅ |
| CI/CD Pipeline | GitHub Actions with parallel execution | ✅ |
| ⚡ Parallel Execution | pytest-xdist with 2 workers | ✅ |
| Network Interception | Mock, block and monitor API calls | ✅ |
| Docker Support | Containerized test execution | 🔄 |

---

## Tech Stack

```
Language        Python 3.11+
UI Testing      Playwright + pytest
AI Layer        Groq API + Llama 3.1
Reporting       Allure Reports
CI/CD           GitHub Actions
Parallel        pytest-xdist
Container       Docker (coming soon)
```

---

## AI Test Case Generator

Uses **Groq API + Llama 3.1** (free, no card needed)
to automatically generate test cases from user stories.

### How It Works

```
User Story (.txt file)
        ↓
AI Agent reads it
        ↓
Generates test cases covering:
  → Happy path
  → Negative scenarios
  → Edge cases
  → Security checks
        ↓
Saves as structured JSON
```

### Time Saved

```
Manual: 1 user story → 2-3 hours
AI:     1 user story → 30 seconds
Saved:  ~80% ✅
```

### Run AI Generator

```bash
python test_agent.py
# Output saved to data/generated/
```

---

## Framework Architecture

```
qa-ai-framework/
│
├── core/                        # Python utilities
│   ├── decorators.py            # @retry, @log_action, @timer
│   ├── config.py                # pydantic-settings, env config
│   └── logger.py                # centralised logging
│
├── pages/                       # Playwright Page Objects
│   ├── base_page.py             # common actions + Allure steps
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── base_test.py             # centralized Allure setup
│   ├── conftest.py              # fixtures + screenshot on fail
│   └── ui/
│       ├── test_login.py        # 4 tests
│       ├── test_products.py     # 4 tests
│       ├── test_cart.py         # 4 tests
│       ├── test_checkout.py     # 3 tests
│       └── test_network.py      # 5 tests
│
├── ai_agents/
│   └── test_generator/
│       ├── agent.py             # Groq + Llama agent
│       └── prompts.py           # Prompt engineering
│
├── data/
│   ├── test_data.py             # test data constants
│   ├── user_stories/            # input for AI agent
│   └── generated/               # AI output (gitignored)
│
├── .github/
│   └── workflows/
│       └── test-pipeline.yml    # CI/CD pipeline
│
└── reports/                     # Allure output (gitignored)
```

---

## Test Coverage

| Page | Tests | Status |
|------|-------|--------|
| Login & Auth | 4 tests | ✅ |
| Products | 4 tests | ✅ |
| Shopping Cart | 4 tests | ✅ |
| Checkout | 3 tests | ✅ |
| Network | 5 tests | ✅ |
| **Total** | **20 tests** | ✅ |

---

## Getting Started

### Installation

```bash
git clone https://github.com/YOURUSERNAME/qa-ai-framework.git
cd qa-ai-framework
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
# Add your credentials to .env
```

### Environment Setup

```
BASE_URL=https://automationexercise.com
BROWSER=chromium
HEADLESS=true
SLOW_MO=0
TIMEOUT=60000
TEST_EMAIL=your-test-email@gmail.com
TEST_PASSWORD=your-test-password
GROQ_API_KEY=your-groq-api-key
```

Get free Groq API key → console.groq.com (no card needed)

---

## How to Run

```bash
# Run all UI tests
python -m pytest tests\ui\ -v

# Run in parallel
python -m pytest tests\ui\ -n 2 -v

# Run with Allure report
python -m pytest tests\ui\ --alluredir=reports\allure-results -v
allure serve reports\allure-results

# View trace on failure
playwright show-trace reports\traces\test_name.zip
```

---

## CI/CD Pipeline

Every push triggers automatic:
- Dependency installation
- Playwright browser setup
- 20 tests in parallel
- Allure report generation
- Artifact upload

View → Actions tab on GitHub

---

## Key Design Decisions

| Decision | Why |
|----------|-----|
| Playwright over Selenium | Faster, better debugging |
| Groq over OpenAI | Free tier, no card needed |
| pytest over unittest | Better fixtures, plugins |
| Pydantic for config | Type safety, auto env reading |
| BaseTest class | Centralized Allure, zero boilerplate |
| Fixture chaining | Reusable state, clean isolation |

---

## Coming Next

- [ ] Docker setup
- [ ] Flaky test analyzer agent
- [ ] Test data generator agent
- [ ] API testing layer
- [ ] Self-healing locators

---

## Author

**Sirisha Lavanya**
Python Automation Lead | Python · Playwright · AI Testing
LinkedIn: linkedin.com/in/sirisha-lavanya-a072b432
GitHub: https://github.com/pamidimukkalasiri/qa-ai-framework
