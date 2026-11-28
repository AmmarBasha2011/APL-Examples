
# apl-source:1
# مثال 2079 — معين نصي من النجوم
# apl-source:2
# Diamond text pattern
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2079-diamond-text-pattern-odd-width.apl
# apl-source:6

# apl-source:7
# # نبني النصف العلوي
# apl-source:8
# # ثم ننسخه معكوسا بدون الصف الأوسط
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
def معين(ن):
  # apl-source:19
  اعلى = []
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    اعلى = اعلى + [" " * (ن - ك) + "*" * (2 * ك - 1)]
  # apl-source:22
  اسفل = اعلى[:-1]
  # apl-source:23
  اسفل.reverse()
  # apl-source:24
  return اعلى + اسفل
# apl-source:25

# apl-source:26
تأكد_يساوي(معين(3), ["  *", " ***", "*****", " ***", "  *"], "٣")
# apl-source:27
تأكد_يساوي(معين(1), ["*"], "١")
# apl-source:28
