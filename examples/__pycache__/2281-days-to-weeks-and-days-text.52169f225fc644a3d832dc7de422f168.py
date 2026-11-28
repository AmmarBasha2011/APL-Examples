
# apl-source:1
# مثال 2281 — أيام إلى أسابيع وأيام
# apl-source:2
# Days to weeks and days
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2281-days-to-weeks-and-days-text.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
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
  return str(ن // 7) + " اسبوع و " + str(ن % 7) + " يوم"
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(0), "0 اسبوع و 0 يوم", "حالة 1")
# apl-source:22
تأكد_يساوي(ف(6), "0 اسبوع و 6 يوم", "حالة 2")
# apl-source:23
تأكد_يساوي(ف(7), "1 اسبوع و 0 يوم", "حالة 3")
# apl-source:24
تأكد_يساوي(ف(30), "4 اسبوع و 2 يوم", "حالة 4")
# apl-source:25
تأكد_يساوي(ف(365), "52 اسبوع و 1 يوم", "حالة 5")
# apl-source:26
