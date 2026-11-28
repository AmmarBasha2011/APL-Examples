
# apl-source:1
# مثال 2045 — عدد البتات الواحدة من 0 إلى ن
# apl-source:2
# Counting bits up to n
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2045-count-set-bits-for-zero-to-n.apl
# apl-source:6

# apl-source:7
# # نعيد استخدام النتيجة المحسوبة سابقا
# apl-source:8
# # فنحصل على حل خطي
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
def عد_بتات(ن):
  # apl-source:19
  ق = [0]
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    ق = ق + [ق[ك >> 1] + (ك & 1)]
  # apl-source:22
  return ق
# apl-source:23

# apl-source:24
تأكد_يساوي(عد_بتات(5), [0, 1, 1, 2, 1, 2], "حتى ٥")
# apl-source:25
تأكد_يساوي(عد_بتات(0), [0], "صفر")
# apl-source:26
تأكد_يساوي(عد_بتات(8)[8], 1, "٨")
# apl-source:27
