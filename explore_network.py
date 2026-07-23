from playwright.sync_api import sync_playwright


SITE = "https://automationexercise.com"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    def on_request(req):
        # CHANGED: Monitoring image files (.png or .jpg) instead of "api"
        if SITE in req.url and (".png" in req.url or ".jpg" in req.url):
            print(f"REQUEST: {req.method} -> {req.url}")

    def on_response(res):
        # CHANGED: Monitoring image files (.png or .jpg) instead of "api"
        if SITE in res.url and (".png" in res.url or ".jpg" in res.url):
            print(f"RESPONSE: {res.status} -> {res.url}")


    page.on("request", on_request)
    page.on("response", on_response)

    print("\n_____Homepage_____")
    page.goto(SITE)
    page.wait_for_load_state("networkidle")
    print("\n_________ProductsPage___________")
    page.goto(f"{SITE}/products")
    page.wait_for_load_state("networkidle")
    print("\n_________search___________")
    page.goto(f"{SITE}/products")
    page.locator("input#search_product").fill("dress")
    page.locator("button#submit_search").click()
    page.wait_for_load_state("networkidle")

    input("\n Press enter to close")
    browser.close()


    # # Print every API call
    # page.on(
    #     "request", lambda req: print(f"REQUEST : {req.url}")
    #     if "api" in req.url
    #     else None
    # )
    #
    # page.on(
    #     "response", lambda res: print(f"RESPONSE : {res.status} -> {res.url}")
    #     if "api" in res.url
    #     else None
    # )
    #
    # #Test 1 - HOme page
    # print("\n____HOMEPAGE____")
    # page.goto("https://automationexercise.com")
    # page.wait_for_load_state("networkidle")
    #
    # #Test 2 - Product Page
    # print("\n____PRODUCT____")
    # page.goto("https://automationexercise.com/products")
    # page.wait_for_load_state("networkidle")
    #
    # input("Press enter to close...")
    # browser.close()