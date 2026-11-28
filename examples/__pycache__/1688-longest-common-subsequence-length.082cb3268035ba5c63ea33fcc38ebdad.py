
# apl-source:1
# مثال 1688 — أطول متتالية جزئية مشتركة
# apl-source:2
# Longest common subsequence length
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1688-longest-common-subsequence-length.apl
# apl-source:6

# apl-source:7
# جدول بطول النصين
# apl-source:8
# نزيد القطر عند التطابق
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
def طول_مشترك(أ, ب):
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
  for ي in range(1, ن + 1):
    # apl-source:28
    for ك in range(1, م + 1):
      # apl-source:29
      if أ[ي - 1] == ب[ك - 1]:
        # apl-source:30
        جدول[ي][ك] = جدول[ي - 1][ك - 1] + 1
      # apl-source:31
      else:
        # apl-source:32
        جدول[ي][ك] = max(جدول[ي - 1][ك], جدول[ي][ك - 1])
  # apl-source:33
  return جدول[ن][م]
# apl-source:34

# apl-source:35
تأكد_يساوي(طول_مشترك("abcde", "ace"), 3, "ثلاثة")
# apl-source:36
تأكد_يساوي(طول_مشترك("abc", "def"), 0, "لا شيء")
# apl-source:37
تأكد_يساوي(طول_مشترك("aaaa", "aa"), 2, "مكررة")
# apl-source:38
