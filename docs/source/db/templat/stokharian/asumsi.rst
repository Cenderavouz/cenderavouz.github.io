================
Asumsi
================

Karena sifatnya yang dibuat sesuai pesanan, ada beberapa asumsi yang membatasi Templat Database ini.

* Pencatatan dan Tampilan dimaksudkan hanya untuk stok hari yang sedang berlangsung (current day). Ini berarti data stok kemarin dan hari lainnya menjadi usang (kecuali untuk penyalinan data Perdana).
* Tampilan koleksi :guilabel:`Stok Harian` diatur per grup sesuai field ``Nama Brg``. Hal ini dimaksudkan untuk memudahkan melihat alur stok barang menurut jam.
* :term:`Action-action <Action>` dimaksudkan untuk dijalankan pada awal hari (sebelum memulai jual-beli).
* Urutan dimaksudkan untuk menyusun catatan barang-barang yang tetap setiap harinya.
* Agregasi ``Masuk`` dihitung berdasarkan penjumlahan field ``Masuk`` untuk tiap-tiap ``Nama Brg``.
* Agregasi ``Total`` dihitung berdasarkan penjumlahan field ``Awal + Masuk - Akhir`` untuk tiap-tiap ``Nama Brg``.