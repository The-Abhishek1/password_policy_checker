import re

# ----------------
# SOC 2 FRAMEWORK
# ----------------
def check(password: str) -> tuple[bool, str]:

	if len(password) < 12:
		return False, "Password must be at least 12 characters long (common SOC 2 expectation)."

	has_upper = any(c.isupper() for c in password)
	has_lower = any(c.islower() for c in password)
	has_digit = any(c.isdigit() for c in password)
	has_special = bool(re.search(r'[^A-Za-z0-9]', password))

	if not (has_upper and has_lower and has_digit and has_special):
		return False, "Password must include uppercase, lowercase, digit, and special characters."

	return True, "Compliant with SOC 2"

