# Password Analyzer 🔐

A Python-based **password compliance analyzer** that evaluates a given password against **six major security and compliance frameworks**.  
The tool helps understand how different standards enforce password policies and highlights where a password fails or passes.

This project is designed for **learning cybersecurity policy enforcement**, compliance standards, and rule-engine design.

---

## ✨ Features

- ✅ Checks password against **6 security frameworks**
- 📋 Interactive CLI menu to select standards
- 🔁 Run a single standard or **all checks at once**
- 🧠 Clear **PASS / FAIL** output with reason
- 🧩 Modular design (easy to add new standards)

---

## 📜 Supported Compliance Standards

1. **NIST SP 800-63B**
2. **PCI-DSS**
3. **ISO/IEC 27001**
4. **HIPAA**
5. **SOC 2**
6. **CIS Controls**

> ⚠️ Note: These checks are **policy-inspired interpretations**, not official legal certifications.

---

## 🖥️ Sample Output

### CLI Execution

```text
$ python3 main.py
Enter the password to check: pasidvrfnvr

Select compliance standard(s) to check:
(comma separated numbers, or type 'all')

    1: NIST
    2: PCI-DSS
    3: ISO-27001
    4: HIPAA
    5: SOC 2
    6: CIS Controls
    all : Run ALL available checks

Your selection -> all

Results

============================================================
    Checking password against 6 standard(s)
============================================================

NIST         | PASS | Compliant with NIST SP 800-63B
PCI-DSS      | FAIL | Password must be at least 12 character long.
ISO-27001    | FAIL | Password must be at least 12 characters long.
HIPAA        | PASS | Compliant with HIPAA.
SOC 2        | FAIL | Password must be at least 12 characters long (common SOC 2 expectation).
CIS Controls | FAIL | Password must be at least 14 characters long.

============================================================

🏗️ Project Structure

Password_Policy/
│
├── main.py                 # CLI entry point
├── checks/                 # Compliance checks package
│   ├── __init__.py
│   ├── nist.py
│   ├── pci_dss.py
│   ├── iso_27001.py
│   ├── hipaa.py
│   ├── soc2.py
│   └── cis.py
│
└── README.md

🚀 Usage

    Run the analyzer:
        python3 main.py
