"""
Xử lý File:
B1: Open
    open(<đường dẫn>, mode = <chế độ>)
                                r: đọc
                                w: ghi đè
                                a: ghi thêm
B2: Process
B3: Close
"""
fp = open("text.txt", mode = "w")
lst = ["a", 1, True, "c", 4.5]
fp.write("-".join(map(str,lst)))            #truyền vào write() chỉ có thể là string
fp.close()