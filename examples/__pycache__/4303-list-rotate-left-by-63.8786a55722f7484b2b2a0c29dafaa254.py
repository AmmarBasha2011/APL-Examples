
# apl-source:1
# مثال 4303 — تدوير لليسار بمقدار 63
# apl-source:2
# Rotate left by 63
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4303-list-rotate-left-by-63.apl
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
  if len(ق) == 0:
    # apl-source:20
    return ق
  # apl-source:21
  ك = 63 % len(ق)
  # apl-source:22
  return ق[ك:] + ق[:ك]
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([3, 1, 2]), [3, 1, 2], "حالة 1")
# apl-source:25
تأكد_يساوي(ف([5]), [5], "حالة 2")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), [4, 5, 6, 1, 2, 3], "حالة 3")
# apl-source:27
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), [7, 4, -2, 0, 7], "حالة 4")
# apl-source:28
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), [30, 20, 10, 10, 20, 10], "حالة 5")
# apl-source:29
