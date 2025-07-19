from cards.base_card import Card


# 技能類別
class Skill:
    def __init__(self, name, damage, cost):
        """
        技能初始化。
        """
        self.name = name  # 技能名稱
        self.damage = damage  # 技能傷害值
        self.cost = cost  # 技能所需能源數量，例如：# cost = {"flame": 2, "wild": 1} 表示需要 2 個火元素或 1 個泛用元素的能源

    def __repr__(self):
        """
        取得技能說明。
        """
        return f"{self.name} - 傷害: {self.damage} / 所需能量: {self.cost}"


# 使者卡類別，繼承自基本卡片類別
class AvatarCard(Card):
    def __init__(self, name, hp, element, skills):
        """
        使者卡初始化。
        """
        super().__init__(name, "avatar")  # 使者卡卡片名稱
        self.hp = hp  # 使者卡當前生命值
        self.max_hp = hp  # 使者卡最大生命值
        self.element = element  # 使者卡元素類型
        self.attached_core = {}  # 已貼附的能源
        self.skills = []  # 使者卡技能列表
        for skill in skills:
            self.skills.append(Skill(skill["name"], skill["damage"], skill["cost"]))

    def __repr__(self):
        """
        取得使者卡的詳細資訊。

        範例輸出：
        1. 【avatar】熾炎之子 (元素：flame，HP：90/90)
            技能：
              0. 爆焰擊 - 傷害：30，耗能：flame:1
              1. 焚野爆破 - 傷害：50，耗能：flame:2, wild:1
            尚未附加任何能源
        """
        info = f"【{self.card_type}】{self.name} (元素：{self.element}，HP：{self.hp}/{self.max_hp})\n"
        info += "    技能：\n"
        for index, skill in enumerate(self.skills):
            info += f"      {index}. {skill.name} - 傷害：{skill.damage} / 所需能量:{skill.cost}\n"
        if self.attached_core:
            attached_core_str = ", ".join(
                f"{key}-{value}" for key, value in self.attached_core.items()
            )
            info += f"    已附加能源：{attached_core_str}\n"
        else:
            info += "    尚未附加任何能源"
        return info

    def take_damage(self, damage):
        """
        使者卡受到傷害。
        """
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_knocked_out(self):
        """
        檢查使者卡是否被擊倒。
        """
        return self.hp <= 0

    def attach_core(self, element):
        """
        附加能源到使者卡。
        """
        self.attached_core[element] = self.attached_core.get(element, 0) + 1
        print(f"【公告】{self.name} 附加 1 張 {element} 能源")
        return True
