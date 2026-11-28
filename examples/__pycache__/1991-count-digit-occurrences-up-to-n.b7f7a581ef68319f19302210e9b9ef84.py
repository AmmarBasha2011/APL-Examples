
# apl-source:1
# مثال 1991 — عدد مرات ظهور رقم حتى ن
# apl-source:2
# Count digit occurrences up to n
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1991-count-digit-occurrences-up-to-n.apl
# apl-source:6

# apl-source:7
# # نحول كل عدد إلى نص
# apl-source:8
# # ونستخدم count لعد الرقم
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
def عد_رقم(ن, ر):
  # apl-source:19
  مج = 0
  # apl-source:20
  for ع in range(1, ن + 1):
    # apl-source:21
    مج = مج + str(ع).count(str(ر))
  # apl-source:22
  return مج
# apl-source:23

# apl-source:24
تأكد_يساوي(عد_رقم(13, 1), 6, "الرقم ١")
# apl-source:25
تأكد_يساوي(عد_رقم(100, 0), 11, "الرقم ٠")
# apl-source:26
تأكد_يساوي(عد_رقم(100, 7), 20, "الرقم ٧")
# apl-source:27
تأكد_يساوي(عد_رقم(25, 2), 9, "الرقم ٢")
# apl-source:28
