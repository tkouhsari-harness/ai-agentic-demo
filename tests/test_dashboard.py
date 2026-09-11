from pathlib import Path

STYLES_PATH = Path(__file__).resolve().parents[1] / "app" / "static" / "styles.css"


def test_dashboard_returns_200(client):
    res = client.get("/")
    assert res.status_code == 200


def test_transfer_page_returns_200(client):
    res = client.get("/transfer")
    assert res.status_code == 200


def test_dashboard_pay_bill_action_links_to_bill_payment_page(client):
    res = client.get("/")
    text = res.get_data(as_text=True)
    assert 'href="/pay-bill"' in text
    assert "Pay Bill" in text


def test_pay_bill_returns_200(client):
    res = client.get("/pay-bill")
    assert res.status_code == 200
    assert "Pay Bill" in res.get_data(as_text=True)


def test_login_returns_200(client):
    res = client.get("/login")
    assert res.status_code == 200


def test_quick_action_cards_are_aligned():
    styles = STYLES_PATH.read_text()
    assert "transform: rotate" not in styles
    assert "grid-template-columns: repeat(4, minmax(0, 1fr))" in styles
    assert "margin-bottom: 120px" not in styles
