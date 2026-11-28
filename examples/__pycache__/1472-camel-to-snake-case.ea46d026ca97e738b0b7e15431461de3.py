
# apl-source:1
# مثال 1472 — من camelCase إلى snake_case
# apl-source:2
# camelCase to snake_case
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1472-camel-to-snake-case.apl
# apl-source:6

# apl-source:7
# نضيف شرطة سفلية قبل كل حرف كبير
# apl-source:8
# ثم نصغر الحرف
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
def الى_ثعباني(اسم):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  for ع in range(len(اسم)):
    # apl-source:21
    ح = اسم[ع]
    # apl-source:22
    if ح.isupper():
      # apl-source:23
      if ع > 0:
        # apl-source:24
        ناتج = ناتج + "_"
      # apl-source:25
      ناتج = ناتج + ح.lower()
    # apl-source:26
    else:
      # apl-source:27
      ناتج = ناتج + ح
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(الى_ثعباني("userName"), "user_name", "اسم")
# apl-source:31
تأكد_يساوي(الى_ثعباني("getHTTPCode"), "get_h_t_t_p_code", "حروف متتالية")
# apl-source:32
تأكد_يساوي(الى_ثعباني("simple"), "simple", "بدون تغيير")
# apl-source:33
