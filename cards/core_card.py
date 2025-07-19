from cards.base_card import Card


# 能源卡類別，繼承自基本卡片類別
class CoreCard(Card):
    def __init__(self, element):
        """
        能源卡初始化。
        """
        element_names = {
            "flame": "火",
            "aqua": "水",
            "terra": "土",
            "storm": "風",
            "wild": "泛用",
        }
        super().__init__(f"{element_names[element]} 核心", "core")
        self.element = (
            element  # 能源類型：火 flame、水 aqua、土 terra、風 storm、泛用 wild
        )

    def __repr__(self):
        """
        取得能源卡的詳細資訊。

        範例輸出：
        1. 【core】火 核心
        """
        return f"【{self.card_type}】{self.name}"
