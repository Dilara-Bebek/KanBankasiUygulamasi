# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 641)
        MainWindow.setStyleSheet("background-color: #bf4342;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-1130, -10, 1631, 741))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Resimler/Ekran Görüntüleri/kan18.png"))
        self.label.setObjectName("label")
        self.grpKayit = QtWidgets.QGroupBox(self.centralwidget)
        self.grpKayit.setGeometry(QtCore.QRect(50, 70, 371, 391))
        self.grpKayit.setStyleSheet("QGroupBox {\n"
"    border: 2px solid black;  /* Siyah renkte 2 piksel kalınlığında kenar */\n"
"    border-radius: 10px;  /* Kenarları oval yapmak için */\n"
"    margin-top: 20px;  /* Başlıkla kutu arasında boşluk */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;  /* Başlığın kenarlarla olan hizasını ayarlamak için */\n"
"    subcontrol-position: top center;  /* Başlığı yukarıda ve ortada konumlandırmak için */\n"
"    padding: 0 5px;  /* Başlığın etrafında boşluk\n"
"")
        self.grpKayit.setTitle("")
        self.grpKayit.setObjectName("grpKayit")
        self.psbKayitKayit = QtWidgets.QPushButton(self.grpKayit)
        self.psbKayitKayit.setGeometry(QtCore.QRect(100, 257, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.psbKayitKayit.setFont(font)
        self.psbKayitKayit.setStyleSheet("background-color: #220901; color:white \n"
"")
        self.psbKayitKayit.setObjectName("psbKayitKayit")
        self.lneKayitSifre = QtWidgets.QLineEdit(self.grpKayit)
        self.lneKayitSifre.setGeometry(QtCore.QRect(50, 160, 261, 41))
        self.lneKayitSifre.setStyleSheet("background-color: #ffccd5;\n"
"")
        self.lneKayitSifre.setObjectName("lneKayitSifre")
        self.lblKayitKullanciAdi = QtWidgets.QLabel(self.grpKayit)
        self.lblKayitKullanciAdi.setGeometry(QtCore.QRect(50, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblKayitKullanciAdi.setFont(font)
        self.lblKayitKullanciAdi.setObjectName("lblKayitKullanciAdi")
        self.lblKayitSifre = QtWidgets.QLabel(self.grpKayit)
        self.lblKayitSifre.setGeometry(QtCore.QRect(50, 140, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblKayitSifre.setFont(font)
        self.lblKayitSifre.setObjectName("lblKayitSifre")
        self.lneKayitKullaniciAdi = QtWidgets.QLineEdit(self.grpKayit)
        self.lneKayitKullaniciAdi.setGeometry(QtCore.QRect(50, 60, 261, 41))
        self.lneKayitKullaniciAdi.setStyleSheet("background-color: #ffccd5;\n"
"")
        self.lneKayitKullaniciAdi.setInputMask("")
        self.lneKayitKullaniciAdi.setObjectName("lneKayitKullaniciAdi")
        self.label_2 = QtWidgets.QLabel(self.grpKayit)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        self.menuHAKKINDA = QtWidgets.QMenu(self.menubar)
        self.menuHAKKINDA.setStyleSheet("QMenu {\n"
"    background-color: #2e2e2e; /* Menü arka plan rengi */\n"
"    color: #ffffff; /* Metin rengi */\n"
"    border: 1px solid #4d4d4d; /* Kenar rengi */\n"
"    border-radius: 8px; /* Köşeleri yuvarlama */\n"
"    padding: 8px; /* İçerik ile kenar arasındaki boşluk */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent; /* Öğelerin arka planı */\n"
"    padding: 5px 30px; /* Öğelerin iç boşluğu */\n"
"    margin: 2px 0px; /* Öğeler arasındaki boşluk */\n"
"    border-radius: 4px; /* Öğelerin köşe yuvarlama */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #4d4d4d; /* Üzerine gelindiğinde arka plan rengi */\n"
"    color: #ffffff; /* Üzerine gelindiğinde metin rengi */\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px; /* Ayırıcı çizgi yüksekliği */\n"
"    background-color: #707070; /* Ayırıcı çizgi rengi */\n"
"    margin: 4px 8px; /* Ayırıcı çizgi ve kenar arasındaki boşluk */\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 12px; /* Genişlik */\n"
"    height: 12px; /* Yükseklik */\n"
"}\n"
"\n"
"QMenu::\n"
"")
        self.menuHAKKINDA.setObjectName("menuHAKKINDA")
        self.menuM_SYONUMUZ_Hayat_kurtarmak_i_in_kan_ba_n_te_vik_ederek_toplum_sa_l_n_iyile_tirmek_ve_ihtiyac_olan_hastalara_g_venli_kan_temin_etmek = QtWidgets.QMenu(self.menuHAKKINDA)
        self.menuM_SYONUMUZ_Hayat_kurtarmak_i_in_kan_ba_n_te_vik_ederek_toplum_sa_l_n_iyile_tirmek_ve_ihtiyac_olan_hastalara_g_venli_kan_temin_etmek.setObjectName("menuM_SYONUMUZ_Hayat_kurtarmak_i_in_kan_ba_n_te_vik_ederek_toplum_sa_l_n_iyile_tirmek_ve_ihtiyac_olan_hastalara_g_venli_kan_temin_etmek")
        self.menuYARDIM = QtWidgets.QMenu(self.menubar)
        self.menuYARDIM.setStyleSheet("QMenu {\n"
"    background-color: #2e2e2e; /* Menü arka plan rengi */\n"
"    color: #ffffff; /* Metin rengi */\n"
"    border: 1px solid #4d4d4d; /* Kenar rengi */\n"
"    border-radius: 8px; /* Köşeleri yuvarlama */\n"
"    padding: 8px; /* İçerik ile kenar arasındaki boşluk */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent; /* Öğelerin arka planı */\n"
"    padding: 5px 30px; /* Öğelerin iç boşluğu */\n"
"    margin: 2px 0px; /* Öğeler arasındaki boşluk */\n"
"    border-radius: 4px; /* Öğelerin köşe yuvarlama */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #4d4d4d; /* Üzerine gelindiğinde arka plan rengi */\n"
"    color: #ffffff; /* Üzerine gelindiğinde metin rengi */\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px; /* Ayırıcı çizgi yüksekliği */\n"
"    background-color: #707070; /* Ayırıcı çizgi rengi */\n"
"    margin: 4px 8px; /* Ayırıcı çizgi ve kenar arasındaki boşluk */\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 12px; /* Genişlik */\n"
"    height: 12px; /* Yükseklik */\n"
"}\n"
"\n"
"QMenu::\n"
"")
        self.menuYARDIM.setObjectName("menuYARDIM")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBu_stil_sayfas_QMenu_n_n_genel_g_r_n_m_n_d_zenlerken_ayn_zamanda_alt_alta_metinleri_destekleyecek_ekilde_d_zenlenmi_tir_E_er_metinler_hala_yanyana_g_r_n_yorsa_HTML_etiketlerini_eklerken_d_zg_n_bi_imlendirilmi_oldu_undan_emin_olun = QtWidgets.QAction(MainWindow)
        self.actionBu_stil_sayfas_QMenu_n_n_genel_g_r_n_m_n_d_zenlerken_ayn_zamanda_alt_alta_metinleri_destekleyecek_ekilde_d_zenlenmi_tir_E_er_metinler_hala_yanyana_g_r_n_yorsa_HTML_etiketlerini_eklerken_d_zg_n_bi_imlendirilmi_oldu_undan_emin_olun.setObjectName("actionBu_stil_sayfas_QMenu_n_n_genel_g_r_n_m_n_d_zenlerken_ayn_zamanda_alt_alta_metinleri_destekleyecek_ekilde_d_zenlenmi_tir_E_er_metinler_hala_yanyana_g_r_n_yorsa_HTML_etiketlerini_eklerken_d_zg_n_bi_imlendirilmi_oldu_undan_emin_olun")
        self.actionHer_Hakk_Sakl_d_r_2024 = QtWidgets.QAction(MainWindow)
        self.actionHer_Hakk_Sakl_d_r_2024.setObjectName("actionHer_Hakk_Sakl_d_r_2024")
        self.actionV_ZYONUMUZ_Kan_ba_n_n_yayg_nla_t_herkesin_ba_oldu_u_ve_hi_bir_hastan_n_kan_ihtiyac_ya_amayaca_bir_d_nya_yaratmak = QtWidgets.QAction(MainWindow)
        self.actionV_ZYONUMUZ_Kan_ba_n_n_yayg_nla_t_herkesin_ba_oldu_u_ve_hi_bir_hastan_n_kan_ihtiyac_ya_amayaca_bir_d_nya_yaratmak.setObjectName("actionV_ZYONUMUZ_Kan_ba_n_n_yayg_nla_t_herkesin_ba_oldu_u_ve_hi_bir_hastan_n_kan_ihtiyac_ya_amayaca_bir_d_nya_yaratmak")
        self.actionHer_Hakk_Sakl_d_r_2025 = QtWidgets.QAction(MainWindow)
        self.actionHer_Hakk_Sakl_d_r_2025.setObjectName("actionHer_Hakk_Sakl_d_r_2025")
        self.action_leti_im = QtWidgets.QAction(MainWindow)
        self.action_leti_im.setObjectName("action_leti_im")
        self.actionE_POSTA_dilarabebek4_gmail_com = QtWidgets.QAction(MainWindow)
        self.actionE_POSTA_dilarabebek4_gmail_com.setObjectName("actionE_POSTA_dilarabebek4_gmail_com")
        self.menuHAKKINDA.addAction(self.menuM_SYONUMUZ_Hayat_kurtarmak_i_in_kan_ba_n_te_vik_ederek_toplum_sa_l_n_iyile_tirmek_ve_ihtiyac_olan_hastalara_g_venli_kan_temin_etmek.menuAction())
        self.menuHAKKINDA.addSeparator()
        self.menuHAKKINDA.addAction(self.actionV_ZYONUMUZ_Kan_ba_n_n_yayg_nla_t_herkesin_ba_oldu_u_ve_hi_bir_hastan_n_kan_ihtiyac_ya_amayaca_bir_d_nya_yaratmak)
        self.menuHAKKINDA.addSeparator()
        self.menuHAKKINDA.addAction(self.actionHer_Hakk_Sakl_d_r_2025)
        self.menuYARDIM.addAction(self.action_leti_im)
        self.menuYARDIM.addSeparator()
        self.menuYARDIM.addAction(self.actionE_POSTA_dilarabebek4_gmail_com)
        self.menubar.addAction(self.menuHAKKINDA.menuAction())
        self.menubar.addAction(self.menuYARDIM.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.psbKayitKayit.setText(_translate("MainWindow", "KAYIT OL"))
        self.lblKayitKullanciAdi.setText(_translate("MainWindow", "Kullanıcı Adı"))
        self.lblKayitSifre.setText(_translate("MainWindow", "Şifre"))
        self.label_2.setText(_translate("MainWindow", "KULLANICI KAYIT"))
        self.menuHAKKINDA.setTitle(_translate("MainWindow", "HAKKINDA"))
        self.menuM_SYONUMUZ_Hayat_kurtarmak_i_in_kan_ba_n_te_vik_ederek_toplum_sa_l_n_iyile_tirmek_ve_ihtiyac_olan_hastalara_g_venli_kan_temin_etmek.setTitle(_translate("MainWindow", "MİSYONUMUZ;\n"
"Hayat kurtarmak için kan bağışını teşvik ederek, toplum sağlığını iyileştirmek ve ihtiyacı olan hastalara güvenli kan temin etmek."))
        self.menuYARDIM.setTitle(_translate("MainWindow", "YARDIM"))
        self.actionBu_stil_sayfas_QMenu_n_n_genel_g_r_n_m_n_d_zenlerken_ayn_zamanda_alt_alta_metinleri_destekleyecek_ekilde_d_zenlenmi_tir_E_er_metinler_hala_yanyana_g_r_n_yorsa_HTML_etiketlerini_eklerken_d_zg_n_bi_imlendirilmi_oldu_undan_emin_olun.setText(_translate("MainWindow", "Bu stil sayfası, QMenu\'nün genel görünümünü düzenlerken aynı zamanda alt alta metinleri destekleyecek şekilde düzenlenmiştir. Eğer metinler hala yanyana görünüyorsa, HTML etiketlerini eklerken düzgün \\n biçimlendirilmiş olduğundan emin olun."))
        self.actionBu_stil_sayfas_QMenu_n_n_genel_g_r_n_m_n_d_zenlerken_ayn_zamanda_alt_alta_metinleri_destekleyecek_ekilde_d_zenlenmi_tir_E_er_metinler_hala_yanyana_g_r_n_yorsa_HTML_etiketlerini_eklerken_d_zg_n_bi_imlendirilmi_oldu_undan_emin_olun.setIconText(_translate("MainWindow", "Bu stil sayfası, QMenu\'nün genel\n"
" görünümünü düzenlerken aynı zamanda\n"
"\n"
" alt alta metinleri destekleyecek şekilde düzenlenmiştir. Eğer metinler hala\n"
"\n"
" yanyana görünüyorsa, HTML etiketlerini eklerken düzgün biçimlendirilmiş\n"
"\n"
" olduğundan emin olun."))
        self.actionBu_stil_sayfas_QMenu_n_n_genel_g_r_n_m_n_d_zenlerken_ayn_zamanda_alt_alta_metinleri_destekleyecek_ekilde_d_zenlenmi_tir_E_er_metinler_hala_yanyana_g_r_n_yorsa_HTML_etiketlerini_eklerken_d_zg_n_bi_imlendirilmi_oldu_undan_emin_olun.setToolTip(_translate("MainWindow", "<html><head/><body><p>Bu stil sayfası, QMenu\'nün genel görünümünü düzenlerken aynı zamanda alt alta metinleri destekleyecek</p><p><br/></p><p> şekilde düzenlenmiştir.</p><p> Eğer metinler hala yanyana görünüyorsa, </p><p>HTML etiketlerini eklerken düzgün \\n biçimlendirilmiş olduğundan emin olun.</p></body></html>"))
        self.actionHer_Hakk_Sakl_d_r_2024.setText(_translate("MainWindow", "Her Hakkı Saklıdır © 2024"))
        self.actionV_ZYONUMUZ_Kan_ba_n_n_yayg_nla_t_herkesin_ba_oldu_u_ve_hi_bir_hastan_n_kan_ihtiyac_ya_amayaca_bir_d_nya_yaratmak.setText(_translate("MainWindow", "VİZYONUMUZ;\n"
"Kan bağışının yaygınlaştığı, herkesin bağışçı olduğu ve hiçbir hastanın kan ihtiyacı yaşamayacağı bir dünya yaratmak."))
        self.actionHer_Hakk_Sakl_d_r_2025.setText(_translate("MainWindow", "Her Hakkı Saklıdır © 2024 "))
        self.action_leti_im.setText(_translate("MainWindow", "İletişim;"))
        self.actionE_POSTA_dilarabebek4_gmail_com.setText(_translate("MainWindow", "E-POSTA: dilarabebek4@gmail.com"))
