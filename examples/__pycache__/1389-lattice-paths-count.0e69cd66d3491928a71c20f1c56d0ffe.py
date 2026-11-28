
# apl-source:1
# مثال 1389 — مسارات الشبكة
# apl-source:2
# Lattice paths count
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1389-lattice-paths-count.apl
# apl-source:6

# apl-source:7
# العدد هو معامل ثنائي C(2n, n)
# apl-source:8
# نحسبه بضرب وقسمة تدريجية
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
def مسارات(ن):
  # apl-source:19
  ر = 1
  # apl-source:20
  for ع in range(1, ن + 1):
    # apl-source:21
    ر = ر * (ن + ع) // ع
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(مسارات(1), 2, "واحد")
# apl-source:25
تأكد_يساوي(مسارات(2), 6, "اثنان")
# apl-source:26
تأكد_يساوي(مسارات(20), 137846528820, "عشرون")
# apl-source:27
