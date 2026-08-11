from pathlib import Path
import re

STYLES = Path(__file__).resolve().parents[1] / "app" / "static" / "styles.css"


def _css_rule(selector: str) -> str:
    styles = STYLES.read_text(encoding="utf-8")
    escaped = re.escape(selector)
    match = re.search(rf"{escaped}\s*\{{([^}}]*)\}}", styles)
    return match.group(1) if match else ""


def test_quick_action_cards_are_aligned():
    """Dashboard quick-action cards must not use offset/rotate transforms."""
    styles = STYLES.read_text(encoding="utf-8")
    assert not re.search(
        r"\.action-card:nth-child\(\d+\)\s*\{[^}]*transform\s*:",
        styles,
    )

    quick_actions = _css_rule(".quick-actions")
    assert "display: flex" in quick_actions
    assert "flex-wrap: wrap" in quick_actions
    assert not re.search(r"margin-bottom\s*:\s*120px", quick_actions)


def test_transaction_status_badges_remain_in_table_cell_flow():
    status_badge = _css_rule(".status-badge")
    assert "display: inline-flex" in status_badge
    assert not re.search(r"position\s*:\s*absolute\b", status_badge)
    assert not re.search(r"margin-left\s*:\s*-", status_badge)
    assert not re.search(r"z-index\s*:", status_badge)
