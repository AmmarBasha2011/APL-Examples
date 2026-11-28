
# apl-source:1
# مثال 2020 — المعكوس الضربي بالباقي
# apl-source:2
# Modular inverse by search
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2020-modular-inverse-brute-force-search.apl
# apl-source:6

# apl-source:7
# # المعكوس موجود فقط إذا كان القاسم المشترك 1
# apl-source:8
# # نبحث بين 1 وm-1
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
def معكوس(ا, م):
  # apl-source:19
  for س in range(1, م):
    # apl-source:20
    if ا * س % م == 1:
      # apl-source:21
      return س
  # apl-source:22
  return -1
# apl-source:23

# apl-source:24
تأكد_يساوي(معكوس(3, 11), 4, "٣ باقي ١١")
# apl-source:25
تأكد_يساوي(معكوس(10, 17), 12, "١٠ باقي ١٧")
# apl-source:26
تأكد_يساوي(معكوس(2, 4), -1, "لا يوجد")
# apl-source:27
