
# apl-source:1
# مثال 2383 — مجموع أول ن عدد أولي
# apl-source:2
# Sum of first n primes
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2383-sum-of-first-n-primes-loop.apl
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
  م = 0
  # apl-source:21
  ي = 1
  # apl-source:22
  while ع < ن:
    # apl-source:23
    ي = ي + 1
    # apl-source:24
    ا = True
    # apl-source:25
    د = 2
    # apl-source:26
    while د * د <= ي:
      # apl-source:27
      if ي % د == 0:
        # apl-source:28
        ا = False
      # apl-source:29
      د = د + 1
    # apl-source:30
    if ا:
      # apl-source:31
      ع = ع + 1
      # apl-source:32
      م = م + ي
  # apl-source:33
  return م
# apl-source:34

# apl-source:35
تأكد_يساوي(ف(1), 2, "حالة 1")
# apl-source:36
تأكد_يساوي(ف(2), 5, "حالة 2")
# apl-source:37
تأكد_يساوي(ف(5), 28, "حالة 3")
# apl-source:38
تأكد_يساوي(ف(10), 129, "حالة 4")
# apl-source:39
تأكد_يساوي(ف(15), 328, "حالة 5")
# apl-source:40
