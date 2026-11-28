
# apl-source:1
# مثال 2226 — هل القائمة مرتبة تصاعديا
# apl-source:2
# Is list sorted ascending
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2226-list-is-sorted-ascending-check.apl
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
  for ي in range(len(ق) - 1):
    # apl-source:20
    if ق[ي] > ق[ي + 1]:
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([3, 1, 2]), False, "حالة 1")
# apl-source:25
تأكد_يساوي(ف([5]), True, "حالة 2")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), True, "حالة 3")
# apl-source:27
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), False, "حالة 4")
# apl-source:28
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), False, "حالة 5")
# apl-source:29
تأكد_يساوي(ف([1, 1, 2]), True, "حالة 6")
# apl-source:30
