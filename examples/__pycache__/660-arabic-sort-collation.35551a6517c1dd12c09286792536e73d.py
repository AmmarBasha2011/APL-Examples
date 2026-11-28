
# apl-source:1
# مثال 660 — ترتيب عربي هجائي
# apl-source:2
# Arabic collation sort
# apl-source:3
# Demonstrates: ترتيب هجائي، مفاتيح حروف، ألف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/660-arabic-sort-collation.apl
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
# ترتيب عربي أبجدي
# apl-source:25
# Demonstrates: خريطة ترتيب الحروف, مفاتيح مقارنة عددية, معالجة الألف
# apl-source:26
# يرتب الأسماء بالترتيب الهجائي العربي لا بالترميز
# apl-source:27

# apl-source:28
ترتيب_حروف = "اأإآبتثجحخدذرزسشصضطظعغفقكلمنهوي"
# apl-source:29
def رتبة(حرف):
  # apl-source:30
  for ي in range(len(ترتيب_حروف)):
    # apl-source:31
    if ترتيب_حروف[ي] == حرف:
      # apl-source:32
      return ي // 1
  # apl-source:33
  return 100
# apl-source:34

# apl-source:35
def مفتاح(كلمة):
  # apl-source:36
  م = []
  # apl-source:37
  for حرف in كلمة:
    # apl-source:38
    م.append(رتبة(حرف))
  # apl-source:39
  while len(م) < 12:
    # apl-source:40
    م.append(100)
  # apl-source:41
  return م
# apl-source:42

# apl-source:43
أسماء = ["زيد", "أحمد", "محمد", "خالد", "بشير", "إياد", "حسن"]
# apl-source:44
مزودة = []
# apl-source:45
for اسم in أسماء:
  # apl-source:46
  مزودة.append([مفتاح(اسم), اسم])
# apl-source:47
مزودة.sort()
# apl-source:48
نتيجة = []
# apl-source:49
for زوج in مزودة:
  # apl-source:50
  نتيجة.append(زوج[1])
# apl-source:51
تأكد_يساوي(نتيجة, ["أحمد", "إياد", "بشير", "حسن", "خالد", "زيد", "محمد"], "الترتيب الهجائي")
# apl-source:52
print("مرتبة:", نتيجة)
# apl-source:53
