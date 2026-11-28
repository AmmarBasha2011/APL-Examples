
# apl-source:1
# مثال 1137 — مجالات ناقصة
# apl-source:2
# Missing ranges
# apl-source:3
# Demonstrates: مسح خطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1137-missing-ranges.apl
# apl-source:6

# apl-source:7
# نقارن كل رقم بما قبله
# apl-source:8
# وأي فجوة نسجلها كمجال
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
def صيغة(أ, ب):
  # apl-source:19
  if أ == ب:
    # apl-source:20
    return str(أ)
  # apl-source:21
  return str(أ) + "->" + str(ب)
# apl-source:22

# apl-source:23
def ناقصة(أ, ادنى, اعلى):
  # apl-source:24
  ناتج = []
  # apl-source:25
  سابق = ادنى - 1
  # apl-source:26
  for س in أ + [اعلى + 1]:
    # apl-source:27
    if س - سابق >= 2:
      # apl-source:28
      ناتج = ناتج + [صيغة(سابق + 1, س - 1)]
    # apl-source:29
    سابق = س
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(ناقصة([0,1,3,50,75], 0, 99), ["2", "4->49", "51->74", "76->99"], "مثال أول")
# apl-source:33
تأكد_يساوي(ناقصة([], 1, 1), ["1"], "فارغة")
# apl-source:34
تأكد_يساوي(ناقصة([-1], -1, -1), [], "لا نقص")
# apl-source:35
تأكد_يساوي(ناقصة([2,3], 1, 5), ["1", "4->5"], "طرفان")
# apl-source:36
