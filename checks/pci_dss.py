import re

# --------------------
# PCI DSS FRAMWORK
# --------------------

def check(password:str) -> tuple[bool, str]:
	"""
	PCI DSS v4.0 complain check
	"""

	if len(password) < 12:
		return False, "Password must be at least 12 character long."

	has_upper = any(c.isupper() for c in password)
	has_lower = any(c.islower() for c in password)
	has_digit = any(c.isdigit() for c in password)
	has_special = bool(re.search(r'[^A-Za-z0-9]', password))

	if not(has_upper and has_lower and has_digit and has_special):
		return False, "Password must include uppercase, lowercase, digit, and special characters."

	return True, "Complian with PCI DSS v4.0"
