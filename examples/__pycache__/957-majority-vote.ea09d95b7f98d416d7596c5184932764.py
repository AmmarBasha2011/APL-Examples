
# apl-source:1
# مثال 957 — تصويت الأغلبية
# apl-source:2
# Majority vote
# apl-source:3
# Demonstrates: مرشح بمرور ثم تحقق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/957-majority-vote.apl
# apl-source:6

# apl-source:7
# تصويت الأغلبية (بوير-مور): مرشح واحد في مرور ثم تحقق في مرور ثان
# apl-source:8
# زمن خطي وذاكرة ثابتة بدون عدّ مستقل لكل قيمة
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
def أغلبية(عناصر):
  # apl-source:19
  مرشح = 0
  # apl-source:20
  عداد = 0
  # apl-source:21
  for س in عناصر:
    # apl-source:22
    if عداد == 0:
      # apl-source:23
      مرشح = س
      # apl-source:24
      عداد = 1
    # apl-source:25
    elif س == مرشح:
      # apl-source:26
      عداد = عداد + 1
    # apl-source:27
    else:
      # apl-source:28
      عداد = عداد - 1
  # apl-source:29
  عدد = 0
  # apl-source:30
  for س in عناصر:
    # apl-source:31
    if س == مرشح:
      # apl-source:32
      عدد = عدد + 1
  # apl-source:33
  if (عدد * 2) > len(عناصر):
    # apl-source:34
    return مرشح
  # apl-source:35
  return -1
# apl-source:36

# apl-source:37
تأكد_يساوي(أغلبية([3, 3, 4, 2, 4, 4, 2, 4, 4]), 4, "أغلبية واضحة")
# apl-source:38
تأكد_يساوي(أغلبية([3, 3, 4, 2, 4, 4, 2, 4]), -1, "لا أغلبية")
# apl-source:39
تأكد_يساوي(أغلبية([7, 7, 7, 7, 1, 2]), 7, "أغلبية ساحقة")
# apl-source:40
