from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import webbrowser

Window.size = (400, 600)


class Test(MDApp):
    popup = None
    table = None
    tab = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('original.kv')

    def on_resize(self, width):
        self.root.ids.change.font_size = width * 0.07

    def click(self):
        content = Builder.load_file('login.kv')
        self.popup = Popup(title='Login', content=content, size_hint=(None, None), size=(150, 150), auto_dismiss=False)
        self.popup.open()

    def logger(self):
        username = self.popup.content.ids.user.text
        password = self.popup.content.ids.password.text
        grade = self.popup.content.ids.grade.text
        names = ("",
                 "Хамраев Азизбек",
                 "Алибеков Шахриёр",
                 "Шермухаммедов Бехруз",
                 "Мухаммадхошимов Шахбоз",
                 "Мавлянов Бехруз",
                 "Максудов Асадбек",
                 "Анваров Аннур",
                 "Султанмуродов Акбархон",
                 "Камолитдинова Азиза",
                 "Абдурахимова Сахиба")
        if username in names and password == "1" and grade == "9В":
            self.popup.dismiss()
            self.root.ids.change.text = f'Добро пожаловать {username}!'
            print(f'Login: {username},', f'password: {password},', f'grade: {grade}')
            self.root.ids.changeit.text = f'Ваш класс: {grade}'
            self.root.ids.log_btn.opacity = 0
            self.root.ids.log_btn.disabled = True
            self.root.ids.cards.opacity = 1
            self.root.ids.cards1.opacity = 1
            self.root.ids.cards2.opacity = 1
            self.root.ids.cards3.opacity = 1
            names = ("",
                     "Английский",
                     "Русский",
                     "Алгебра",
                     "Геометрия",
                     "Физика",
                     "Химия",
                     "Биология",
                     "Основы Конструкционных прав",
                     "Русский",
                     "Литература")
            self.table = MDDataTable(
                pos_hint={"center_y": 0.5, "center_x": 0.5},
                size_hint=(0.9, 0.85),
                use_pagination=True,
                rows_num=7,
                column_data=[
                    ("Предметы:", dp(45)),
                    (username, dp(45)),
                ],

                row_data=[(name, "I    II   III  IV  Год") if name == "" else (
                    name, "5   5   5   5   5") for name in names],
            )
            self.root.ids.screen1.add_widget(self.table)

            names = ("",
                     "Английский",
                     "Русский",
                     "Алгебра",
                     "Геометрия",
                     "Физика",
                     "Химия",
                     "Биология",
                     "Основы Конструкционных прав",
                     "Русский",
                     "Литература")

            self.tab = MDDataTable(
                pos_hint={"center_y": 0.5, "center_x": 0.5},
                size_hint=(0.95, 0.95),
                use_pagination=True,
                rows_num=7,
                column_data=[
                    ("", dp(45)),
                    ("", dp(30)),
                    ("", dp(30)),
                    ("", dp(30)),
                    ("", dp(30)),
                    ("", dp(30)),
                    ("", dp(30)),
                ],

                row_data=[(name, "[color=#FF0000]1.15.2023[/color]", "[color=#FF0000]2.15.2023[/color]",
                           "[color=#FF0000]3.15.2023[/color]", "[color=#FF0000]4.15.2023[/color]",
                           "[color=#FF0000]5.15.2023[/color]",
                           "[color=#FF0000]6.15.2023[/color]") if name == "" else
                          (name, "Pb p21-22", "Pb p23-24", "Pb p25-26", "Pb p27-28", "Pb p29-30",
                           "Pb p31-32") if name == "Английский" else
                          (name, "Упр-37", "Упр-49", "Упр-50", "Упр-55", "Упр-60",
                           "Упр-66") if name == "Русский" else
                          (name, "стр-64 №3-7", "стр-65 №3-7", "стр-67 №3-7", "стр-70 №3-7", "стр-84 №3-7",
                           "стр-91 №3-7") if name == "Алгебра" else
                          (name, "стр-10 повтор", "стр-14 параллелограмм", "стр-24 изучить", "стр-29 прямоугольники",
                           "стр-30 прочитать",
                           "стр-37 №5-6") if name == "Геометрия" else
                          (name, "Повтор", "Прочитать параграф-5", "Атомы", "Кинематика", "Статика",
                           "Подготовка к контрольной") if name == "Физика" else
                          (name, "Водородное соединение", "Электролиты", "Не электролиты", "Таблица Менделеева",
                           " Подгатовка к проверочной работе",
                           "Изучение атома") if name == "Химия" else
                          (name, "Pb p23-24", "Упр-49", "стр-64 №3-7", "стр-19 прямоугольники", "Статика",
                           "Изучение атома") if name == "Русский" else
                          (name, "Pb p23-24", "Упр-49", "стр-64 №3-7", "стр-19 прямоугольники", "Статика",
                           "Изучение атома") if name == "Русский" else
                          (name, "Pb p23-24", "Упр-49", "стр-64 №3-7", "стр-19 прямоугольники", "Статика",
                           "Изучение атома") if name == "Русский" else
                          (name, "Pb p25-26", "Упр-50", "стр-70 №5-3", "стр-19 прямоугольники", "Статика",
                           "Изучение атома") for name in names]
            )
            self.root.ids.screen2.add_widget(self.tab)

    def link(self):
        webbrowser.open(
            "https://docs.google.com/forms/d/e/1FAIpQLSeg8SJ3TEZVCj89O4CBTB7oqdnMLfgfVOvnkhb3jzC-VnvG5w/viewform")

    def linking(self):
        webbrowser.open("https://www.instagram.com/sehriyouz/")

    def quit(self):
        self.root.ids.change.text = f'Добро пожаловать'
        self.root.ids.changeit.text = f'Ваш класс:'
        self.root.ids.log_btn.opacity = 1
        self.root.ids.log_btn.disabled = False
        self.root.ids.cards.opacity = 0
        self.root.ids.cards1.opacity = 0
        self.root.ids.cards2.opacity = 0
        self.root.ids.cards3.opacity = 0
        self.table.destroy = MDDataTable
        self.table = MDDataTable()
        self.tab = MDDataTable()
        self.root.ids.screen1.add_widget(self.table)
        self.root.ids.screen2.add_widget(self.tab)


if __name__ == '__main__':
    app = Test()
    Window.bind(on_resize=app.on_resize)
    app.run()
