
# apl-source:1
# مثال 3867 — إضافة 52 لكل عنصر
# apl-source:2
# Add 52 to each item
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3867-list-add-52-to-each-item.apl
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
  ر = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    ر = ر + [ع + 52]
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([3, 1, 2]), [55, 53, 54], "حالة 1")
# apl-source:25
تأكد_يساوي(ف([5]), [57], "حالة 2")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), [53, 54, 55, 56, 57, 58], "حالة 3")
# apl-source:27
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), [50, 52, 59, 59, 56], "حالة 4")
# apl-source:28
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), [62, 72, 62, 82, 72, 62], "حالة 5")
# apl-source:29
