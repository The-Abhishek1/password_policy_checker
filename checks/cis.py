import re

# ---------------
# CIS FRAMEWORK
# ---------------
def check(password: str) -> tuple[bool, str]:

	if len(password) < 14:
		return False, "Password must be at least 14 characters long."

	if len(set(password)) < 5:
		return False, "Password uses too few unique characters (avoid repetition)."

	if re.search(r"(1234|abcd|qwert|password|letmein|admin)", password.lower()):
		return False, "Password contains a common or sequential patterns."

	return True, "Compliant with CIS Controls v8"
