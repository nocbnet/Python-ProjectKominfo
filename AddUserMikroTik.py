from routeros_api import RouterOsApiPool

# Daftar Site dan IP Router
sites = {
    "OPD DISHUB": "10.75.12.2",
    "OPD DPRKP": "10.75.12.6",
    "OPD DPMTSP": "10.75.12.10",
    "OPD RUMAH SAKIT KHUSUS PARU": "10.75.12.14",
    "OPD DINAS PENDIDIKAN, PEMUDA DAN OLAH RAGA": "10.75.12.18",
    "OPD DINAS PEMBERDAYAAN MASYARAKAT DAN DESA": "10.75.12.22",
    "OPD DINAS SOSIAL": "10.75.12.34",
    "OPD SATUAN POLISI PAMONG PRAJA": "10.75.12.38",
    "OPD UPTD METROLOGI LEGAL KAB. KARAWANG": "10.75.12.46",
    "OPD SEKRETARIAT DAERAH (GEDUNG MANGKUDIDJOJO) - ASDA 3": "10.75.12.74",
    "OPD SEKRETARIAT DAERAH (GEDUNG SACA KUSUMA) - ASDA 1": "10.75.12.78",
    "OPD SEKRETARIAT DPRD": "10.75.12.82",
    "OPD GEDUNG PARIPURNA DPRD": "10.75.12.86",
    "OPD DINAS KOMUNIKASI DAN INFORMATIKA": "10.75.12.90",
    "OPD BADAN PERENCANAAN PEMBANGUNAN DAERAH": "10.75.12.94",
    "OPD DINAS PERIKANAN": "10.75.12.98",
    "OPD BADAN PENDAPATAN DAERAH": "10.75.12.102",
    "OPD BADAN PENGELOLAAN KEUANGAN DAN ASET DAERAH": "10.75.12.106",
    "OPD DINAS LINGKUNGAN HIDUP": "10.75.12.50",
    "OPD DINAS KEPENDUDUKAN DAN PENCATATAN SIPIL": "10.75.12.26",
    "OPD DINAS TENAGA KERJA DAN TRANSMIGRASI": "10.75.12.30",
    "OPD BADAN PENANGGULANGAN BENCANA DAERAH": "10.75.12.42",
    "OPD UPTD LEMBAGA PENYIARAN PUBLIK STURADA 89.4 FM": "10.75.12.54",
    "OPD DINAS PERTANIAN DAN KETAHANAN PANGAN": "10.75.12.58",
    "OPD DINAS ARSIP DAN PERPUSTAKAAN": "10.75.12.62",
    "OPD BIDANG KETAHANAN PANGAN PADA DINAS PERTANIAN DAN KETAHANAN PANGAN": "10.75.12.66",
    "OPD SEKRETARIAT DAERAH (GEDUNG SACA KUSUMA) - ASDA 2": "10.75.12.70",
    "OPD DINAS KOPERASI, USAHA KECIL DAN MENENGAH": "10.75.12.110",
    "OPD DINAS PEMBERDAYAAN PEREMPUAN DAN PERLINDUNGAN": "10.75.12.114",
    "OPD BADAN KESATUAN BANGSA DAN POLITIK": "10.75.12.118",
    "OPD UPTD PERPUSTAKAAN": "10.75.12.122",
    "OPD INSPEKTORAT": "10.75.12.126",
    "OPD DINAS PERINDUSTRIAN DAN PERDAGANGAN": "10.75.12.130",
    "OPD DINAS PENGENDALIAN PENDUDUK DAN KELUARGA": "10.75.12.134",
    "OPD BADAN KEPEGAWAIAN DAN PENGEMBANGAN SUMBER DAYA MANUSIA": "10.75.12.138",
    "OPD DINAS PEKERJAAN UMUM DAN PENATAAN RUANG": "10.75.12.142",
    "OPD DINAS PARIWISATA DAN KEBUDAYAAN": "10.75.12.146",
    "OPD RUMAH SAKIT UMUM DAERAH": "10.75.12.150",
    "OPD DINAS KESEHATAN KARAWANG": "10.75.12.154"
}

# Username dan Password Router MikroTik
username = 'bnetkrw'
password = 'bnet2024!!'

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
