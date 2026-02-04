from checks import ALL_CHECKERS
import sys

# ------------------
# CHOICE FUNCTION
# -----------------
def print_menu():
	print("\nSelect compliance standard(s) to check: ")
	print("(comma separated numbers, or type 'all') \n")

	for key in sorted(ALL_CHECKERS.keys(), key=int):
		name, _ = ALL_CHECKERS[key]
		print(f"	{key}: {name}")

	print("	all : Run ALL available checks")

# -------------------------
# CHECK SELECTED STANDARD
# -------------------------
def get_selected_checkers(choice: str) -> list[tuple, callable]:
	choice = choice.strip().lower()

	if choice in ("all", "a", "everything"):
		return list(ALL_CHECKERS.values())

	selected = []
	invalid = []
	
	for part in choice.split(","):
		key = part.strip()
		if key in ALL_CHECKERS:
			selected.append(ALL_CHECKERS[key])
		elif key:
			invalid.append(key)

	if invalid:
		print("Warning: These keys were not recognized ->", ", ".join(invalid))
		
	return selected

# ---------------3
# MAIN FUNCTION
# ---------------

def main():
	if len(sys.argv) > 1 and (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
		print("Usage: python main.py")
		print("Run interactively to check a password against standards.")
		sys.exit(0)

	password = input("Enter the password to check: ").strip()

	if not password:
		print("Error: Password cannot be empty.")
		return

	print_menu()
	user_choice = input("\nYour selection -> ").strip()

	selected = get_selected_checkers(user_choice)

	if not selected:
		print("No valid standards were selected.")
		return

	print("\n" + "=" * 60)
	print(f"	Checking password against {len(selected)} standard(s)")
	print("=" * 60 + "\n")

	for name, check_fun in selected:
		passed, message = check_fun(password)
		status = "PASS" if passed else "FAIL"
		print(f"{name:12} | {status:4} | {message}")

	print("\n" + "=" * 60)


if __name__ == "__main__":
	main()









	
