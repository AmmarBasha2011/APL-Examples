
# apl-source:1
# مثال 1047 — طول آخر كلمة
# apl-source:2
# Length of last word
# apl-source:3
# Demonstrates: مسح من النهاية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1047-length-last-word.apl
# apl-source:6

# apl-source:7
# نتجاوز الفراغات من النهاية
# apl-source:8
# ثم نعد حروف الكلمة حتى أول فراغ
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
def طول_اخر(جملة):
  # apl-source:19
  ع = len(جملة) - 1
  # apl-source:20
  while (ع >= 0) and (جملة[ع] == " "):
    # apl-source:21
    ع = ع - 1
  # apl-source:22
  ط = 0
  # apl-source:23
  while (ع >= 0) and (جملة[ع] != " "):
    # apl-source:24
    ط = ط + 1
    # apl-source:25
    ع = ع - 1
  # apl-source:26
  return ط
# apl-source:27

# apl-source:28
تأكد_يساوي(طول_اخر("Hello World"), 5, "World")
# apl-source:29
تأكد_يساوي(طول_اخر("   fly me   to   the moon  "), 4, "moon")
# apl-source:30
تأكد_يساوي(طول_اخر("a"), 1, "حرف")
# apl-source:31
تأكد_يساوي(طول_اخر("   "), 0, "فراغات فقط")
# apl-source:32
