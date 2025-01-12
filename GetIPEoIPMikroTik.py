from routeros_api import RouterOsApiPool
import time

# Daftar Site dan IP Router
sites = {
    "UPTD PKM TELAGASARI": "10.75.8.22",
    "UPTD PKM KLARI": "10.75.8.26",
    "UPTD PKM CIAMPEL": "10.75.8.30",
    "UPTD PKM MAJALAYA": "10.75.8.34",
    "UPTD PKM CIKAMPEK UTARA": "10.75.8.38",
    "UPTD PKM JOMIN": "10.75.8.42",
    "UPTD PKM TIRTAMULYA": "10.75.8.46",
    "UPTD PKM PACING": "10.75.8.50",
    "UPTD PKM LEMAHABANG": "10.75.8.54",
    "UPTD PKM BALONGSARI": "10.75.8.58",
    "UPTD PKM LEMAHDUHUR": "10.75.8.62",
    "UPTD PKM TUNGGAKJATI": "10.75.8.66",
    "UPTD PKM RAWAMERTA": "10.75.8.70",
    "UPTD PKM KUTAMUKTI": "10.75.8.74",
    "UPTD PKM PLAWAD": "10.75.8.78",
    "UPTD PKM WANAKERTA": "10.75.8.82",
    "UPTD PKM CURUG": "10.75.8.86",
    "UPTD PKM PANGKALAN": "10.75.8.90",
    "UPTD PKM LOJI": "10.75.8.94",
    "UPTD PKM WADAS": "10.75.8.98"
}

# Username dan Password Router MikroTik
username = 'bnet'
password = 'bnetpastimaju'

# Fungsi untuk mengambil IP address dari interface dengan nama mengandung 'eoip'
def get_eoip_ip_addresses(router_ip, username, password):
    try:
        # Koneksi ke API MikroTik
        connection = RouterOsApiPool(router_ip, username=username, password=password, port=8728, plaintext_login=True)
        api = connection.get_api()

        # Mengambil daftar interface
        interface_resource = api.get_resource('/interface')
        interfaces = interface_resource.get()

        # Filter interface yang mengandung 'eoip'
        eoip_interfaces = [iface for iface in interfaces if 'eoip' in iface.get('name', '').lower()]

        if not eoip_interfaces:
            print(f"Tidak ada interface dengan nama mengandung 'eoip' di router {router_ip}")
            return

        # Mengambil IP address berdasarkan interface
        ip_address_resource = api.get_resource('/ip/address')
        ip_addresses = ip_address_resource.get()

        for eoip_iface in eoip_interfaces:
            eoip_name = eoip_iface['name']
            for ip in ip_addresses:
                if ip.get('interface') == eoip_name:
                    print(f"{ip.get('address')}".replace('/30', ''))

        # Menutup koneksi API
        connection.disconnect()
    except Exception as e:
        print(f"Error saat mengambil IP address dari interface 'eoip' di {router_ip}: {e}")

# Main function untuk mengiterasi dan membuat user pada setiap router
def main():

    for site_name, router_ip in sites.items():
        get_eoip_ip_addresses(router_ip, username, password)

if __name__ == "__main__":
    main()
