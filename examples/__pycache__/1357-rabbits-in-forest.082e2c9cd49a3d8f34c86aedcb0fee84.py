
# apl-source:1
# مثال 1357 — أرانب الغابة
# apl-source:2
# Rabbits in forest
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1357-rabbits-in-forest.apl
# apl-source:6

# apl-source:7
# الإجابة x تعني أن للأرنب x زميل بنفس اللون
# apl-source:8
# نجمع الأرانب في مجموعات حجمها x زائد واحد
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
def عدد_الارانب(اجابات):
  # apl-source:19
  عدّاد = {}
  # apl-source:20
  for ا in اجابات:
    # apl-source:21
    عدّاد[ا] = عدّاد.get(ا, 0) + 1
  # apl-source:22
  مجموع = 0
  # apl-source:23
  for ا in عدّاد:
    # apl-source:24
    حجم = ا + 1
    # apl-source:25
    مجموعات = (عدّاد[ا] + حجم - 1) // حجم
    # apl-source:26
    مجموع = مجموع + مجموعات * حجم
  # apl-source:27
  return مجموع
# apl-source:28

# apl-source:29
تأكد_يساوي(عدد_الارانب([1,1,2]), 5, "خمسة")
# apl-source:30
تأكد_يساوي(عدد_الارانب([10,10,10]), 11, "أحد عشر")
# apl-source:31
تأكد_يساوي(عدد_الارانب([]), 0, "فارغة")
# apl-source:32
