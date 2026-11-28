
# apl-source:1
# مثال 1234 — شحن الطرود
# apl-source:2
# Capacity to ship packages within days
# apl-source:3
# Demonstrates: بحث ثنائي على الجواب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1234-ship-packages.apl
# apl-source:6

# apl-source:7
# السعة بين أكبر طرد ومجموع الطرود
# apl-source:8
# نتحقق بعدد الأيام اللازمة جشعاً
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
def ايام(اوزان, سعة):
  # apl-source:19
  ع = 1
  # apl-source:20
  حمل = 0
  # apl-source:21
  for و in اوزان:
    # apl-source:22
    if حمل + و > سعة:
      # apl-source:23
      ع = ع + 1
      # apl-source:24
      حمل = 0
    # apl-source:25
    حمل = حمل + و
  # apl-source:26
  return ع
# apl-source:27

# apl-source:28
def اقل_سعة(اوزان, د):
  # apl-source:29
  يسار = 0
  # apl-source:30
  يمين = 0
  # apl-source:31
  for و in اوزان:
    # apl-source:32
    if و > يسار:
      # apl-source:33
      يسار = و
    # apl-source:34
    يمين = يمين + و
  # apl-source:35
  while يسار < يمين:
    # apl-source:36
    وسط = (يسار + يمين) // 2
    # apl-source:37
    if ايام(اوزان, وسط) <= د:
      # apl-source:38
      يمين = وسط
    # apl-source:39
    else:
      # apl-source:40
      يسار = وسط + 1
  # apl-source:41
  return يسار
# apl-source:42

# apl-source:43
تأكد_يساوي(اقل_سعة([1,2,3,4,5,6,7,8,9,10], 5), 15, "مثال أول")
# apl-source:44
تأكد_يساوي(اقل_سعة([3,2,2,4,1,4], 3), 6, "مثال ثان")
# apl-source:45
تأكد_يساوي(اقل_سعة([1,2,3,1,1], 4), 3, "مثال ثالث")
# apl-source:46
