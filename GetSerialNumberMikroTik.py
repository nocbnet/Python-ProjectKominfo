from routeros_api import RouterOsApiPool

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
