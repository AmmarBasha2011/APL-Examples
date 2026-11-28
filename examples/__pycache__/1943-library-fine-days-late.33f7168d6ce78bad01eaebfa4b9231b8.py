
# apl-source:1
# مثال 1943 — غرامة تأخير كتب المكتبة
# apl-source:2
# Library late fine
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1943-library-fine-days-late.apl
# apl-source:6

# apl-source:7
# # نحسب الأيام المتأخرة بعد فترة السماح
# apl-source:8
# # ونحدد الغرامة لكل كتاب بسقف 20
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
def غرامة(ايام_التأخر):
  # apl-source:19
  فعلي = ايام_التأخر - 3
  # apl-source:20
  if فعلي <= 0:
    # apl-source:21
    return 0
  # apl-source:22
  return min(فعلي * 2, 20)
# apl-source:23

# apl-source:24
def مجموع_الغرامات(قائمة):
  # apl-source:25
  مج = 0
  # apl-source:26
  for ع in قائمة:
    # apl-source:27
    مج = مج + غرامة(ع)
  # apl-source:28
  return مج
# apl-source:29

# apl-source:30
تأكد_يساوي(غرامة(2), 0, "ضمن السماح")
# apl-source:31
تأكد_يساوي(غرامة(5), 4, "يومان")
# apl-source:32
تأكد_يساوي(غرامة(30), 20, "سقف")
# apl-source:33
تأكد_يساوي(مجموع_الغرامات([0, 4, 10, 50]), 36, "مجموع")
# apl-source:34
