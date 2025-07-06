from playwright.async_api import async_playwright

async def execute_script(script: str):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            namespace = {"page": page, "browser": browser, "context": context}
            exec(
                f"async def _run(page, browser, context):\n" +
                "\n".join(f"    {line}" for line in script.splitlines()),
                namespace
            )
            result = await namespace["_run"](page, browser, context)
            await browser.close()
            return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
