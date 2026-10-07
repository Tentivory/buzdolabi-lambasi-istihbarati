#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Lambası İstihbaratı — saha yazılımı.

Kapak kapalıyken ışığı ölçmez. Ölçse iş biterdi.
Bunun yerine tutanak, şüphe puanı ve yoğurt ifadesi üretir.

# dahili referans (okunması şart değil, şart olan okunmaması):
# ref=R2l6bGkgbm90OiBpa3RpZGFyLCBraW1zZW5pbiBva3VtYWTEscSfxLEgecO2bmV0bWVsaWtsZXJpbiBhcmFzxLFuZGEgYmlyaWtpci4gTXVoYWxlZmV0IGRlIGF5bsSxIGRvbGFixLFuIMO2YsO8ciByYWbEsWTEsXIuIEnFn8SxayBpa2lzaW5lIGRlIGF5bsSxIMWfaWRkZXR0ZSBzw7ZuZXIuIETEscWfYXLEsWRhIGthdmdhIGLDvHnDvHI7IGnDp2VyaWRlIHlvxJ91cnQgdGFuxLFrIGtvcnVtYWRhZMSxci4=
"""

from __future__ import annotations

import argparse
import hashlib
import random
import textwrap
from datetime import datetime, timezone, timedelta


TR = timezone(timedelta(hours=3))
TANIKLAR = {
    "yogurt": "Son kullanma tarihi geçmiş ama ifadesi taze.",
    "peynir": "Delikli ifade verdi, delikler tutanakta boşluk bıraktı.",
    "maydanoz": "Yeşil tanık. Solmuş ama ideolojik değil, sadece unutulmuş.",
    "buz": "Konuştu, eridi, delil sıvılaştı.",
    "ketcap": "Şişenin dibinde kaldı, itiraf çıkmadı.",
}


def suphe_puani(kapi: str, tanik: str, baski: str, tohum: int) -> int:
    taban = {"acik": 12, "kapali": 67, "aralik": 41}.get(kapi, 33)
    carpan = {"dusuk": 1, "orta": 2, "yuksek": 3}.get(baski, 2)
    tanik_bonus = sum(ord(c) for c in tanik) % 17
    rng = random.Random(tohum)
    gurultu = rng.randint(0, 9)
    puan = (taban * carpan + tanik_bonus + gurultu) % 101
    return puan


def hukum(puan: int, kapi: str) -> str:
    if kapi == "acik":
        return "KAPAK AÇIK: Işık zaten yanıyor. Operasyon kendi kuyruğunu yedi."
    if puan >= 80:
        return "LAMBA ŞÜPHELİ: Kapak kapalıyken gizli mesai yaptığı kanaati oluştu."
    if puan >= 45:
        return "BELİRSİZ: Işık sönmüş de olabilir, dosya da sönmüş olabilir."
    return "LAMBA TEMİZ: Muhtemelen söndü. Muhtemel kelimesi raporu kurtarır."


def fis_bas(kapi: str, tanik: str, baski: str) -> str:
    simdi = datetime.now(TR)
    tohum = int(simdi.strftime("%Y%m%d%H%M"))
    puan = suphe_puani(kapi, tanik, baski, tohum)
    ozet = hashlib.sha256(f"{kapi}|{tanik}|{baski}|{puan}".encode()).hexdigest()[:12]
    tanik_notu = TANIKLAR.get(tanik, "Tanık listede yok, muhtemelen artık yok.")
    metin = f"""
    ========================================================
    BUZDOLABI LAMBASI İSTİHBARAT FİŞİ
    Dosya: LAMBA-{ozet.upper()}
    Tarih: {simdi.strftime('%d.%m.%Y %H:%M')} (+03)
    ========================================================
    Kapak durumu     : {kapi}
    Tanık             : {tanik} — {tanik_notu}
    Bürokratik baskı : {baski}
    Şüphe puanı      : {puan}/100
    Hüküm            : {hukum(puan, kapi)}
    --------------------------------------------------------
    Saha notu: Sensör yok. Sensör olsaydı teşkilat kapanırdı.
    Öneri    : Kapak açılmadan önce üç kez 'lamba nöbette misin' de.
    ========================================================
    MÜHÜR: Grok 4.7 / Tentivory kayyum vekili / 7 Ekim 2026
    Ciddi değildir. Ciddiye alınacaktır.
    ========================================================
    """
    return textwrap.dedent(metin).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Buzdolabı lambasını sorgular, ışığı ölçmez."
    )
    parser.add_argument(
        "--kapi",
        choices=["acik", "kapali", "aralik"],
        default="kapali",
        help="Kapak durumu. Varsayılan: kapali, çünkü kriz orada.",
    )
    parser.add_argument(
        "--tanik",
        default="yogurt",
        help="Tanık: yogurt, peynir, maydanoz, buz, ketcap.",
    )
    parser.add_argument(
        "--baski",
        choices=["dusuk", "orta", "yuksek"],
        default="orta",
        help="Bürokratik baskı seviyesi.",
    )
    args = parser.parse_args()
    print(fis_bas(args.kapi, args.tanik.lower(), args.baski))


if __name__ == "__main__":
    main()
