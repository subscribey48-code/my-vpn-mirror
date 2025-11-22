import requests

# Sumber Data (Kita coba beberapa mirror biar ga gagal)
URLS = [
    "http://www.vpngate.net/api/iphone/",
    "https://raw.githubusercontent.com/Dragon2fly/vpngate-with-proxy/master/vpngate.csv",
    "http://219.100.37.247/api/iphone/"
]

def main():
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for url in URLS:
        try:
            print(f"Mencoba download dari: {url}")
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200 and ("HostName" in resp.text or "#HostName" in resp.text):
                # SIMPAN FILE
                with open("vpngate.csv", "w", encoding="utf-8") as f:
                    f.write(resp.text)
                print("✅ SUKSES! File vpngate.csv berhasil diupdate.")
                return
        except Exception as e:
            print(f"❌ Gagal: {e}")

if __name__ == "__main__":
    main()
