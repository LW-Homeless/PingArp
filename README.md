# PingArp
PingArp herramienta que permite determinar si una dirección IP esta activa y es accesible en la red local mediante un escaneo ARP.
La herramienta acepta como parámetro (-t) puede recibir una direcion IP o un rango de dirección IP separados por comas(,), también soporta notación CIDR.

# Requisitos
- Python 3.7.x o superior.
- setuptools.
- Npcap o WinPcap se puede descargar del siguiente links. (https://nmap.org/npcap/).


# Dependencias
colorama==0.4.4
scapy==2.4.4
tabulate==0.8.9

# Instrucciones de uso
- Descarga o clona el repositorio.
- Instale las dependencia con el siguiente comando.

```
pip install -r requirements.txt

```
- Luego, ejecuta el archivo PingArp.py con el siguiente comando.

```
python PingArp -t [rango de IPS o IP]
```

# Ejemplos

```
python PingArp -t 192.168.18.1
```
Realiza un PingArp a la dirección IP indicada en el parámetro -t (192.168.18.1)

```
python PingArp -t 192.168.18.1,192.168.18.2,192.168.18.3
```
Realiza un PingArp a la direccines IPs indicadas en el parámetro -t (192.168.18.1,192.168.18.2,192.168.18.3). Nota: Las direcciones IPs se separan por comas(,).

```
python PingArp -t 192.168.18.1/24
```
Realiza un PingArp a la direccines IPs indicadas en el parámetro -t en este caso se utiliza notación CIDR, en el ejemplo se escanera desde la IP 192.168.18.1 hasta 192.168.18.255.

# Demostración
![alt text](https://github.com/LW-Homeless/PingArp/blob/main/PingArp.gif)
