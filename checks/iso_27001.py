import re

# ---------------------
# ISO 27001 FRAMEWORK
# ---------------------

def check(password: str) -> tuple[bool,str]:
	"""
	ISO 27001 framework requirements
	"""

	if len(password) < 12:
		return False, "Password must be at least 12 characters long."

	has_upper = any(c.isupper() for c in password)
	has_lower = any(c.islower() for c in password)
	has_digit = any(c.isdigit() for c in password)
	has_special = bool(re.search(r'[^A-Za-z0-9]', password))

	if not(has_upper and has_lower and has_digit and has_special):
		return False, "Password must include uppercase, lowercase, digit, and special characters."

	return True, "Compliant with ISO 27001."
