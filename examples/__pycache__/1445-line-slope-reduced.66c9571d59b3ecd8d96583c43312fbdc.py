
# apl-source:1
# مثال 1445 — ميل الخط مختزلاً
# apl-source:2
# Reduced slope of line through two points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1445-line-slope-reduced.apl
# apl-source:6

# apl-source:7
# نقسم الفرقين على قاسمهما المشترك
# apl-source:8
# ونجعل المقام موجباً
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
def قاسم(أ, ب):
  # apl-source:19
  if أ < 0:
    # apl-source:20
    أ = -أ
  # apl-source:21
  if ب < 0:
    # apl-source:22
    ب = -ب
  # apl-source:23
  while ب != 0:
    # apl-source:24
    ت = أ % ب
    # apl-source:25
    أ = ب
    # apl-source:26
    ب = ت
  # apl-source:27
  return أ
# apl-source:28

# apl-source:29
def ميل(أ, ب):
  # apl-source:30
  فس = ب[0] - أ[0]
  # apl-source:31
  فص = ب[1] - أ[1]
  # apl-source:32
  if فس == 0:
    # apl-source:33
    return "vertical"
  # apl-source:34
  ق = قاسم(فس, فص)
  # apl-source:35
  فس = فس // ق
  # apl-source:36
  فص = فص // ق
  # apl-source:37
  if فس < 0:
    # apl-source:38
    فس = -فس
    # apl-source:39
    فص = -فص
  # apl-source:40
  return [فص, فس]
# apl-source:41

# apl-source:42
تأكد_يساوي(ميل([0,0], [2,4]), [2, 1], "ميل اثنين")
# apl-source:43
تأكد_يساوي(ميل([0,0], [2,-4]), [-2, 1], "ميل سالب")
# apl-source:44
تأكد_يساوي(ميل([1,1], [1,5]), "vertical", "رأسي")
# apl-source:45
تأكد_يساوي(ميل([0,0], [6,3]), [1, 2], "نصف")
# apl-source:46
