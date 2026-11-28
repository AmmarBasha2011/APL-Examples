
# apl-source:1
# مثال 2247 — موضع التوازن
# apl-source:2
# Equilibrium index
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2247-list-equilibrium-index-left-right.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ف(ق):
  # apl-source:19
  ك = sum(ق)
  # apl-source:20
  ي2 = 0
  # apl-source:21
  for ي in range(len(ق)):
    # apl-source:22
    if ي2 == ك - ي2 - ق[ي]:
      # apl-source:23
      return ي
    # apl-source:24
    ي2 = ي2 + ق[ي]
  # apl-source:25
  return -1
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([1, 3, 5, 2, 2]), 2, "حالة 1")
# apl-source:28
تأكد_يساوي(ف([1, 2, 3]), -1, "حالة 2")
# apl-source:29
تأكد_يساوي(ف([2, 0, 2]), 1, "حالة 3")
# apl-source:30
تأكد_يساوي(ف([5]), 0, "حالة 4")
# apl-source:31
