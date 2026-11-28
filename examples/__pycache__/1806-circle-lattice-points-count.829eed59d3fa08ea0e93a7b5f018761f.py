
# apl-source:1
# مثال 1806 — النقاط الصحيحة داخل دائرة
# apl-source:2
# Lattice points inside a circle
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1806-circle-lattice-points-count.apl
# apl-source:6

# apl-source:7
# x² + y² ≤ r²
# apl-source:8
# نمر على المربع المحيط
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
def نقاط_صحيحة(نق):
  # apl-source:19
  عد = 0
  # apl-source:20
  for س in range(-نق, نق + 1):
    # apl-source:21
    for ص in range(-نق, نق + 1):
      # apl-source:22
      if س * س + ص * ص <= نق * نق:
        # apl-source:23
        عد = عد + 1
  # apl-source:24
  return عد
# apl-source:25

# apl-source:26
تأكد_يساوي(نقاط_صحيحة(0), 1, "نقطة")
# apl-source:27
تأكد_يساوي(نقاط_صحيحة(1), 5, "واحد")
# apl-source:28
تأكد_يساوي(نقاط_صحيحة(2), 13, "اثنان")
# apl-source:29
تأكد_يساوي(نقاط_صحيحة(5), 81, "خمسة")
# apl-source:30
