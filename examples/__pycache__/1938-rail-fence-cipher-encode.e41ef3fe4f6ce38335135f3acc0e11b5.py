
# apl-source:1
# مثال 1938 — تشفير سياج السكة
# apl-source:2
# Rail fence cipher encode
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1938-rail-fence-cipher-encode.apl
# apl-source:6

# apl-source:7
# نتحرك للأسفل ثم للأعلى بين الصفوف
# apl-source:8
# نقرأ الصفوف بالترتيب
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
def سياج(س, ن):
  # apl-source:19
  صفوف = []
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    صفوف = صفوف + [""]
  # apl-source:22
  ي = 0
  # apl-source:23
  اتجاه = 1
  # apl-source:24
  for ح in س:
    # apl-source:25
    صفوف[ي] = صفوف[ي] + ح
    # apl-source:26
    if ي == 0:
      # apl-source:27
      اتجاه = 1
    # apl-source:28
    if ي == ن - 1:
      # apl-source:29
      اتجاه = -1
    # apl-source:30
    ي = ي + اتجاه
  # apl-source:31
  خرج = ""
  # apl-source:32
  for ص in صفوف:
    # apl-source:33
    خرج = خرج + ص
  # apl-source:34
  return خرج
# apl-source:35

# apl-source:36
تأكد_يساوي(سياج("wearediscovered", 3), "wecrerdsoeeaivd", "ثلاثة صفوف")
# apl-source:37
تأكد_يساوي(سياج("abcd", 2), "acbd", "صفان")
# apl-source:38
