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
