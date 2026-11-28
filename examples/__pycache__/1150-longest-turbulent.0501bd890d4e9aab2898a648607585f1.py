
# apl-source:1
# مثال 1150 — أطول تذبذب
# apl-source:2
# Longest turbulent subarray
# apl-source:3
# Demonstrates: مسح واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1150-longest-turbulent.apl
# apl-source:6

# apl-source:7
# نتتبع طول التذبذب الحالي
# apl-source:8
# ونعيد العدّ عند تساوي جارين
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
def اطول_تذبذب(أ):
  # apl-source:19
  if len(أ) < 2:
    # apl-source:20
    return len(أ)
  # apl-source:21
  اطول = 1
  # apl-source:22
  حالي = 1
  # apl-source:23
  سابق = 0
  # apl-source:24
  for ع in range(1, len(أ)):
    # apl-source:25
    if أ[ع] > أ[ع - 1]:
      # apl-source:26
      اتجاه = 1
    # apl-source:27
    elif أ[ع] < أ[ع - 1]:
      # apl-source:28
      اتجاه = -1
    # apl-source:29
    else:
      # apl-source:30
      اتجاه = 0
    # apl-source:31
    if اتجاه == 0:
      # apl-source:32
      حالي = 1
    # apl-source:33
    elif اتجاه == -سابق:
      # apl-source:34
      حالي = حالي + 1
    # apl-source:35
    else:
      # apl-source:36
      حالي = 2
    # apl-source:37
    سابق = اتجاه
    # apl-source:38
    if حالي > اطول:
      # apl-source:39
      اطول = حالي
  # apl-source:40
  return اطول
# apl-source:41

# apl-source:42
تأكد_يساوي(اطول_تذبذب([9,4,2,10,7,8,8,1,9]), 5, "مثال أول")
# apl-source:43
تأكد_يساوي(اطول_تذبذب([4,8,12,16]), 2, "تصاعدي")
# apl-source:44
تأكد_يساوي(اطول_تذبذب([100]), 1, "عنصر")
# apl-source:45
تأكد_يساوي(اطول_تذبذب([9,9]), 1, "متساويان")
# apl-source:46
