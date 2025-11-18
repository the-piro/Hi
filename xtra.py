from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Btn:
    def __init__(self):
        self._button = []
        self._header_button = []
        self._footer_button = []

    def data_button(self, key, data, position=None):
        btn = InlineKeyboardButton(text=key, callback_data=data)
        if not position:
            self._button.append(btn)
        elif position == "header":
            self._header_button.append(btn)
        elif position == "footer":
            self._footer_button.append(btn)

    def url_button(self, key, url, position=None):
        btn = InlineKeyboardButton(text=key, url=url)
        if not position:
            self._button.append(btn)
        elif position == "header":
            self._header_button.append(btn)
        elif position == "footer":
            self._footer_button.append(btn)

    def new_row(self):
        self._button.append(None)

    def build_menu(self, b_cols=2, h_cols=8, f_cols=8):
        menu = []
        row = []
        for btn in self._button:
            if btn is None:
                if row:
                    menu.append(row)
                row = []
            else:
                row.append(btn)
                if len(row) == b_cols:
                    menu.append(row)
                    row = []
        if row:
            menu.append(row)
        if self._header_button:
            menu.insert(0, self._header_button)
        if self._footer_button:
            menu.append(self._footer_button)
        return InlineKeyboardMarkup(menu)
