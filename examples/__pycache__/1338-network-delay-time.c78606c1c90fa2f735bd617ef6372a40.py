import time
# apl-source:1
# مثال 1338 — زمن تأخر الشبكة
# apl-source:2
# Network delay time
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1338-network-delay-time.apl
# apl-source:6

# apl-source:7
# نحسب أقصر زمن لكل عقدة بخوارزمية بيلمان فورد
# apl-source:8
# الجواب أكبر زمن بينها
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
def تأخر_الشبكة(حواف, ن, بداية):
  # apl-source:19
  كبير = 1000000000
  # apl-source:20
  زمن = [كبير] * (ن + 1)
  # apl-source:21
  زمن[بداية] = 0
  # apl-source:22
  for جولة in range(ن):
    # apl-source:23
    for ح in حواف:
      # apl-source:24
      if زمن[ح[0]] + ح[2] < زمن[ح[1]]:
        # apl-source:25
        زمن[ح[1]] = زمن[ح[0]] + ح[2]
  # apl-source:26
  اقصى = 0
  # apl-source:27
  for ع in range(1, ن + 1):
    # apl-source:28
    if زمن[ع] > اقصى:
      # apl-source:29
      اقصى = زمن[ع]
  # apl-source:30
  if اقصى == كبير:
    # apl-source:31
    return -1
  # apl-source:32
  return اقصى
# apl-source:33

# apl-source:34
تأكد_يساوي(تأخر_الشبكة([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2, "مثال أول")
# apl-source:35
تأكد_يساوي(تأخر_الشبكة([[1,2,1]], 2, 1), 1, "عقدتان")
# apl-source:36
تأكد_يساوي(تأخر_الشبكة([[1,2,1]], 2, 2), -1, "لا يصل")
# apl-source:37
