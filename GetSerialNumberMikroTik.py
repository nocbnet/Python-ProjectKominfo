from routeros_api import RouterOsApiPool

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

# Fungsi untuk mengambil data routerboard (type dan serial number)
def get_routerboard_info(router_ip, username, password):
    try:
        # Koneksi ke API MikroTik
        connection = RouterOsApiPool(router_ip, username=username, password=password, port=8728, plaintext_login=True)
        api = connection.get_api()

        # Mengambil informasi routerboard (type dan serial number)
        routerboard_resource = api.get_resource('/system/routerboard')
        routerboard_info = routerboard_resource.get()

        # Output Type dan Serialnumber
        for info in routerboard_info:
            print(f"{info.get('model')}")
            print(f"{info.get('serial-number')}\n")

        # Menutup koneksi API
        connection.disconnect()
    except Exception as e:
        print(f"Error saat mengambil data routerboard di {router_ip}: {e}\n")

# Main function untuk mengiterasi dan membuat user pada setiap router
def main():

    for site_name, router_ip in sites.items():
        get_routerboard_info(router_ip, username, password)

if __name__ == "__main__":
    main()
