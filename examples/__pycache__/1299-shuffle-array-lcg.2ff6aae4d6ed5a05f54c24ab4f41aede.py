
# apl-source:1
# مثال 1299 — خلط قائمة
# apl-source:2
# Shuffle with linear congruential generator
# apl-source:3
# Demonstrates: مولد خطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1299-shuffle-array-lcg.apl
# apl-source:6

# apl-source:7
# مولد خطي يعطي أرقاماً ثابتة من نفس البذرة
# apl-source:8
# فيتكرر الخلط نفسه
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
class مولد:
  # apl-source:19
  def __init__(ذات, بذرة):
    # apl-source:20
    ذات.ح = بذرة
# apl-source:21

  # apl-source:22
  def تالي(ذات):
    # apl-source:23
    ذات.ح = (ذات.ح * 1103515245 + 12345) % 2147483648
    # apl-source:24
    return ذات.ح
# apl-source:25

# apl-source:26
def اخلط(أ, بذرة):
  # apl-source:27
  ق = list(أ)
  # apl-source:28
  م = مولد(بذرة)
  # apl-source:29
  for ع in range(len(ق) - 1, 0, -1):
    # apl-source:30
    ج = م.تالي() % (ع + 1)
    # apl-source:31
    ت = ق[ع]
    # apl-source:32
    ق[ع] = ق[ج]
    # apl-source:33
    ق[ج] = ت
  # apl-source:34
  return ق
# apl-source:35

# apl-source:36
اصل = [1, 2, 3, 4, 5, 6]
# apl-source:37
ا = اخلط(اصل, 42)
# apl-source:38
تأكد_يساوي(sorted(ا), اصل, "نفس العناصر")
# apl-source:39
تأكد_يساوي(اخلط(اصل, 42), ا, "نفس البذرة نفس الخلط")
# apl-source:40
تأكد_يساوي(اصل, [1, 2, 3, 4, 5, 6], "الأصل لم يتغير")
# apl-source:41
