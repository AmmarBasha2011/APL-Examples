
# apl-source:1
# مثال 1837 — أقل سعة لشحن الطرود
# apl-source:2
# Minimum ship capacity in days
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1837-ship-packages-capacity-days.apl
# apl-source:6

# apl-source:7
# نحسب الأيام لسعة معينة
# apl-source:8
# نبحث عن أصغر سعة تكفي
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
def أيام_الشحن(أوزان, سعة):
  # apl-source:19
  عدد = 1
  # apl-source:20
  حمولة = 0
  # apl-source:21
  for ع in أوزان:
    # apl-source:22
    if حمولة + ع > سعة:
      # apl-source:23
      عدد = عدد + 1
      # apl-source:24
      حمولة = 0
    # apl-source:25
    حمولة = حمولة + ع
  # apl-source:26
  return عدد
# apl-source:27

# apl-source:28
def أقل_سعة(أوزان, أيام_مسموحة):
  # apl-source:29
  يسار = 0
  # apl-source:30
  يمين = 0
  # apl-source:31
  for ع in أوزان:
    # apl-source:32
    يسار = max(يسار, ع)
    # apl-source:33
    يمين = يمين + ع
  # apl-source:34
  while يسار < يمين:
    # apl-source:35
    وسط = (يسار + يمين) // 2
    # apl-source:36
    if أيام_الشحن(أوزان, وسط) <= أيام_مسموحة:
      # apl-source:37
      يمين = وسط
    # apl-source:38
    else:
      # apl-source:39
      يسار = وسط + 1
  # apl-source:40
  return يسار
# apl-source:41

# apl-source:42
تأكد_يساوي(أقل_سعة([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15, "عشرة طرود")
# apl-source:43
تأكد_يساوي(أقل_سعة([3, 2, 2, 4, 1, 4], 3), 6, "ستة")
# apl-source:44
تأكد_يساوي(أقل_سعة([1, 2, 3, 1, 1], 4), 3, "ثلاثة")
# apl-source:45
