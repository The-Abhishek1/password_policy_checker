from .nist import check as nist
from .pci_dss import check as pci_dss
from .iso_27001 import check as iso_27001
from .hipaa import check as hipaa

ALL_CHECKERS = {
	"1": ("NIST", nist),
	"2": ("PCI-DSS", pci_dss),
	"3": ("ISO-27001", iso_27001),
	"4": ("HIPAA", hipaa),
}
