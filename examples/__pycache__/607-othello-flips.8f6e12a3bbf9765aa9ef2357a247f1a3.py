
# apl-source:1
# مثال 607 — قلب أقراص أوتيلو
# apl-source:2
# Othello flips
# apl-source:3
# Demonstrates: أوتيلو، اتجاهات، قلب أقراص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/607-othello-flips.apl
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
# أوتيلو (ريفيرسي): قانونية النقلة وقلب الأقراص
# apl-source:25
# Demonstrates: ثمانية اتجاهات, حصر بين لونين, قلب متسلسل
# apl-source:26
# قرص جديد يقلب كل أقراص الخصم المحصورة
# apl-source:27

# apl-source:28
اتجاهات = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
# apl-source:29

# apl-source:30
def مقلوبة(لوحة, س, ص, لون):
  # apl-source:31
  خصم = "أبيض"
  # apl-source:32
  if لون == "أبيض":
    # apl-source:33
    خصم = "أسود"
  # apl-source:34
  كل_المقلوبة = []
  # apl-source:35
  for اتجاه in اتجاهات:
    # apl-source:36
    سلسلة = []
    # apl-source:37
    أ = س + اتجاه[0]
    # apl-source:38
    ب = ص + اتجاه[1]
    # apl-source:39
    while أ >= 0 and أ < 4 and ب >= 0 and ب < 4 and لوحة[أ][ب] == خصم:
      # apl-source:40
      سلسلة.append([أ, ب])
      # apl-source:41
      أ = أ + اتجاه[0]
      # apl-source:42
      ب = ب + اتجاه[1]
    # apl-source:43
    if len(سلسلة) > 0 and أ >= 0 and أ < 4 and ب >= 0 and ب < 4 and لوحة[أ][ب] == لون:
      # apl-source:44
      for خلية in سلسلة:
        # apl-source:45
        كل_المقلوبة.append(خلية)
  # apl-source:46
  return كل_المقلوبة
# apl-source:47

# apl-source:48
لوحة = [
  # apl-source:49
  ["", "", "", ""],
  # apl-source:50
  ["", "أبيض", "أسود", ""],
  # apl-source:51
  ["", "أسود", "أبيض", ""],
  # apl-source:52
  ["", "", "", ""]
# apl-source:53
]
# apl-source:54
نقلة = مقلوبة(لوحة, 0, 1, "أسود")
# apl-source:55
print("أقراص مقلوبة بالنقلة (0,1):", نقلة)
# apl-source:56
تأكد_يساوي(نقلة, [[1, 1]], "قرص واحد مقلوب عموديا")
# apl-source:57
تأكد_يساوي(len(مقلوبة(لوحة, 0, 0, "أسود")), 0, "نقلة غير قانونية")
# apl-source:58
نقلة2 = مقلوبة(لوحة, 0, 2, "أبيض")
# apl-source:59
تأكد_يساوي(len(نقلة2), 1, "نقلة الأبيض القانونية")
# apl-source:60
