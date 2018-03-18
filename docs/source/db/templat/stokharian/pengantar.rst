=========
Pengantar
=========

Dokumen ini adalah dokumentasi Templat Stok Harian, sebuah templat database pengelolaan persediaan barang bagi penjual pulsa perseorangan (konter).

Bantuan
-------

Merasa kesulitan? Kami senang membantu!

* Coba baca :doc:`../../db-faq` - berisi jawaban dari pertanyaan-pertanyaan yang sering muncul.
* Mencari arti istilah tertentu? Coba :doc:`../../db-daftar-istilah`, :ref:`Indeks <genindex>`, atau :doc:`Daftar Isi <index>`.
* :ref:`Cari dengan kata kunci <search>`.

Selayang Pandang
----------------

.. index:: Database
.. index:: Memento Database
.. index:: Templat Memento Database

Dokumentasi ini berisi penjelasan templat pengelolaan data barang dan stok harian ke dalam sebuah :term:`database <Database>`. Garis besar dokumentasi ini terdiri dari:

* :doc:`Mulai <memulai>` dengan memasang :term:`Memento Database <Memento Database>`, beserta :term:`Templat Memento Database <Templat Memento Database>`.
* :doc:`Pemakaian <memakai>` database seperti penambahan, pencatatan, penyalinan dan laporan data.
* :doc:`Kaidah <../../db-kaidah>` sebagai referensi mengenai aplikasi dan berkas templat.
* :doc:`Asumsi <asumsi>` berupa catatan tentang batasan penggunaan.


Informasi Templat
-----------------

Templat ini terdiri dari koleksi-koleksi dan script seperti tertera di bawah:


Koleksi
~~~~~~~

**Daftar Barang**

=================  =================  =================
Field              Tipe               Tampilkan sbg
=================  =================  =================
Nama Brg           Teks               nama
Jenis              Jenis              deskripsi
Urutan             Tombol Radio       
=================  =================  =================


**Stok Harian**

*UTAMA*

=================  =================  =================
Nama Field         Tipe               Tampilkan sbg
=================  =================  =================
Nama Brg           Teks               
Jenis              Jenis              
Kegiatan           Tombol Radio       
Nominal            Integer       
@Harga             Mata Uang       
Keterangan         Teks       
=================  =================  =================


*KODE*

=================  =================  ==================
Nama Field         Tipe               Tampilkan sbg
=================  =================  ==================
Tgl                Tanggal            status
Waktu              Jam                status
Urutan             Integer       
_agreall           Kalkulasi       
_agre+             Kalkulasi       
key                Teks               nama
vstate             Integer            
Hubungan           Tautan ke entri
=================  =================  ==================

Script
~~~~~~

**Trigger**

- symbolKey
- updateKey

**Action**

- Salin Data Stok Umum
- Salin Stok Perdana Terakhir
- Laporan Hari Ini
- Data Contoh


