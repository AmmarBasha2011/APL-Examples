
# apl-source:1
# مثال 1846 — ثلاثيات مجموعها صفر
# apl-source:2
# Count triplets summing to zero
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1846-three-sum-zero-count.apl
# apl-source:6

# apl-source:7
# نرتب القائمة
# apl-source:8
# نتجاوز المكرر
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
def ثلاثيات(ق):
  # apl-source:19
  ق = ق + []
  # apl-source:20
  ق.sort()
  # apl-source:21
  عد = 0
  # apl-source:22
  for ي in range(len(ق) - 2):
    # apl-source:23
    if ي == 0 or ق[ي] != ق[ي - 1]:
      # apl-source:24
      ك = ي + 1
      # apl-source:25
      ج = len(ق) - 1
      # apl-source:26
      while ك < ج:
        # apl-source:27
        مجموع = ق[ي] + ق[ك] + ق[ج]
        # apl-source:28
        if مجموع == 0:
          # apl-source:29
          عد = عد + 1
          # apl-source:30
          ك = ك + 1
          # apl-source:31
          while ك < ج and ق[ك] == ق[ك - 1]:
            # apl-source:32
            ك = ك + 1
        # apl-source:33
        elif مجموع < 0:
          # apl-source:34
          ك = ك + 1
        # apl-source:35
        else:
          # apl-source:36
          ج = ج - 1
  # apl-source:37
  return عد
# apl-source:38

# apl-source:39
تأكد_يساوي(ثلاثيات([-1, 0, 1, 2, -1, -4]), 2, "اثنان")
# apl-source:40
تأكد_يساوي(ثلاثيات([0, 0, 0]), 1, "أصفار")
# apl-source:41
تأكد_يساوي(ثلاثيات([1, 2, 3]), 0, "لا يوجد")
# apl-source:42
