
# apl-source:1
# مثال 1737 — عدد الكلمات في فيز بز
# apl-source:2
# FizzBuzz counts
# apl-source:3
# Demonstrates: منطق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1737-fizz-buzz-count-range.apl
# apl-source:6

# apl-source:7
# مضاعفات الثلاثة والخمسة والاثنين معاً
# apl-source:8
# نصنف كل عدد
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
def عد_فيز(ن):
  # apl-source:19
  فيز = 0
  # apl-source:20
  بز = 0
  # apl-source:21
  كلاهما = 0
  # apl-source:22
  for ك in range(1, ن + 1):
    # apl-source:23
    if ك % 15 == 0:
      # apl-source:24
      كلاهما = كلاهما + 1
    # apl-source:25
    elif ك % 3 == 0:
      # apl-source:26
      فيز = فيز + 1
    # apl-source:27
    elif ك % 5 == 0:
      # apl-source:28
      بز = بز + 1
  # apl-source:29
  return [فيز, بز, كلاهما]
# apl-source:30

# apl-source:31
تأكد_يساوي(عد_فيز(15), [4, 2, 1], "خمسة عشر")
# apl-source:32
تأكد_يساوي(عد_فيز(2), [0, 0, 0], "اثنان")
# apl-source:33
تأكد_يساوي(عد_فيز(30), [8, 4, 2], "ثلاثون")
# apl-source:34
