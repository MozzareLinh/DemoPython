
import random
from datetime import *

list_film_type = {
    1: "Việt Nam",
    2: "Nước Ngoài"
}

#########    Global_Var    #########
startHotTime = time(18, 00, 00)
endHotTime = time(22, 00, 00)
generated_Ticket = 0
### Ca chiếu ###
list_show_time = {
    1: {
        "startTime": time(7, 00, 00),
        "endTime": time(9, 00, 00)
    },
    2: {
        "startTime": time(9, 00, 00),
        "endTime": time(11, 00, 00)
    },
    3: {
        "startTime": time(12, 00, 00),
        "endTime": time(15, 00, 00)
    },
    4: {
        "startTime": time(15, 00, 00),
        "endTime": time(17, 00, 00)
    },
    5: {
        "startTime": time(18, 00, 00),
        "endTime": time(20, 00, 00)
    },
    6: {
        "startTime": time(20, 00, 00),
        "endTime": time(22, 00, 00)
    }
}
### - ###

### Phòng chiếu theo ca chiếu ##
film_schedule = {
    1: {
        1: {
            'time': 1,
            'seats': 25,
            'id_film': 1,
        },
        2: {
            'time': 1,
            'seats': 25,
            'id_film': 2,
        },
        3: {
            'time': 1,
            'seats': 25,
            'id_film': 11,
        }
    },
    2: {
        1: {
            'time': 2,
            'seats': 25,
            'id_film': 1,
        },
        2: {
            'time': 2,
            'seats': 25,
            'id_film': 2,
        },
        3: {
            'time': 2,
            'seats': 25,
            'id_film': 5,
        }
    },
    3: {
        1: {
            'time': 3,
            'seats': 25,
            'id_film': 3,
        },
        2: {
            'time': 3,
            'seats': 25,
            'id_film': 5,
        },
        3: {
            'time': 3,
            'seats': 25,
            'id_film': 6,
        }

    },
    4: {
        1: {
            'time': 4,
            'seats': 25,
            'id_film': 3,
        },
        2: {
            'time': 4,
            'seats': 25,
            'id_film': 6,
        },
        3: {
            'time': 4,
            'seats': 25,
            'id_film': 8,
        }

    },
    5: {
        1: {
            'time': 5,
            'seats': 25,
            'id_film': 7,
        },
        2: {
            'time': 5,
            'seats': 25,
            'id_film': 10,
        },
        3: {
            'time': 5,
            'seats': 25,
            'id_film': 11,
        }

    },
    6: {
        1: {
            'time': 6,
            'seats': 25,
            'id_film': 7,
        },
        2: {
            'time': 6,
            'seats': 25,
            'id_film': 8,
        },
        3: {
            'time': 6,
            'seats': 25,
            'id_film': 10,
        }
    }
}
### ###

### Mảng ghế ###
rows, cols = 5, 5
num_arrays = 6 * 3
# Tạo một list chứa 6 mảng 2 chiều 3x4 với giá trị ban đầu là 0
arr = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(num_arrays)]
arr[1][0][0] = 1


### - ###


### Ticket ###
class Ticket:
    def __init__(self, id, name, startTime, room, seat, typeFilm, price, recentroom):
        self.id = id
        self.name = name
        self.startTime = startTime
        self.room = room
        self.seat = seat
        self.typeFilm = typeFilm
        self.price = price
        self.recentroom = recentroom

    ### Film ###


class Film:
    def __init__(self, id, name, timeDuration, showtime, type):
        self.id = id
        self.name = name
        self.timeDuration = timeDuration
        self.totalvalue = 0
        self.showtime = showtime
        self.type = type

    def add_benefit(self, price):
        self.totalvalue += price


