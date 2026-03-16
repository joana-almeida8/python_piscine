import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.tournament_cards = []
        self.t_card = TournamentCard()

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return (f"{card.name} (ID: {card.card_id}):\n"
                "- Interfaces: [Card, Combatable, Rankable]"
                f"- Rating: {card.rating}"
                f"- Record: {card.record}")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        match_cards = []
        for card in self.tournament_cards:
            if card1_id == card.card_id:
                card1 = card 
                match_cards.append(card)
            elif card2_id == card.card_id:
                card2 = card
                match_cards.append(card)
    
        random.shuffle(match_cards)
        attacker, defender = match_cards[0], match_cards[1]

        while attacker.health > 0 and defender.health > 0:
            damage_report = attacker.attack(defender)
            defender.defend(damage_report['damage_dealt'])
            attacker, defender = defender, attacker
    
        winner = card1 if card1.health > 0 else card2
        loser = card2 if card2.health < 0 else card1
        
        winner.rating += 16
        loser.rating -= 16

        winner.update_wins(1)
        loser.update_losses(1)

        return {'winner': {winner.card_id},
                'loser': {loser.card_id},
                'winner_rating': {winner.rating},
                'loser_rating': {loser.rating}}

    def get_leaderboard(self) -> list:
        ...

    def generate_tournament_report(self) -> dict:
        ...
