const fs = require("fs");
const path = require("path");

const styles = fs.readFileSync(
  path.join(__dirname, "../app/static/styles.css"),
  "utf8"
);

function getCssRule(selector) {
  const escapedSelector = selector.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const match = styles.match(new RegExp(`${escapedSelector}\\s*\\{([^}]*)\\}`));
  return match ? match[1] : "";
}

test("transaction status badges remain in the table cell flow", () => {
  const statusBadgeRule = getCssRule(".status-badge");

  expect(statusBadgeRule).toContain("display: inline-flex");
  expect(statusBadgeRule).not.toMatch(/position\s*:\s*absolute\b/);
  expect(statusBadgeRule).not.toMatch(/margin-left\s*:\s*-/);
  expect(statusBadgeRule).not.toMatch(/z-index\s*:/);
});

test("quick action cards stay aligned without transform offsets", () => {
  expect(styles).not.toMatch(/\.action-card:nth-child\(\d+\)\s*\{[^}]*transform\s*:/);

  const quickActionsRule = getCssRule(".quick-actions");
  expect(quickActionsRule).toContain("display: flex");
  expect(quickActionsRule).toContain("flex-wrap: wrap");
  expect(quickActionsRule).not.toMatch(/margin-bottom\s*:\s*120px/);
});
