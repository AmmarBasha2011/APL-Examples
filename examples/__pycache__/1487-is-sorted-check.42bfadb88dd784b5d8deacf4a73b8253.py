
# apl-source:1
# مثال 1487 — هل القائمة مرتبة
# apl-source:2
# Is the list sorted
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1487-is-sorted-check.apl
# apl-source:6

# apl-source:7
# نقارن كل جارين
# apl-source:8
# نتتبع هل رأينا صعوداً وهبوطاً
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
def نوع_الترتيب(أ):
  # apl-source:19
  صعود = False
  # apl-source:20
  هبوط = False
  # apl-source:21
  for ع in range(1, len(أ)):
    # apl-source:22
    if أ[ع] > أ[ع - 1]:
      # apl-source:23
      صعود = True
    # apl-source:24
    if أ[ع] < أ[ع - 1]:
      # apl-source:25
      هبوط = True
  # apl-source:26
  if صعود and هبوط:
    # apl-source:27
    return "غير مرتبة"
  # apl-source:28
  if هبوط:
    # apl-source:29
    return "تنازلية"
  # apl-source:30
  return "تصاعدية"
# apl-source:31

# apl-source:32
تأكد_يساوي(نوع_الترتيب([1, 2, 2, 5]), "تصاعدية", "صاعدة")
# apl-source:33
تأكد_يساوي(نوع_الترتيب([9, 4, 4, 1]), "تنازلية", "هابطة")
# apl-source:34
تأكد_يساوي(نوع_الترتيب([1, 3, 2]), "غير مرتبة", "مختلطة")
# apl-source:35
