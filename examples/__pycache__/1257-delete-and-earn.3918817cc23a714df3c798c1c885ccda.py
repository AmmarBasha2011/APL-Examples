
# apl-source:1
# مثال 1257 — احذف واكسب
# apl-source:2
# Delete and earn
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1257-delete-and-earn.apl
# apl-source:6

# apl-source:7
# نجمع نقاط كل قيمة
# apl-source:8
# ثم نحلها كمسألة سرقة بيوت متجاورة
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
def اكسب(أ):
  # apl-source:19
  if len(أ) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  اقصى = 0
  # apl-source:22
  for س in أ:
    # apl-source:23
    if س > اقصى:
      # apl-source:24
      اقصى = س
  # apl-source:25
  نقاط = [0] * (اقصى + 1)
  # apl-source:26
  for س in أ:
    # apl-source:27
    نقاط[س] = نقاط[س] + س
  # apl-source:28
  سابق = 0
  # apl-source:29
  حالي = 0
  # apl-source:30
  for ن in نقاط:
    # apl-source:31
    جديد = max(حالي, سابق + ن)
    # apl-source:32
    سابق = حالي
    # apl-source:33
    حالي = جديد
  # apl-source:34
  return حالي
# apl-source:35

# apl-source:36
تأكد_يساوي(اكسب([3,4,2]), 6, "مثال أول")
# apl-source:37
تأكد_يساوي(اكسب([2,2,3,3,3,4]), 9, "مثال ثان")
# apl-source:38
تأكد_يساوي(اكسب([1]), 1, "عنصر")
# apl-source:39
تأكد_يساوي(اكسب([]), 0, "فارغة")
# apl-source:40
