
# apl-source:1
# مثال 2013 — الجذر التربيعي الصحيح بطريقة نيوتن
# apl-source:2
# Integer sqrt Newton
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2013-integer-sqrt-newton-iteration.apl
# apl-source:6

# apl-source:7
# # نبدأ من العدد نفسه
# apl-source:8
# # ونتوقف عندما يتوقف التقدير عن النقصان
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
def جذر(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return ن
  # apl-source:21
  س = ن
  # apl-source:22
  ص = (س + ن // س) // 2
  # apl-source:23
  while ص < س:
    # apl-source:24
    س = ص
    # apl-source:25
    ص = (س + ن // س) // 2
  # apl-source:26
  return س
# apl-source:27

# apl-source:28
تأكد_يساوي(جذر(0), 0, "صفر")
# apl-source:29
تأكد_يساوي(جذر(8), 2, "٨")
# apl-source:30
تأكد_يساوي(جذر(99), 9, "٩٩")
# apl-source:31
تأكد_يساوي(جذر(16), 4, "١٦")
# apl-source:32
تأكد_يساوي(جذر(1000000000000), 1000000, "تريليون")
# apl-source:33
