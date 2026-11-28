
# apl-source:1
# مثال 1969 — نتيجة لعبة تنس من النقاط
# apl-source:2
# Tennis game score from points
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1969-tennis-game-score-from-points.apl
# apl-source:6

# apl-source:7
# # إذا وصل اللاعبان إلى 3 نقاط فأكثر نطبق قاعدة التعادل
# apl-source:8
# # الفوز يحتاج فارق نقطتين
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
def نتيجة(ا, ب):
  # apl-source:19
  اسماء = ["0", "15", "30", "40"]
  # apl-source:20
  if ا >= 3 and ب >= 3:
    # apl-source:21
    if ا == ب:
      # apl-source:22
      return "Deuce"
    # apl-source:23
    if abs(ا - ب) >= 2:
      # apl-source:24
      if ا > ب:
        # apl-source:25
        return "Game A"
      # apl-source:26
      return "Game B"
    # apl-source:27
    if ا > ب:
      # apl-source:28
      return "Advantage A"
    # apl-source:29
    return "Advantage B"
  # apl-source:30
  if ا >= 4:
    # apl-source:31
    return "Game A"
  # apl-source:32
  if ب >= 4:
    # apl-source:33
    return "Game B"
  # apl-source:34
  return اسماء[ا] + "-" + اسماء[ب]
# apl-source:35

# apl-source:36
تأكد_يساوي(نتيجة(0, 0), "0-0", "بداية")
# apl-source:37
تأكد_يساوي(نتيجة(2, 1), "30-15", "عادي")
# apl-source:38
تأكد_يساوي(نتيجة(3, 3), "Deuce", "تعادل")
# apl-source:39
تأكد_يساوي(نتيجة(4, 3), "Advantage A", "أفضلية")
# apl-source:40
تأكد_يساوي(نتيجة(3, 5), "Game B", "فوز بعد تعادل")
# apl-source:41
تأكد_يساوي(نتيجة(4, 1), "Game A", "فوز سريع")
# apl-source:42
