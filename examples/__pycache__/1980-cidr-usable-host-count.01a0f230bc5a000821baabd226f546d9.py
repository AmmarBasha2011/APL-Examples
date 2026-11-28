
# apl-source:1
# مثال 1980 — عدد المضيفين في شبكة CIDR
# apl-source:2
# CIDR usable hosts
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1980-cidr-usable-host-count.apl
# apl-source:6

# apl-source:7
# # نحجز عنوان الشبكة وعنوان البث
# apl-source:8
# # وفي الشبكات الصغيرة جدا نرجع صفرا
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
def مضيفون(بادئة):
  # apl-source:19
  if بادئة > 30:
    # apl-source:20
    return 0
  # apl-source:21
  return 2 ** (32 - بادئة) - 2
# apl-source:22

# apl-source:23
تأكد_يساوي(مضيفون(24), 254, "/24")
# apl-source:24
تأكد_يساوي(مضيفون(16), 65534, "/16")
# apl-source:25
تأكد_يساوي(مضيفون(30), 2, "/30")
# apl-source:26
تأكد_يساوي(مضيفون(32), 0, "/32")
# apl-source:27
