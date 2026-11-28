
# apl-source:1
# مثال 2266 — العدد الأولي ذو الترتيب ن
# apl-source:2
# Nth prime by counting
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2266-nth-prime-by-counting-loop.apl
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
def ف(ن):
  # apl-source:19
  ع = 0
  # apl-source:20
  ي = 1
  # apl-source:21
  while ع < ن:
    # apl-source:22
    ي = ي + 1
    # apl-source:23
    ا = True
    # apl-source:24
    د = 2
    # apl-source:25
    while د * د <= ي:
      # apl-source:26
      if ي % د == 0:
        # apl-source:27
        ا = False
      # apl-source:28
      د = د + 1
    # apl-source:29
    if ا:
      # apl-source:30
      ع = ع + 1
  # apl-source:31
  return ي
# apl-source:32

# apl-source:33
تأكد_يساوي(ف(1), 2, "حالة 1")
# apl-source:34
تأكد_يساوي(ف(2), 3, "حالة 2")
# apl-source:35
تأكد_يساوي(ف(5), 11, "حالة 3")
# apl-source:36
تأكد_يساوي(ف(10), 29, "حالة 4")
# apl-source:37
تأكد_يساوي(ف(25), 97, "حالة 5")
# apl-source:38
