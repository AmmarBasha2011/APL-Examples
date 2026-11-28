
# apl-source:1
# مثال 329 — تجميع زوجي وفردي
# apl-source:2
# Group by parity
# apl-source:3
# Demonstrates: تصنيف قائمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/329-group-parity.apl
# apl-source:6

# apl-source:7
def صنف_زوجية(أرقام):
    # apl-source:8
    زوجية = []
    # apl-source:9
    فردية = []
    # apl-source:10
    for ع in أرقام:
        # apl-source:11
        if ع % 2 == 0:
            # apl-source:12
            زوجية.append(ع)
        # apl-source:13
        else:
            # apl-source:14
            فردية.append(ع)
    # apl-source:15
    return {"زوجية": زوجية, "فردية": فردية}
# apl-source:16

# apl-source:17
ن = صنف_زوجية([1, 2, 3, 4, 5, 6, 7, 8, 9])
# apl-source:18
print("الزوجية:", ن["زوجية"])
# apl-source:19
print("الفردية:", ن["فردية"])
# apl-source:20
