
# apl-source:1
# مثال 761 — جدول الكودونات
# apl-source:2
# Codon table
# apl-source:3
# Demonstrates: 64 كودوناً، إطار ثلاثي، وقف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/761-codon-table.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# ترجمة DNA إلى بروتين بجدول الكودونات القياسي
# apl-source:25
# Demonstrates: قاموس 64 كودوناً, إطار قراءة بثلاثيات, كودونات وقف
# apl-source:26
# ATG تبدأ الميثيونين، وTAA/TAG/TGA توقف (*)
# apl-source:27

# apl-source:28
كودونات = {
  # apl-source:29
  "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
  # apl-source:30
  "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
  # apl-source:31
  "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
  # apl-source:32
  "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
  # apl-source:33
  "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
  # apl-source:34
  "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
  # apl-source:35
  "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
  # apl-source:36
  "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
  # apl-source:37
  "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
  # apl-source:38
  "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
  # apl-source:39
  "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
  # apl-source:40
  "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
  # apl-source:41
  "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
  # apl-source:42
  "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
  # apl-source:43
  "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
  # apl-source:44
  "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
# apl-source:45
}
# apl-source:46

# apl-source:47
def ترجم(تسلسل):
  # apl-source:48
  بروتين = ""
  # apl-source:49
  ي = 0
  # apl-source:50
  while ي + 3 <= len(تسلسل):
    # apl-source:51
    بروتين = بروتين + كودونات.get(تسلسل[ي:ي + 3], "؟")
    # apl-source:52
    ي = ي + 3
  # apl-source:53
  return بروتين
# apl-source:54

# apl-source:55
def حتى_الوقف(تسلسل):
  # apl-source:56
  بروتين = ""
  # apl-source:57
  ي = 0
  # apl-source:58
  while ي + 3 <= len(تسلسل):
    # apl-source:59
    حمض = كودونات.get(تسلسل[ي:ي + 3], "؟")
    # apl-source:60
    if حمض == "*":
      # apl-source:61
      return بروتين
    # apl-source:62
    بروتين = بروتين + حمض
    # apl-source:63
    ي = ي + 3
  # apl-source:64
  return بروتين
# apl-source:65

# apl-source:66
تأكد_يساوي(ترجم("ATGGCTTAA"), "MA*", "بداية ووقف")
# apl-source:67
تأكد_يساوي(ترجم("TTT"), "F", "فينيل ألانين")
# apl-source:68
تأكد_يساوي(ترجم("ATG"), "M", "ميثيونين البداية")
# apl-source:69
تأكد_يساوي(ترجم("TGGTGG"), "WW", "تربتوفان مزدوج")
# apl-source:70
تأكد_يساوي(ترجم("ATGC"), "M", "بقايا تُهمل")
# apl-source:71
تأكد_يساوي(ترجم(""), "", "تسلسل فارغ")
# apl-source:72

# apl-source:73
تأكد_يساوي(حتى_الوقف("ATGGCTTAAAGAAGA"), "MA", "التوقف عند النجمة")
# apl-source:74
تأكد_يساوي(حتى_الوقف("ATGAAACCC"), "MKP", "بلا وقف")
# apl-source:75
تأكد_يساوي(len(كودونات), 64, "جدول كامل")
# apl-source:76

# apl-source:77
print("ترجمة:", ترجم("ATGGCTTAA"))
# apl-source:78
