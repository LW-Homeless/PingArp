import scapy.all as scapy

from model.MacVendor import MacVendor


class ScanArp:

    def __init__(self):
        self.__result_scan = []

    def run_scan(self, ips):
        for ip in ips:
            packet_list = [scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip)]
            response = scapy.srp(packet_list, verbose=0, timeout=10)

            packet_count = len(response[0])
            for pkt in range(packet_count):
                self.__result_scan.append([response[0][pkt][1].psrc, response[0][pkt][1].hwsrc,
                                           MacVendor.get_vendor_mac(response[0][pkt][1].hwsrc)])

        return self.__result_scan
