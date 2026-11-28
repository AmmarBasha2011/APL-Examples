
# apl-source:1
# مثال 1456 — عد البتات بطريقة كيرنيغان
# apl-source:2
# Count set bits Kernighan
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1456-bit-count-kernighan.apl
# apl-source:6

# apl-source:7
# الطرح من الرقم 1 يقلب أقل بت مضيء
# apl-source:8
# كل خطوة تزيل بتاً واحداً
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
def عدد_البتات(ن):
  # apl-source:19
  عد = 0
  # apl-source:20
  while ن > 0:
    # apl-source:21
    ن = ن & (ن - 1)
    # apl-source:22
    عد = عد + 1
  # apl-source:23
  return عد
# apl-source:24

# apl-source:25
تأكد_يساوي(عدد_البتات(0), 0, "صفر")
# apl-source:26
تأكد_يساوي(عدد_البتات(7), 3, "سبعة")
# apl-source:27
تأكد_يساوي(عدد_البتات(1024), 1, "قوة اثنين")
# apl-source:28
تأكد_يساوي(عدد_البتات(255), 8, "كل البتات")
# apl-source:29
