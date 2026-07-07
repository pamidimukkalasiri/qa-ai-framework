# qa-ai-framework
> Python + Playwright + Crew AI - Under active development

## Current Status
Complete - Core + Playwright Layer
Complete - Advanced Playwright Features 

## Tech Stack
Python . Playwright . pytest . allure . pytest- xdist. Crew AI(In progress)

### Built so far
- Centralised logger
- Config Management (pydantic-settings)
- Custom decorators (@retry @log_action @timer)
- BasePage with Page Object pattern
- HomePage and LoginPage
- ProductPage and CartPage
- checkout page
- Full E2E test - login to order placement
- Test data separation
- Network interception - block, monitor, track
- Parallel execution - 4 workers
- Trace viewer for debugging
- Allure reports - steps, screenshots, dashboard
- BaseTest - centralized severity and story
- Auto screenshot on failure

## Test Coverage
| Page       | Tests   | Status |
|------------|---------|--------|
| Login      | 4 tests | ✅     |
| Products   | 4 tests | ✅     |
| Cart       | 4 tests | ✅     |
| Checkout   | 3 tests | ✅     |
| Network    | 5 tests | ✅     |
| **Total**  | **20**  | ✅     |

## How to Run
### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Install browsers
playwright install chromium

# Setup environment
cp .env.example .env
# Add your test credentials to .env
```

# Run Tests
## Run single test file
python -m pytest tests\ui\test_login.py -v

## Run all UI tests
python -m pytest tests\ui\ -v

## Run in parallel — 2 workers
python -m pytest tests\ui\ -n 4 -v

## Run specific test
python -m pytest tests\ui\test_login.py::TestLogin::test_valid_login -v

# Allure Reports
## Run tests and save allure results
python -m pytest tests\ui\ --alluredir=reports\allure-results -v

## Open live report in browser
allure serve reports\allure-results

## Generate static HTML report
allure generate reports\allure-results --clean -o reports\allure-html

## Open static HTML report
allure open reports\allure-html

# Run Parallel + Allure together
python -m pytest tests\ui\ -n 2 --alluredir=reports\allure-results -v

# Trace Viewer
## View trace for failed test
playwright show-trace reports\traces\test_name.zip
## Or drag zip file to online viewer
## https://trace.playwright.dev

### Next Steps
- Playwright page Objects
- AI test case generator with Crew AI
- CI/CD pipeline
- Allure reports

## How to run
pip install -r requirement.txt
playwright install chromium

##Author
Sirisha Lavanya | Test Architech
