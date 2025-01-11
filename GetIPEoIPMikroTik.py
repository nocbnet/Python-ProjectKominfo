from routeros_api import RouterOsApiPool
import time

# Daftar Site dan IP Router
sites = {
    "PUSKESMAS BATUJAYA": "10.75.8.102",
    "PUSKESMAS CIBUAYA": "10.75.8.106",
    "PUSKESMAS PAKISJAYA": "10.75.8.110",
    "PUSKESMAS PEDES": "10.75.8.114",
    "PUSKESMAS SUNGAI BUNTU": "10.75.8.118",
    "PUSKESMAS TIRTAJAYA": "10.75.8.122",
    "PUSKESMAS MEDANGASEM": "10.75.8.126",
    "PUSKESMAS JAYAKERTA": "10.75.8.130",
    "PUSKESMAS KALANGSARI": "10.75.8.134",
    "PUSKESMAS PASIR RUKEM": "10.75.8.138",
    "PUSKESMAS BAYURLOR": "10.75.8.142",
    "PUSKESMAS CILAMAYA": "10.75.8.146",
    "PUSKESMAS SUKATANI": "10.75.8.150",
    "PUSKESMAS KERTAMUKTI": "10.75.8.154",
    "PUSKESMAS TEMPURAN": "10.75.8.158",
    "PUSKESMAS CICINDE": "10.75.8.162",
    "PUSKESMAS GEMPOL": "10.75.8.166",
    "PUSKESMAS CIKAMPEK": "10.75.8.170",
    "PUSKESMAS JATI SARI": "10.75.8.174",
    "PUSKESMAS PURWASARI": "10.75.8.178",
    "PUSKESMAS NAGASARI": "10.75.8.182",
    "PUSKESMAS TANJUNGPURA": "10.75.8.186",
    "PUSKESMAS KUTAWALUYA": "10.75.8.190",
    "PUSKESMAS RENGASDENGKLOK": "10.75.8.194",
    "PUSKESMAS KOTA BARU": "10.75.8.198",
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
