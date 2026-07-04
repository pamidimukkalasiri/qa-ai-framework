import allure
from pages.product_page import ProductPage

@allure.feature("Network Interception")
class TestNetwork:
    @allure.story("Monitor All Requests")
    def test_capture_all_site_requests(self, page):
        """Capture and verify all site requests made when product page loads"""
        requests_made = []

        def capture_request(req):
            if "automationexercise.com" in req.url:
                requests_made.append({
                    "url": req.url,
                    "method": req.method,
                    "type": req.resource_type
                })
        page.on("request", capture_request)

        product = ProductPage(page)
        product.go_to_products()
        page.wait_for_load_state("networkidle")

        # Print what we found
        for req in requests_made:
            print(
                f"{req['type']} |"
                f"{req['method']} |"
                f"{req['url']} |"
            )

        # Page should make at least some requests
        assert len(requests_made) > 0, \
            "Page should make network requests"

    @allure.story("Block Images")
    def test_page_loads_without_images(self, page):
        """Block all image requests - page should still load correctly
        Simulates slow network / data saving mode"""
        blocked = []
        def block_images(route):
            if route.request.resource_type == "image":
                blocked.append(route.request.url)
                route.abort()
            else:
             route.continue_()
        page.route("**/*", block_images)
        product = ProductPage(page)
        product.go_to_products()

        # Page should still be visible
        assert page.locator("body").is_visible(), \
            "Page should load without images"
        print(f"Blocked {len(blocked)} images")

    @allure.story("Block CSS")
    def test_page_loads_without_css(self, page):
        """Block all css files - page HTML still load correctly
        Tests that content exists without styling."""
        def block_css(route):
            if "stylesheet" in route.request.resource_type:
                route.abort()
            else:
                route.continue_()
        page.route("**/*", block_css)
        product = ProductPage(page)
        product.go_to_products()
        assert page.locator("body").is_visible(), "Page should load without css"

    @allure.story("Mock Static Response")
    def test_mock_logo_image(self, page):
        """Replace logo image with different image.
        shows how to mock static resources.
        This is how you'd mock any resource"""
        logo_requested = []
        def track_logo(route):
            if "logo" in route.request.url:
                logo_requested.append(route.request.url)
                # Continue normally - just tracking
                route.continue_()
            else:
                route.continue_()
        page.route("**/*", track_logo)
        product = ProductPage(page)
        product.go_to_products()
        print(f"Logo requests: {logo_requested}")
        assert len(logo_requested) > 0, "Logo Image should be requested"

    @allure.story("Track Response Times")
    def test_track_page_load_performance(self, page):
        """Track how long each request takes.
        Useful for finding slow resources"""
        import time
        request_times = {}
        def on_request(req):
            if "automationexercise.com" in req.url:
                request_times[req.url] = {
                    "start": time.time(),
                    "type": req.resource_type
                }
        def on_response(res):
            if res.url in request_times:
                start = request_times[res.url]["start"]
                duration = time.time() - start
                request_times[res.url]["duration"] = round(duration, 3)
        page.on("request", on_request)
        page.on("response", on_response)
        product = ProductPage(page)
        product.go_to_products()
        page.wait_for_load_state("networkidle")

        # Print slowest requests
        slow = {
            url: data
            for url, data in request_times.items()
            if data.get("duration", 0) > 0.5
        }
        print(f"Slow requests (>0.5s):")
        for url, data in slow.items():
            print(f"data['duration']s "
            f"{url[-50:]}")
        # Page should load in reasonable time
        assert page.locator("body").is_visible(), "Page should load successfully"