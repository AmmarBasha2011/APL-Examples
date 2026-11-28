
# apl-source:1
# مثال 1281 — ثلاثية متزايدة
# apl-source:2
# Increasing triplet subsequence
# apl-source:3
# Demonstrates: مسح واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1281-longest-increasing-triplet.apl
# apl-source:6

# apl-source:7
# نحتفظ بأصغر قيمتين رأيناهما
# apl-source:8
# وأي عنصر يتجاوزهما يكمل الثلاثية
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
def ثلاثية(أ):
  # apl-source:19
  اول = 1000000000
  # apl-source:20
  ثان = 1000000000
  # apl-source:21
  for س in أ:
    # apl-source:22
    if س <= اول:
      # apl-source:23
      اول = س
    # apl-source:24
    elif س <= ثان:
      # apl-source:25
      ثان = س
    # apl-source:26
    else:
      # apl-source:27
      return True
  # apl-source:28
  return False
# apl-source:29

# apl-source:30
تأكد_يساوي(ثلاثية([1,2,3,4,5]), True, "تصاعدي")
# apl-source:31
تأكد_يساوي(ثلاثية([5,4,3,2,1]), False, "تنازلي")
# apl-source:32
تأكد_يساوي(ثلاثية([2,1,5,0,4,6]), True, "متقطعة")
# apl-source:33
تأكد_يساوي(ثلاثية([1,1,1]), False, "متساوية")
# apl-source:34
