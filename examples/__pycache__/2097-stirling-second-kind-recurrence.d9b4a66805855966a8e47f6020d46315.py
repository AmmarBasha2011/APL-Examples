
# apl-source:1
# مثال 2097 — أعداد ستيرلنغ من النوع الثاني
# apl-source:2
# Stirling numbers second kind
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2097-stirling-second-kind-recurrence.apl
# apl-source:6

# apl-source:7
# # S(n,k) = k*S(n-1,k) + S(n-1,k-1)
# apl-source:8
# # نبني جدولا
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
def ستيرلنغ(ن, ك):
  # apl-source:19
  ج = []
  # apl-source:20
  for ي in range(ن + 1):
    # apl-source:21
    ج = ج + [[0] * (ك + 1)]
  # apl-source:22
  ج[0][0] = 1
  # apl-source:23
  for ي in range(1, ن + 1):
    # apl-source:24
    for ز in range(1, ك + 1):
      # apl-source:25
      ج[ي][ز] = ز * ج[ي - 1][ز] + ج[ي - 1][ز - 1]
  # apl-source:26
  return ج[ن][ك]
# apl-source:27

# apl-source:28
تأكد_يساوي(ستيرلنغ(4, 2), 7, "٤،٢")
# apl-source:29
تأكد_يساوي(ستيرلنغ(5, 3), 25, "٥،٣")
# apl-source:30
تأكد_يساوي(ستيرلنغ(6, 3), 90, "٦،٣")
# apl-source:31
تأكد_يساوي(ستيرلنغ(5, 1), 1, "٥،١")
# apl-source:32
