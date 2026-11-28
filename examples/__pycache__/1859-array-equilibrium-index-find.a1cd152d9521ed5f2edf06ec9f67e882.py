
# apl-source:1
# مثال 1859 — نقطة توازن المصفوفة
# apl-source:2
# Equilibrium index of an array
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1859-array-equilibrium-index-find.apl
# apl-source:6

# apl-source:7
# المجموع الكلي معروف
# apl-source:8
# نحدث مجموع اليسار تدريجياً
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
def توازن(ق):
  # apl-source:19
  كل = 0
  # apl-source:20
  for ع in ق:
    # apl-source:21
    كل = كل + ع
  # apl-source:22
  يسار = 0
  # apl-source:23
  for ك in range(len(ق)):
    # apl-source:24
    if يسار == كل - يسار - ق[ك]:
      # apl-source:25
      return ك
    # apl-source:26
    يسار = يسار + ق[ك]
  # apl-source:27
  return -1
# apl-source:28

# apl-source:29
تأكد_يساوي(توازن([1, 7, 3, 6, 5, 6]), 3, "كلاسيكي")
# apl-source:30
تأكد_يساوي(توازن([1, 2, 3]), -1, "لا يوجد")
# apl-source:31
تأكد_يساوي(توازن([2, 1, -1]), 0, "الأول")
# apl-source:32
