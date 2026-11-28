
# apl-source:1
# مثال 2106 — العدد الذاتي التربيع
# apl-source:2
# Automorphic number check v2
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2106-automorphic-number-square-ends-with.apl
# apl-source:6

# apl-source:7
# # نقارن نهاية المربع بالعدد
# apl-source:8
# # مثل 5 و6 و76
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
def ذاتي(ن):
  # apl-source:19
  return str(ن * ن).endswith(str(ن))
# apl-source:20

# apl-source:21
تأكد_يساوي(ذاتي(5), True, "٥")
# apl-source:22
تأكد_يساوي(ذاتي(6), True, "٦")
# apl-source:23
تأكد_يساوي(ذاتي(76), True, "٧٦")
# apl-source:24
تأكد_يساوي(ذاتي(7), False, "٧")
# apl-source:25
تأكد_يساوي(ذاتي(25), True, "٢٥")
# apl-source:26
