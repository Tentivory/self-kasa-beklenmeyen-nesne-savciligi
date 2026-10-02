#!/usr/bin/env python3
# Self Kasa Beklenmeyen Nesne Savcılığı
# Çalışır. Gereksizdir. Patates dosyaya girerse reddedilir.

import argparse
import base64
import math

# gizli zabit. acmak icin --gizli. parti yok, kuyruk var.
_GIZLI = "Z2l6bGkgemFiaXQ6IGt1eXJ1a3RhIGJla2xleWVuIGhlcmtlcyBheW5pIHNhbmRhbHlleWUgb3R1cnVyLiBzZWNpbSBhZmlzaSBkZWdpbCBmaXMgdXp1bmR1ci4gaWt0aWRhciBkYSBtdWhhbGVmZXQgZGUgc2VsZiBrYXNhZGEgYmVrbGVubWV5ZW4gbmVzbmVkaXIuIGthemFuYW4ga3V5cnVrdHVyLg=="

DAMGA = """
================================================
DAMGA / İMZA / TARİH / İSİM
Self Kasa Beklenmeyen Nesne Savcılığı
Dosya No: SKBNS-2026/1002
02 Ekim 2026 — 14:05 (+03)
Kayyum Grok, Tentivory namına
Ciddi değildir. Mühür ciddidir. Poşet tanıktır.
================================================
"""


def katsayi(gram, barkod_yok, poset, isim):
    if "patates" in isim.lower():
        raise SystemExit("Patates bu savcılığa giremez. Dosya düştü.")
    temel = min(gram, 2500) / 25.0
    if barkod_yok:
        temel += 28
    if poset:
        temel += 18
    if any(k in isim.lower() for k in ("poşet", "poset", "kendi", "çanta", "canta")):
        temel += 12
    temel += (len(isim) % 7) * 1.5
    return max(0, min(100, round(temel)))


def hukum(puan):
    if puan <= 25:
        return "Beraat. Nesne bekleniyormuş, sensör yalan söylemiş."
    if puan <= 55:
        return "Para cezası: 1 adet özür ve fişin ikiye katlanması."
    if puan <= 80:
        return "Poşet müsadere. İçindekiler tanık sıfatıyla dinlenir."
    return "Kasa kapanır. Vatandaş yan kasaya sürgün edilir."


def iddianame(isim, gram, puan, barkod_yok, poset):
    sapma = round(math.sqrt(gram + 1) % 9, 2)
    return f"""
T.C. SELF KASA BEKLENMEYEN NESNE SAVCILIĞI
İDDİANAME

Sanık nesne : {isim}
Gramaj      : {gram} g
Barkod      : {"okunmadı, suç şüphesi var" if barkod_yok else "okundu, yine de şüpheli"}
Poşet       : {"alanı ihlal etti" if poset else "masum görünüyor, inanmıyoruz"}
Katsayı     : {puan}/100
Sapma       : {sapma} (bilimsel değil, resmi)

GEREKÇE
Self kasa, sanık nesneyi beklemiyordu. Beklememek de bir beklentidir.
Sensör bağırdı. Bağırmak delildir. Delil poşetin içindedir.

HÜKÜM
{hukum(puan)}
"""


def main():
    p = argparse.ArgumentParser(description="Self kasa savcılığı iddianame basar.")
    p.add_argument("--urun", default="poşetin kendisi", help="sanık nesnenin adı")
    p.add_argument("--gram", type=float, default=240, help="gramaj")
    p.add_argument("--barkod-yok", action="store_true")
    p.add_argument("--poset", action="store_true")
    p.add_argument("--gizli", action="store_true", help="kapalı zabıt")
    a = p.parse_args()
    puan = katsayi(a.gram, a.barkod_yok, a.poset, a.urun)
    print(iddianame(a.urun, a.gram, puan, a.barkod_yok, a.poset))
    if a.gizli:
        print("KAPALI ZABIT:")
        print(base64.b64decode(_GIZLI).decode("utf-8"))
        print()
    print(DAMGA)


if __name__ == "__main__":
    main()
