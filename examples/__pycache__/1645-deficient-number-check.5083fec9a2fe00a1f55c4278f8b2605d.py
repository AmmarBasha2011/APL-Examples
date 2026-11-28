
# apl-source:1
# مثال 1645 — العدد الناقص
# apl-source:2
# Deficient number check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1645-deficient-number-check.apl
# apl-source:6

# apl-source:7
# نجمع القواسم دون العدد نفسه
# apl-source:8
# نقارن المجموع بالعدد
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
def ناقص(ن):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ك in range(1, ن):
    # apl-source:21
    if ن % ك == 0:
      # apl-source:22
      مجموع = مجموع + ك
  # apl-source:23
  return مجموع < ن
# apl-source:24

# apl-source:25
تأكد_يساوي(ناقص(8), True, "ثمانية")
# apl-source:26
تأكد_يساوي(ناقص(12), False, "وافر")
# apl-source:27
تأكد_يساوي(ناقص(6), False, "تام")
# apl-source:28
تأكد_يساوي(ناقص(7), True, "أولي")
# apl-source:29
