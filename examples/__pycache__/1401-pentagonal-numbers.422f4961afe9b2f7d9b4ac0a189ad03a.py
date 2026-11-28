
# apl-source:1
# مثال 1401 — الأعداد الخماسية
# apl-source:2
# Pentagonal numbers
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1401-pentagonal-numbers.apl
# apl-source:6

# apl-source:7
# الحد ن يساوي ن(3ن-1)/2
# apl-source:8
# نختبر الانتماء بالمرور على الحدود
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
def خماسية(ن):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    ناتج = ناتج + [ك * (3 * ك - 1) // 2]
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
def خماسي(عدد):
  # apl-source:25
  ك = 1
  # apl-source:26
  while ك * (3 * ك - 1) // 2 < عدد:
    # apl-source:27
    ك = ك + 1
  # apl-source:28
  return ك * (3 * ك - 1) // 2 == عدد
# apl-source:29

# apl-source:30
تأكد_يساوي(خماسية(5), [1,5,12,22,35], "خمسة حدود")
# apl-source:31
تأكد_يساوي(خماسي(22), True, "اثنان وعشرون")
# apl-source:32
تأكد_يساوي(خماسي(23), False, "ثلاثة وعشرون")
# apl-source:33
