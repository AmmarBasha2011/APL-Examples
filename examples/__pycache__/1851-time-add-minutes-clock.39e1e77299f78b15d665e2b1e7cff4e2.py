
# apl-source:1
# مثال 1851 — إضافة دقائق إلى الوقت
# apl-source:2
# Add minutes to clock time
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1851-time-add-minutes-clock.apl
# apl-source:6

# apl-source:7
# نحول الوقت إلى دقائق
# apl-source:8
# نعيد التحويل بمقياس يوم كامل
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
def أضف_دقائق(س, د, زيادة):
  # apl-source:19
  كل = (س * 60 + د + زيادة) % 1440
  # apl-source:20
  return [كل // 60, كل % 60]
# apl-source:21

# apl-source:22
تأكد_يساوي(أضف_دقائق(10, 30, 45), [11, 15], "عادي")
# apl-source:23
تأكد_يساوي(أضف_دقائق(23, 50, 20), [0, 10], "منتصف الليل")
# apl-source:24
تأكد_يساوي(أضف_دقائق(0, 0, 1440), [0, 0], "يوم كامل")
# apl-source:25
