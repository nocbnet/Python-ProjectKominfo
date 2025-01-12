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
    "UPTD PKM ANGGADITA": "10.75.8.18",
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
    "UPTD PKM WADAS": "10.75.8.98",
}

# Username dan Password Router MikroTik
username = 'bnet'
password = 'bnetpastimaju'

# Fungsi untuk mengubah port Winbox, disable port www (80) dan https (443)
def change_winbox_port_and_disable_services(ip_address):
    try:
        connection = RouterOsApiPool(ip_address, username=username, password=password, port=8728, plaintext_login=True)
        api = connection.get_api()
        
        # Mengubah port Winbox ke 8299
        api.get_resource('/ip/service').set(port="8299", numbers='winbox')
        
        # Menonaktifkan service www (port 80)
        api.get_resource('/ip/service').set(disabled="yes", numbers='www')
        
        # Menonaktifkan service https (port 443)
        api.get_resource('/ip/service').set(disabled="yes", numbers='www-ssl')

        # Menonaktifkan service ftp (port 21)
        api.get_resource('/ip/service').set(disabled="yes", numbers='ftp')
        
        print(f"Port Winbox di {ip_address} berhasil diubah menjadi 8299, dan port www serta https dinonaktifkan")
        connection.disconnect()
    except Exception as e:
        print(f"Gagal mengubah port Winbox atau menonaktifkan layanan di {ip_address}: {e}")

# Main function untuk mengiterasi dan membuat user pada setiap router
def main():
    # Loop melalui semua perangkat dan ubah port Winbox
    for name, ip in sites.items():
        change_winbox_port_and_disable_services(ip)

if __name__ == "__main__":
    main()
