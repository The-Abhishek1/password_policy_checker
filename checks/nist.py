
# -------------------------
# CHECKING NIST FRAMEWORK
# -------------------------

def check(password: str) -> tuple[bool, str]:
	"""
	NIST SP 800-63B complaint check
	"""

	if len(password) < 8:
		return False, "Must be at least 8 characters long"

	if not all(32<= ord(c) <=126 for c in password):
		return False, "Password must use printable ASCII characters."

	return True, "Compliant with NIST SP 800-63B"
