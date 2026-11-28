
# apl-source:1
# مثال 2275 — طرق تفكيك مبلغ بعملات 1 و5 و10
# apl-source:2
# Coin change ways 1 5 10
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2275-coin-change-ways-one-five-ten.apl
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
  ط = [0] * (ن + 1)
  # apl-source:20
  ط[0] = 1
  # apl-source:21
  for ع in [1, 5, 10]:
    # apl-source:22
    for ي in range(ع, ن + 1):
      # apl-source:23
      ط[ي] = ط[ي] + ط[ي - ع]
  # apl-source:24
  return ط[ن]
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:27
تأكد_يساوي(ف(5), 2, "حالة 2")
# apl-source:28
تأكد_يساوي(ف(10), 4, "حالة 3")
# apl-source:29
تأكد_يساوي(ف(25), 12, "حالة 4")
# apl-source:30
تأكد_يساوي(ف(100), 121, "حالة 5")
# apl-source:31
