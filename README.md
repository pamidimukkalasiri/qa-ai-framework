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

## Test Coverage
| Page | Tests | Status |
|------|-------|--------|
| Login | 4 tests | ✅ |
| Products | 4 tests | ✅ |
| Cart | 4 tests | ✅ |
| Checkout | 3 tests | ✅ |

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
