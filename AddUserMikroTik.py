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

# Fungsi untuk membuat user baru di MikroTik
def create_user(router_ip, username, password, user_name, user_password, user_group):
    try:
        # Koneksi ke API MikroTik
        connection = RouterOsApiPool(router_ip, username=username, password=password, port=8728, plaintext_login=True)
        api = connection.get_api()

        # Menambahkan user baru
        user_resource = api.get_resource('/user/')
        user_resource.add(name=user_name, password=user_password, group=user_group)

        print(f"User {user_name} berhasil dibuat di router {router_ip}")

        # Menutup koneksi API
        connection.disconnect()
    except Exception as e:
        print(f"Error saat membuat user di {router_ip}: {e}")

# Main function untuk mengiterasi dan membuat user pada setiap router
def main():
    # Username, password dan group untuk user baru
    user_name = "kominfo"
    user_password = "Aptika@86##"
    user_group = "full"

    for site_name, router_ip in sites.items():
        create_user(router_ip, username, password, user_name, user_password, user_group)

if __name__ == "__main__":
    main()
