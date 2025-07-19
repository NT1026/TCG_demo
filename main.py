from game import Game
from player import Player
from utils.card_loader import load_deck_from_file


def main():
    print("歡迎來到【Element Clash：元素衝突】！")

    # 輸入玩家名稱
    # name1 = input("請輸入玩家 1 名稱：")
    # name2 = input("請輸入玩家 2 名稱：")
    name1 = "nt1026"
    name2 = "simon"

    # 載入牌組
    deck1 = load_deck_from_file("data/cards_player.json")
    deck2 = load_deck_from_file("data/cards_player.json")

    # 載入玩家
    player1 = Player(name1, deck1)
    player2 = Player(name2, deck2)

    # 開始遊戲
    game = Game(player1, player2)
    game.start()


if __name__ == "__main__":
    main()
