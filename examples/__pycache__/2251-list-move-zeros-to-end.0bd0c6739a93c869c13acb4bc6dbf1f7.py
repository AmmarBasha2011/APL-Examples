
# apl-source:1
# مثال 2251 — نقل الأصفار للنهاية
# apl-source:2
# Move zeros to end
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2251-list-move-zeros-to-end.apl
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
  ص = 0
  # apl-source:21
  for ع in ق:
    # apl-source:22
    if ع == 0:
      # apl-source:23
      ص = ص + 1
    # apl-source:24
    else:
      # apl-source:25
      ر = ر + [ع]
  # apl-source:26
  for ي in range(ص):
    # apl-source:27
    ر = ر + [0]
  # apl-source:28
  return ر
# apl-source:29

# apl-source:30
تأكد_يساوي(ف([0, 1, 0, 3]), [1, 3, 0, 0], "حالة 1")
# apl-source:31
تأكد_يساوي(ف([1, 2]), [1, 2], "حالة 2")
# apl-source:32
تأكد_يساوي(ف([0, 0]), [0, 0], "حالة 3")
# apl-source:33
تأكد_يساوي(ف([4, 0, 5, 0, 6]), [4, 5, 6, 0, 0], "حالة 4")
# apl-source:34
