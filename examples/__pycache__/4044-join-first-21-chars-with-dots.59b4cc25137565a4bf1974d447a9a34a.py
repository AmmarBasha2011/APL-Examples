
# apl-source:1
# مثال 4044 — ربط أول 21 أحرف بنقاط
# apl-source:2
# Join first 21 chars with dots
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4044-join-first-21-chars-with-dots.apl
# apl-source:6

# apl-source:7
# # ندخل النص
# apl-source:8
# # ونقارن النتيجة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def ف(ن):
  # apl-source:19
  return ".".join(ن[:21])
# apl-source:20

# apl-source:21
تأكد_يساوي(ف("hello"), "h.e.l.l.o", "حالة 1")
# apl-source:22
تأكد_يساوي(ف("ab"), "a.b", "حالة 2")
# apl-source:23
تأكد_يساوي(ف("abcdefghijklmn"), "a.b.c.d.e.f.g.h.i.j.k.l.m.n", "حالة 3")
# apl-source:24
تأكد_يساوي(ف(""), "", "حالة 4")
# apl-source:25
