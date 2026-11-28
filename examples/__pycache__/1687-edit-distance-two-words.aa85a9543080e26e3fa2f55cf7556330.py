
# apl-source:1
# مثال 1687 — مسافة التحرير بين كلمتين
# apl-source:2
# Edit distance between two words
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1687-edit-distance-two-words.apl
# apl-source:6

# apl-source:7
# جدول من البادئات
# apl-source:8
# نأخذ أقل كلفة من الثلاث عمليات
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
def مسافة_تحرير(أ, ب):
  # apl-source:19
  ن = len(أ)
  # apl-source:20
  م = len(ب)
  # apl-source:21
  جدول = []
  # apl-source:22
  for ي in range(ن + 1):
    # apl-source:23
    صف = []
    # apl-source:24
    for ك in range(م + 1):
      # apl-source:25
      صف.append(0)
    # apl-source:26
    جدول.append(صف)
  # apl-source:27
  for ي in range(ن + 1):
    # apl-source:28
    جدول[ي][0] = ي
  # apl-source:29
  for ك in range(م + 1):
    # apl-source:30
    جدول[0][ك] = ك
  # apl-source:31
  for ي in range(1, ن + 1):
    # apl-source:32
    for ك in range(1, م + 1):
      # apl-source:33
      كلفة = 1
      # apl-source:34
      if أ[ي - 1] == ب[ك - 1]:
        # apl-source:35
        كلفة = 0
      # apl-source:36
      جدول[ي][ك] = min(min(جدول[ي - 1][ك] + 1, جدول[ي][ك - 1] + 1), جدول[ي - 1][ك - 1] + كلفة)
  # apl-source:37
  return جدول[ن][م]
# apl-source:38

# apl-source:39
تأكد_يساوي(مسافة_تحرير("kitten", "sitting"), 3, "كلاسيكي")
# apl-source:40
تأكد_يساوي(مسافة_تحرير("abc", "abc"), 0, "متطابقتان")
# apl-source:41
تأكد_يساوي(مسافة_تحرير("", "abc"), 3, "فارغة")
# apl-source:42
