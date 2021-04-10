import csv
import os


class MacVendor:

    @staticmethod
    def get_vendor_mac(mac):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "mac-vendor-normalized.csv")
        file = open(path, "rt", encoding="UTF-8")
        reader = csv.reader(file, delimiter=",")

        for line in reader:
            mac_vendor = mac[:8].upper()
            if mac_vendor == line[0]:
                return line[2]
        return "Unknown"

        file.close()
