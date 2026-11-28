
# apl-source:1
# مثال 2128 — هل العدد سداسي
# apl-source:2
# Hexagonal number test
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2128-hexagonal-number-membership-test.apl
# apl-source:6

# apl-source:7
# # نزيد n حتى نبلغ العدد
# apl-source:8
# # كل عدد سداسي مثلثي أيضا
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
def سداسي(ن):
  # apl-source:19
  ك = 1
  # apl-source:20
  while ك * (2 * ك - 1) < ن:
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return ك * (2 * ك - 1) == ن
# apl-source:23

# apl-source:24
تأكد_يساوي(سداسي(6), True, "٦")
# apl-source:25
تأكد_يساوي(سداسي(15), True, "١٥")
# apl-source:26
تأكد_يساوي(سداسي(28), True, "٢٨")
# apl-source:27
تأكد_يساوي(سداسي(10), False, "١٠")
# apl-source:28
تأكد_يساوي(سداسي(1), True, "١")
# apl-source:29
