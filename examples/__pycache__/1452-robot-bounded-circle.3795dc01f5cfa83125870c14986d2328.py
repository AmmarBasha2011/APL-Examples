
# apl-source:1
# مثال 1452 — روبوت يدور في دائرة
# apl-source:2
# Robot bounded in a circle
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1452-robot-bounded-circle.apl
# apl-source:6

# apl-source:7
# نكرر التعليمات أربع مرات
# apl-source:8
# إذا عاد للأصل فهو محدود
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
def محدود(تعليمات):
  # apl-source:19
  س = 0
  # apl-source:20
  ص = 0
  # apl-source:21
  اتجاه = 0
  # apl-source:22
  حركة = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  # apl-source:23
  for مرة in range(4):
    # apl-source:24
    for ح in تعليمات:
      # apl-source:25
      if ح == "G":
        # apl-source:26
        س = س + حركة[اتجاه][0]
        # apl-source:27
        ص = ص + حركة[اتجاه][1]
      # apl-source:28
      elif ح == "L":
        # apl-source:29
        اتجاه = (اتجاه + 3) % 4
      # apl-source:30
      elif ح == "R":
        # apl-source:31
        اتجاه = (اتجاه + 1) % 4
  # apl-source:32
  return س == 0 and ص == 0
# apl-source:33

# apl-source:34
تأكد_يساوي(محدود("GGLLGG"), True, "يعود")
# apl-source:35
تأكد_يساوي(محدود("GG"), False, "مستقيم")
# apl-source:36
تأكد_يساوي(محدود("GL"), True, "مربع")
# apl-source:37
