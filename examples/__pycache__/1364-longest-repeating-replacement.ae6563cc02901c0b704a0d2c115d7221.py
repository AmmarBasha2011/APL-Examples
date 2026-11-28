
# apl-source:1
# مثال 1364 — أطول تكرار باستبدال
# apl-source:2
# Longest repeating character replacement
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1364-longest-repeating-replacement.apl
# apl-source:6

# apl-source:7
# النافذة صالحة إذا كان الباقي بعد أكثر حرف تكراراً أقل من ك أو يساويه
# apl-source:8
# نوسعها ونضيقها
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
def اطول_تكرار(نص_, ك):
  # apl-source:19
  عدّ = {}
  # apl-source:20
  يسار = 0
  # apl-source:21
  اكثر = 0
  # apl-source:22
  اقصى = 0
  # apl-source:23
  for يمين in range(len(نص_)):
    # apl-source:24
    ح = نص_[يمين]
    # apl-source:25
    عدّ[ح] = عدّ.get(ح, 0) + 1
    # apl-source:26
    if عدّ[ح] > اكثر:
      # apl-source:27
      اكثر = عدّ[ح]
    # apl-source:28
    if (يمين - يسار + 1) - اكثر > ك:
      # apl-source:29
      عدّ[نص_[يسار]] = عدّ[نص_[يسار]] - 1
      # apl-source:30
      يسار = يسار + 1
    # apl-source:31
    if يمين - يسار + 1 > اقصى:
      # apl-source:32
      اقصى = يمين - يسار + 1
  # apl-source:33
  return اقصى
# apl-source:34

# apl-source:35
تأكد_يساوي(اطول_تكرار("ABAB", 2), 4, "أربعة")
# apl-source:36
تأكد_يساوي(اطول_تكرار("AABABBA", 1), 4, "أربعة ثانية")
# apl-source:37
تأكد_يساوي(اطول_تكرار("A", 0), 1, "حرف")
# apl-source:38
