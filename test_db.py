from app.database.db_queries import (
    save_problem, get_active_rules, get_decision_history
)

# Test saving a problem
problem_id = save_problem("How can we reduce production waste?")
print(f"✅ Problem saved with ID: {problem_id}")

# Test loading rules
rules = get_active_rules()
print(f"\n✅ Company rules ({len(rules)} found):")
for rule in rules:
    print(f"  - [{rule['category']}] {rule['rule_text']}")

# Test loading history
history = get_decision_history()
print(f"\n✅ Past decisions ({len(history)} found):")
for h in history:
    print(f"  - {h['problem']} → {h['outcome']}")