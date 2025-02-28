# -- coding: utf-8 --
"""
Created on Tue May 28 09:28:59 2024

@author: Dilara Bebek
"""
##--------DİLARA BEBEK----------2212721018----------KAN BANKASI UYGULAMASI----------------------##

##--------------------KÜTÜPHANELER--------------------------------------------------------------##
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore
import anamenuUI 
import girisUI 
import kayitUI 
import sqlite3


#------------------ VERİ TABANI OLUŞTUR---------
#----------------------------------------------
class Veritabani:
    def __init__(self):
        self.conn = sqlite3.connect("veritabani.db") # Veritabanına bağlan
        self.curs = self.conn.cursor() # Veritabanı işlemleri için imleç oluştur
        self.tablolari_olustur() # Tabloları oluştur
        
    def tablolari_olustur(self):
        # Bagisci bilgilerini tutan tablo oluşturma sorgusu
        sorguCretblwKayitTutucu=("CREATE TABLE IF NOT EXISTS tblwKayitTutucu (  \
                                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                                 BagisciAdi TEXT NOT NULL,\
                                 BagisciSoyadi TEXT NOT NULL,\
                                 Tc TEXT NOT NULL, \
                                 Cinsiyet TEXT NOT NULL, \
                                 DogumTarihi TEXT NOT NULL, \
                                 BagisciTelefon TEXT NOT NULL, \
                                 BagisciEposta TEXT NOT NULL, \
                                 BagisciEv TEXT NOT NULL, \
                                 YakinAdi TEXT NOT NULL, \
                                 YakinSoyadi TEXT NOT NULL, \
                                 YakinTelefon TEXT NOT NULL, \
                                 Kilo TEXT NOT NULL, \
                                 Boy TEXT NOT NULL, \
                                 KronikHastalik TEXT NOT NULL, \
                                 Ilac TEXT NOT NULL , \
                                 Alerji TEXT NOT NULL, \
                                 Sigara TEXT NOT NULL, \
                                 GecmisMudahale TEXT NOT NULL, \
                                 NotBilgisi TEXT NOT NULL, \
                                 KanBagisTarihi TEXT NOT NULL , \
                                 KanGrubu TEXT NOT NULL, \
                                 RhFaktoru TEXT NOT NULL, \
                                 BagisTuru TEXT NOT NULL, \
                                 Sehir TEXT NOT NULL, \
                                 SonKanBagisiTarihi TEXT NOT NULL, \
                                 IlkKanBagisi TEXT NOT NULL)")
        
        
        # Kullanıcı bilgilerini tutan tablo oluşturma sorgusu
        sorguCretblUsers = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """

        self.curs.execute(sorguCretblwKayitTutucu) # Bagisci tablosunu oluştur
        self.curs.execute(sorguCretblUsers) # Kullanıcı  tablosunu oluştur
        self.conn.commit()  # Veritabanı işlemlerini kaydet
        
    def execute(self, sorgu, params=()):
        # Veritabanı sorgusu çalıştır
        self.curs.execute(sorgu, params)
        self.conn.commit()

    def fetchall(self, sorgu, params=()):
        # Veritabanından tüm sonuçları getir
        self.curs.execute(sorgu, params)
        return self.curs.fetchall()

    def fetchone(self, sorgu, params=()):
        # Veritabanından tek bir sonuç getir
        self.curs.execute(sorgu, params)
        return self.curs.fetchone()

    def close(self):
        # Veritabanı bağlantısını kapat
        self.conn.close()
        




##-------------------- UYGULAMA CLASS YAPISI-----------------##
##-----------------------------------------------------------##
class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.veritabani = Veritabani() # Veritabanı nesnesini oluştur
        self.initUI() # Arayüzü başlat

    def initUI(self):
        # Giriş ekranı
        self.penGiris = QMainWindow()
        self.uiGiris = girisUI.Ui_MainWindow()
        self.uiGiris.setupUi(self.penGiris)
        self.penGiris.show() # Giriş ekranını göster

        # Kayıt ekranı
        self.penKayit = QMainWindow()
        self.uiKayit = kayitUI.Ui_MainWindow()
        self.uiKayit.setupUi(self.penKayit)

        # Ana menü ekranı
        self.penAna = QMainWindow()
        self.uiAna = anamenuUI.Ui_MainWindow()
        self.uiAna.setupUi(self.penAna)

        # Sinyal-slot bağlantıları
        self.uiGiris.psbGirisGiris.clicked.connect(self.girisYap)
        self.uiGiris.psbKayit.clicked.connect(self.kayitOl)

        self.uiKayit.psbKayitKayit.clicked.connect(self.kaydiTamamla)

        self.uiAna.psbRandevuAl.clicked.connect(self.ekle)
        self.uiAna.psRandevuListele.clicked.connect(self.listele)
        self.uiAna.psCikis.clicked.connect(self.cikis)
        self.uiAna.psRavdevuSil.clicked.connect(self.sil)
        self.uiAna.psRandevuAra.clicked.connect(self.ara)
        self.uiAna.tblwKayitTutucu.itemSelectionChanged.connect(self.doldur)
        self.uiAna.psGuncelle.clicked.connect(self.guncelle)
 
        # Mevcut kayıtları listele
        self.listele() 






    def ekle(self):
        # Bağışçı bilgilerini al ve veritabanına ekle
        _lneBagisciAdi = self.uiAna.lneBagisciAdi.text()
        _lneBagisciSoyadi = self.uiAna.lneBagisciSoyadi.text()
        _lneTc = self.uiAna.lneTc.text()
        _cmbCinsiyet = self.uiAna.cmbCinsiyet.currentText()
        _dteDogumTarihi = self.uiAna.dteDogumTarihi.date().toString(QtCore.Qt.ISODate)
        _lneBagisciTelefon = self.uiAna.lneBagisciTelefon.text()
        _lneBagisciEposta = self.uiAna.lneBagisciEposta.text()
        _lneBagisciEv = self.uiAna.lneBagisciEv.text()
        _lneYakinAdi = self.uiAna.lneYakinAdi.text()
        _lneYakinSoyadi = self.uiAna.lneYakinSoyadi.text()
        _lneYakinTelefon = self.uiAna.lneYakinTelefon.text()
        _spnKilo = self.uiAna.spnKilo.value()
        _lneBoy = self.uiAna.lneBoy.text()

        # Checkbox değerlerini al
        _chkbKronikHastalik = "Kronik Hasta" if self.uiAna.chkbKronikHastalik.isChecked() else "Kronik Hasta değil"
        _chkbIlac = "Düzenli İlaç Kullanıyor" if self.uiAna.chkbIlac.isChecked() else "Düzenli İlaç Kullanmıyor"
        _chkbAlerji = "Alerjik Hasta" if self.uiAna.chkbAlerji.isChecked() else "Alerjik Hasta Değil"
        _chkbSigara = "Sigara Veya Alkol kullanıyor" if self.uiAna.chkbSigara.isChecked() else "Sigara Veya Alkol Kullanmıyor"

        _txeGecmisMudahale = self.uiAna.txeGecmisMudahale.toPlainText()
        _txeNotBilgisi = self.uiAna.txeNotBilgisi.toPlainText()
        _cldwKanBagisTarihi = self.uiAna.cldwKanBagisTarihi.selectedDate().toString(QtCore.Qt.ISODate)
        _cmbKanGrubu = self.uiAna.cmbKanGrubu.currentText()
        _cmbRhFaktoru = self.uiAna.cmbRhFaktoru.currentText()
        _cmbBagisTuru = self.uiAna.cmbBagisTuru.currentText()
        _cmbSehir = self.uiAna.cmbSehir.currentText()
        _lneSonKanBagisiTarihi = self.uiAna.lneSonKanBagisiTarihi.text()
        _chkblkKanBagisi = "İlk Defa Kan Bağışı Yapıyor" if self.uiAna.chkblkKanBagisi.isChecked() else "Daha Önce Kan Bağışı Yapmamış"
        
        
        # Veritabanına bağışçı bilgilerini ekle
        self.veritabani.execute("INSERT INTO tblwKayitTutucu \
                     (BagisciAdi,BagisciSoyadi,Tc,Cinsiyet,DogumTarihi,BagisciTelefon,\
                     BagisciEposta,BagisciEv,YakinAdi,YakinSoyadi,YakinTelefon, \
                     Kilo,Boy,KronikHastalik,Ilac,Alerji,Sigara,GecmisMudahale, \
                     NotBilgisi,KanBagisTarihi,KanGrubu,RhFaktoru,BagisTuru,Sehir, \
                     SonKanBagisiTarihi,IlkKanBagisi) \
                     VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , \
                     (_lneBagisciAdi, _lneBagisciSoyadi, _lneTc, _cmbCinsiyet, _dteDogumTarihi, \
                     _lneBagisciTelefon, _lneBagisciEposta, _lneBagisciEv, _lneYakinAdi, \
                     _lneYakinSoyadi, _lneYakinTelefon, _spnKilo, _lneBoy, _chkbKronikHastalik, \
                     _chkbIlac, _chkbAlerji, _chkbSigara, _txeGecmisMudahale, _txeNotBilgisi, \
                     _cldwKanBagisTarihi, _cmbKanGrubu, _cmbRhFaktoru, _cmbBagisTuru, _cmbSehir, _lneSonKanBagisiTarihi, \
                     _chkblkKanBagisi))
            
            
        self.listele()  # Kayıtları güncelle ve tabloyu yenile

        

    def listele(self):
        self.uiAna.tblwKayitTutucu.setRowCount(0) # Tabloyu temizle
        
        # Tablo başlıklarını ayarla
        self.uiAna.tblwKayitTutucu.setHorizontalHeaderLabels(('No', 'Ad', 'Soyad', 'TC', 'Cinsiyet', 'Doğum', \
                                                      'Tlf No', 'E-Posta', 'Adres', 'Ykn. Adı', 'Ykn. Soyad', 'Yakın Tlf',\
                                                      'Kilo', 'Boy', 'Hastalık', 'İlaç', 'Alerji', 'Bağımlı', 'Müdahale',\
                                                      'Not', 'Tarih', 'Kan', 'Rh', 'Bağış', 'Şehir', 'Son Bağ.', 'İlk Bağ.'))
        
         # Sütunları tablo genişliğine göre otomatik olarak ayarla
        self.uiAna.tblwKayitTutucu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tblwKayitTutucu = self.veritabani.fetchall("SELECT * FROM tblwKayitTutucu") # Veritabanından tüm kayıtları al
        # Kayıtları tabloya ekle
        for satirIndeks, satirVeri in enumerate(tblwKayitTutucu):
            self.uiAna.tblwKayitTutucu.insertRow(satirIndeks)
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.uiAna.tblwKayitTutucu.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
                
                
                
                
         # Doldurulan alanlarını temizle   
        self.uiAna.lneBagisciAdi.clear()
        self.uiAna.lneBagisciSoyadi.clear()
        self.uiAna.lneTc.clear()
        self.uiAna.cmbCinsiyet.setCurrentIndex(-1)
        self.uiAna.dteDogumTarihi.setDate(QtCore.QDate.currentDate())
        self.uiAna.lneBagisciTelefon.clear()
        self.uiAna.lneBagisciEposta.clear()
        self.uiAna.lneBagisciEv.clear()
        self.uiAna.lneYakinAdi.clear()
        self.uiAna.lneYakinSoyadi.clear()
        self.uiAna.lneYakinTelefon.clear()
        self.uiAna.spnKilo.setValue(55)
        self.uiAna.lneBoy.clear()
        self.uiAna.chkbKronikHastalik.setChecked(False)
        self.uiAna.chkbIlac.setChecked(False)
        self.uiAna.chkbAlerji.setChecked(False)
        self.uiAna.chkbSigara.setChecked(False)
        self.uiAna.txeGecmisMudahale.clear()
        self.uiAna.txeNotBilgisi.clear()
        self.uiAna.cldwKanBagisTarihi.setSelectedDate(QtCore.QDate.currentDate()) 
        self.uiAna.cmbKanGrubu.setCurrentIndex(-1)
        self.uiAna.cmbRhFaktoru.setCurrentIndex(-1)
        self.uiAna.cmbBagisTuru.setCurrentIndex(-1)
        self.uiAna.cmbSehir.setCurrentIndex(-1)
        self.uiAna.lneSonKanBagisiTarihi.clear()  
        self.uiAna.chkblkKanBagisi.setChecked(False)


                
                
        
    def cikis(self):
        # Programdan çıkış için onay al
        cevap = QMessageBox.question(self.penAna, "ÇIKIŞ", "Programdan çıkmak istediğinize emin misiniz?", \
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:
            # Veritabanı bağlantısını kapat ve programdan çık
            self.veritabani.close()
            QApplication.quit()
        else:
            # Çıkış işlemi iptal edilirse ana pencereyi göster
            self.penAna.show()    
        
        
    def sil(self): 
        #Silme işlemi için onay al
        cevap = QMessageBox.question(self.penAna, "KAYIT SİL", "Kaydı silmek istediğinize emin misiniz?", \
                                   QMessageBox.Yes | QMessageBox.No )
        if cevap == QMessageBox.Yes:
            secili = self.uiAna.tblwKayitTutucu.selectedItems()
            if secili: # Eğer bir satır seçilmişse
                silinecek = secili[0].text() 
                try:
                    # Veritabanından seçilen kaydı sil
                    self.veritabani.curs.execute("DELETE FROM tblwKayitTutucu WHERE Id = ?", (silinecek,))
                    self.veritabani.conn.commit()
                    self.listele()
                    self.uiAna.statusbar.showMessage("Kayıt başarı ile silindi.", 10000)
                except Exception as Hata:
                    self.uiAna.statusbar.showMessage("Silme işlemi sırasında hata oluştu: " + str(Hata), 10000)
            else:
                self.uiAna.statusbar.showMessage("Lütfen silmek için bir kayıt seçin.", 10000)
        else:  
            self.uiAna.statusbar.showMessage("Silme işlemi iptal edildi...", 10000)
        
    
    def ara(self):
        #Aranacak değerleri al
        aranan1 = self.uiAna.lneBagisciAdi.text()
        aranan2 = self.uiAna.lneBagisciSoyadi.text()
        aranan3 = self.uiAna.lneTc.text()
        
        #Veritabanında ara ve sonuçları tabloya yaz
        self.veritabani.curs.execute("SELECT * FROM tblwKayitTutucu WHERE BagisciAdi=? OR BagisciSoyadi=? OR Tc=? OR (BagisciAdi=? AND BagisciSoyadi=?)", (aranan1, aranan2, aranan3, aranan1, aranan2))
        self.uiAna.tblwKayitTutucu.clear()
        for satirIndeks, satirVeri in enumerate(self.veritabani.curs):
            self.uiAna.tblwKayitTutucu.insertRow(satirIndeks)
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.uiAna.tblwKayitTutucu.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
    
    
    def doldur(self):
       # Seçili satırdaki bilgileri form alanlarına doldur
       secili = self.uiAna.tblwKayitTutucu.selectedItems()
       if secili:
           self.uiAna.lneBagisciAdi.setText(secili[1].text())
           self.uiAna.lneBagisciSoyadi.setText(secili[2].text())
           self.uiAna.lneTc.setText(secili[3].text())
           self.uiAna.cmbCinsiyet.setCurrentText(secili[4].text())
           self.uiAna.dteDogumTarihi.setDate(QtCore.QDate.fromString(secili[5].text(), "yyyy-MM-dd"))
           self.uiAna.lneBagisciTelefon.setText(secili[6].text())
           self.uiAna.lneBagisciEposta.setText(secili[7].text())
           self.uiAna.lneBagisciEv.setText(secili[8].text())
           self.uiAna.lneYakinAdi.setText(secili[9].text())
           self.uiAna.lneYakinSoyadi.setText(secili[10].text())
           self.uiAna.lneYakinTelefon.setText(secili[11].text())
           self.uiAna.spnKilo.setValue(int(secili[12].text()))
           self.uiAna.lneBoy.setText(secili[13].text())
           self.uiAna.chkbKronikHastalik.setChecked(secili[14].text() == "Kronik Hasta")
           self.uiAna.chkbIlac.setChecked(secili[15].text() == "Düzenli İlaç Kullanıyor")
           self.uiAna.chkbAlerji.setChecked(secili[16].text() == "Alerjik Hasta")
           self.uiAna.chkbSigara.setChecked(secili[17].text() == "Sigara Veya Alkol kullanıyor")
           self.uiAna.txeGecmisMudahale.setPlainText(secili[18].text())
           self.uiAna.txeNotBilgisi.setPlainText(secili[19].text())
           self.uiAna.cldwKanBagisTarihi.setSelectedDate(QtCore.QDate.fromString(secili[20].text(), QtCore.Qt.ISODate))
           self.uiAna.cmbKanGrubu.setCurrentText(secili[21].text())
           self.uiAna.cmbRhFaktoru.setCurrentText(secili[22].text())
           self.uiAna.cmbBagisTuru.setCurrentText(secili[23].text())
           self.uiAna.cmbSehir.setCurrentText(secili[24].text())
           self.uiAna.lneSonKanBagisiTarihi.setText(secili[25].text())
           self.uiAna.chkblkKanBagisi.setChecked(secili[26].text() == "İlk Defa Kan Bağışı Yapıyor")
           

    def guncelle(self):
        # Güncellenecek kaydın seçili mi
        secili = self.uiAna.tblwKayitTutucu.selectedItems()
        if secili:
            _Id = secili[0].text()
            _lneBagisciAdi = self.uiAna.lneBagisciAdi.text()
            _lneBagisciSoyadi = self.uiAna.lneBagisciSoyadi.text()
            _lneTc = self.uiAna.lneTc.text()
            _cmbCinsiyet = self.uiAna.cmbCinsiyet.currentText()
            _dteDogumTarihi = self.uiAna.dteDogumTarihi.date().toString(QtCore.Qt.ISODate)
            _lneBagisciTelefon = self.uiAna.lneBagisciTelefon.text()
            _lneBagisciEposta = self.uiAna.lneBagisciEposta.text()
            _lneBagisciEv = self.uiAna.lneBagisciEv.text()
            _lneYakinAdi = self.uiAna.lneYakinAdi.text()
            _lneYakinSoyadi = self.uiAna.lneYakinSoyadi.text()
            _lneYakinTelefon = self.uiAna.lneYakinTelefon.text()
            _spnKilo = self.uiAna.spnKilo.value()
            _lneBoy = self.uiAna.lneBoy.text()
            
            _chkbKronikHastalik = "Kronik Hasta" if self.uiAna.chkbKronikHastalik.isChecked() else "Kronik Hasta değil"
            _chkbIlac = "Düzenli İlaç Kullanıyor" if self.uiAna.chkbIlac.isChecked() else "Düzenli İlaç Kullanmıyor"
            _chkbAlerji = "Alerjik Hasta" if self.uiAna.chkbAlerji.isChecked() else "Alerjik Hasta Değil"
            _chkbSigara = "Sigara Veya Alkol kullanıyor" if self.uiAna.chkbSigara.isChecked() else "Sigara Veya Alkol Kullanmıyor"
            
            _txeGecmisMudahale = self.uiAna.txeGecmisMudahale.toPlainText()
            _txeNotBilgisi = self.uiAna.txeNotBilgisi.toPlainText()
            _cldwKanBagisTarihi = self.uiAna.cldwKanBagisTarihi.selectedDate().toString(QtCore.Qt.ISODate)
            _cmbKanGrubu = self.uiAna.cmbKanGrubu.currentText()
            _cmbRhFaktoru = self.uiAna.cmbRhFaktoru.currentText()
            _cmbBagisTuru = self.uiAna.cmbBagisTuru.currentText()
            _cmbSehir = self.uiAna.cmbSehir.currentText()
            _lneSonKanBagisiTarihi = self.uiAna.lneSonKanBagisiTarihi.text()
            _chkblkKanBagisi = "İlk Defa Kan Bağışı Yapıyor" if self.uiAna.chkblkKanBagisi.isChecked() else "Daha Önce Kan Bağışı Yapmamış"
           
            # Veritabanında güncelleme işlemini yap
            self.veritabani.execute("""
                UPDATE tblwKayitTutucu SET BagisciAdi=?,BagisciSoyadi=?,Tc=?,Cinsiyet=?,DogumTarihi=?,BagisciTelefon=?,\
                BagisciEposta=?,BagisciEv=?,YakinAdi=?,YakinSoyadi=?,YakinTelefon=?, \
                Kilo=?,Boy=?,KronikHastalik=?,Ilac=?,Alerji=?,Sigara=?,GecmisMudahale=?, \
                NotBilgisi=?,KanBagisTarihi=?,KanGrubu=?,RhFaktoru=?,BagisTuru=?,Sehir=?, \
                SonKanBagisiTarihi=?,IlkKanBagisi=? WHERE Id=?
            """, (_lneBagisciAdi,_lneBagisciSoyadi,_lneTc,_cmbCinsiyet,_dteDogumTarihi,_lneBagisciTelefon,_lneBagisciEposta,_lneBagisciEv,_lneYakinAdi, \
                       _lneYakinSoyadi,_lneYakinTelefon,_spnKilo,_lneBoy,_chkbKronikHastalik,_chkbIlac,_chkbAlerji,_chkbSigara,_txeGecmisMudahale,_txeNotBilgisi, \
                       _cldwKanBagisTarihi,_cmbKanGrubu,_cmbRhFaktoru,_cmbBagisTuru,_cmbSehir,_lneSonKanBagisiTarihi,_chkblkKanBagisi,_Id))
            self.listele() # Güncellenen kayıtları listele
            self.uiAna.statusbar.showMessage("GÜNCELLEME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...", 10000)
        else:
            self.uiAna.statusbar.showMessage("Lütfen bir kayıt seçin...", 10000)            
            


    def girisYap(self):
        # Kullanıcı adı ve şifreyi al
        username = self.uiGiris.lneGirisKullaniciAdi.text()
        password = self.uiGiris.lneGirisSifre.text()
        # Veritabanında kullanıcı adı ve şifreyi kontrol et
        result = self.veritabani.fetchone("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        # Kullanıcı adı ve şifre doğruysa ana pencereyi göster
        if result:
            self.penGiris.hide() # Giriş penceresini gizle
            self.penAna.show() # Ana pencereyi göster
        else:
            # Kullanıcı adı veya şifre yanlışsa uyarı mesajı göster
            QMessageBox.warning(self.penGiris, "Hata", "Kullanıcı adı veya şifre hatalı!")

    def kayitOl(self):
        # Kayıt penceresini göster
        self.penKayit.show()

    def kaydiTamamla(self):
        # Kullanıcı adı ve şifreyi al
        username = self.uiKayit.lneKayitKullaniciAdi.text()
        password = self.uiKayit.lneKayitSifre.text()
        try:  # Yeni kullanıcıyı veritabanına ekle
            self.veritabani.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            QMessageBox.information(self.penKayit, "Başarılı", "Kayıt başarıyla tamamlandı!")
            self.penKayit.hide() # Kayıt penceresini gizle
        except sqlite3.IntegrityError:
            QMessageBox.warning(self.penKayit, "Hata", "Bu kullanıcı adı zaten alınmış. Başka bir kullanıcı adı deneyin.")

#------------------------- UYGULAMA--------------------
#-----------------------------------------------------
if __name__ == "__main__":
    uyg = QApplication(sys.argv) # QApplication nesnesi oluştur
    uygulama = Uygulama() # Uygulama Class çalışması
    sys.exit(uyg.exec_())  # Uygulama döngüsünü başlat
