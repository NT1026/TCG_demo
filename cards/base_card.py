# 基本卡片類別
class Card:
    def __init__(self, name, card_type):
        """
        初始化卡片名稱及類型。
        """
        self.name = name  # 卡片名稱
        self.card_type = card_type  # 卡片類型 (使者卡 avatar、能源卡 core、符文卡 rune)
