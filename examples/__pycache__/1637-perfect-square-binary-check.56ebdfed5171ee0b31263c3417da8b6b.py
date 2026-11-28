
# apl-source:1
# مثال 1637 — هل العدد مربع كامل
# apl-source:2
# Perfect square check by binary search
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1637-perfect-square-binary-check.apl
# apl-source:6

# apl-source:7
# نبحث عن عدد مربعه يساوي المدخل
# apl-source:8
# نحصر البحث بين 1 والعدد
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
  ج = ن
  # apl-source:21
  while ي <= ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if م * م == ن:
      # apl-source:24
      return True
    # apl-source:25
    elif م * م < ن:
      # apl-source:26
      ي = م + 1
    # apl-source:27
    else:
      # apl-source:28
      ج = م - 1
  # apl-source:29
  return False
# apl-source:30

# apl-source:31
تأكد_يساوي(مربع_كامل(16), True, "ستة عشر")
# apl-source:32
تأكد_يساوي(مربع_كامل(14), False, "أربعة عشر")
# apl-source:33
تأكد_يساوي(مربع_كامل(1), True, "واحد")
# apl-source:34
