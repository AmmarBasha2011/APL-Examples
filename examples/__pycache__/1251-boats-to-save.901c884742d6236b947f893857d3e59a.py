
# apl-source:1
# مثال 1251 — قوارب النجاة
# apl-source:2
# Boats to save people
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1251-boats-to-save.apl
# apl-source:6

# apl-source:7
# نرتب الأوزان ونجمع أثقل شخص بأخف شخص
# apl-source:8
# لو لم يتسعا يركب الأثقل وحده
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
def قوارب(اوزان, حد):
  # apl-source:19
  ق = sorted(اوزان)
  # apl-source:20
  ي = 0
  # apl-source:21
  ن = len(ق) - 1
  # apl-source:22
  ع = 0
  # apl-source:23
  while ي <= ن:
    # apl-source:24
    if ق[ي] + ق[ن] <= حد:
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    ن = ن - 1
    # apl-source:27
    ع = ع + 1
  # apl-source:28
  return ع
# apl-source:29

# apl-source:30
تأكد_يساوي(قوارب([1,2], 3), 1, "قارب")
# apl-source:31
تأكد_يساوي(قوارب([3,2,2,1], 3), 3, "ثلاثة")
# apl-source:32
تأكد_يساوي(قوارب([3,5,3,4], 5), 4, "أربعة")
# apl-source:33
تأكد_يساوي(قوارب([], 5), 0, "فارغة")
# apl-source:34
