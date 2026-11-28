
# apl-source:1
# مثال 256 — يوم الأسبوع بمعادلة زيلر
# apl-source:2
# Zeller's congruence
# apl-source:3
# Demonstrates: حساب يوم الأسبوع لأي تاريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/256-zeller-weekday.apl
# apl-source:6

# apl-source:7
def يوم_الأسبوع_زيلر(يوم_م, شهر_م, سنة_م):
    # apl-source:8
    ش_معدل = شهر_م
    # apl-source:9
    س_معدلة = سنة_م
    # apl-source:10
    if ش_معدل < 3:
        # apl-source:11
        ش_معدل = ش_معدل + 12
        # apl-source:12
        س_معدلة = س_معدلة - 1
    # apl-source:13
    بقية_قرن = س_معدلة % 100
    # apl-source:14
    قرن = س_معدلة // 100
    # apl-source:15
    مؤشر = (يوم_م + (13 * (ش_معدل + 1)) // 5 + بقية_قرن + بقية_قرن // 4 + قرن // 4 + 5 * قرن) % 7
    # apl-source:16
    أيام = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"]
    # apl-source:17
    return أيام[مؤشر]
# apl-source:18

# apl-source:19
print("1 يناير 2000:", يوم_الأسبوع_زيلر(1, 1, 2000))
# apl-source:20
print("23 نوفمبر 2026:", يوم_الأسبوع_زيلر(23, 11, 2026))
# apl-source:21
print("15 مايو 1990:", يوم_الأسبوع_زيلر(15, 5, 1990))
# apl-source:22
