
# apl-source:1
# مثال 965 — خط بريسنهام
# apl-source:2
# Bresenham line
# apl-source:3
# Demonstrates: متغير قرار صحيح واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/965-bresenham.apl
# apl-source:6

# apl-source:7
# خط بريسنهام: رسم خط شبكي بنقاط صحيحة دون حساب كسور
# apl-source:8
# متغير قرار واحد يحدد متى نصعد صفاً
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
def خط(س0, ص0, س1, ص1):
  # apl-source:19
  نقاط = []
  # apl-source:20
  فرق_س = س1 - س0
  # apl-source:21
  فرق_ص = ص1 - ص0
  # apl-source:22
  د = (2 * فرق_ص) - فرق_س
  # apl-source:23
  ص = ص0
  # apl-source:24
  for س in range(س0, س1 + 1):
    # apl-source:25
    نقاط = نقاط + [[س, ص]]
    # apl-source:26
    if د > 0:
      # apl-source:27
      ص = ص + 1
      # apl-source:28
      د = د - (2 * فرق_س)
    # apl-source:29
    د = د + (2 * فرق_ص)
  # apl-source:30
  return نقاط
# apl-source:31

# apl-source:32
نقاط = خط(0, 0, 5, 3)
# apl-source:33
تأكد_يساوي(len(نقاط), 6, "عدد النقاط")
# apl-source:34
تأكد_يساوي(نقاط[1][0], 1, "س النقطة الثانية")
# apl-source:35
تأكد_يساوي(نقاط[1][1], 1, "ص النقطة الثانية")
# apl-source:36
تأكد_يساوي(نقاط[2][1], 1, "ص النقطة الثالثة")
# apl-source:37
تأكد_يساوي(نقاط[3][1], 2, "ص النقطة الرابعة")
# apl-source:38
تأكد_يساوي(نقاط[5][0], 5, "س النهاية")
# apl-source:39
تأكد_يساوي(نقاط[5][1], 3, "ص النهاية")
# apl-source:40