class ManageFilm:  # author NAT
    def __init__(self):
        self.list_film_name = []

    def searchFilmByName(self, name):
        for film in self.list_film_name:
            if film.name == name:
                return film
        return None

    def searchFilmByString(self, string):
        mylist = []
        for film in self.list_film_name:
            if film.name.find(string):
                mylist.append(film)
        return mylist

    def searchFilmById(self, id):
        for film in self.list_film_name:
            if film.id == id:
                return film
        return None

    def searchFilmByIndex(self, index):
        if index - 1 > len(self.list_film_name):
            return None
        return self.list_film_name[index - 1]
    def dislplay_all_film(self):
        item = self.list_film_name
        for i in range(len(item)):
            print(f"{i + 1} - {item[i].name}")

    def get_side_film(self):
        return len(self.list_film_name)


# Khoi Tao Quan Ly Phim
manageFilm = ManageFilm()

Film1 = Film(1, "Đào, Phở và Piano", time(2, 30, 00), [1, 2], 1)
Film2 = Film(2, "Mai", time(2, 15, 00), [1, 2], 1)
Film3 = Film(3, "Thanh Gươm Diệt Quỷ: Phép Màu Tình Thân, Cho Đến Chuyến Đặc Huấn Của Đại Trụ", time(2, 30, 00), [3, 4],
             2)
Film4 = Film(5, "Bà Thím Báo Thù", time(2, 30, 00), [2, 3], 2)
Film5 = Film(6, "Bơi Đêm", time(2, 15, 00), [3, 4], 2)
Film6 = Film(7, "Cún Cưng Đại Náo Nhà Hát", time(2, 30, 00), [5, 6], 2)
Film7 = Film(8, "Gia Đình x Điệp Viên Mã: Trắng", time(2, 15, 00), [4, 6], 2)
Film8 = Film(10, "Madame Web", time(2, 15, 00), [5, 6], 2)
Film9 = Film(11, "Nàng Thơ Của Miller", time(2, 15, 00), [1, 5], 2)
manageFilm.list_film_name.append(Film1)
manageFilm.list_film_name.append(Film2)
manageFilm.list_film_name.append(Film3)
manageFilm.list_film_name.append(Film4)
manageFilm.list_film_name.append(Film5)
manageFilm.list_film_name.append(Film6)
manageFilm.list_film_name.append(Film7)
manageFilm.list_film_name.append(Film8)
manageFilm.list_film_name.append(Film9)


