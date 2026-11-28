
# apl-source:1
# مثال 1232 — تقسيم بأقل مجموع أكبر
# apl-source:2
# Split array largest sum
# apl-source:3
# Demonstrates: بحث ثنائي على الجواب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1232-split-array-largest-sum.apl
# apl-source:6

# apl-source:7
# نبحث ثنائياً عن الحد الأعلى للمجموع
# apl-source:8
# ونتحقق بعدد الأجزاء اللازمة جشعاً
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
def اجزاء_لازمة(أ, حد):
  # apl-source:19
  ع = 1
  # apl-source:20
  مج = 0
  # apl-source:21
  for س in أ:
    # apl-source:22
    if مج + س > حد:
      # apl-source:23
      ع = ع + 1
      # apl-source:24
      مج = س
    # apl-source:25
    else:
      # apl-source:26
      مج = مج + س
  # apl-source:27
  return ع
# apl-source:28

# apl-source:29
def قسم(أ, م):
  # apl-source:30
  يسار = 0
  # apl-source:31
  يمين = 0
  # apl-source:32
  for س in أ:
    # apl-source:33
    if س > يسار:
      # apl-source:34
      يسار = س
    # apl-source:35
    يمين = يمين + س
  # apl-source:36
  while يسار < يمين:
    # apl-source:37
    وسط = (يسار + يمين) // 2
    # apl-source:38
    if اجزاء_لازمة(أ, وسط) <= م:
      # apl-source:39
      يمين = وسط
    # apl-source:40
    else:
      # apl-source:41
      يسار = وسط + 1
  # apl-source:42
  return يسار
# apl-source:43

# apl-source:44
تأكد_يساوي(قسم([7,2,5,10,8], 2), 18, "مثال أول")
# apl-source:45
تأكد_يساوي(قسم([1,2,3,4,5], 2), 9, "مثال ثان")
# apl-source:46
تأكد_يساوي(قسم([1,4,4], 3), 4, "ثلاثة أجزاء")
# apl-source:47
