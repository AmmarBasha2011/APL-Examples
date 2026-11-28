
# apl-source:1
# مثال 1403 — أطول سلسلة كولاتز
# apl-source:2
# Longest Collatz chain start
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1403-longest-collatz-start.apl
# apl-source:6

# apl-source:7
# نخزن أطوال السلاسل المحسوبة في قاموس
# apl-source:8
# كل سلسلة تتوقف عند عدد معروف الطول
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
def اطول_بداية(حد):
  # apl-source:19
  ذاكرة = {1: 1}
  # apl-source:20
  افضل = 1
  # apl-source:21
  افضل_طول = 1
  # apl-source:22
  for بداية in range(2, حد):
    # apl-source:23
    ن = بداية
    # apl-source:24
    خطوات = 0
    # apl-source:25
    while ن not in ذاكرة:
      # apl-source:26
      if ن % 2 == 0:
        # apl-source:27
        ن = ن // 2
      # apl-source:28
      else:
        # apl-source:29
        ن = 3 * ن + 1
      # apl-source:30
      خطوات = خطوات + 1
    # apl-source:31
    طول_ = خطوات + ذاكرة[ن]
    # apl-source:32
    ذاكرة[بداية] = طول_
    # apl-source:33
    if طول_ > افضل_طول:
      # apl-source:34
      افضل_طول = طول_
      # apl-source:35
      افضل = بداية
  # apl-source:36
  return افضل
# apl-source:37

# apl-source:38
تأكد_يساوي(اطول_بداية(10), 9, "أقل من عشرة")
# apl-source:39
تأكد_يساوي(اطول_بداية(100), 97, "أقل من مئة")
# apl-source:40
تأكد_يساوي(اطول_بداية(1000), 871, "أقل من ألف")
# apl-source:41
