
# apl-source:1
# مثال 1054 — نمط الكلمات
# apl-source:2
# Word pattern
# apl-source:3
# Demonstrates: تقابل واحد لواحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1054-word-pattern.apl
# apl-source:6

# apl-source:7
# كل حرف في النمط يقابل كلمة واحدة وبالعكس
# apl-source:8
# نتحقق بمقارنة أول ظهور لكل عنصر في الطرفين
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
def اول_ظهور(قائمة_, ع):
  # apl-source:19
  ف = 0
  # apl-source:20
  while قائمة_[ف] != قائمة_[ع]:
    # apl-source:21
    ف = ف + 1
  # apl-source:22
  return ف
# apl-source:23

# apl-source:24
def يتبع(نمط, جملة):
  # apl-source:25
  كلمات = جملة.split(" ")
  # apl-source:26
  if len(نمط) != len(كلمات):
    # apl-source:27
    return False
  # apl-source:28
  for ع in range(len(نمط)):
    # apl-source:29
    if اول_ظهور(list(نمط), ع) != اول_ظهور(كلمات, ع):
      # apl-source:30
      return False
  # apl-source:31
  return True
# apl-source:32

# apl-source:33
تأكد_يساوي(يتبع("abba", "dog cat cat dog"), True, "يتبع")
# apl-source:34
تأكد_يساوي(يتبع("abba", "dog cat cat fish"), False, "كلمة مختلفة")
# apl-source:35
تأكد_يساوي(يتبع("aaaa", "dog cat cat dog"), False, "حرف واحد لكلمات")
# apl-source:36
تأكد_يساوي(يتبع("abba", "dog dog dog dog"), False, "كلمة واحدة لحرفين")
# apl-source:37
