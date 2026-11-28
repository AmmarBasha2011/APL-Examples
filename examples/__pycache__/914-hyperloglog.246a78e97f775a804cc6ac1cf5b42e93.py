
# apl-source:1
# مثال 914 — تقدير المميزة الاحتمالي
# apl-source:2
# HyperLogLog
# apl-source:3
# Demonstrates: بادئات أصفار التجزئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/914-hyperloglog.apl
# apl-source:6

# apl-source:7
# HyperLogLog: تقدير عدد العناصر المميزة بذاكرة صغيرة ثابتة
# apl-source:8
# يعتمد على أطوال بادئات الأصفار في التجزئة
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
ماسك = 4294967295
# apl-source:19

# apl-source:20
# تجزئة 32-بت حتمية (تضاعيف ونشر)
# apl-source:21
def تجزئة(س):
  # apl-source:22
  س = (س * 2654435761) % 4294967296
  # apl-source:23
  س = (س ^ (س >> 16)) % 4294967296
  # apl-source:24
  س = (س * 2246822519) % 4294967296
  # apl-source:25
  س = (س ^ (س >> 13)) % 4294967296
  # apl-source:26
  return س
# apl-source:27

# apl-source:28
def تقدير_مميزة(قيم, بت):
  # apl-source:29
  عدد_سجلات = 2 ** بت
  # apl-source:30
  سجلات = []
  # apl-source:31
  for _ in range(عدد_سجلات):
    # apl-source:32
    سجلات = سجلات + [0]
  # apl-source:33
  for v in قيم:
    # apl-source:34
    س = تجزئة(v)
    # apl-source:35
    مؤشر = س >> (32 - بت)
    # apl-source:36
    باقي = (س * (2 ** بت)) % 4294967296
    # apl-source:37
    رو = 1
    # apl-source:38
    while (باقي & (2147483648)) == 0 and رو <= 32 - بت:
      # apl-source:39
      رو = رو + 1
      # apl-source:40
      باقي = (باقي * 2) % 4294967296
    # apl-source:41
    if رو > سجلات[مؤشر]:
      # apl-source:42
      سجلات[مؤشر] = رو
  # apl-source:43
  مجموع = 0
  # apl-source:44
  for r in سجلات:
    # apl-source:45
    مجموع = مجموع + 0.5 ** r
  # apl-source:46
  return int(0.673 * عدد_سجلات * عدد_سجلات / مجموع)
# apl-source:47

# apl-source:48
قيم = []
# apl-source:49
for i in range(100):
  # apl-source:50
  قيم = قيم + [i]
# apl-source:51
تقدير = تقدير_مميزة(قيم, 4)
# apl-source:52
print("التقدير لـ 100 عنصر:", تقدير)
# apl-source:53

# apl-source:54
# التقدير قريب من المئة (خوارزمية احتمالية: نتسامح بهامش)
# apl-source:55
if تقدير < 85:
  # apl-source:56
  print("فشل: التقدير منخفض جداً", تقدير)
  # apl-source:57
  قياسي_نظام_اخرج(1)
# apl-source:58
if تقدير > 120:
  # apl-source:59
  print("فشل: التقدير مرتفع جداً", تقدير)
  # apl-source:60
  قياسي_نظام_اخرج(1)
# apl-source:61
print("ناجح: التقدير ضمن الهامش")
# apl-source:62

# apl-source:63
# التكرارات لا تغيّر التقدير
# apl-source:64
مكررة = []
# apl-source:65
for i in range(50):
  # apl-source:66
  مكررة = مكررة + [i]
  # apl-source:67
  مكررة = مكررة + [i]
  # apl-source:68
  مكررة = مكررة + [i]
# apl-source:69
تقدير2 = تقدير_مميزة(مكررة, 4)
# apl-source:70
print("التقدير لـ 50 مميزاً مكررة:", تقدير2)
# apl-source:71
if تقدير2 < 40:
  # apl-source:72
  print("فشل: تقدير المكررة منخفض", تقدير2)
  # apl-source:73
  قياسي_نظام_اخرج(1)
# apl-source:74
if تقدير2 > 80:
  # apl-source:75
  print("فشل: تقدير المكررة مرتفع", تقدير2)
  # apl-source:76
  قياسي_نظام_اخرج(1)
# apl-source:77
print("ناجح: التكرار لا يؤثر")
# apl-source:78
# حتمية: نفس الدخل يعطي نفس التقدير تماماً
# apl-source:79
تأكد_يساوي(تقدير_مميزة(مكررة, 4), تقدير2, "حتمية التقدير")
# apl-source:80
