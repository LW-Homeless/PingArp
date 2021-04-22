import datetime
import os

from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from tabulate import tabulate
from colorama import init, Fore

from model.ScanArp import ScanArp


class PingArp:

    def main(self):

        init()
        try:
            if os.name == "posix":
                os.system("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")

            parser = ArgumentParser(prog="PingArg", description="PingArp herramienta que permite determinar\n"
                                    "si una dirección IP esta activa y es accesible en la red local\n"
                                    "mediante un escaneo ARP.",
                                    formatter_class=RawTextHelpFormatter)

            parser.add_argument("-t", type=str, metavar="",
                                help="IP(s) a escanear. Estas direcciones pueden ser unicamente una direccion IP,"
                                     "\ndirecciones IPs separados por coma(,) o un rango de IP utilizando notacion CIDR.\n")

            args = parser.parse_args()
            ips = args.t.split(",")
            scan = ScanArp()

            print(Fore.RED + "PingArp v1.0.0.\nCreado por: Homeless")

            date = datetime.datetime.now()
            print(Fore.RED + "Iniciado: ", date.strftime("%H:%M:%S"))

            table = scan.run_scan(ips)

            if len(table) > 0:
                header = ["IP", "MAC ADDRESS", "MAC VENDOR"]
                print(Fore.GREEN + tabulate(table, header, tablefmt="psql"))
                date = datetime.datetime.now()
                print(Fore.RED + "Finalizado: ", date.strftime("%H:%M:%S"))
            else:
                print(Fore.YELLOW + "\n[!] No se obtuvieron resultados. para el rango -> " + args.t)
                date = datetime.datetime.now()
                print(Fore.RED + "Finalizado: ", date.strftime("%H:%M:%S"))
        except AttributeError:
            print(Fore.YELLOW + "[!] La opcion -t es obligatoria, para mas informacion ejecute PingArp.py -h ")
        except RuntimeError:
            print(Fore.YELLOW + "\n[!] PingArp no se puede ejecutar, WinPcap o Npcap no esta instalado,"
                                " visite: https://nmap.org/npcap/ para su descarga y instalacion.")
        except PermissionError:
            print(Fore.YELLOW + "\n[!] PingArp necesita permiso de super usuario"
                                " o usuario adminitrador, para su ejecución.")
        except KeyboardInterrupt:
            print(Fore.LIGHTBLUE_EX + "Haz cancelado la ejecucion del programa, Bye!")
            exit(0)


if __name__ == '__main__':
    app = PingArp()
    app.main()
