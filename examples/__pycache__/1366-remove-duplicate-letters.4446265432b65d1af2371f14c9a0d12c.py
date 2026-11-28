
# apl-source:1
# مثال 1366 — حذف الحروف المكررة
# apl-source:2
# Remove duplicate letters smallest order
# apl-source:3
# Demonstrates: مكدس أحادي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1366-remove-duplicate-letters.apl
# apl-source:6

# apl-source:7
# نسجل آخر ظهور لكل حرف
# apl-source:8
# ونستخدم مكدساً نخرج منه الأكبر إن كان سيأتي لاحقاً
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
def احذف_المكرر(نص_):
  # apl-source:19
  اخير = {}
  # apl-source:20
  for ع in range(len(نص_)):
    # apl-source:21
    اخير[نص_[ع]] = ع
  # apl-source:22
  موجود = {}
  # apl-source:23
  مكدس = []
  # apl-source:24
  for ع in range(len(نص_)):
    # apl-source:25
    ح = نص_[ع]
    # apl-source:26
    if not موجود.get(ح, False):
      # apl-source:27
      while (len(مكدس) > 0) and (مكدس[len(مكدس) - 1] > ح) and (اخير[مكدس[len(مكدس) - 1]] > ع):
        # apl-source:28
        موجود[مكدس.pop()] = False
      # apl-source:29
      مكدس = مكدس + [ح]
      # apl-source:30
      موجود[ح] = True
  # apl-source:31
  ناتج = ""
  # apl-source:32
  for ح in مكدس:
    # apl-source:33
    ناتج = ناتج + ح
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
تأكد_يساوي(احذف_المكرر("bcabc"), "abc", "مثال أول")
# apl-source:37
تأكد_يساوي(احذف_المكرر("cbacdcbc"), "acdb", "مثال ثان")
# apl-source:38
تأكد_يساوي(احذف_المكرر("a"), "a", "حرف")
# apl-source:39
