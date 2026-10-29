# path ~/.config/GnuChanNotification/GnuChanNotification.py
#
# WARNING: bu gercek bir Python betigi degil, bir AYAR dosyasidir.
#
# GnuChanNotification, dunst gibi calisan bir bildirim sunucusudur: oturum
# veri yolunda (session bus) "org.freedesktop.Notifications" adini tutar ve
# diger programlarin gonderdigi bildirimleri ekrana cizer. Bir program size bir
# bildirim gonderdiginde — posta, muzik calar, ya da notify-send — onu bu
# program gosterir.
#
# Ne renkte, ne boyutta, nerede ve ne kadar sure cizecegini burada ayarlarsin.
# Begendigin degeri degistir, kaydet, bir sonraki calistirmada gecerli olur.

Version = "0.1.0"

gcl_Notification.Main(
    # ---- renkler --------------------------------------------------------
    # Balonun govdesi. Masaustunun en koyu moru.
    Background="#21102f",

    # Balonun ikinci govde bandi. Biraz daha acik mor.
    BackgroundAlt="#2b1740",

    # Balonun cevresindeki cizgi.
    Frame="#65428a",

    # Baslik satirinin rengi (gonderenin ozeti).
    Title="#f5eaff",

    # Govde metninin rengi.
    Body="#d8c8ed",

    # Vurgu rengi: baglantilar ve fare uzerindeyken kenar.
    Accent="#b98aff",

    # Acil (critical) bir bildirimin cevre rengi. Kirmiziya calan mor.
    Urgent="#ff5c8a",

    # Saydam bir resmin uzerine cizilecegi renk.
    IconBackground="#170b22",

    # ---- sekil ----------------------------------------------------------
    # Balonun genisligi (piksel). Yuksekligi icindeki metne gore kendiliginden
    # ayarlanir; sen sadece genisligi verirsin.
    Width=360,

    # Balonun icindeki yazi ile kenari arasindaki bosluk.
    Padding=14,

    # Balonun ekran kenarindan uzakligi.
    Margin=14,

    # Iki balon arasindaki bosluk.
    Gap=10,

    # Kose yuvarlakligi.
    Corner=14,

    # Varsa resmin (ikonun) kenar uzunlugu.
    IconSize=48,

    # ---- yazi -----------------------------------------------------------
    # Baslik yazisinin fontu. Iki satir ayni fontu paylasir; govde bir kademe
    # kucuk cizilir.
    Font="monospace:pixelsize=13",

    # Govde yazisinin, baslik fontuna gore yuzdesi (100 = ayni boy).
    BodyScale=90,

    # ---- davranis -------------------------------------------------------
    # Balonun duracagi kose: "top-right", "top-left", "bottom-right",
    # "bottom-left", "top-center", "bottom-center".
    Position="top-right",

    # Gonderen bir sure belirtmezse balonun kac milisaniye duracagi.
    Timeout=5000,

    # Ayni anda ekranda en fazla kac balon duracagi.
    MaxVisible=5,

    # Resmi ciz (True) ya da cizme (False).
    ShowIcon=True,

    # Govde metnini ciz (True) ya da cizme (False).
    ShowBody=True,

    # Ust kenardan ne kadar asagida baslayacagi. Masaustunun kendi cubugu
    # yukarida; balonun onun altinda kalmamasi icin bu bosluk birakilir.
    TopOffset=50,

    # Her balonun ustunde, kalan sureyi gosteren ince bir zaman cubugu cizilsin
    # mi. Suresi hic bitmeyecek bir bildirimde cubuk cizilmez.
    ShowTimer=True,

    # Baslik ve govde en fazla kac satira kadar buyuyebilir. Balon yazisina gore
    # kendiliginden buyur; bu yalnizca bir tavandir.
    MaxSummaryLines=3,
    MaxBodyLines=12,
)