class ManageTicket:
    def __init__(self):
        self.tickets = []
        self.total = 0
        self.generateid = 0
        self.refund = 0

    ### Phương Thức ###
    def sell_ticket(self, ticket, schedule):  # author NAT
        self.tickets.append(ticket)
        # tru di 1 ghe
        set_matrix_seats(ticket.recentroom, ticket.seat[0], ticket.seat[1])
        film_schedule[schedule][ticket.room]['seats'] -= 1
        # cong tong doanh thu
        self.total += ticket.price
        # cong tien vao phim
        recent_film = manageFilm.searchFilmByName(ticket.name)
        if (recent_film):
            recent_film.add_benefit(ticket.price)
        return True

    def cancel_ticket(self):
        _id = int(input("Nhập mã vé của khách hàng: "))
        if len(self.tickets) == 0:
            return None
        else:
            for i in range(len(self.tickets)):
                if self.tickets[i].id == _id:
                    unset_matrix_seats(self.tickets[i].recentroom, self.tickets[i].seat[0], self.tickets[i].seat[1])
                    #convert to datetime
                    datetimeTicket = datetime.combine(datetime.today(), self.tickets[i].startTime)

                    #compare
                    diffTime = (datetimeTicket - datetime.now()).total_seconds()
                    if diffTime < 0:
                        print("Vé đã quá hạn")
                        return False
                    # print(diffTime)
                    if (datetimeTicket - datetime.now()).total_seconds() > 4 * 60 * 60:
                        if self.tickets[i].typeFilm == 1:
                            self.total -= self.tickets[i].price * 0.6
                            manageFilm.searchFilmByName(self.tickets[i].name).totalvalue -= self.tickets[i].price * 0.6
                            self.refund += self.tickets[i].price * 0.6
                        else:
                            self.total -= self.tickets[i].price * 0.8
                            manageFilm.searchFilmByName(self.tickets[i].name).totalvalue -= self.tickets[i].price * 0.8
                            self.refund += self.tickets[i].price * 0.8
                        print("Đã hoàn tiền")
                    self.tickets.pop(i)
                    return True
        return None

    def get_id(self):
        return self.generateid

    ################## Thống Kê ###################

    # ve ban theo loai phim
    def display_tickets_by_type(self):  # author NAT
        vn_ticket = 0
        ng_ticket = 0
        for item in self.tickets:
            if item.typeFilm == 1:
                vn_ticket += 1
            else:
                ng_ticket += 1
        print("Thống kê đã bán vé theo loại phim:")
        print("Phim Việt Nam:", vn_ticket)
        print("Phim Nước Ngoài:", ng_ticket)

    #

    # doanh thu theo phim
    def display_benefit_by_film(self):  # author: Hieu
        # Hiển thị danh sach phim gom id va ten
        print("Danh sách phim:")
        manageFilm.dislplay_all_film()
        ip_id_name = None
        while True:
            try:
                ip_id_name = int(input("Nhập id phim:"))
                if 0< ip_id_name < manageFilm.get_side_film():
                    break;
                else:
                    print("Số không tồn tại!")
            except ValueError:
                print("Hãy nhập số nguyên:")
        res = manageFilm.searchFilmById(manageFilm.list_film_name[ip_id_name - 1].id)
        if res is None:
            print("không tìm thấy phim")
        else:
            print("Tổng thu =", res.totalvalue)
    # top 6 phim doanh thu cao nhat
    def top_6_benefits(self):
        arr = manageFilm.list_film_name
        n = len(manageFilm.list_film_name)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j].totalvalue < arr[j + 1].totalvalue:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("Top 6 phim có doanh thu cao nhất:")
        for i in range(6):
            print(f"{i + 1}. {arr[i].name}")
        print("\nTop 6 phim có doanh thu thấp nhất:")
        index = 1
        for i in range(n - 1, n - 7, -1):
            print(f"{index}. {arr[i].name}")
            index += 1

    # danh sach ve dang cho
    def display_pending_tickets(self):
        index = 1
        print("\nDanh sách các vé đang chờ theo thời gian chiếu:")
        for item in self.tickets:
            if item.startTime > datetime.now().time():
                print(f"\n{index}. mã vé: {item.id}", end=" ")
                print(f" Tên phim: {item.name}", end=" ")
                print(f" Thời gian: {item.startTime}", end=" ")
                print(f" Loại: {list_film_type[item.typeFilm]}", end=" ")
                print(f". Phòng: {item.room}", end=" ")
                print(f" Gia tien: {item.price}", end=" ")
                index += 1

    def sort_by_show_time(self):
        arr = []
        print("Danh sách phim:")
        manageFilm.dislplay_all_film()
        while True:
            try:
                ip_id_name = int(input("Nhập id phim:"))
                break;
            except ValueError:
                print("Hãy nhập số nguyên:")
        res = manageFilm.searchFilmById(manageFilm.list_film_name[ip_id_name-1])
        if res is None:
            print("không tìm thấy phim")
        else:
            res = res.name
            ans = 0
            for i in range(len(self.tickets)):
                if self.tickets[i].name == res:
                    arr.append(self.tickets[i])
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j].startTime > arr[j + 1].startTime:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        index = 1
        for item in arr:
            print(f"\n{index}. mã vé: {item.id}", end=" ")
            print(f" Tên phim: {item.name}", end=" ")
            print(f" Thời gian: {item.startTime}", end=" ")
            print(f" Loại: {list_film_type[item.typeFilm]}", end=" ")
            print(f". Phòng: {item.room}", end=" ")
            print(f" Gia tien: {item.price}", end=" ")
            index += 1

    def Cac_ve_da_ban_theo_ten_phim(self):
        # Hiển thị danh sach phim gom id va ten
        print("Danh sách phim:")
        manageFilm.dislplay_all_film()
        ip_id_name = None
        while True:
            try:
                ip_id_name = int(input("Nhập id phim:"))
                if 0 < ip_id_name < manageFilm.get_side_film():
                    break;
            except ValueError:
                print("Hãy nhập số nguyên:")
        res = manageFilm.searchFilmByIndex(ip_id_name)
        # print(res)
        if res is None:
            print("không tìm thấy phim")
        else:
            arr_sort = []
            res = res.name
            ans = 0
            for i in range(len(self.tickets)):
                if self.tickets[i].name == res:
                    arr_sort.append(self.tickets[i])
            n = len(arr_sort)
            print(f"Lựa chọn tiêu chí sắp xếp: ")
            print(f"1. Tăng dần theo thời gian")
            print(f"2. Giảm dần theo thời gian")
            sort_type = 0
            while sort_type != 1 and sort_type != 2:
                sort_type = int(input(f"Lựa chọn: "))
            if sort_type == 1:
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if arr_sort[j].startTime > arr_sort[j + 1].startTime:
                            arr_sort[j], arr_sort[j + 1] = arr_sort[j + 1], arr_sort[j]
            elif sort_type == 2:
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if arr_sort[j].startTime < arr_sort[j + 1].startTime:
                            arr_sort[j], arr_sort[j + 1] = arr_sort[j + 1], arr_sort[j]
            index = 1
            for item in arr_sort:
                print(f"\n{index}. mã vé: {item.id}", end=" ")
                print(f" Tên phim: {item.name}", end=" ")
                print(f" Thời gian: {item.startTime}", end=" ")
                print(f" Loại: {list_film_type[item.typeFilm]}", end=" ")
                print(f". Phòng: {item.room}", end=" ")
                print(f" Gia tien: {item.price}", end=" ")
                index += 1

    def display_benefit_by_show_time(self):
        print("Các khung thời gian chiêu phim:")
        arr = []
        for item in self.tickets:
            if len(arr) == 0:
                arr.append(item)
            else:
                check = True
                for i in range(len(arr)):
                    if arr[i].startTime == item.startTime:
                        check = False
                if check:
                    arr.append(item)
        n = len(arr)
        ip = None
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j].startTime > arr[j + 1].startTime:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        for i in range(len(arr)):
            print(f"{i + 1}. {arr[i].startTime}")
        while True:
            try:
                ip = int(input("Mời nhập khung giờ:"))
                if ip <= 0 or ip > len(arr):
                    print("Mời nhập lại")
                else:
                    break;
            except ValueError:
                print("Mờ nhập số nguyên")
        ans = 0
        for item in self.tickets:
            if item.startTime == arr[ip-1].startTime:
                ans += item.price
        print(f"\nDoanh thu theo khung thoi gian {arr[ip-1].startTime} = {ans}")

    def display_total_refund(self):
        print(f"Tổng tiền hoàn trả vé cho khách hàng: {self.refund}")

    def display_tickets_by_film(self):
        print(f"Tổng số vé đã bán của từng bộ phim: ")
        index = 1
        for i in manageFilm.list_film_name:
            print(f"{index}. {i.name}: {sum_tickets_by_film(i.name)}")
            index += 1



