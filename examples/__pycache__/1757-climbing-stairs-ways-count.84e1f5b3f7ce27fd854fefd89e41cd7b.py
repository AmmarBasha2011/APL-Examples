
# apl-source:1
# مثال 1757 — طرق صعود الدرج
# apl-source:2
# Climbing stairs ways
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1757-climbing-stairs-ways-count.apl
# apl-source:6

# apl-source:7
# الطرق إلى ن = طرق ن-1 + ن-2
# apl-source:8
# نحتفظ بآخر قيمتين
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
def طرق_الدرج(ن):
  # apl-source:19
  أ = 1
  # apl-source:20
  ب = 1
  # apl-source:21
  for ك in range(ن - 1):
    # apl-source:22
    ت = أ + ب
    # apl-source:23
    أ = ب
    # apl-source:24
    ب = ت
  # apl-source:25
  return ب
# apl-source:26

# apl-source:27
تأكد_يساوي(طرق_الدرج(1), 1, "درجة")
# apl-source:28
تأكد_يساوي(طرق_الدرج(2), 2, "درجتان")
# apl-source:29
تأكد_يساوي(طرق_الدرج(5), 8, "خمس")
# apl-source:30
تأكد_يساوي(طرق_الدرج(10), 89, "عشر")
# apl-source:31
