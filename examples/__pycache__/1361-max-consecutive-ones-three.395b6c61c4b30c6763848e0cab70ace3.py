
# apl-source:1
# مثال 1361 — آحاد متتالية مع قلب
# apl-source:2
# Max consecutive ones with k flips
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1361-max-consecutive-ones-three.apl
# apl-source:6

# apl-source:7
# نوسع النافذة ونعد الأصفار داخلها
# apl-source:8
# نضيق من اليسار عند تجاوز الحد
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
def اطول_آحاد(ب, ك):
  # apl-source:19
  يسار = 0
  # apl-source:20
  اصفار = 0
  # apl-source:21
  اقصى = 0
  # apl-source:22
  for يمين in range(len(ب)):
    # apl-source:23
    if ب[يمين] == 0:
      # apl-source:24
      اصفار = اصفار + 1
    # apl-source:25
    while اصفار > ك:
      # apl-source:26
      if ب[يسار] == 0:
        # apl-source:27
        اصفار = اصفار - 1
      # apl-source:28
      يسار = يسار + 1
    # apl-source:29
    if يمين - يسار + 1 > اقصى:
      # apl-source:30
      اقصى = يمين - يسار + 1
  # apl-source:31
  return اقصى
# apl-source:32

# apl-source:33
تأكد_يساوي(اطول_آحاد([1,1,1,0,0,0,1,1,1,1,0], 2), 6, "ستة")
# apl-source:34
تأكد_يساوي(اطول_آحاد([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10, "عشرة")
# apl-source:35
تأكد_يساوي(اطول_آحاد([0,0], 0), 0, "أصفار فقط")
# apl-source:36
