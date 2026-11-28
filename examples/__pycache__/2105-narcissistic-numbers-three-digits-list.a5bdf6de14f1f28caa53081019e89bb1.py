
# apl-source:1
# مثال 2105 — الأعداد النرجسية ذات ثلاثة أرقام
# apl-source:2
# Three digit narcissistic numbers
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2105-narcissistic-numbers-three-digits-list.apl
# apl-source:6

# apl-source:7
# # نفحص من 100 إلى 999
# apl-source:8
# # 153 مثال شهير
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
def نرجسي(ن):
  # apl-source:19
  مج = 0
  # apl-source:20
  for ر in str(ن):
    # apl-source:21
    مج = مج + int(ر) ** 3
  # apl-source:22
  return مج == ن
# apl-source:23

# apl-source:24
ق = []
# apl-source:25
for ن in range(100, 1000):
  # apl-source:26
  if نرجسي(ن):
    # apl-source:27
    ق = ق + [ن]
# apl-source:28
تأكد_يساوي(ق, [153, 370, 371, 407], "الأربعة")
# apl-source:29
