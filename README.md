# qa-ai-framework
> Python + Playwright + Crew AI - Under active development

## Current Status
Core Utilities

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

### Normal Run — Single Worker
python -m pytest tests\ui\test_login.py -v

### Run all UI tests
python -m pytest tests\ui\ -v

### Parallel run - 4 workers
python -m pytest tests\ui\ -n 4 -v

### Run specific Test file
python -m pytest tests\ui\test_cart.py -v

### View Trace on Failure
playwright show-trace reports\trace.zip


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
