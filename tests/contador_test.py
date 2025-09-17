from pathlib import Path
from playwright.sync_api import sync_playwright

def test_incremento_contador(tmp_path):
    html_path = Path(__file__).resolve().parents[1] / "index.html"
    url = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Abre seu arquivo HTML local
        page.goto(url)

        # Verifica o contador inicial
        contador = page.locator("#contador")
        assert contador.inner_text() == "Você clicou 0 vezes."

        # Clica no botão 3 vezes
        for _ in range(3):
            page.click("text=Clique aqui")

        # Verifica se o contador atualizou para 3
        assert contador.inner_text() == "Você clicou 3 vezes."

        browser.close()
