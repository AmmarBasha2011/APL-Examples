
# apl-source:1
# مثال 2255 — مجموع أرقام كل العناصر
# apl-source:2
# Digit sum across items
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2255-list-sum-of-digits-of-all-items.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ف(ق):
  # apl-source:19
  م = 0
  # apl-source:20
  for ع in ق:
    # apl-source:21
    for ر in str(ع):
      # apl-source:22
      م = م + int(ر)
  # apl-source:23
  return م
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([12, 34]), 10, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([5]), 5, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([100, 200]), 3, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([999]), 27, "حالة 4")
# apl-source:29
