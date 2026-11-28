
# apl-source:1
# مثال 840 — جاوس-جوردان
# apl-source:2
# Gauss-Jordan
# apl-source:3
# Demonstrates: اختزال كامل للصفوف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/840-gauss-jordan.apl
# apl-source:6

# apl-source:7
# حذف جاوس-جوردان: حل نظام معادلات خطية بالاختزال الكامل للصفوف
# apl-source:8
# 2س + ص = 5 ، س + 3ص = 5  =>  س = 2 ، ص = 1
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
def حل_نظام(معاملات, ثوابت):
  # apl-source:19
  ن = len(معاملات)
  # apl-source:20
  # مصفوفة مزدادة
  # apl-source:21
  م = []
  # apl-source:22
  for i in range(ن):
    # apl-source:23
    صف = []
    # apl-source:24
    for ج in range(ن):
      # apl-source:25
      صف = صف + [معاملات[i][ج]]
    # apl-source:26
    صف = صف + [ثوابت[i]]
    # apl-source:27
    م = م + [صف]
  # apl-source:28
  for عمود in range(ن):
    # apl-source:29
    محور = م[عمود][عمود]
    # apl-source:30
    for ج in range(ن + 1):
      # apl-source:31
      م[عمود][ج] = م[عمود][ج] / محور
    # apl-source:32
    for i in range(ن):
      # apl-source:33
      if i != عمود:
        # apl-source:34
        عامل = م[i][عمود]
        # apl-source:35
        for ج in range(ن + 1):
          # apl-source:36
          م[i][ج] = م[i][ج] - عامل * م[عمود][ج]
  # apl-source:37
  حل = []
  # apl-source:38
  for i in range(ن):
    # apl-source:39
    حل = حل + [م[i][ن]]
  # apl-source:40
  return حل
# apl-source:41

# apl-source:42
حل = حل_نظام(
  # apl-source:43
  [
    # apl-source:44
    [2.0, 1.0],
    # apl-source:45
    [1.0, 3.0]
  # apl-source:46
  ],
  # apl-source:47
  [5.0, 5.0]
# apl-source:48
)
# apl-source:49
print("الحل =", حل)
# apl-source:50

# apl-source:51
تأكد_يساوي(حل[0], 2.0, "س = 2")
# apl-source:52
تأكد_يساوي(حل[1], 1.0, "ص = 1")
# apl-source:53

# apl-source:54
# نظام 3 متغيرات: س+ص+ع=6 ، س-ص+ع=2 ، 2س+ص-ع=1
# apl-source:55
حل3 = حل_نظام(
  # apl-source:56
  [
    # apl-source:57
    [1.0, 1.0, 1.0],
    # apl-source:58
    [1.0, -1.0, 1.0],
    # apl-source:59
    [2.0, 1.0, -1.0]
  # apl-source:60
  ],
  # apl-source:61
  [6.0, 2.0, 1.0]
# apl-source:62
)
# apl-source:63
print("الحل الثلاثي =", حل3)
# apl-source:64
تأكد_يساوي(round(حل3[0], 9), 1.0, "س = 1")
# apl-source:65
تأكد_يساوي(round(حل3[1], 9), 2.0, "ص = 2")
# apl-source:66
تأكد_يساوي(round(حل3[2], 9), 3.0, "ع = 3")
# apl-source:67
