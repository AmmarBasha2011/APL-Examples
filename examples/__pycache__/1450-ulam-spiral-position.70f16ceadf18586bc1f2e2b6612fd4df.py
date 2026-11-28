
# apl-source:1
# مثال 1450 — موضع لولب أولام
# apl-source:2
# Position of n in square spiral
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1450-ulam-spiral-position.apl
# apl-source:6

# apl-source:7
# نتحرك يميناً ثم لأعلى ثم يساراً ثم لأسفل
# apl-source:8
# طول الضلع يزيد كل ضلعين
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
def موضع(ن):
  # apl-source:19
  س = 0
  # apl-source:20
  ص = 0
  # apl-source:21
  اتجاهات = [[1,0],[0,1],[-1,0],[0,-1]]
  # apl-source:22
  اتجاه = 0
  # apl-source:23
  ضلع = 1
  # apl-source:24
  حالي = 1
  # apl-source:25
  while حالي < ن:
    # apl-source:26
    for خطوة in range(ضلع):
      # apl-source:27
      if حالي < ن:
        # apl-source:28
        س = س + اتجاهات[اتجاه][0]
        # apl-source:29
        ص = ص + اتجاهات[اتجاه][1]
        # apl-source:30
        حالي = حالي + 1
    # apl-source:31
    اتجاه = (اتجاه + 1) % 4
    # apl-source:32
    if اتجاه % 2 == 0:
      # apl-source:33
      ضلع = ضلع + 1
  # apl-source:34
  return [س, ص]
# apl-source:35

# apl-source:36
تأكد_يساوي(موضع(1), [0, 0], "الأصل")
# apl-source:37
تأكد_يساوي(موضع(5), [-1, 1], "خمسة")
# apl-source:38
تأكد_يساوي(موضع(9), [1, -1], "تسعة")
# apl-source:39
تأكد_يساوي(موضع(10), [2, -1], "عشرة")
# apl-source:40
