
# apl-source:1
# مثال 1242 — عدد إلى إنجليزية
# apl-source:2
# Integer to English words
# apl-source:3
# Demonstrates: تقسيم لثلاثيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1242-integer-to-english.apl
# apl-source:6

# apl-source:7
# نقسم العدد إلى مجموعات من ثلاثة أرقام
# apl-source:8
# ونضيف Thousand وMillion وBillion
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
def ثلاثة(ن):
  # apl-source:19
  احاد = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
  # apl-source:20
  عشرات = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
  # apl-source:21
  اجزاء = []
  # apl-source:22
  if ن >= 100:
    # apl-source:23
    اجزاء = اجزاء + [احاد[ن // 100]]
    # apl-source:24
    اجزاء = اجزاء + ["Hundred"]
    # apl-source:25
    ن = ن % 100
  # apl-source:26
  if ن >= 20:
    # apl-source:27
    اجزاء = اجزاء + [عشرات[ن // 10]]
    # apl-source:28
    ن = ن % 10
  # apl-source:29
  if ن > 0:
    # apl-source:30
    اجزاء = اجزاء + [احاد[ن]]
  # apl-source:31
  return " ".join(اجزاء)
# apl-source:32

# apl-source:33
def بالكلمات(ن):
  # apl-source:34
  if ن == 0:
    # apl-source:35
    return "Zero"
  # apl-source:36
  اسماء = ["", "Thousand", "Million", "Billion"]
  # apl-source:37
  اجزاء = []
  # apl-source:38
  ع = 0
  # apl-source:39
  while ن > 0:
    # apl-source:40
    ب = ن % 1000
    # apl-source:41
    if ب > 0:
      # apl-source:42
      ق = ثلاثة(ب)
      # apl-source:43
      if اسماء[ع] != "":
        # apl-source:44
        ق = ق + " " + اسماء[ع]
      # apl-source:45
      اجزاء.insert(0, ق)
    # apl-source:46
    ن = ن // 1000
    # apl-source:47
    ع = ع + 1
  # apl-source:48
  return " ".join(اجزاء)
# apl-source:49

# apl-source:50
تأكد_يساوي(بالكلمات(123), "One Hundred Twenty Three", "مئة وثلاثة وعشرون")
# apl-source:51
تأكد_يساوي(بالكلمات(12345), "Twelve Thousand Three Hundred Forty Five", "آلاف")
# apl-source:52
تأكد_يساوي(بالكلمات(1000000), "One Million", "مليون")
# apl-source:53
تأكد_يساوي(بالكلمات(0), "Zero", "صفر")
# apl-source:54
تأكد_يساوي(بالكلمات(1000010), "One Million Ten", "مليون وعشرة")
# apl-source:55
