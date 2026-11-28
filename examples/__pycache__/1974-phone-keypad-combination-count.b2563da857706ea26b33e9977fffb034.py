
# apl-source:1
# مثال 1974 — عدد تركيبات أحرف لوحة الهاتف
# apl-source:2
# Phone keypad combination count
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1974-phone-keypad-combination-count.apl
# apl-source:6

# apl-source:7
# # الأزرار 7 و9 عليها أربعة أحرف
# apl-source:8
# # وباقي الأزرار من 2 إلى 8 عليها ثلاثة
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
def عدد_تركيبات(ارقام):
  # apl-source:19
  if len(ارقام) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  حروف = {"2": 3, "3": 3, "4": 3, "5": 3, "6": 3, "7": 4, "8": 3, "9": 4}
  # apl-source:22
  ن = 1
  # apl-source:23
  for ر in ارقام:
    # apl-source:24
    ن = ن * حروف[ر]
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(عدد_تركيبات("23"), 9, "٢٣")
# apl-source:28
تأكد_يساوي(عدد_تركيبات("79"), 16, "٧٩")
# apl-source:29
تأكد_يساوي(عدد_تركيبات(""), 0, "فارغ")
# apl-source:30
تأكد_يساوي(عدد_تركيبات("2379"), 144, "أربعة أزرار")
# apl-source:31