def display_all_schedule_by_films(id):
    for i in range(len(manageFilm.list_film_name)):
        if manageFilm.list_film_name[i].id == id:
            return manageFilm.list_film_name[i].showtime
    return 0


def sum_tickets_by_film(film_name):
    count = 0
    for i in range(len(manage.tickets)):
        if film_name == manage.tickets[i].name:
            count += 1
    return count


def get_room_by_schedule(id_schedule, id_film):
    my_list = []
    for item in film_schedule[id_schedule]:
        if film_schedule[id_schedule][item]['id_film'] == id_film and film_schedule[id_schedule][item]['seats'] != 0:
            my_list.append(item)
    return my_list


def search_film(id):
    for i in range(len(manageFilm.list_film_name)):
        if manageFilm.list_film_name[i].id == id:
            return manageFilm.list_film_name[i]
    return 0


def display_maxtrix_seats(index):
    for row in arr[index - 1]:
        print(row)


# def display_available_seats_by_index(index):
# k = film_schedule[index]['seat']
# for key, value in k:
# print(f"{seats[key]['name']}: {value}")
def set_matrix_seats(index, i, j):
    if (check_matrix_seats(index, i, j)):
        arr[index - 1][i - 1][j - 1] = 1


def check_matrix_seats(index, i, j):
    if arr[index - 1][i - 1][j - 1] == 1:
        return False
    return True


