import random
import time
from cards.avatar_card import AvatarCard
from cards.core_card import CoreCard


class Player:
    def __init__(self, name, deck):
        self.name = name  # 玩家名稱
        self.deck = deck  # 玩家牌組
        self.hand = []  # 玩家手牌
        self.active_avatar = None  # 主戰使者
        self.num_of_avatar_is_knocked_out = 0  # 被擊倒的使者數量

    def shuffle_deck(self):
        """
        洗牌。
        """
        random.shuffle(self.deck)
        print(f"【公告】{self.name} 的牌組已洗牌！")
        return

    def draw_starting_hand(self, count=5):
        """
        抽起始手牌。
        """
        print(f"【公告】{self.name} 抽取 {count} 張起始手牌。")
        self.draw_avatar_card()  # 確保至少抽一張使者牌
        for _ in range(count - 1):
            self.draw_card()
        return

    def draw_avatar_card(self):
        """
        抽一張使者牌。
        """
        avatar_cards = [card for card in self.deck if isinstance(card, AvatarCard)]
        if avatar_cards:
            card = avatar_cards[0]
            self.deck.remove(card)
            self.hand.append(card)
            print(f"【公告】{self.name} 抽了 1 張使者牌。")
        return

    def draw_card(self):
        """
        抽一張牌。
        """
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            print(f"【公告】{self.name} 抽了 1 張牌。")
            time.sleep(0.5)
        else:
            print(f"【公告】{self.name} 的牌堆已空，無法抽牌。")
            time.sleep(0.5)
        return

    def show_hand(self):
        """
        顯示手牌。
        """
        print(f"【公告】顯示 {self.name} 的手牌：\n")
        for index, card in enumerate(self.hand):
            print(f"{index}. {card}")
        time.sleep(0.5)
        return

    def choose_active_avatar(self):
        """
        選擇主戰使者。
        """
        print(f"【公告】{self.name} 請選擇主戰使者。")
        avatar_indexes = [
            index
            for index, card in enumerate(self.hand)
            if isinstance(card, AvatarCard)
        ]
        if not avatar_indexes:
            print(f"【公告】{self.name} 手牌中無使者卡可用。")
            time.sleep(0.5)
            self.avatar = None
            return

        for index in avatar_indexes:
            print(f"{index}. {self.hand[index]}")

        while True:
            try:
                choice = int(input(f"{'*' * 10}\n【輸入】請輸入使者卡編號："))
                if choice in avatar_indexes:
                    self.active_avatar = self.hand.pop(choice)
                    print(
                        f"{'*' * 10}\n【公告】{self.name} 的主戰使者已決定為：\n{self.active_avatar}"
                    )
                    time.sleep(0.5)
                    return
                else:
                    print(f"{'*' * 10}\n【警告】請選擇有效的使者卡。")
            except:
                print(f"{'*' * 10}\n【警告】輸入錯誤，請輸入有效的編號。")

    def replace_avatar_if_knocked_out(self):
        """
        如果主戰使者被擊倒，則從手牌選擇新的主戰使者。
        """
        if not self.active_avatar:
            print(f"【公告】{self.name} 的主戰使者已被擊倒，請選擇新的主戰使者。")
            time.sleep(0.5)
            self.choose_active_avatar()
        else:
            print(f"【公告】{self.name} 目前的主戰使者為：\n\n{self.active_avatar}")
            time.sleep(0.5)
        return

    def attach_core(self):
        """
        貼附能源卡到主戰使者。
        """
        if not self.active_avatar:
            print(f"{'*' * 10}\n【公告】尚未設定主戰使者，無法貼附能源。")
            time.sleep(0.5)
            return

        core_indexes = [
            index for index, card in enumerate(self.hand) if isinstance(card, CoreCard)
        ]
        if not core_indexes:
            print(f"{'*' * 10}\n【公告】手牌中沒有能源卡可貼。")
            time.sleep(0.5)
            return

        for index in core_indexes:
            print(f"{index}. {self.hand[index]}")

        while True:
            try:
                choice = int(
                    input(f"{'*' * 10}\n【輸入】選擇要貼的能源編號 (輸入 -1 跳過、輸入 -2 顯示手牌)：")
                )
                if choice == -1:
                    return
                if choice == -2:
                    self.show_hand()
                    continue
                if choice in core_indexes:
                    card = self.hand.pop(choice)
                    self.active_avatar.attach_core(card.element)
                    return
                else:
                    print(f"{'*' * 10}\n【警告】請選擇有效能源卡。")
            except:
                print(f"{'*' * 10}\n【警告】輸入錯誤，請輸入有效的編號。")

    def attack(self, opponent):
        """
        發動技能攻擊對手的主戰使者。
        """
        print(f"對手 {opponent.name} 的主戰使者為：\n\n{opponent.active_avatar}")
        time.sleep(0.5)

        print(
            f"{'*' * 10}\n【公告】{self.name} 的 {self.active_avatar.name} 準備攻擊。\n{self.active_avatar}"
        )
        time.sleep(0.5)

        while True:
            try:
                choice = int(
                    input(f"{'*' * 10}\n【輸入】請選擇要使用的技能編號 (輸入 -1 跳過攻擊階段)：")
                )
                if choice == -1:
                    return
                if 0 <= choice < len(self.active_avatar.skills):
                    skill = self.active_avatar.skills[choice]
                    if self.can_use_skill(skill):
                        opponent.active_avatar.take_damage(skill.damage)
                        print(
                            f"{'*' * 10}\n【公告】自己 {self.active_avatar.name} 使用 {skill.name} 對 {opponent.name} 的 {opponent.active_avatar.name} 造成 {skill.damage} 傷害！"
                        )
                        time.sleep(0.5)
                        print(
                            f"【公告】對手 {opponent.name} 的 {opponent.active_avatar.name} 狀態如下：\n\n{opponent.active_avatar}\n"
                        )
                        time.sleep(0.5)

                        if opponent.active_avatar.is_knocked_out():
                            opponent.num_of_avatar_is_knocked_out += 1
                            print(
                                f"【公告】對手 {opponent.name} 的 {opponent.active_avatar.name} 已被擊倒！"
                            )
                            print(
                                f"【公告】對手 {opponent.name} 已有 {opponent.num_of_avatar_is_knocked_out} 張使者被擊倒。"
                            )
                            opponent.active_avatar = None
                            time.sleep(0.5)
                        else:
                            print(
                                f"【公告】對手 {opponent.name} 的 {opponent.active_avatar.name} 仍然存活。"
                            )
                        return
                    else:
                        print(f"{'*' * 10}\n【警告】能量不足，無法使用此技能。")
                else:
                    print(f"{'*' * 10}\n【警告】請選擇有效技能。")
            except Exception as e:
                print(e)
                print(f"{'*' * 10}\n【警告】輸入錯誤，請輸入有效的編號。")

    def can_use_skill(self, skill):
        """
        檢查是否可以使用技能。
        """
        attached = self.active_avatar.attached_core

        # 檢查是否滿足 cost
        for element, required in skill.cost.items():
            available = attached.get(element, 0)
            if available >= required:
                break
            else:
                continue
        else:
            return False
        return True

    def has_active_avatar(self):
        """
        檢查玩家是否有主戰使者。
        """
        if self.active_avatar and self.active_avatar.hp > 0:
            return True
        return False

    def has_avatar_in_hand(self):
        """
        檢查玩家是否有使者在手牌。
        """
        for card in self.hand:
            if isinstance(card, AvatarCard):
                return True
        return False
