
# apl-source:1
# مثال 1145 — ترتيب متذبذب
# apl-source:2
# Wiggle sort
# apl-source:3
# Demonstrates: مسح واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1145-wiggle-sort.apl
# apl-source:6

# apl-source:7
# نتأكد في كل موضع من اتجاه المقارنة
# apl-source:8
# ونبدل الجارين لو خالفا الاتجاه
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
def تذبذب(أ):
  # apl-source:19
  ق = list(أ)
  # apl-source:20
  for ع in range(1, len(ق)):
    # apl-source:21
    if ع % 2 == 1:
      # apl-source:22
      if ق[ع] < ق[ع - 1]:
        # apl-source:23
        ت = ق[ع]
        # apl-source:24
        ق[ع] = ق[ع - 1]
        # apl-source:25
        ق[ع - 1] = ت
    # apl-source:26
    else:
      # apl-source:27
      if ق[ع] > ق[ع - 1]:
        # apl-source:28
        ت = ق[ع]
        # apl-source:29
        ق[ع] = ق[ع - 1]
        # apl-source:30
        ق[ع - 1] = ت
  # apl-source:31
  return ق
# apl-source:32

# apl-source:33
def متذبذبة(ق):
  # apl-source:34
  for ع in range(1, len(ق)):
    # apl-source:35
    if ع % 2 == 1:
      # apl-source:36
      if ق[ع] < ق[ع - 1]:
        # apl-source:37
        return False
    # apl-source:38
    else:
      # apl-source:39
      if ق[ع] > ق[ع - 1]:
        # apl-source:40
        return False
  # apl-source:41
  return True
# apl-source:42

# apl-source:43
for عينة in [[3,5,2,1,6,4], [1,2,3,4,5], [5,4,3,2,1], [1,1,1]]:
  # apl-source:44
  تأكد_يساوي(متذبذبة(تذبذب(عينة)), True, "عينة " + str(عينة))
# apl-source:45
تأكد_يساوي(تذبذب([1,2]), [1,2], "اثنان")
# apl-source:46
