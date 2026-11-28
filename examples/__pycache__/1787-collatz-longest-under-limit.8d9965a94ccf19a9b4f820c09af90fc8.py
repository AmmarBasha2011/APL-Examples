
# apl-source:1
# مثال 1787 — أطول متتالية كولاتز
# apl-source:2
# Longest Collatz chain under limit
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1787-collatz-longest-under-limit.apl
# apl-source:6

# apl-source:7
# نحسب طول كل متتالية
# apl-source:8
# نحتفظ بالأطول
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
def طول_كولاتز(ن):
  # apl-source:19
  عد = 1
  # apl-source:20
  while ن != 1:
    # apl-source:21
    if ن % 2 == 0:
      # apl-source:22
      ن = ن // 2
    # apl-source:23
    else:
      # apl-source:24
      ن = 3 * ن + 1
    # apl-source:25
    عد = عد + 1
  # apl-source:26
  return عد
# apl-source:27

# apl-source:28
def أطول_بداية(حد):
  # apl-source:29
  أفضل = 1
  # apl-source:30
  طول_أفضل = 1
  # apl-source:31
  for ك in range(1, حد):
    # apl-source:32
    ط = طول_كولاتز(ك)
    # apl-source:33
    if ط > طول_أفضل:
      # apl-source:34
      طول_أفضل = ط
      # apl-source:35
      أفضل = ك
  # apl-source:36
  return أفضل
# apl-source:37

# apl-source:38
تأكد_يساوي(طول_كولاتز(27), 112, "سبعة وعشرون")
# apl-source:39
تأكد_يساوي(أطول_بداية(10), 9, "تحت عشرة")
# apl-source:40
تأكد_يساوي(أطول_بداية(30), 27, "تحت ثلاثين")
# apl-source:41
