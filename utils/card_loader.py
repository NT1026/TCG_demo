import json
from cards.avatar_card import AvatarCard
from cards.core_card import CoreCard


def load_deck_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        raw_cards = json.load(f)

    deck = []
    for card in raw_cards:
        if card["type"] == "avatar":
            deck.append(
                AvatarCard(
                    name=card["name"],
                    hp=card["hp"],
                    element=card["element"],
                    skills=card["skills"],
                )
            )
        elif card["type"] == "core":
            deck.append(CoreCard(element=card["element"]))
        elif card["type"] == "rune":
            # TODO
            pass
        else:
            print(f"未知卡片類型：{card}")
    return deck
