from cards.base_card import Card


# 符文卡類別，繼承自基本卡片類別
class RuneCard(Card):
    # 初始化卡片
    def __init__(self, name, effect):
        super().__init__(name, "rune")
        self.effect = effect  # 函式 (TODO)
    
    # 取得符文卡的詳細資訊
    def __repr__(self):
        return f"RuneCard(name={self.name}, effect={self.effect})"