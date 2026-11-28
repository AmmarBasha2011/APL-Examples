
# apl-source:1
# مثال 1268 — حلزون ملء
# apl-source:2
# Generate spiral matrix
# apl-source:3
# Demonstrates: حدود أربعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1268-spiral-matrix-two.apl
# apl-source:6

# apl-source:7
# نملأ الضلع العلوي ثم الأيمن ثم السفلي ثم الأيسر
# apl-source:8
# ونضيق الحدود بعد كل ضلع
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
def املأ_حلزونيا(ن):
  # apl-source:19
  م = []
  # apl-source:20
  for ع in range(ن):
    # apl-source:21
    م = م + [[0] * ن]
  # apl-source:22
  أعلى = 0
  # apl-source:23
  أسفل = ن - 1
  # apl-source:24
  يسار = 0
  # apl-source:25
  يمين = ن - 1
  # apl-source:26
  ق = 1
  # apl-source:27
  while (أعلى <= أسفل) and (يسار <= يمين):
    # apl-source:28
    for ج in range(يسار, يمين + 1):
      # apl-source:29
      م[أعلى][ج] = ق
      # apl-source:30
      ق = ق + 1
    # apl-source:31
    أعلى = أعلى + 1
    # apl-source:32
    for ص in range(أعلى, أسفل + 1):
      # apl-source:33
      م[ص][يمين] = ق
      # apl-source:34
      ق = ق + 1
    # apl-source:35
    يمين = يمين - 1
    # apl-source:36
    if أعلى <= أسفل:
      # apl-source:37
      for ج in range(يمين, يسار - 1, -1):
        # apl-source:38
        م[أسفل][ج] = ق
        # apl-source:39
        ق = ق + 1
      # apl-source:40
      أسفل = أسفل - 1
    # apl-source:41
    if يسار <= يمين:
      # apl-source:42
      for ص in range(أسفل, أعلى - 1, -1):
        # apl-source:43
        م[ص][يسار] = ق
        # apl-source:44
        ق = ق + 1
      # apl-source:45
      يسار = يسار + 1
  # apl-source:46
  return م
# apl-source:47

# apl-source:48
تأكد_يساوي(املأ_حلزونيا(3), [[1,2,3],[8,9,4],[7,6,5]], "ثلاثة")
# apl-source:49
تأكد_يساوي(املأ_حلزونيا(1), [[1]], "واحد")
# apl-source:50
تأكد_يساوي(املأ_حلزونيا(4), [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]], "أربعة")
# apl-source:51
