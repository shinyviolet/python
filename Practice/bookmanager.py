class Book:
 
    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
 
    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)
 
class BookManager:

    books = []

    def __init__(self):
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。',1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借出书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lendbook()
            elif choice == 4:
                self.returnbook()
            elif choice == 5:
                break

    def show_all_book(self):
        for book in self.books:
            print(book)
            print('')
    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author=input('请输入作者名：')
        new_comment=input('请输入书评：')
        new_book=Book(new_name,new_author,new_comment)
        self.books.append(new_book)
        print('书籍已录入成功！\n')
    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None
    def lendbook(self):
        bookname=input('请输入你要借阅的书名:')
        res=self.check_book(bookname)
        if res != None:
            if res.state == 1:
                print('这本书已经被借走了\n')
            else:
                print('借书成功\n')
                res.state=1
        else:
            print('查无此书\n')
    def returnbook(self):
        bookname=input('请输入你要还的书名:')
        returncheck=self.check_book(bookname)
        returncheck.state=0
        print('还书成功！')
manager = BookManager()
manager.menu()