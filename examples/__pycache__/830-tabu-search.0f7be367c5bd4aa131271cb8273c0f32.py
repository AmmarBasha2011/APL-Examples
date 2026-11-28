
# apl-source:1
# مثال 830 — بحث تابو
# apl-source:2
# Tabu search
# apl-source:3
# Demonstrates: قائمة محرمات، جوار موسع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/830-tabu-search.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# بحث تابو: جوار موسع مع قائمة محرمات قصيرة الذاكرة
# apl-source:25
# Demonstrates: قائمة تابو, قبول أفضل جار غير محرم, خروج من الحلول المحلية
# apl-source:26

# apl-source:27
def هدف(س):
  # apl-source:28
  return (س - 7) * (س - 7)
# apl-source:29

# apl-source:30
def بحث_تابو(بداية, خطوات):
  # apl-source:31
  س = بداية
  # apl-source:32
  أفضل = س
  # apl-source:33
  أفضل_قيمة = هدف(س)
  # apl-source:34
  تابو = [س]
  # apl-source:35
  for خطوة in range(خطوات):
    # apl-source:36
    مرشحون = []
    # apl-source:37
    for جار in [س - 2, س - 1, س + 1, س + 2]:
      # apl-source:38
      if جار >= 0 and جار <= 15 and (جار in تابو) == False:
        # apl-source:39
        مرشحون.append(جار)
    # apl-source:40
    if len(مرشحون) == 0:
      # apl-source:41
      return [أفضل, أفضل_قيمة]
    # apl-source:42
    أقرب = مرشحون[0]
    # apl-source:43
    for جار in مرشحون:
      # apl-source:44
      if هدف(جار) < هدف(أقرب):
        # apl-source:45
        أقرب = جار
    # apl-source:46
    س = أقرب
    # apl-source:47
    if هدف(س) < أفضل_قيمة:
      # apl-source:48
      أفضل = س
      # apl-source:49
      أفضل_قيمة = هدف(س)
    # apl-source:50
    تابو.append(س)
    # apl-source:51
    if len(تابو) > 3:
      # apl-source:52
      تابو.pop(0)
  # apl-source:53
  return [أفضل, أفضل_قيمة]
# apl-source:54

# apl-source:55
تأكد_يساوي(بحث_تابو(5, 10), [7, 0], "الوصول للحل الأمثل")
# apl-source:56
تأكد_يساوي(بحث_تابو(0, 15), [7, 0], "من الطرف البعيد")
# apl-source:57
تأكد_يساوي(بحث_تابو(14, 15), [7, 0], "من الطرف الآخر")
# apl-source:58
تأكد_يساوي(هدف(7), 0, "قيمة الأمثل")
# apl-source:59
