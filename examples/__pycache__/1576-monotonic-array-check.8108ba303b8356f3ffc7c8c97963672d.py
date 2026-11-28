
# apl-source:1
# مثال 1576 — هل المصفوفة رتيبة
# apl-source:2
# Monotonic array check
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1576-monotonic-array-check.apl
# apl-source:6

# apl-source:7
# نتتبع هل ظهر صعود وهل ظهر هبوط
# apl-source:8
# الرتيبة لا يظهر فيها الاثنان
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
def رتيبة(أ):
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
  return (صعود and هبوط) == False
# apl-source:27

# apl-source:28
تأكد_يساوي(رتيبة([1, 2, 2, 3]), True, "تصاعدية")
# apl-source:29
تأكد_يساوي(رتيبة([6, 5, 4, 4]), True, "تنازلية")
# apl-source:30
تأكد_يساوي(رتيبة([1, 3, 2]), False, "ليست رتيبة")
# apl-source:31
تأكد_يساوي(رتيبة([5]), True, "وحيدة")
# apl-source:32
