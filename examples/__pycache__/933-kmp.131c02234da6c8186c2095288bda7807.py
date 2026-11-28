
# apl-source:1
# مثال 933 — نوث-موريس-برات
# apl-source:2
# KMP string search
# apl-source:3
# Demonstrates: جدول فشل بادئة-لاحقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/933-kmp.apl
# apl-source:6

# apl-source:7
# كارثة السلاسل: نوث-موريس-برات يبحث بلا رجوع في النص
# apl-source:8
# جدول أطول بادئة-لاحقة يحدد مقدار القفز عند الفشل
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
def جدول_فشل(نمط):
  # apl-source:19
  م = len(نمط)
  # apl-source:20
  جدول = []
  # apl-source:21
  for _ in range(م):
    # apl-source:22
    جدول = جدول + [0]
  # apl-source:23
  ك = 0
  # apl-source:24
  for i in range(1, م):
    # apl-source:25
    while ك > 0 and نمط[i] != نمط[ك]:
      # apl-source:26
      ك = جدول[ك - 1]
    # apl-source:27
    if نمط[i] == نمط[ك]:
      # apl-source:28
      ك = ك + 1
    # apl-source:29
    جدول[i] = ك
  # apl-source:30
  return جدول
# apl-source:31

# apl-source:32
def ابحث(نص, نمط):
  # apl-source:33
  جدول = جدول_فشل(نمط)
  # apl-source:34
  مواضع = []
  # apl-source:35
  ق = 0
  # apl-source:36
  for i in range(len(نص)):
    # apl-source:37
    while ق > 0 and نص[i] != نمط[ق]:
      # apl-source:38
      ق = جدول[ق - 1]
    # apl-source:39
    if نص[i] == نمط[ق]:
      # apl-source:40
      ق = ق + 1
    # apl-source:41
    if ق == len(نمط):
      # apl-source:42
      مواضع = مواضع + [i - len(نمط) + 1]
      # apl-source:43
      ق = جدول[ق - 1]
  # apl-source:44
  return مواضع
# apl-source:45

# apl-source:46
جدول = جدول_فشل("ababd")
# apl-source:47
print("جدول ababd:", جدول)
# apl-source:48
مواضع = ابحث("ababcabcabababd", "ababd")
# apl-source:49
print("المواضع:", مواضع)
# apl-source:50

# apl-source:51
تأكد_يساوي(len(جدول), 5, "طول الجدول")
# apl-source:52
تأكد_يساوي(جدول[0], 0, "جدول[0]")
# apl-source:53
تأكد_يساوي(جدول[1], 0, "جدول[1]")
# apl-source:54
تأكد_يساوي(جدول[2], 1, "جدول[2]")
# apl-source:55
تأكد_يساوي(جدول[3], 2, "جدول[3]")
# apl-source:56
تأكد_يساوي(جدول[4], 0, "جدول[4]")
# apl-source:57
تأكد_يساوي(len(مواضع), 1, "مطابقة واحدة")
# apl-source:58
تأكد_يساوي(مواضع[0], 10, "عند الموضع 10")
# apl-source:59

# apl-source:60
# مطابقات متعددة
# apl-source:61
متعدد = ابحث("aaaa", "aa")
# apl-source:62
تأكد_يساوي(len(متعدد), 3, "ثلاث مطابقات متداخلة")
# apl-source:63
# لا مطابقة
# apl-source:64
تأكد_يساوي(len(ابحث("abc", "xyz")), 0, "لا مطابقة")
# apl-source:65
