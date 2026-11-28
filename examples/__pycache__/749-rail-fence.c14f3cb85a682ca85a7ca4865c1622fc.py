
# apl-source:1
# مثال 749 — تشفير السياج
# apl-source:2
# Rail fence cipher
# apl-source:3
# Demonstrates: مسار متعرج، قضبان، اتجاه متقلب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/749-rail-fence.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# تشفير السياج (Rail Fence): نص على قضبان متعرجة
# apl-source:25
# Demonstrates: مسار متعرج, قضبان نصية, اتجاه يتقلب
# apl-source:26
# الحروف تُوزع صعوداً ونزولاً بين القضبان ثم تُقرأ قضيباً قضيباً
# apl-source:27

# apl-source:28
def شفر_سياج(نص, قضبان):
  # apl-source:29
  if قضبان <= 1:
    # apl-source:30
    return نص
  # apl-source:31
  صفوف = []
  # apl-source:32
  for ي in range(قضبان):
    # apl-source:33
    صفوف.append("")
  # apl-source:34
  صف = 0
  # apl-source:35
  اتجاه = 1
  # apl-source:36
  for ي in range(len(نص)):
    # apl-source:37
    صفوف[صف] = صفوف[صف] + نص[ي]
    # apl-source:38
    if صف == 0:
      # apl-source:39
      اتجاه = 1
    # apl-source:40
    elif صف == قضبان - 1:
      # apl-source:41
      اتجاه = -1
    # apl-source:42
    صف = صف + اتجاه
  # apl-source:43
  ناتج = ""
  # apl-source:44
  for سطر in صفوف:
    # apl-source:45
    ناتج = ناتج + سطر
  # apl-source:46
  return ناتج
# apl-source:47

# apl-source:48
تأكد_يساوي(شفر_سياج("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN", "المتجه الكلاسيكي")
# apl-source:49
تأكد_يساوي(شفر_سياج("HELLOWORLD", 2), "HLOOLELWRD", "قضيبان")
# apl-source:50
تأكد_يساوي(شفر_سياج("ABCDE", 1), "ABCDE", "قضيب واحد لا يغير")
# apl-source:51
تأكد_يساوي(len(شفر_سياج("ABCDEFGHIJKLM", 4)), 13, "الطول محفوظ")
# apl-source:52
تأكد_يساوي(شفر_سياج("", 3), "", "نص فارغ")
# apl-source:53

# apl-source:54
print("السياج:", شفر_سياج("WEAREDISCOVEREDFLEEATONCE", 3))
# apl-source:55
