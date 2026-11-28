
# apl-source:1
# مثال 686 — قارئ FEN
# apl-source:2
# FEN parser
# apl-source:3
# Demonstrates: شطرنج، ترميز موقف، حقول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/686-fen-parse.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# قارئ ترميز فورسيث-إدواردز FEN لمواقف الشطرنج
# apl-source:25
# Demonstrates: تقسيم الحقول الستة, فك صفوف اللوحة, عد القطع
# apl-source:26

# apl-source:27
def اقرأ_فين(فين):
  # apl-source:28
  حقول = فين.split(" ")
  # apl-source:29
  صفوف = حقول[0].split("/")
  # apl-source:30
  قطع = 0
  # apl-source:31
  بيض = 0
  # apl-source:32
  سود = 0
  # apl-source:33
  خانات = 0
  # apl-source:34
  for صف in صفوف:
    # apl-source:35
    for ي in range(len(صف)):
      # apl-source:36
      ح = صف[ي]
      # apl-source:37
      if ح in "12345678":
        # apl-source:38
        خانات = خانات + int(ح)
      # apl-source:39
      else:
        # apl-source:40
        خانات = خانات + 1
        # apl-source:41
        قطع = قطع + 1
        # apl-source:42
        if ح in "PNBRQK":
          # apl-source:43
          بيض = بيض + 1
        # apl-source:44
        else:
          # apl-source:45
          سود = سود + 1
  # apl-source:46
  return [صفوف, حقول[1], حقول[2], حقول[3], int(حقول[4]), int(حقول[5]), قطع, بيض, سود, خانات]
# apl-source:47

# apl-source:48
بداية = اقرأ_فين("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
# apl-source:49
تأكد_يساوي(بداية[6], 32, "32 قطعة في البداية")
# apl-source:50
تأكد_يساوي(بداية[7], 16, "16 أبيض")
# apl-source:51
تأكد_يساوي(بداية[8], 16, "16 أسود")
# apl-source:52
تأكد_يساوي(بداية[9], 64, "64 خانة")
# apl-source:53
تأكد_يساوي(بداية[1], "w", "الأبيض يبدأ")
# apl-source:54
تأكد_يساوي(بداية[2], "KQkq", "كل حقوق التبييت")
# apl-source:55
تأكد_يساوي(بداية[3], "-", "لا تجاوز")
# apl-source:56
تأكد_يساوي(بداية[4], 0, "نصف نقلة صفر")
# apl-source:57
تأكد_يساوي(بداية[5], 1, "النقلة الأولى")
# apl-source:58
تأكد_يساوي(len(بداية[0]), 8, "ثمانية صفوف")
# apl-source:59

# apl-source:60
بعد_e4 = اقرأ_فين("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
# apl-source:61
تأكد_يساوي(بعد_e4[1], "b", "الأسود يلعب بعد e4")
# apl-source:62
تأكد_يساوي(بعد_e4[3], "e3", "خانة التجاوز e3")
# apl-source:63
تأكد_يساوي(بعد_e4[6], 32, "ما زالت 32 قطعة")
# apl-source:64

# apl-source:65
نهاية = اقرأ_فين("8/8/4k3/8/8/4K3/8/8 w - - 12 47")
# apl-source:66
تأكد_يساوي(نهاية[6], 2, "ملكان فقط")
# apl-source:67
تأكد_يساوي(نهاية[5], 47, "النقلة 47")
# apl-source:68
print("قطع البداية:", بداية[6])
# apl-source:69
