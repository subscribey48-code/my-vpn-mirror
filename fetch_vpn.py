import requests

# KITA AMBIL LANGSUNG DARI SUMBERNYA
# GitHub Actions (Server USA) biasanya tidak diblokir oleh VPNGate
URLS = [
    "http://www.vpngate.net/api/iphone/",      # Link Utama
    "http://219.100.37.247/api/iphone/",       # Link IP Direct (Jepang)
    "https://vpngate.net/api/iphone/"          # Link HTTPS
]

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    for url in URLS:
        try:
            print(f"Mencoba download dari OFFICIAL: {url}")
            # Timeout 60 detik biar sabar
            resp = requests.get(url, headers=headers, timeout=60)
            
            # Validasi apakah isinya CSV yang benar?
            if resp.status_code == 200 and ("HostName" in resp.text or "#HostName" in resp.text):
                # SIMPAN FILE JADI 'vpngate.csv'
                with open("vpngate.csv", "w", encoding="utf-8") as f:
                    f.write(resp.text)
                print(f"✅ SUKSES! Berhasil download dari {url}")
                return # Berhenti jika sudah berhasil
            else:
                print(f"⚠️ Gagal (Status {resp.status_code}) atau konten salah.")
                
        except Exception as e:
            print(f"❌ Error koneksi ke {url}: {e}")

    print("😭 Gagal download dari semua link official.")
    exit(1) # Kasih kode error biar Action-nya merah

if __name__ == "__main__":
    main()
