
# apl-source:1
# مثال 1085 — لغز إبريقي الماء
# apl-source:2
# Water and jug problem
# apl-source:3
# Demonstrates: القاسم المشترك الأكبر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1085-water-jug.apl
# apl-source:6

# apl-source:7
# الكميات الممكنة هي مضاعفات القاسم المشترك الأكبر للسعتين
# apl-source:8
# بشرط ألا تتجاوز مجموع السعتين
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
def ق_م(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    ت = أ % ب
    # apl-source:21
    أ = ب
    # apl-source:22
    ب = ت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def يمكن_قياس(س, ص, ز):
  # apl-source:26
  if ز > (س + ص):
    # apl-source:27
    return False
  # apl-source:28
  if ز == 0:
    # apl-source:29
    return True
  # apl-source:30
  return (ز % ق_م(س, ص)) == 0
# apl-source:31

# apl-source:32
تأكد_يساوي(يمكن_قياس(3, 5, 4), True, "3 و5 إلى 4")
# apl-source:33
تأكد_يساوي(يمكن_قياس(2, 6, 5), False, "2 و6 إلى 5")
# apl-source:34
تأكد_يساوي(يمكن_قياس(1, 2, 3), True, "1 و2 إلى 3")
# apl-source:35
تأكد_يساوي(يمكن_قياس(2, 6, 9), False, "أكبر من المجموع")
# apl-source:36
