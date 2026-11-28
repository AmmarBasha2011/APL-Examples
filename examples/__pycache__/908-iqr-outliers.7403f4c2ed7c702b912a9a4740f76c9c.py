
# apl-source:1
# مثال 908 — كشف الشاذة بالربيعيات
# apl-source:2
# IQR outliers
# apl-source:3
# Demonstrates: سياج مرة ونصف من المدى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/908-iqr-outliers.apl
# apl-source:6

# apl-source:7
# كشف القيم الشاذة بسياج المدى الربيعي (IQR)
# apl-source:8
# شاذة إن خرجت عن [ر1 - 1.5*IQR, ر3 + 1.5*IQR]
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
def رتّب(قيم):
  # apl-source:19
  م = []
  # apl-source:20
  for x in قيم:
    # apl-source:21
    م = م + [x]
  # apl-source:22
  ن = len(م)
  # apl-source:23
  for i in range(ن):
    # apl-source:24
    for ج in range(i + 1, ن):
      # apl-source:25
      if م[ج] < م[i]:
        # apl-source:26
        مؤقت = م[i]
        # apl-source:27
        م[i] = م[ج]
        # apl-source:28
        م[ج] = مؤقت
  # apl-source:29
  return م
# apl-source:30

# apl-source:31
def وسيط(مرتبة):
  # apl-source:32
  ن = len(مرتبة)
  # apl-source:33
  if ن % 2 == 1:
    # apl-source:34
    return مرتبة[ن // 2]
  # apl-source:35
  return (مرتبة[ن // 2 - 1] + مرتبة[ن // 2]) / 2
# apl-source:36

# apl-source:37
def ربيعيات(قيم):
  # apl-source:38
  م = رتّب(قيم)
  # apl-source:39
  ن = len(م)
  # apl-source:40
  if ن % 2 == 0:
    # apl-source:41
    نصف = ن // 2
    # apl-source:42
    سفلى = م[:نصف]
    # apl-source:43
    عليا = م[نصف:]
  # apl-source:44
  else:
    # apl-source:45
    نصف = ن // 2
    # apl-source:46
    سفلى = م[:نصف]
    # apl-source:47
    عليا = م[نصف + 1:]
  # apl-source:48
  return [وسيط(سفلى), وسيط(م), وسيط(عليا)]
# apl-source:49

# apl-source:50
def شاذة(قيم):
  # apl-source:51
  ر = ربيعيات(قيم)
  # apl-source:52
  مدى = ر[2] - ر[0]
  # apl-source:53
  أدنى = ر[0] - 1.5 * مدى
  # apl-source:54
  أعلى = ر[2] + 1.5 * مدى
  # apl-source:55
  نتيجة = []
  # apl-source:56
  for x in قيم:
    # apl-source:57
    if (x < أدنى) or (x > أعلى):
      # apl-source:58
      نتيجة = نتيجة + [x]
  # apl-source:59
  return نتيجة
# apl-source:60

# apl-source:61
قيم = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# apl-source:62
ر = ربيعيات(قيم)
# apl-source:63
print("الربيعيات:", ر)
# apl-source:64
print("الشاذة:", شاذة(قيم))
# apl-source:65

# apl-source:66
تأكد_يساوي(ر[0], 3, "الربيع الأول")
# apl-source:67
تأكد_يساوي(ر[1], 5.5, "الوسيط")
# apl-source:68
تأكد_يساوي(ر[2], 8, "الربيع الثالث")
# apl-source:69

# apl-source:70
ش = شاذة(قيم)
# apl-source:71
تأكد_يساوي(len(ش), 1, "قيمة شاذة واحدة")
# apl-source:72
تأكد_يساوي(ش[0], 100, "المئة هي الشاذة")
# apl-source:73

# apl-source:74
# بلا شاذة في بيانات متقاربة
# apl-source:75
تأكد_يساوي(len(شاذة([10, 11, 12, 13, 14])), 0, "لا شاذة")
# apl-source:76
