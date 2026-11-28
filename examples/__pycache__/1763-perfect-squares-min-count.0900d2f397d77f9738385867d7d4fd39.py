
# apl-source:1
# مثال 1763 — أقل عدد مربعات كاملة
# apl-source:2
# Minimum perfect squares summing to n
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1763-perfect-squares-min-count.apl
# apl-source:6

# apl-source:7
# جدول لكل مجموع
# apl-source:8
# نجرب كل مربع أصغر
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
def أقل_مربعات(ن):
  # apl-source:19
  جدول = [0]
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    جدول.append(ن)
  # apl-source:22
  for م in range(1, ن + 1):
    # apl-source:23
    ج = 1
    # apl-source:24
    while ج * ج <= م:
      # apl-source:25
      جدول[م] = min(جدول[م], جدول[م - ج * ج] + 1)
      # apl-source:26
      ج = ج + 1
  # apl-source:27
  return جدول[ن]
# apl-source:28

# apl-source:29
تأكد_يساوي(أقل_مربعات(12), 3, "اثنا عشر")
# apl-source:30
تأكد_يساوي(أقل_مربعات(13), 2, "ثلاثة عشر")
# apl-source:31
تأكد_يساوي(أقل_مربعات(1), 1, "واحد")
# apl-source:32
