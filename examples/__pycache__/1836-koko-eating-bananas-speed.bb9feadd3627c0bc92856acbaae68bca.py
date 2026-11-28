
# apl-source:1
# مثال 1836 — أقل سرعة أكل
# apl-source:2
# Minimum eating speed
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1836-koko-eating-bananas-speed.apl
# apl-source:6

# apl-source:7
# نختبر سرعة ممكنة
# apl-source:8
# نقلص المدى بحسب الساعات
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
def ساعات(أكوام, سرعة):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ع in أكوام:
    # apl-source:21
    مجموع = مجموع + (ع + سرعة - 1) // سرعة
  # apl-source:22
  return مجموع
# apl-source:23

# apl-source:24
def أقل_سرعة(أكوام, حد):
  # apl-source:25
  يسار = 1
  # apl-source:26
  يمين = 1
  # apl-source:27
  for ع in أكوام:
    # apl-source:28
    يمين = max(يمين, ع)
  # apl-source:29
  while يسار < يمين:
    # apl-source:30
    وسط = (يسار + يمين) // 2
    # apl-source:31
    if ساعات(أكوام, وسط) <= حد:
      # apl-source:32
      يمين = وسط
    # apl-source:33
    else:
      # apl-source:34
      يسار = وسط + 1
  # apl-source:35
  return يسار
# apl-source:36

# apl-source:37
تأكد_يساوي(أقل_سرعة([3, 6, 7, 11], 8), 4, "أربعة")
# apl-source:38
تأكد_يساوي(أقل_سرعة([30, 11, 23, 4, 20], 5), 30, "ثلاثون")
# apl-source:39
تأكد_يساوي(أقل_سرعة([30, 11, 23, 4, 20], 6), 23, "ثلاث وعشرون")
# apl-source:40
