
# apl-source:1
# مثال 1500 — نتيجة الشوط في التنس
# apl-source:2
# Tennis game score
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1500-tennis-game-score.apl
# apl-source:6

# apl-source:7
# النقاط تعلن 15 و30 و40
# apl-source:8
# التعادل والأفضلية بعد الأربعين
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
def نتيجة_الشوط(أ, ب):
  # apl-source:19
  أسماء = ["0", "15", "30", "40"]
  # apl-source:20
  if أ >= 4 and أ - ب >= 2:
    # apl-source:21
    return "فوز اللاعب الأول"
  # apl-source:22
  if ب >= 4 and ب - أ >= 2:
    # apl-source:23
    return "فوز اللاعب الثاني"
  # apl-source:24
  if أ >= 3 and ب >= 3:
    # apl-source:25
    if أ == ب:
      # apl-source:26
      return "تعادل"
    # apl-source:27
    if أ > ب:
      # apl-source:28
      return "أفضلية الأول"
    # apl-source:29
    return "أفضلية الثاني"
  # apl-source:30
  return أسماء[أ] + "-" + أسماء[ب]
# apl-source:31

# apl-source:32
تأكد_يساوي(نتيجة_الشوط(2, 1), "30-15", "عادي")
# apl-source:33
تأكد_يساوي(نتيجة_الشوط(3, 3), "تعادل", "تعادل")
# apl-source:34
تأكد_يساوي(نتيجة_الشوط(4, 3), "أفضلية الأول", "أفضلية")
# apl-source:35
تأكد_يساوي(نتيجة_الشوط(2, 4), "فوز اللاعب الثاني", "فوز")
# apl-source:36
