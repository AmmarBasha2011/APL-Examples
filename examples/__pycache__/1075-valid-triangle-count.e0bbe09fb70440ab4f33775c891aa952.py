
# apl-source:1
# مثال 1075 — عدد المثلثات الصالحة
# apl-source:2
# Valid triangle number
# apl-source:3
# Demonstrates: ترتيب ومؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1075-valid-triangle-count.apl
# apl-source:6

# apl-source:7
# بعد الترتيب يكفي أن يتجاوز مجموع الضلعين الأصغرين الأكبر
# apl-source:8
# نثبت الأكبر ونعد الأزواج بمؤشرين
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
def عدد_مثلثات(اضلاع):
  # apl-source:19
  ق = sorted(اضلاع)
  # apl-source:20
  عدد_ = 0
  # apl-source:21
  for ك in range(len(ق) - 1, 1, -1):
    # apl-source:22
    ي = 0
    # apl-source:23
    ل = ك - 1
    # apl-source:24
    while ي < ل:
      # apl-source:25
      if (ق[ي] + ق[ل]) > ق[ك]:
        # apl-source:26
        عدد_ = عدد_ + (ل - ي)
        # apl-source:27
        ل = ل - 1
      # apl-source:28
      else:
        # apl-source:29
        ي = ي + 1
  # apl-source:30
  return عدد_
# apl-source:31

# apl-source:32
تأكد_يساوي(عدد_مثلثات([2, 2, 3, 4]), 3, "ثلاثة")
# apl-source:33
تأكد_يساوي(عدد_مثلثات([4, 2, 3, 4]), 4, "أربعة")
# apl-source:34
تأكد_يساوي(عدد_مثلثات([1, 1, 3]), 0, "لا مثلث")
# apl-source:35
