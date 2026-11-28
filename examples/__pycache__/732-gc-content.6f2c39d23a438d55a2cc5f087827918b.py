
# apl-source:1
# مثال 732 — نسبة GC
# apl-source:2
# GC content
# apl-source:3
# Demonstrates: نوافذ منزلقة، نسب مئوية، أغنى نافذة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/732-gc-content.apl
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
# نسبة GC في تسلسل DNA ونوافذها المنزلقة
# apl-source:25
# Demonstrates: عد شرطي, نسبة مئوية, نافذة منزلقة
# apl-source:26
# الجينات تميل لمناطق غنية بـGC
# apl-source:27

# apl-source:28
def نسبة_gc(سلسلة):
  # apl-source:29
  عدد = 0
  # apl-source:30
  for ي in range(len(سلسلة)):
    # apl-source:31
    if سلسلة[ي] == "G" or سلسلة[ي] == "C":
      # apl-source:32
      عدد = عدد + 1
  # apl-source:33
  return عدد * 100.0 / len(سلسلة)
# apl-source:34

# apl-source:35
def نوافذ(سلسلة, عرض):
  # apl-source:36
  ناتج = []
  # apl-source:37
  for بداية in range(len(سلسلة) - عرض + 1):
    # apl-source:38
    ناتج.append(نسبة_gc(سلسلة[بداية:بداية + عرض]))
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
def أغنى_نافذة(سلسلة, عرض):
  # apl-source:42
  قيم = نوافذ(سلسلة, عرض)
  # apl-source:43
  أفضل = 0
  # apl-source:44
  for ي in range(1, len(قيم)):
    # apl-source:45
    if قيم[ي] > قيم[أفضل]:
      # apl-source:46
      أفضل = ي
  # apl-source:47
  return [أفضل, قيم[أفضل]]
# apl-source:48

# apl-source:49
تأكد_يساوي(نسبة_gc("ATGC"), 50.0, "نصف GC")
# apl-source:50
تأكد_يساوي(نسبة_gc("GGCC"), 100.0, "كامل GC")
# apl-source:51
تأكد_يساوي(نسبة_gc("ATAT"), 0.0, "بلا GC")
# apl-source:52
تأكد_يساوي(round(نسبة_gc("ATGCCGTA"), 1), 50.0, "ثمانية قواعد")
# apl-source:53
ن = نوافذ("ATGGCCAT", 4)
# apl-source:54
تأكد_يساوي(len(ن), 5, "خمس نوافذ")
# apl-source:55
تأكد_يساوي(ن[0], 50.0, "أول نافذة")
# apl-source:56
تأكد_يساوي(ن[2], 100.0, "نافذة GGCC كاملة")
# apl-source:57
غ = أغنى_نافذة("ATGGCCAT", 4)
# apl-source:58
تأكد_يساوي(غ, [2, 100.0], "الأغنى عند 2")
# apl-source:59
print("نسبة ATGCCGTA:", نسبة_gc("ATGCCGTA"))
# apl-source:60
