
# apl-source:1
# مثال 2095 — أعداد كاتالان بالمتتالية التراجعية
# apl-source:2
# Catalan numbers DP
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2095-catalan-numbers-dp-convolution.apl
# apl-source:6

# apl-source:7
# # C(n+1) = مجموع C(i)*C(n-i)
# apl-source:8
# # نخزن الحدود السابقة
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
def كاتالان(ن):
  # apl-source:19
  ق = [1]
  # apl-source:20
  for م in range(ن):
    # apl-source:21
    مج = 0
    # apl-source:22
    for ي in range(م + 1):
      # apl-source:23
      مج = مج + ق[ي] * ق[م - ي]
    # apl-source:24
    ق = ق + [مج]
  # apl-source:25
  return ق[ن]
# apl-source:26

# apl-source:27
تأكد_يساوي(كاتالان(0), 1, "٠")
# apl-source:28
تأكد_يساوي(كاتالان(5), 42, "٥")
# apl-source:29
تأكد_يساوي(كاتالان(6), 132, "٦")
# apl-source:30
تأكد_يساوي(كاتالان(10), 16796, "١٠")
# apl-source:31
