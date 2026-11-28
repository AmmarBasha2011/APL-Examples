
# apl-source:1
# مثال 1981 — تحويل لون سداسي إلى RGB
# apl-source:2
# Hex color to RGB
# apl-source:3
# Demonstrates: ألوان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1981-hex-color-to-rgb-triple.apl
# apl-source:6

# apl-source:7
# # نتجاهل علامة # في البداية
# apl-source:8
# # ونقرأ ثلاثة أزواج
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
def الى_rgb(س):
  # apl-source:19
  if س[0] == "#":
    # apl-source:20
    س = س[1:]
  # apl-source:21
  return [int(س[0:2], 16), int(س[2:4], 16), int(س[4:6], 16)]
# apl-source:22

# apl-source:23
تأكد_يساوي(الى_rgb("#ff8000"), [255, 128, 0], "برتقالي")
# apl-source:24
تأكد_يساوي(الى_rgb("#000000"), [0, 0, 0], "أسود")
# apl-source:25
تأكد_يساوي(الى_rgb("1a2b3c"), [26, 43, 60], "بلا علامة")
# apl-source:26
