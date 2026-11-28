
# apl-source:1
# مثال 924 — ضغط LZ77
# apl-source:2
# LZ77 compression
# apl-source:3
# Demonstrates: مراجع مسافة وطول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/924-lz77.apl
# apl-source:6

# apl-source:7
# ضغط LZ77: استبدال التكرارات بمراجع (مسافة، طول) للخلف
# apl-source:8
# أساس خوارزميات ZIP و gzip
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
def اضغط(سلسلة, نافذة, نظرة):
  # apl-source:19
  رموز = []
  # apl-source:20
  i = 0
  # apl-source:21
  ن = len(سلسلة)
  # apl-source:22
  while i < ن:
    # apl-source:23
    أفضل_مسافة = 0
    # apl-source:24
    أفضل_طول = 0
    # apl-source:25
    بداية = i - نافذة
    # apl-source:26
    if بداية < 0:
      # apl-source:27
      بداية = 0
    # apl-source:28
    for ج in range(بداية, i):
      # apl-source:29
      طول_مطابق = 0
      # apl-source:30
      while طول_مطابق < نظرة and i + طول_مطابق < ن and سلسلة[ج + طول_مطابق] == سلسلة[i + طول_مطابق]:
        # apl-source:31
        طول_مطابق = طول_مطابق + 1
      # apl-source:32
      if طول_مطابق > أفضل_طول:
        # apl-source:33
        أفضل_مسافة = i - ج
        # apl-source:34
        أفضل_طول = طول_مطابق
    # apl-source:35
    if أفضل_طول >= 2:
      # apl-source:36
      تالي = ""
      # apl-source:37
      if i + أفضل_طول < ن:
        # apl-source:38
        تالي = سلسلة[i + أفضل_طول]
      # apl-source:39
      رموز = رموز + [[أفضل_مسافة, أفضل_طول, تالي]]
      # apl-source:40
      i = i + أفضل_طول + 1
    # apl-source:41
    else:
      # apl-source:42
      رموز = رموز + [[0, 0, سلسلة[i]]]
      # apl-source:43
      i = i + 1
  # apl-source:44
  return رموز
# apl-source:45

# apl-source:46
def فك(رموز):
  # apl-source:47
  خرج = ""
  # apl-source:48
  for رمز in رموز:
    # apl-source:49
    if رمز[1] >= 2:
      # apl-source:50
      بداية = len(خرج) - رمز[0]
      # apl-source:51
      for i in range(رمز[1]):
        # apl-source:52
        خرج = خرج + خرج[بداية + i]
    # apl-source:53
    if رمز[2] != "":
      # apl-source:54
      خرج = خرج + رمز[2]
  # apl-source:55
  return خرج
# apl-source:56

# apl-source:57
رموز = اضغط("abracadabra", 8, 4)
# apl-source:58
print("الرموز:", رموز)
# apl-source:59
مفكوك = فك(رموز)
# apl-source:60
print("المفكوك:", مفكوك)
# apl-source:61

# apl-source:62
تأكد_يساوي(مفكوك, "abracadabra", "الفك يعيد الأصل")
# apl-source:63
# آخر رمز مرجع بطول 4 ومسافة 7 (abra الأخيرة)
# apl-source:64
آخر = رموز[len(رموز) - 1]
# apl-source:65
تأكد_يساوي(آخر[0], 7, "المسافة 7")
# apl-source:66
تأكد_يساوي(آخر[1], 4, "الطول 4")
# apl-source:67

# apl-source:68
# نص متكرر يضغط جيداً
# apl-source:69
مكرر = "abcabcabcabc"
# apl-source:70
رموز2 = اضغط(مكرر, 8, 4)
# apl-source:71
تأكد_يساوي(فك(رموز2), مكرر, "فك المتكرر")
# apl-source:72
if len(رموز2) >= len(مكرر):
  # apl-source:73
  print("فشل: لم يحدث ضغط")
  # apl-source:74
  قياسي_نظام_اخرج(1)
# apl-source:75
print("ناجح: ضغط المتكرر إلى", len(رموز2), "رموز")
# apl-source:76
