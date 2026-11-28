
# apl-source:1
# مثال 1660 — العدد الذاتي التربيع
# apl-source:2
# Automorphic number check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1660-automorphic-number-check.apl
# apl-source:6

# apl-source:7
# نحسب المربع
# apl-source:8
# نقارن آخر أرقامه بالعدد
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
  مربع = ن * ن
  # apl-source:20
  قاعدة = 1
  # apl-source:21
  ك = ن
  # apl-source:22
  while ك > 0:
    # apl-source:23
    قاعدة = قاعدة * 10
    # apl-source:24
    ك = ك // 10
  # apl-source:25
  return مربع % قاعدة == ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ذاتي(5), True, "خمسة")
# apl-source:28
تأكد_يساوي(ذاتي(76), True, "ستة وسبعون")
# apl-source:29
تأكد_يساوي(ذاتي(7), False, "سبعة")
# apl-source:30
تأكد_يساوي(ذاتي(625), True, "625")
# apl-source:31
