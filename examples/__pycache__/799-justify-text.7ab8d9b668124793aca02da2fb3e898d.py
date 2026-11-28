
# apl-source:1
# مثال 799 — ضبط النص
# apl-source:2
# Text justification
# apl-source:3
# Demonstrates: توزيع فراغات، قسمة وباقي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/799-justify-text.apl
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
# ضبط النص بعرض ثابت: توزيع الفراغات بالتساوي بين الكلمات
# apl-source:25
# Demonstrates: تجميع الأسطر بالطول, قسمة وباقي لتوزيع الفراغات, سطر أخير بضبط يسار
# apl-source:26

# apl-source:27
def كرر(نص, عدد):
  # apl-source:28
  ناتج = ""
  # apl-source:29
  for ي in range(عدد):
    # apl-source:30
    ناتج = ناتج + نص
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
def اضبط(كلمات, عرض):
  # apl-source:34
  أسطر = []
  # apl-source:35
  سطر = [كلمات[0]]
  # apl-source:36
  طول_سطر = len(كلمات[0])
  # apl-source:37
  for ي in range(1, len(كلمات)):
    # apl-source:38
    ك = كلمات[ي]
    # apl-source:39
    if طول_سطر + 1 + len(ك) <= عرض:
      # apl-source:40
      سطر.append(ك)
      # apl-source:41
      طول_سطر = طول_سطر + 1 + len(ك)
    # apl-source:42
    else:
      # apl-source:43
      أسطر.append(سطر)
      # apl-source:44
      سطر = [ك]
      # apl-source:45
      طول_سطر = len(ك)
  # apl-source:46
  أسطر.append(سطر)
  # apl-source:47
  ناتج = []
  # apl-source:48
  for ي in range(len(أسطر) - 1):
    # apl-source:49
    س = أسطر[ي]
    # apl-source:50
    if len(س) == 1:
      # apl-source:51
      ناتج.append(س[0])
    # apl-source:52
    else:
      # apl-source:53
      مجموع = 0
      # apl-source:54
      for ك in س:
        # apl-source:55
        مجموع = مجموع + len(ك)
      # apl-source:56
      فراغات = عرض - مجموع
      # apl-source:57
      فجوات = len(س) - 1
      # apl-source:58
      أساس = فراغات // فجوات
      # apl-source:59
      إضافي = فراغات % فجوات
      # apl-source:60
      نص = ""
      # apl-source:61
      for ك in range(len(س) - 1):
        # apl-source:62
        نص = نص + س[ك]
        # apl-source:63
        if ك < إضافي:
          # apl-source:64
          نص = نص + كرر(" ", أساس + 1)
        # apl-source:65
        else:
          # apl-source:66
          نص = نص + كرر(" ", أساس)
      # apl-source:67
      نص = نص + س[len(س) - 1]
      # apl-source:68
      ناتج.append(نص)
  # apl-source:69
  ناتج.append(" ".join(أسطر[len(أسطر) - 1]))
  # apl-source:70
  return ناتج
# apl-source:71

# apl-source:72
كلمات = "The quick brown fox jumps over the lazy dog".split(" ")
# apl-source:73
نتيجة = اضبط(كلمات, 20)
# apl-source:74
تأكد_يساوي(نتيجة, ["The  quick brown fox", "jumps  over the lazy", "dog"], "ضبط بعرض 20")
# apl-source:75
تأكد_يساوي(len(نتيجة[0]), 20, "السطر الأول ممتلئ")
# apl-source:76
تأكد_يساوي(len(نتيجة[1]), 20, "السطر الثاني ممتلئ")
# apl-source:77
نتيجة2 = اضبط("one two three four five six".split(" "), 11)
# apl-source:78
تأكد_يساوي(نتيجة2, ["one     two", "three  four", "five six"], "ضبط بعرض 11")
# apl-source:79
