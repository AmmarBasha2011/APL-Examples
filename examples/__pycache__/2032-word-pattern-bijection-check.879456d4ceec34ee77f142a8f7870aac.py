
# apl-source:1
# مثال 2032 — مطابقة نمط الحروف مع الكلمات
# apl-source:2
# Word pattern bijection
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2032-word-pattern-bijection-check.apl
# apl-source:6

# apl-source:7
# # نقسم الجملة إلى كلمات
# apl-source:8
# # ونتحقق من التقابل في الاتجاهين
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
def نمط(ن, جملة):
  # apl-source:19
  كلمات = جملة.split(" ")
  # apl-source:20
  if len(كلمات) != len(ن):
    # apl-source:21
    return False
  # apl-source:22
  خ1 = {}
  # apl-source:23
  خ2 = {}
  # apl-source:24
  for ك in range(len(ن)):
    # apl-source:25
    if ن[ك] in خ1 and خ1[ن[ك]] != كلمات[ك]:
      # apl-source:26
      return False
    # apl-source:27
    if كلمات[ك] in خ2 and خ2[كلمات[ك]] != ن[ك]:
      # apl-source:28
      return False
    # apl-source:29
    خ1[ن[ك]] = كلمات[ك]
    # apl-source:30
    خ2[كلمات[ك]] = ن[ك]
  # apl-source:31
  return True
# apl-source:32

# apl-source:33
تأكد_يساوي(نمط("abba", "dog cat cat dog"), True, "مطابق")
# apl-source:34
تأكد_يساوي(نمط("abba", "dog cat cat fish"), False, "كلمة مختلفة")
# apl-source:35
تأكد_يساوي(نمط("aaaa", "dog cat cat dog"), False, "حرف واحد")
# apl-source:36