def unset_matrix_seats(index, i, j):
    arr[index - 1][i - 1][j - 1] = 0


# recentroom >0 and < 18
manage = ManageTicket()
newTicket1 = Ticket(111, 'Đào, Phở và Piano', time(7, 00, 00), 1, [2, 2], 1, 50000, 1)
newTicket2 = Ticket(112, 'Thanh Gươm Diệt Quỷ: Phép Màu Tình Thân, Cho Đến Chuyến Đặc Huấn Của Đại Trụ',
                    time(12, 00, 00), 1, [2, 3], 2, 60000, 7)
newTicket3 = Ticket(113, 'Mai', time(9, 00, 00), 2, [3, 3], 1, 50000, 2)
newTicket5 = Ticket(115, 'Bà Thím Báo Thù', time(9, 00, 00), 3, [3, 4], 2, 60000, 6)
newTicket6 = Ticket(116, 'Bơi Đêm', time(15, 00, 00), 2, [3, 3], 2, 60000, 11)
newTicket7 = Ticket(117, 'Cún Cưng Đại Náo Nhà Hát', time(20, 00, 00), 1, [1, 3], 2, 72000, 16)
newTicket8 = Ticket(118, 'Gia Đình x Điệp Viên Mã: Trắng', time(20, 00, 00), 3, [4, 2], 2, 72000, 17)
newTicket10 = Ticket(120, 'Madame Web', time(18, 00, 00), 2, [3, 1], 2, 72000, 14)
newTicket11 = Ticket(121, 'Nàng Thơ Của Miller', time(7, 00, 00), 3, [3, 1], 2, 60000, 3)
manage.sell_ticket(newTicket1, 1)
manage.sell_ticket(newTicket2, 3)
manage.sell_ticket(newTicket3, 1)
manage.sell_ticket(newTicket5, 2)
manage.sell_ticket(newTicket6, 3)
manage.sell_ticket(newTicket7, 5)
manage.sell_ticket(newTicket8, 6)
manage.sell_ticket(newTicket10, 6)
manage.sell_ticket(newTicket11, 5)


def Welcome():
    print("\nChào mừng bạn đã đến với chúng tôi:")
    print("Để bắt đầu mua vé hãy lựa chọn:")
    print("1. Bắt đầu")
    print("2. Thoát")
    ip1 = input("Lựa chọn: ")
    while ip1 != '1' and ip1 != '2':
        print("Cú pháp không hợp lệ, hãy nhập lại: ")
        ip1 = input("Lựa chọn: ")
    if ip1 == '1':
        Pmain()
    elif ip1 == '2':
        print("Thoát chương trình...")
        return 1


def Pmain():
    print("\n1. Mua vé: ")
    print("2. Hủy vé: ")
    print("3. Thống kê:")
    print("4. Quay lại:")
    ip_test = input("Nhập lựa chọn: ")
    while not ip_test.isnumeric():
        ip_test = input("Nhập lựa chọn: ")
    ip = int(ip_test)
    while int(ip) < 1 or int(ip) > 4:
        ip_test = input("Nhập lựa chọn: ")
        if ip_test.isnumeric():
            ip = int(ip_test)
    try:
        if ip == 1:
            InMuaVeTheoTenPhim()
        elif ip == 2:
            if (manage.cancel_ticket()):
                print("Hủy vé thành công!")
                Pmain()
            else:
                print("Hủy vé không thành công!")
                Pmain()
        elif ip == 3:
            InThongKe()
        elif ip == 4:
            Welcome()
    except ValueError:
        print("Lỗi thực hiện")
        Pmain()

