# Status kondisi pembelian
stok_tersedia = True
punya_uang_tunai = False
punya_kartu_kredit = True

# Logika Matematika (AND, OR)
bisa_beli = stok_tersedia and (punya_uang_tunai or punya_kartu_kredit)

# Menampilkan hasil
print("\n--- Status Pembelian Barang ---")
if bisa_beli:
    print("Status: Pembelian Berhasil (True)")
else:
    print("Status: Pembelian Gagal (False)")