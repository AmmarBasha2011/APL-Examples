
# apl-source:1
# مثال 1716 — الجذر الرقمي بالتكرار
# apl-source:2
# Digital root recursively
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1716-recursive-digit-root.apl
# apl-source:6

# apl-source:7
# الدالة تستدعي نفسها بمجموع الأرقام
# apl-source:8
# نتوقف عند رقم واحد
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
def جذر_رقمي(ن):
  # apl-source:19
  if ن < 10:
    # apl-source:20
    return ن
  # apl-source:21
  مجموع = 0
  # apl-source:22
  while ن > 0:
    # apl-source:23
    مجموع = مجموع + ن % 10
    # apl-source:24
    ن = ن // 10
  # apl-source:25
  return جذر_رقمي(مجموع)
# apl-source:26

# apl-source:27
تأكد_يساوي(جذر_رقمي(38), 2, "ثمانية وثلاثون")
# apl-source:28
تأكد_يساوي(جذر_رقمي(9), 9, "تسعة")
# apl-source:29
تأكد_يساوي(جذر_رقمي(99999), 9, "تسعات")
# apl-source:30
