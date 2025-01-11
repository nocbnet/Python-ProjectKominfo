from routeros_api import RouterOsApiPool
import time

# Daftar Site dan IP Router
sites = {
    "KELURAHAN KARANGPAWITAN": "10.75.0.2",
    "KELURAHAN WETAN": "10.75.0.6",
    "KELURAHAN ADIARSA TIMUR": "10.75.0.10",
    "KELURAHAN TANJUNG MEKAR": "10.75.0.14",
    "KELURAHAN KULON": "10.75.0.18",
    "KELURAHAN ADIARSA BARAT": "10.75.0.22",
    "KELURAHAN NAGASARI": "10.75.0.26",
    "KELURAHAN TANJUNG PURA": "10.75.0.30",
    "KELURAHAN PLAWAD": "10.75.0.34",
    "KELURAHAN PALUMBOSARI": "10.75.0.38",
    "KELURAHAN MEKAR JATI": "10.75.0.42",
    "KELURAHAN TUNGGAK JATI": "10.75.0.46",
    "UPTD PKM ADIARSA": "10.75.8.2",
    "UPTD PKM TELUKJAMBE": "10.75.8.6",
    "UPTD PKM KARAWANG": "10.75.8.10",
    "UPTD PKM KARAWANG KULON": "10.75.8.14",
    "UPTD PKM ANGGADITA": "10.75.8.18"
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
