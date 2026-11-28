
# apl-source:1
# مثال 1239 — مقارنة الإصدارات
# apl-source:2
# Compare version numbers
# apl-source:3
# Demonstrates: تقسيم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1239-compare-versions.apl
# apl-source:6

# apl-source:7
# نقسم على النقاط ونقارن رقماً رقماً
# apl-source:8
# والناقص يعامل كصفر
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
def قارن(أ, ب):
  # apl-source:19
  س = أ.split(".")
  # apl-source:20
  ص = ب.split(".")
  # apl-source:21
  ن = max(len(س), len(ص))
  # apl-source:22
  for ع in range(ن):
    # apl-source:23
    ق1 = 0
    # apl-source:24
    ق2 = 0
    # apl-source:25
    if ع < len(س):
      # apl-source:26
      ق1 = int(س[ع])
    # apl-source:27
    if ع < len(ص):
      # apl-source:28
      ق2 = int(ص[ع])
    # apl-source:29
    if ق1 < ق2:
      # apl-source:30
      return -1
    # apl-source:31
    if ق1 > ق2:
      # apl-source:32
      return 1
  # apl-source:33
  return 0
# apl-source:34

# apl-source:35
تأكد_يساوي(قارن("1.01", "1.001"), 0, "أصفار بادئة")
# apl-source:36
تأكد_يساوي(قارن("1.0", "1.0.0"), 0, "ناقص")
# apl-source:37
تأكد_يساوي(قارن("0.1", "1.1"), -1, "أصغر")
# apl-source:38
تأكد_يساوي(قارن("1.2.10", "1.2.9"), 1, "عشرة أكبر من تسعة")
# apl-source:39
