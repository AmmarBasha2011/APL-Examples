
# apl-source:1
# مثال 2027 — هل النص الأول تتابع من الثاني
# apl-source:2
# Is subsequence two pointers
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2027-is-subsequence-two-pointer-scan.apl
# apl-source:6

# apl-source:7
# # مؤشر على النص الأول يتقدم عند التطابق
# apl-source:8
# # ننجح إذا استنفدنا النص الأول
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
def تتابع(ا, ب):
  # apl-source:19
  ي = 0
  # apl-source:20
  for ح in ب:
    # apl-source:21
    if ي < len(ا) and ح == ا[ي]:
      # apl-source:22
      ي = ي + 1
  # apl-source:23
  return ي == len(ا)
# apl-source:24

# apl-source:25
تأكد_يساوي(تتابع("abc", "ahbgdc"), True, "موجود")
# apl-source:26
تأكد_يساوي(تتابع("axc", "ahbgdc"), False, "غير موجود")
# apl-source:27
تأكد_يساوي(تتابع("", "abc"), True, "فارغ")
# apl-source:28
