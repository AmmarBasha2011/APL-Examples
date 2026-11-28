
# apl-source:1
# مثال 2267 — عدد توأم الأولية
# apl-source:2
# Twin prime pairs count
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2267-twin-prime-pairs-count-below.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def اولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  د = 2
  # apl-source:22
  while د * د <= ن:
    # apl-source:23
    if ن % د == 0:
      # apl-source:24
      return False
    # apl-source:25
    د = د + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def ف(ن):
  # apl-source:29
  ع = 0
  # apl-source:30
  for ي in range(2, ن - 1):
    # apl-source:31
    if اولي(ي) and اولي(ي + 2):
      # apl-source:32
      ع = ع + 1
  # apl-source:33
  return ع
# apl-source:34

# apl-source:35
تأكد_يساوي(ف(10), 2, "حالة 1")
# apl-source:36
تأكد_يساوي(ف(20), 4, "حالة 2")
# apl-source:37
تأكد_يساوي(ف(50), 6, "حالة 3")
# apl-source:38
تأكد_يساوي(ف(100), 8, "حالة 4")
# apl-source:39
