
# apl-source:1
# مثال 608 — قابلية حل لغز الخمسة عشر
# apl-source:2
# 15-puzzle solvability
# apl-source:3
# Demonstrates: معكوسات، تكافؤ، لغز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/608-puzzle-15.apl
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
# لغز الخمسة عشر: هل الوضع قابل للحل؟
# apl-source:25
# Demonstrates: عد المعكوسات, تكافؤ الصف الفارغ, قاعدة الحل
# apl-source:26
# نصف الترتيبات الممكنة فقط قابلة للحل
# apl-source:27

# apl-source:28
def قابل_للحل(بلاطات):
  # apl-source:29
  معكوسات = 0
  # apl-source:30
  مسطحة = []
  # apl-source:31
  for بلاط in بلاطات:
    # apl-source:32
    if بلاط != 0:
      # apl-source:33
      مسطحة.append(بلاط)
  # apl-source:34
  for ي in range(len(مسطحة)):
    # apl-source:35
    for ج in range(ي + 1, len(مسطحة)):
      # apl-source:36
      if مسطحة[ي] > مسطحة[ج]:
        # apl-source:37
        معكوسات = معكوسات + 1
  # apl-source:38
  صف_الفارغ_من_الأسفل = 4 - (بلاطات.index(0) // 4)
  # apl-source:39
  if صف_الفارغ_من_الأسفل % 2 == 0:
    # apl-source:40
    return معكوسات % 2 == 1
  # apl-source:41
  return معكوسات % 2 == 0
# apl-source:42

# apl-source:43
محلول = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
# apl-source:44
تأكد_يساوي(قابل_للحل(محلول), True, "الوضع المحلول قابل")
# apl-source:45
مبدل = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,14,0]
# apl-source:46
تأكد_يساوي(قابل_للحل(مبدل), False, "تبديل قطعتين مستحيل")
# apl-source:47
عشوائي = [5,1,3,4,2,6,7,8,9,10,11,12,13,14,15,0]
# apl-source:48
نتيجة = قابل_للحل(عشوائي)
# apl-source:49
print("الوضع الثالث قابل للحل:", نتيجة)
# apl-source:50
تأكد_يساوي(نتيجة, True, "معكوسان = قابل")
# apl-source:51
