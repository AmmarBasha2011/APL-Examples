
# apl-source:1
# مثال 1812 — مطابقة نمط الكلمات
# apl-source:2
# Word pattern match
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1812-word-pattern-match-check.apl
# apl-source:6

# apl-source:7
# نقسم الجملة
# apl-source:8
# نربط الحرف بالكلمة
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
def يطابق(نمط, جملة):
  # apl-source:19
  كلمات = جملة.split(" ")
  # apl-source:20
  if len(كلمات) != len(نمط):
    # apl-source:21
    return False
  # apl-source:22
  أ = {}
  # apl-source:23
  ب = {}
  # apl-source:24
  for ك in range(len(نمط)):
    # apl-source:25
    ح = نمط[ك]
    # apl-source:26
    ك_كلمة = كلمات[ك]
    # apl-source:27
    if ح in أ:
      # apl-source:28
      if أ[ح] != ك_كلمة:
        # apl-source:29
        return False
    # apl-source:30
    else:
      # apl-source:31
      أ[ح] = ك_كلمة
    # apl-source:32
    if ك_كلمة in ب:
      # apl-source:33
      if ب[ك_كلمة] != ح:
        # apl-source:34
        return False
    # apl-source:35
    else:
      # apl-source:36
      ب[ك_كلمة] = ح
  # apl-source:37
  return True
# apl-source:38

# apl-source:39
تأكد_يساوي(يطابق("abba", "dog cat cat dog"), True, "مطابق")
# apl-source:40
تأكد_يساوي(يطابق("abba", "dog cat cat fish"), False, "كلمة مختلفة")
# apl-source:41
تأكد_يساوي(يطابق("aaaa", "dog cat cat dog"), False, "نمط واحد")
# apl-source:42
