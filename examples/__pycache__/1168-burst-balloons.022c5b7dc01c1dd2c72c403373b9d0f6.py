
# apl-source:1
# مثال 1168 — انفجار البالونات
# apl-source:2
# Burst balloons maximum coins
# apl-source:3
# Demonstrates: برمجة ديناميكية بمجالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1168-burst-balloons.apl
# apl-source:6

# apl-source:7
# نختار آخر بالون يُفجَّر في كل مجال
# apl-source:8
# فتكون حدوده معروفة ومستقلة
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
def اقصى_عملات(ب):
  # apl-source:19
  أ = [1] + ب + [1]
  # apl-source:20
  ن = len(أ)
  # apl-source:21
  د = []
  # apl-source:22
  for ع in range(ن):
    # apl-source:23
    د = د + [[0] * ن]
  # apl-source:24
  for مدى in range(2, ن):
    # apl-source:25
    for يسار in range(ن - مدى):
      # apl-source:26
      يمين = يسار + مدى
      # apl-source:27
      for ك in range(يسار + 1, يمين):
        # apl-source:28
        قيمة = أ[يسار] * أ[ك] * أ[يمين] + د[يسار][ك] + د[ك][يمين]
        # apl-source:29
        if قيمة > د[يسار][يمين]:
          # apl-source:30
          د[يسار][يمين] = قيمة
  # apl-source:31
  return د[0][ن - 1]
# apl-source:32

# apl-source:33
تأكد_يساوي(اقصى_عملات([3,1,5,8]), 167, "مثال أول")
# apl-source:34
تأكد_يساوي(اقصى_عملات([1,5]), 10, "اثنان")
# apl-source:35
تأكد_يساوي(اقصى_عملات([7]), 7, "واحد")
# apl-source:36
تأكد_يساوي(اقصى_عملات([]), 0, "فارغة")
# apl-source:37
