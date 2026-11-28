
# apl-source:1
# مثال 1436 — انعكاس نقطة
# apl-source:2
# Reflect a point across axes
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1436-reflect-point.apl
# apl-source:6

# apl-source:7
# الانعكاس حول س يعكس إشارة ص
# apl-source:8
# وحول القطر يبدل الإحداثيين
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
def اعكس_نقطة(نقطة, محور):
  # apl-source:19
  if محور == "x":
    # apl-source:20
    return [نقطة[0], -نقطة[1]]
  # apl-source:21
  if محور == "y":
    # apl-source:22
    return [-نقطة[0], نقطة[1]]
  # apl-source:23
  return [نقطة[1], نقطة[0]]
# apl-source:24

# apl-source:25
تأكد_يساوي(اعكس_نقطة([3, 5], "x"), [3, -5], "حول السيني")
# apl-source:26
تأكد_يساوي(اعكس_نقطة([3, 5], "y"), [-3, 5], "حول الصادي")
# apl-source:27
تأكد_يساوي(اعكس_نقطة([3, 5], "diag"), [5, 3], "حول القطر")
# apl-source:28
