import re

# -----------------
# HIPAA FRAMEWORK
# -----------------

def check(password: str) -> tuple[bool, str]:
	"""
	HIPAA framwork
	"""

	if len(password) < 8:
		return False, "Password must be at least 8 characters long."

	if not all(32<= ord(c) <= 126 for c in password):
		return False, "Password must use printable ASCII characters."
	
	if all(c == password[0] for c in password) or re.match(r'^(12345678|abcdefgh|qwertyui|password|letmein)$', password.lower()):
		return False, "Password is too common or weak."
		
	return True, "Compliant with HIPAA."
