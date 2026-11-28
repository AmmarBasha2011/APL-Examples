
# apl-source:1
# مثال 1252 — توزيع الكعك
# apl-source:2
# Assign cookies
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1252-assign-cookies.apl
# apl-source:6

# apl-source:7
# نعطي أصغر كعكة تكفي أقل طفل شرهاً
# apl-source:8
# ونتقدم في القائمتين المرتبتين
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
def ارضِ(اطفال, كعك):
  # apl-source:19
  ا = sorted(اطفال)
  # apl-source:20
  ك = sorted(كعك)
  # apl-source:21
  ي = 0
  # apl-source:22
  for حجم in ك:
    # apl-source:23
    if (ي < len(ا)) and (ا[ي] <= حجم):
      # apl-source:24
      ي = ي + 1
  # apl-source:25
  return ي
# apl-source:26

# apl-source:27
تأكد_يساوي(ارضِ([1,2,3], [1,1]), 1, "طفل واحد")
# apl-source:28
تأكد_يساوي(ارضِ([1,2], [1,2,3]), 2, "اثنان")
# apl-source:29
تأكد_يساوي(ارضِ([10,9,8], [1,2]), 0, "لا أحد")
# apl-source:30
