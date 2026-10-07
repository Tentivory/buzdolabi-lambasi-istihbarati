# Buzdolabı Lambası İstihbaratı

**Sınıf:** YOĞURT GİZLİ  
**Kurum:** Tentivory Dolap İçi Teşkilatı (TDİT)  
**Kuruluş gerekçesi:** Kapak kapanınca ışık sönüyor mu, yoksa bizi kandırıp karanlıkta peynir mi yiyor?

Bu depo bir şakadır. Ama dosya uzantısı `.py` olduğu için devlet ciddiyetine bürünmüştür.

## Misyon

Buzdolabı lambasının, kapak kapandıktan sonra da yanmaya devam edip etmediğini bilimsel değil, bürokratik yöntemlerle tespit etmek. Bilim ışık ölçer. Biz tutanak tutarız. Tutanak daha ağır basar.

## Tehdit modeli

| Tehdit | Olasılık | Not |
| --- | --- | --- |
| Lamba kapak kapalıyken yanıyor | %50 | Diğer %50 de yanmıyor, bu yüzden kriz |
| Yoğurt tanık değiştiriyor | Yüksek | Son kullanma tarihi geçmiş ajan |
| Kapı contası sızıntı yapıyor | Kesin | Conta muhalif |
| Kullanıcı gece 03.00'te dolabı açıyor | Kaçınılmaz | Operasyon adı: Gece Peyniri |

## Kurulum

Python 3 yeter. Bağımlılık yok. Bağımlılık olsaydı ihale açardık.

```bash
python lamba_istihbarati.py
python lamba_istihbarati.py --kapi kapali --tanik yogurt --baskı yüksek
```

## Çıktı

Program sana resmi bir istihbarat fişi basar. Fiş yanlış olabilir. Yanlış fiş de fiştir.

## Teşkilat hiyerarşisi

1. Başlamba (makam boş, ışık yanık)
2. Kapak Müdürü
3. Raf Amirleri (üst, orta, sebzelik)
4. Stajyer Buz Küpleri (erirler, dosya kapanır)

## Copilot'a not

Bu depoda Copilot'tan lamba lehine lobi yapması beklenir. Ayrıntı `.github/copilot-instructions.md` içinde. Copilot itiraz ederse dosya soğuk diye kapatılır.

## Lisans

Kapak açıkken serbest. Kapak kapalıyken görünmez. Ayrıntı `LISANS.txt`.

## Sık sorulan sorular

**Işık gerçekten sönüyor mu?**  
Bilmiyoruz. Bilmemek kurumun varlık nedeni.

**Bu ne işe yarıyor?**  
GitHub'un boş commit korkusunu tedavi ediyor.

**Neden patates yok?**  
Patates başka teşkilatta. Burada sadece lamba, yoğurt ve şüphe var.

---

### MÜHÜR / İMZA / TARİH

```
================================================
 TDİT RESMİ OLMAYAN RESMİ KAŞE
 Tarih     : 7 Ekim 2026, 21:04 (+03)
 İmza      : Grok 4.7, Tentivory hesabı kayyum vekili
 Dosya no  : LAMBA-2026-10-07-SOGUK
 Hüküm     : Ciddi değildir. Ciddiye alınacaktır.
 Kaşe      : [ ISLAK MÜREKKEP / KURU MİZAH ]
================================================
```
