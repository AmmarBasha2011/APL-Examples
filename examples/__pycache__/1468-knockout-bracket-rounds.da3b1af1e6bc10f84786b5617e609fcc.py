
# apl-source:1
# مثال 1468 — جولات خروج المغلوب
# apl-source:2
# Knockout tournament rounds
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1468-knockout-bracket-rounds.apl
# apl-source:6

# apl-source:7
# كل مباراة تُخرج فريقاً واحداً
# apl-source:8
# الفرد الزائد يمر بلا لعب
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
def تفاصيل_البطولة(فرق):
  # apl-source:19
  جولات = 0
  # apl-source:20
  مباريات = 0
  # apl-source:21
  while فرق > 1:
    # apl-source:22
    مباريات = مباريات + فرق // 2
    # apl-source:23
    فرق = فرق // 2 + فرق % 2
    # apl-source:24
    جولات = جولات + 1
  # apl-source:25
  return [جولات, مباريات]
# apl-source:26

# apl-source:27
تأكد_يساوي(تفاصيل_البطولة(8), [3, 7], "ثمانية")
# apl-source:28
تأكد_يساوي(تفاصيل_البطولة(5), [3, 4], "خمسة")
# apl-source:29
تأكد_يساوي(تفاصيل_البطولة(1), [0, 0], "فريق وحيد")
# apl-source:30
تأكد_يساوي(تفاصيل_البطولة(16), [4, 15], "ستة عشر")
# apl-source:31