def InThongKe():
    print("\n1. Thống kê các vé đã bán theo tên phim:")
    print("2. Tổng doanh thu đã thu được:")
    print("3. Thống kê số lượng vé đã bán của mỗi loại vé:")
    print("4. Hiển thị danh sách các vé đang chờ theo thời gian chiếu:")
    print("5. Hiển thị doanh thu theo khung thời gian chiếu:")
    print("6. Hiển thị doanh thu theo phim:")
    print("7. Hiển thị top 6 phim có doanh thu cao nhất:")
    print("8. Thống kê tổng số vé đã bán của từng bộ phim:")
    print("9. Thống kê tổng tiền hoàn trả vé cho khách hàng:")
    print("10. Quay lại")
    ckip = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while True:
        try:
            ip = int(input("Nhập lựa chọn:"))
            if ip in ckip:
                if ip == 1:
                    print("===============================")
                    manage.Cac_ve_da_ban_theo_ten_phim()
                    InThongKe()
                    break;
                if ip == 2:
                    print("===============================")
                    print(f"Doanh thu: {manage.total}")
                    print("===============================")
                    InThongKe()
                if ip == 3:
                    print("===============================")
                    manage.display_tickets_by_type()
                    print("===============================")
                    InThongKe()
                if ip == 4:
                    print("===============================")
                    manage.display_pending_tickets()
                    print("===============================")
                    InThongKe()
                if ip == 5:
                    print("===============================")
                    manage.display_benefit_by_show_time()
                    print("===============================")
                    InThongKe()
                if ip == 6:
                    print("===============================")
                    manage.display_benefit_by_film()
                    print("===============================")
                    InThongKe()
                if ip == 7:
                    print("===============================")
                    manage.top_6_benefits()
                    print("===============================")
                    InThongKe()
                if ip == 8:
                    print("===============================")
                    manage.display_tickets_by_film()
                    print("===============================")
                    InThongKe()
                if ip == 9:
                    print("===============================")
                    manage.display_total_refund()
                    print("===============================")
                    InThongKe()
                if ip == 10:
                    Pmain()
                break;
            else:
                print("Mời nhập lại:")
        except ValueError:
            print("Mời nhập số nguyên")


def after_buy_ticket():
    print("1. Mua tiếp:")
    print("2. Xem thống kê:")
    print("3. Thoát ra menu")
    arr = [1, 2, 3]
    try:
        while (True):
            op = int(input("Nhập: "))
            if op in arr:
                if op == 1:
                    InMuaVeTheoTenPhim()
                    break
                elif op == 2:
                    InThongKe()
                    break
                elif op == 3:
                    Pmain()
                    break
            else:
                print("Lựa chọn không tồn tại!")
    except ValueError:
        print("Mời nhập số nguyên:")
        after_buy_ticket()


