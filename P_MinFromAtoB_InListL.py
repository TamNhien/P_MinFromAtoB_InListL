def find_min(L, a, b):
    if not L: return "Danh sách trống"
    if not (0 <= a < b <= len(L)): return "Vị trí không hợp lệ"
    return min(L[a:b+1])

if __name__ == "__main__":
    L = list(map(int, input("Nhập vào danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
    a, b = map(int, input("Nhập vào số nguyên dương a và b (a < b < len(L)): ").split())
    print("Số nhỏ nhất từ vị trí", a, "đến vị trí", b, "là : ", find_min(L, a, b))
