
# apl-source:1
# مثال 1858 — ثاني أصغر قيمة مختلفة
# apl-source:2
# Second smallest distinct value
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1858-second-smallest-distinct-value.apl
# apl-source:6

# apl-source:7
# نحدث الأصغر والثاني
# apl-source:8
# التكرار لا يحسب
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
def ثاني_أصغر(ق):
  # apl-source:19
  أول = 1000000
  # apl-source:20
  ثان = 1000000
  # apl-source:21
  for ع in ق:
    # apl-source:22
    if ع < أول:
      # apl-source:23
      ثان = أول
      # apl-source:24
      أول = ع
    # apl-source:25
    elif ع < ثان and ع != أول:
      # apl-source:26
      ثان = ع
  # apl-source:27
  return ثان
# apl-source:28

# apl-source:29
تأكد_يساوي(ثاني_أصغر([4, 2, 2, 7, 3]), 3, "تكرار")
# apl-source:30
تأكد_يساوي(ثاني_أصغر([9, 1]), 9, "اثنان")
# apl-source:31
تأكد_يساوي(ثاني_أصغر([5, 4, 3, 2, 1]), 2, "هابطة")
# apl-source:32
