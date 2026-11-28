
# apl-source:1
# مثال 1572 — أقل عدد أرصفة
# apl-source:2
# Minimum platforms for trains
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1572-minimum-platforms-needed.apl
# apl-source:6

# apl-source:7
# نرتب الوصول والمغادرة
# apl-source:8
# نتحرك بمؤشرين ونتتبع القمة
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
def أرصفة(وصول, مغادرة):
  # apl-source:19
  وص = []
  # apl-source:20
  مغ = []
  # apl-source:21
  for ع in وصول:
    # apl-source:22
    وص.append(ع)
  # apl-source:23
  for ع in مغادرة:
    # apl-source:24
    مغ.append(ع)
  # apl-source:25
  وص.sort()
  # apl-source:26
  مغ.sort()
  # apl-source:27
  ي = 0
  # apl-source:28
  ج = 0
  # apl-source:29
  حالي = 0
  # apl-source:30
  أقصى = 0
  # apl-source:31
  while ي < len(وص):
    # apl-source:32
    if وص[ي] <= مغ[ج]:
      # apl-source:33
      حالي = حالي + 1
      # apl-source:34
      ي = ي + 1
      # apl-source:35
      if حالي > أقصى:
        # apl-source:36
        أقصى = حالي
    # apl-source:37
    else:
      # apl-source:38
      حالي = حالي - 1
      # apl-source:39
      ج = ج + 1
  # apl-source:40
  return أقصى
# apl-source:41

# apl-source:42
تأكد_يساوي(أرصفة([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]), 3, "ثلاثة")
# apl-source:43
تأكد_يساوي(أرصفة([100, 300], [200, 400]), 1, "بلا تزامن")
# apl-source:44
