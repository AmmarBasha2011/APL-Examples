
# apl-source:1
# مثال 1308 — تركيبات الهاتف
# apl-source:2
# Phone letter combinations count
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1308-letter-combinations-count.apl
# apl-source:6

# apl-source:7
# كل رقم له حروف
# apl-source:8
# نبني التركيبات بحلقات تراكمية
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
def تركيبات(ارقام):
  # apl-source:19
  if ارقام == "":
    # apl-source:20
    return []
  # apl-source:21
  خريطة = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
  # apl-source:22
  ناتج = [""]
  # apl-source:23
  for ر in ارقام:
    # apl-source:24
    جديد = []
    # apl-source:25
    for ق in ناتج:
      # apl-source:26
      for ح in خريطة[ر]:
        # apl-source:27
        جديد = جديد + [ق + ح]
    # apl-source:28
    ناتج = جديد
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(تركيبات("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"], "اثنان وثلاثة")
# apl-source:32
تأكد_يساوي(تركيبات(""), [], "فارغة")
# apl-source:33
تأكد_يساوي(تركيبات("2"), ["a","b","c"], "رقم واحد")
# apl-source:34
تأكد_يساوي(len(تركيبات("79")), 16, "سبعة وتسعة")
# apl-source:35
