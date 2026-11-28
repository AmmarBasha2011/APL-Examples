
# apl-source:1
# مثال 1086 — مربع كامل
# apl-source:2
# Valid perfect square
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1086-valid-perfect-square.apl
# apl-source:6

# apl-source:7
# نبحث عن جذر صحيح بين 1 والعدد
# apl-source:8
# لو وجدنا ج×ج يساوي العدد فهو مربع
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
def مربع_كامل(ن):
  # apl-source:19
  ي = 1
  # apl-source:20
  ل = ن
  # apl-source:21
  while ي <= ل:
    # apl-source:22
    وسط = (ي + ل) // 2
    # apl-source:23
    if (وسط * وسط) == ن:
      # apl-source:24
      return True
    # apl-source:25
    if (وسط * وسط) < ن:
      # apl-source:26
      ي = وسط + 1
    # apl-source:27
    else:
      # apl-source:28
      ل = وسط - 1
  # apl-source:29
  return False
# apl-source:30

# apl-source:31
تأكد_يساوي(مربع_كامل(16), True, "16")
# apl-source:32
تأكد_يساوي(مربع_كامل(14), False, "14")
# apl-source:33
تأكد_يساوي(مربع_كامل(1), True, "1")
# apl-source:34
تأكد_يساوي(مربع_كامل(808201), True, "899 تربيع")
# apl-source:35
تأكد_يساوي(مربع_كامل(2147483647), False, "أكبر عدد 32 بت")
# apl-source:36
