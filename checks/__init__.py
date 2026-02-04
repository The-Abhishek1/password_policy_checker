from .nist import check as nist
from .pci_dss import check as pci_dss
from .iso_27001 import check as iso_27001
from .hipaa import check as hipaa
from .cis import check as cis
from .soc2 import check as soc2

ALL_CHECKERS = {
	"1": ("NIST", nist),
	"2": ("PCI-DSS", pci_dss),
	"3": ("ISO-27001", iso_27001),
	"4": ("HIPAA", hipaa),
	"5": ("SOC 2", soc2),
	"6": ("CIS Controls", cis),
}
