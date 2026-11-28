
# apl-source:1
# مثال 637 — إحلال الصفحات
# apl-source:2
# Page replacement
# apl-source:3
# Demonstrates: FIFO، أمثل، أخطاء صفحات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/637-page-replacement.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# إحلال الصفحات: FIFO والأمثل (OPT)
# apl-source:25
# Demonstrates: طابور إحلال, إحلال أمثل بأبعد استخدام, مقارنة أخطاء الصفحات
# apl-source:26
# الأمثل نظري؛ FIFO واقعي بسيط
# apl-source:27

# apl-source:28
def أخطاء_fifo(مرجع, سعة):
  # apl-source:29
  ذاكرة = []
  # apl-source:30
  طابور = []
  # apl-source:31
  أخطاء = 0
  # apl-source:32
  for صفحة in مرجع:
    # apl-source:33
    موجودة = صفحة in ذاكرة
    # apl-source:34
    if موجودة == False:
      # apl-source:35
      أخطاء = أخطاء + 1
      # apl-source:36
      if len(ذاكرة) >= سعة:
        # apl-source:37
        أقدم = طابور.pop(0)
        # apl-source:38
        ذاكرة.remove(أقدم)
      # apl-source:39
      ذاكرة.append(صفحة)
      # apl-source:40
      طابور.append(صفحة)
  # apl-source:41
  return أخطاء
# apl-source:42

# apl-source:43
def أخطاء_أمثل(مرجع, سعة):
  # apl-source:44
  ذاكرة = []
  # apl-source:45
  أخطاء = 0
  # apl-source:46
  for ي in range(len(مرجع)):
    # apl-source:47
    صفحة = مرجع[ي]
    # apl-source:48
    موجودة = صفحة in ذاكرة
    # apl-source:49
    if موجودة == False:
      # apl-source:50
      أخطاء = أخطاء + 1
      # apl-source:51
      if len(ذاكرة) >= سعة:
        # apl-source:52
        أبعد = -1
        # apl-source:53
        ضحية = ذاكرة[0]
        # apl-source:54
        for موجودة in ذاكرة:
          # apl-source:55
          تالي = 1000000000
          # apl-source:56
          for ج in range(ي + 1, len(مرجع)):
            # apl-source:57
            if مرجع[ج] == موجودة:
              # apl-source:58
              تالي = ج
          # apl-source:59
          if تالي > أبعد:
            # apl-source:60
            أبعد = تالي
            # apl-source:61
            ضحية = موجودة
        # apl-source:62
        ذاكرة.remove(ضحية)
      # apl-source:63
      ذاكرة.append(صفحة)
  # apl-source:64
  return أخطاء
# apl-source:65

# apl-source:66
مرجع = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
# apl-source:67
ف = أخطاء_fifo(مرجع, 3)
# apl-source:68
م = أخطاء_أمثل(مرجع, 3)
# apl-source:69
print("أخطاء FIFO:", ف, " وأخطاء الأمثل:", م)
# apl-source:70
تأكد_يساوي(ف, 9, "FIFO تسع أخطاء")
# apl-source:71
تأكد_يساوي(م, 7, "الأمثل سبع أخطاء")
# apl-source:72
تأكد_يساوي(م <= ف, True, "الأمثل لا يتجاوز FIFO")
# apl-source:73
