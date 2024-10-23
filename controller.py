# Gerekli kütüphanelerin içe aktarılması
import smtplib  # SMTP protokolü üzerinden e-posta göndermek için kullanılır
import socket   # Sunucuya bağlantı kurmak için soket işlemlerini kullanır
import time     # Döngüde bekleme süreleri için kullanılır
from email.mime.text import MIMEText  # E-posta metni oluşturmak için
from email.mime.multipart import MIMEMultipart  # E-posta'nın birden fazla parçadan oluşmasını sağlar (örn. metin + ekler)

# Birincil mail sunucusu bilgileri (Noktanyus.com)
PRIMARY_MAIL_SERVER = 'smtp.noktanyus.com'  # Birincil SMTP sunucusu
PRIMARY_MAIL_PORT = 587  # SMTP bağlantı portu
PRIMARY_USERNAME = 'kullanici@noktanyus.com'  # SMTP sunucusuna giriş için kullanıcı adı
PRIMARY_PASSWORD = 'sifre'  # SMTP sunucusuna giriş için şifre

# Alternatif mail sunucusu bilgileri (Gmail veya başka bir sunucu)
ALTERNATIVE_MAIL_SERVER = 'smtp.gmail.com'  # Alternatif SMTP sunucusu (örneğin Gmail)
ALTERNATIVE_MAIL_PORT = 587  # Alternatif SMTP bağlantı portu
ALTERNATIVE_USERNAME = 'alternatif@gmail.com'  # Alternatif sunucu için kullanıcı adı
ALTERNATIVE_PASSWORD = 'alternatif_sifre'  # Alternatif sunucu için şifre

# Uyarı maili gönderilecek adres
ALERT_EMAIL = 'alert@ornek.com'  # Uyarı gönderilecek e-posta adresi

# Uyarı mesajı oluşturma fonksiyonu
def create_email():
    """
    Uyarı e-postası oluşturur. Bağlantı sorunları hakkında bilgi verir.
    """
    msg = MIMEMultipart()  # Çok parçalı bir e-posta oluşturur (header + body)
    msg['From'] = PRIMARY_USERNAME  # Gönderen adresi (birincil kullanıcı adı)
    msg['To'] = ALERT_EMAIL  # Alıcı adresi
    msg['Subject'] = 'Sunucu Bağlantı Sorunu Bildirimi'  # E-postanın konusu

    # E-posta gövdesi (mesaj içeriği)
    body = """
    Sayın Yetkili,

    Sunucunuzdan yapılan bağlantı denemesi başarısız olmuştur. Bu durum, sunucuda elektrik veya internet kesintisi gibi bir sorun olduğunu göstermektedir.

    Lütfen gerekli kontrolleri yapınız.

    Saygılarımızla,
    Sunucu İzleme Sistemi
    """
    
    # Gövdeyi e-postaya ekler
    msg.attach(MIMEText(body, 'plain'))  
    return msg  # Hazır e-posta döndürülür

# E-posta gönderme fonksiyonu
def send_email(smtp_server, smtp_port, username, password):
    """
    Verilen SMTP sunucusu üzerinden uyarı e-postası gönderir.
    smtp_server: Kullanılacak SMTP sunucusu
    smtp_port: SMTP sunucusunun portu
    username: SMTP sunucusuna giriş için kullanıcı adı
    password: SMTP sunucusuna giriş için şifre
    """
    try:
        # E-posta mesajını oluştur
        msg = create_email()

        # SMTP sunucusuna bağlan
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Bağlantıyı güvenli hale getirmek için TLS kullanılır
        server.login(username, password)  # SMTP sunucusuna giriş yapılır
        text = msg.as_string()  # E-posta mesajı string formatına çevrilir
        server.sendmail(username, ALERT_EMAIL, text)  # E-posta gönderilir
        server.quit()  # Bağlantı kapatılır
        print(f"Uyarı e-postası başarıyla {smtp_server} üzerinden gönderildi.")
    except Exception as e:
        # Herhangi bir hata olursa, hata mesajı yazdırılır
        print(f"E-posta gönderilirken hata oluştu ({smtp_server}): {e}")

# Mail sunucusuna bağlanmayı dene
def check_mail_server(mail_server, mail_port):
    """
    Belirtilen mail sunucusuna soket bağlantısı kurarak bağlanmayı dener.
    mail_server: Bağlanılacak mail sunucusu
    mail_port: Sunucunun portu
    """
    try:
        # Mail sunucusuna soket bağlantısı kur
        with socket.create_connection((mail_server, mail_port), timeout=10) as sock:
            print(f"{mail_server} sunucusuna başarıyla bağlanıldı.")
            return True  # Bağlantı başarılı
    except Exception as e:
        # Bağlantı başarısız olursa hata mesajı yazdırılır
        print(f"{mail_server} sunucusuna bağlanılamadı: {e}")
        return False  # Bağlantı başarısız

# Ana döngü
def main():
    """
    Sürekli olarak birincil sunucuya bağlanmayı dener. Eğer başarısız olursa,
    alternatif bir sunucu üzerinden uyarı maili gönderir.
    """
    while True:
        # Birincil sunucuya bağlanmayı dene
        if not check_mail_server(PRIMARY_MAIL_SERVER, PRIMARY_MAIL_PORT):
            # Eğer birincil sunucuya bağlanılamazsa alternatif sunucudan mail gönder
            send_email(ALTERNATIVE_MAIL_SERVER, ALTERNATIVE_MAIL_PORT, ALTERNATIVE_USERNAME, ALTERNATIVE_PASSWORD)
        # 60 saniye bekle ve yeniden dene
        time.sleep(60)

# Eğer bu dosya doğrudan çalıştırıldıysa, ana fonksiyon çalıştırılır
if __name__ == "__main__":
    main()
