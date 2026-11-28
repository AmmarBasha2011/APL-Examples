
# apl-source:1
# مثال 1703 — حاصل الضرب دون العنصر نفسه
# apl-source:2
# Product of array except self
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1703-product-except-self-list.apl
# apl-source:6

# apl-source:7
# حاصل ما قبل العنصر
# apl-source:8
# ثم حاصل ما بعده
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
def ضرب_الباقي(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  ناتج = []
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    ناتج.append(1)
  # apl-source:23
  بادئة = 1
  # apl-source:24
  for ك in range(ن):
    # apl-source:25
    ناتج[ك] = بادئة
    # apl-source:26
    بادئة = بادئة * ق[ك]
  # apl-source:27
  لاحقة = 1
  # apl-source:28
  for ك in range(ن - 1, -1, -1):
    # apl-source:29
    ناتج[ك] = ناتج[ك] * لاحقة
    # apl-source:30
    لاحقة = لاحقة * ق[ك]
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(ضرب_الباقي([1, 2, 3, 4]), [24, 12, 8, 6], "أربعة")
# apl-source:34
تأكد_يساوي(ضرب_الباقي([2, 0, 3]), [0, 6, 0], "صفر")
# apl-source:35