def InMuaVeTheoTenPhim():
    print('\nĐể chọn ra bộ phim yêu thích, hãy nhập số thứ tự của phim:')
    # Hien Thi danh sach cac loai phim
    manageFilm.dislplay_all_film()
    print("\nBạn chọn phim số:", end=" ")
    ip_test = input()
    while not ip_test.isnumeric():
        ip_test = input("Nhập lựa chọn: ")
    ip_name = int(ip_test)
    while int(ip_name) < 1 or int(ip_name) > manageFilm.get_side_film():
        ip_test = input("Nhập lựa chọn: ")
        if ip_test.isnumeric():
            ip_name = int(ip_test)
    film_selected = manageFilm.searchFilmById(manageFilm.list_film_name[ip_name-1].id)
    # ---------
    print("Khung giờ chiếu bộ phim này là:")
    # Hien thi cac khung gio cua phim
    res = display_all_schedule_by_films(film_selected.id)

    if len(res):
        for i in range(len(res)):
            print(f"Ca {res[i]}", list_show_time[res[i]]["startTime"], "-", list_show_time[res[i]]["endTime"])
    else:
        print("Không có suất chiếu")
        print("Bạn có muốn tiếp tục xem phim không ?")
        print("1. Có")
        print("2. Không")
        try:
            lb = int(input())
            if lb == 1:
                InMuaVeTheoTenPhim()
            elif lb == 2:
                Welcome()
            else:
                print("Mời nhập lại")
        except ValueError:
            print("Phải nhập số nguyên")

    # Chon ca chieu phim (film_schedule)
    print("Chọn ca chiếu cho phim:")
    while True:
        try:
            ip_time = int(input())
            if ip_time in res:
                break;
            else:
                print("Mời nhập đúng số ca trong danh sách:")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

    # Chon phong chieu
    rooms = get_room_by_schedule(ip_time, film_selected.id)

    if len(rooms):
        for i in range(len(rooms)):
            print(f"Phòng {rooms[i]}")
    else:
        print("Không có phòng chiếu")
        print("Bạn có muốn tiếp tục xem phim không ?")
        print("1. Có")
        print("2. Không")
        try:
            lb = int(input())
            if lb == 1:
                InMuaVeTheoTenPhim()
            elif lb == 2:
                Welcome()
            else:
                print("Mời nhập lại")
        except ValueError:
            print("Phải nhập số nguyên")

    # Chon room
    print("Chọn phòng chiếu:")
    while True:
        try:
            ip_room = int(input())
            if ip_room in rooms:
                break;
            else:
                print("Mời nhập đúng số phòng trong danh sách:")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

    print("Danh sách ghế còn trống:")
    # Hien thi danh sach ghe con trong

    recent_room = 3 * ip_time - (3 - ip_room)
    display_maxtrix_seats(recent_room)
    # input toa do ghe
    i = 0
    j = 0
    while True:
        i_test = input("Nhập số hàng: ")
        while not i_test.isnumeric():
            i_test = input("Nhập lại số hàng: ")
        i = int(i_test)
        while int(i) < 1 or int(i) > 5:
            i_test = input("Nhập lại số hàng: ")
            if i_test.isnumeric():
                i = int(i_test)
        j_test = input("Nhập số cột: ")
        while not j_test.isnumeric():
            j_test = input("Nhập lại số cột: ")
        j = int(j_test)
        while int(j) < 1 or int(j) > 5:
            j_test = input("Nhập lại số cột: ")
            if j_test.isnumeric():
                j = int(j_test)
        if check_matrix_seats(recent_room, i, j):
            print("Đặt ví trí thành công!")
            break
        else:
            print("Vị trí này đã có người đặt rồi, mời bạn chọ vị trí khác: ")
    # ---------
    print("\nThông tin vé bạn đặt: ")

    output_price = 0
    if (film_selected.type == 2):
        if startHotTime <= list_show_time[ip_time]["startTime"] <= endHotTime:
            output_price = 70000
        else:
            output_price = 60000
    else:
        if startHotTime <= list_show_time[ip_time]["startTime"] <= endHotTime:
            output_price = 60000
        else:
            output_price = 50000
    newTicket = Ticket(random.randint(1, 1000), film_selected.name, list_show_time[ip_time]["startTime"], ip_room,
                       [i, j], film_selected.type, output_price, recent_room)

    print("Mã vé:", newTicket.id)
    print("Tên phim:", newTicket.name)
    print("Thể loại:", list_film_type[newTicket.typeFilm])
    print("Phòng:", newTicket.room, "Hàng:", newTicket.seat[0], "Cột: ", newTicket.seat[1])
    print("Thời gian:", newTicket.startTime)
    print("Giá Tiền:", newTicket.price)

    # input opsion
    print("\nBạn có chắc muốn mua vé này?")
    print("1. Có")
    print("2. Hủy")
    lb = int(input())
    if int(lb) < 1 or int(lb) > 2:
        print("Mời nhập lại:")
        lb = int(input())
    if lb == 1:
        manage.sell_ticket(newTicket, ip_time)
        print("Mua vé thành công!")
        after_buy_ticket()
    else:
        print("Quay lại...")
        Welcome()



################# MAIN ##################
Welcome()


