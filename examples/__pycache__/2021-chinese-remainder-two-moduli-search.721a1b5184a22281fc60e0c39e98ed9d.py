
# apl-source:1
# مثال 2021 — مبرهنة الباقي الصينية لمقياسين
# apl-source:2
# Chinese remainder two moduli
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2021-chinese-remainder-two-moduli-search.apl
# apl-source:6

# apl-source:7
# # الحل الأصغر يقع بين 0 وm1*m2
# apl-source:8
# # إن لم نجد فلا حل
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
def باقي_صيني(ا1, م1, ا2, م2):
  # apl-source:19
  for س in range(م1 * م2):
    # apl-source:20
    if س % م1 == ا1 and س % م2 == ا2:
      # apl-source:21
      return س
  # apl-source:22
  return -1
# apl-source:23

# apl-source:24
تأكد_يساوي(باقي_صيني(2, 3, 3, 5), 8, "٣ و٥")
# apl-source:25
تأكد_يساوي(باقي_صيني(1, 4, 2, 9), 29, "٤ و٩")
# apl-source:26
تأكد_يساوي(باقي_صيني(0, 2, 1, 4), -1, "بلا حل")
# apl-source:27
