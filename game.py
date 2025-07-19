class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player_index = 0
        self.turn_count = 1
        self.game_over = False

    def start(self):
        """
        開始遊戲，雙方洗牌並抽起始手牌，選擇初始主戰使者。
        """
        print(f"{'*' * 10}\n【公告】{self.players[0].name} vs {self.players[1].name}")
        print(f"【公告】遊戲開始！")
        self.shuffle_and_draw()
        self.select_starting_avatars()

        while not self.game_over:
            self.play_turn()

    def shuffle_and_draw(self):
        """
        雙方洗牌並抽起始手牌。
        """
        for player in self.players:
            print("*" * 10)
            player.shuffle_deck()
            player.draw_starting_hand()

    def select_starting_avatars(self):
        """
        雙方選擇初始主戰使者。
        """
        print(f"{'*' * 10}\n【公告】雙方選擇初始主戰使者。")
        for player in self.players:
            print("*" * 10)
            player.choose_active_avatar()

    def play_turn(self):
        """
        執行當前玩家 (current_player) 的回合。
        """
        current = self.players[self.current_player_index]
        opponent = self.players[1 - self.current_player_index]

        print(f"{'*' * 10}\n【公告】回合 {self.turn_count}：{current.name} 的回合。")
        print(f"{'*' * 10}\n【公告】進入 {current.name} 的抽牌階段。")
        current.draw_card()

        print(f"{'*' * 10}\n【公告】進入 {current.name} 的補位階段。")
        current.replace_avatar_if_knocked_out()

        print(f"{'*' * 10}\n【公告】進入 {current.name} 的資源階段。")
        current.attach_core()

        print(f"{'*' * 10}\n【公告】進入 {current.name} 的行動階段。\n{'*' * 10}")
        current.attack(opponent)

        print(f"{'*' * 10}\n【公告】{current.name} 的回合結束。")

        self.check_game_over()
        self.current_player_index = 1 - self.current_player_index
        self.turn_count += 1

    def check_game_over(self):
        """
        檢查遊戲是否結束。
        """
        for player in self.players:
            if not player.deck:
                print(f"{'*' * 10}\n【公告】{player.name} 的牌庫已經空了，無法抽牌！")
                print(
                    f"【公告】{self.players[1 - self.players.index(player)].name} 獲勝！\n{'*' * 10}"
                )
                self.game_over = True
                return
            if not player.has_active_avatar() and not player.has_avatar_in_hand():
                print(
                    f"{'*' * 10}\n【公告】{player.name} 的主戰使者已被擊倒，且手牌無其他使者卡！"
                )
                print(
                    f"【公告】{self.players[1 - self.players.index(player)].name} 獲勝！\n{'*' * 10}"
                )
                self.game_over = True
                return

            if player.num_of_avatar_is_knocked_out >= 2:
                print(f"{'*' * 10}\n【公告】{player.name} 的主戰使者已被擊倒超過 2 次！")
                print(
                    f"【公告】{self.players[1 - self.players.index(player)].name} 獲勝！\n{'*' * 10}"
                )
                self.game_over = True
                return
