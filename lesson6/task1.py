import sys
from enum import Enum
from PyQt5 import QtWidgets, QtGui, QtCore
from threading import Event

# Размер цветных, круглых лейблов
lbl_size = 80

# Событие остановки светофора
tl_stop_event = Event()


class Color(Enum):
    """ Перечисление: цвета светофора """
    Red = 'red'
    Yellow = 'yellow'
    Green = 'green'


class TimeToSleep(Enum):
    """ Перечисление: времена задержки каждого цвета светофора """
    Red = 7
    Yellow = 2
    Green = 8


class TrafficLightWidget(QtWidgets.QWidget):
    """ Класс, описывающий виджет со светофором и кнопкой управления """

    def __init__(self):
        super().__init__()
        # Задаем внешний вид видежта
        self._init_UI()

        # Предыдущий лейбл, нужен для сброса цвета предыдущего лейбла
        self._prev_lbl = self._lbl_red
        # Объект светофора, запускаем в отдельном треде, получать от него сигналы о смене цветов
        self._traffic_light = TrafficLight()

        # Подключаем сигналы кнопок и светофора
        self._connect_signals()

    def _init_UI(self):
        """ Задает внешний вид виджета """
        # Устанавливаем название, иконку и размеры приложения -------------------------------------
        self.setWindowTitle("Светофор")
        self.setWindowIcon(QtGui.QIcon('traffic_light.svg'))
        self.setGeometry(100, 100, 500, 400)

        # Цветные, круглые лейблы -----------------------------------------------------------------
        self._lbl_red = QtWidgets.QLabel(self)
        self._lbl_yellow = QtWidgets.QLabel(self)
        self._lbl_green = QtWidgets.QLabel(self)

        # Вертикальная сетка для лейблов
        v_grid_lbls = QtWidgets.QVBoxLayout()

        # Задаем стили каждому лейблу и помещаем их в сетку v_grid_lbls
        lbls = [self._lbl_red, self._lbl_yellow, self._lbl_green]
        for lbl in lbls:
            lbl.setFixedSize(lbl_size, lbl_size)
            lbl.setStyleSheet(self._get_lbl_style())
            v_grid_lbls.addWidget(lbl)

        # Кнопка управления светофором ------------------------------------------------------------
        self._btn_start = QtWidgets.QPushButton('Старт')
        self._btn_start.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))

        # Основная сетка - горизонтальная, помещаем туда первую сетку и кнопку --------------------
        h_grid = QtWidgets.QHBoxLayout()
        h_grid.addLayout(v_grid_lbls)
        h_grid.addWidget(self._btn_start)

        # Устанавливаем основную сетку на виджет --------------------------------------------------
        self.setLayout(h_grid)

    def _get_lbl_style(self, color='grey'):
        """
        Генерирует стиль лейбла с заданным цветом
        :param color: цвет лейбла
        :type color: str
        :return: строка с css-стилями лейбла
        :type: str
        """
        return f'background-color: {color}; border-radius: {lbl_size / 2}px; border: 0.5px solid grey'

    def _get_lbl_by_color(self, color):
        """
        Возвращает лейбл по заданному цвету
        :param color: цвет
        :type: Color
        :return: лейбл, соответствующий цветцу color
        :type: QLabel
        """
        if color == Color.Red:
            return self._lbl_red
        elif color == Color.Yellow:
            return self._lbl_yellow
        else:
            return self._lbl_green

    def _connect_signals(self):
        """ Подключение сигналов к слотам """
        self._btn_start.clicked.connect(self._on_btn_start_clicked)
        self._traffic_light.color_changed.connect(self._on_color_changed)

    def _on_btn_start_clicked(self):
        """ Слот сигнала, испускающийся по клику на кноку управления светофором """
        if self._btn_start.text() == 'Старт':
            # Запуск цикла
            self._btn_start.setText('Стоп')

            # Сбрасываем внутренний флаг события остановки светофора
            tl_stop_event.clear()
            # Сбрасываем флаг остановки цикла цветов
            self._traffic_light.stop_color_loop = False
            # Сбрасываем предыдущий лейбл на самый первый
            self._prev_lbl = self._lbl_red

            # Запуск цикла цветов светофора
            self._traffic_light.start()
        else:
            # Остановка цикла
            self._btn_start.setText('Старт')

            # "Выключаем" текущий лейбл светофора
            self._prev_lbl.setStyleSheet(self._get_lbl_style())
            # Сигнализируем об остановке цветового уикла
            self._traffic_light.stop_color_loop = True

            # Устанавливаем флаг события остановки светофора
            tl_stop_event.set()

    def _on_color_changed(self, color):
        """
        Слот сигнала светофора о смене цветов
        :param color: текущий цвет светофора
        :type color: Color
        """
        # Сбрасываем цвет предыдущего лейбла ("отключаем" его)
        self._prev_lbl.setStyleSheet(self._get_lbl_style())

        # Получаем текущий лейбл по цвету светофора
        cur_lbl = self._get_lbl_by_color(color)
        # "Включаем" текущий лейбл - задаем ему нужный цвет
        cur_lbl.setStyleSheet(self._get_lbl_style(color.value))

        # Запоминаем текущий лейбл в качестве предыдущего для следующего цвета
        self._prev_lbl = cur_lbl


class TrafficLight(QtCore.QThread):
    """ Класс, описывающий объект 'Светофор' """

    # Сигнал о смене цвета
    color_changed = QtCore.pyqtSignal(object)

    # Список цветов светофора
    __colors = [Color.Red, Color.Yellow, Color.Green, Color.Yellow]
    # Список времен задержки каждого цвета светофора
    __times = [TimeToSleep.Red, TimeToSleep.Yellow, TimeToSleep.Green, TimeToSleep.Yellow]

    def __init__(self):
        super(TrafficLight, self).__init__()
        # Остановить ли цикл цветов светофора
        self.stop_color_loop = False

    def run(self):
        while not tl_stop_event.is_set():
            for color, time_to_sleep in zip(self.__colors, self.__times):
                if self.stop_color_loop:
                    return

                self.color_changed.emit(color)
                tl_stop_event.wait(time_to_sleep.value)


def main():
    """
    Основная функция
    Создает приложение со светофором и кнопками включения и выключения цикла цветов у светофора
    """
    tl_app = QtWidgets.QApplication(sys.argv)

    tl_widget = TrafficLightWidget()
    tl_widget.show()

    tl_app.exec()


main()
