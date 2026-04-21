from player import Player
from deck import Deck
from table import Table
from helper_functions import wanna_play_again
game_on = True
while game_on:
    # deciding number of cards in War
    number_of_cards_in_war = 3
    # create a new Tablw to play on
    table = Table()
    # create  a new deck for every new game
    deck = Deck()
    # Must shuffle it before distributing
    deck.deck_shuffle()
    # create 2 players: Hard-coded for this Project as Player has no choice of its own
    player1 = Player("Jatin")
    player2 = Player("Shiv")

    # split cards equallty to both of them:
    for _ in range(26):
        player1.add_card(deck.draw_one())
        player2.add_card(deck.draw_one())

    # Now lets start the game:
    while len(player1) and len(player2):
        # This loop finishes when either one or both have no Cards to draw
        # update Round Number after every draw
        table.new_round()
        print(f"\n-----------------------------------------")
        print(f"{table} : {player1.get_name()} has {len(player1)} cards : {player2.get_name()} has {len(player2)} cards\n")
        # draw cards from each player and compare:
        table.add_cards(player1.draw_cards(1), player2.draw_cards(1))
        print(f"Added 1 card from each player to table: ")
        print(
            f"Now: {player1.get_name()} has {len(player1)} cards : {player2.get_name()} has {len(player2)} cards\n")
        status = table.compare()
        print(f"------------Comparing------------")
        if status == "p1":
            # player 1 won
            print(
                f"{player1.get_name()} Won this Round and will recieve {len(table)} cards")
            player1.add_won_cards(table.draw_table_cards())
        elif status == "p2":
            # player 2 won
            print(
                f"{player2.get_name()} Won this Round and will recieve {len(table)} cards")
            player2.add_won_cards(table.draw_table_cards())
        else:
            # its a Tie and status=="tie"
            # War : Both players must add - number_of_cards_in_war- on the Table
            # check if both have sufficient war cards or not
            print(f"-------------War------------")
            if player1.has_sufficient_war_cards(number_of_cards_in_war) and player2.has_sufficient_war_cards(number_of_cards_in_war):
                # War can happen
                print(
                    f"Adding {number_of_cards_in_war} cards from both players to the table")
                table.add_cards(player1.draw_cards(number_of_cards_in_war),
                                player2.draw_cards(number_of_cards_in_war))

            elif player1.has_sufficient_war_cards(number_of_cards_in_war) and not player2.has_sufficient_war_cards(number_of_cards_in_war):
                # player 1 won
                print(
                    f"{player1.get_name()} Won the Game! as {player2.get_name()} cant fight War")
                break
            elif not player1.has_sufficient_war_cards(number_of_cards_in_war) and player2.has_sufficient_war_cards(number_of_cards_in_war):
                # player 2 won
                print(
                    f"{player2.get_name()} Won the Game! as {player1.get_name()} cant fight War")
                break
            else:
                # both dont have sufficient cards to play war:
                # Just continue single Card logic
                continue

    else:
        if not len(player1) and not len(player2):
            # both have 0 cards while table is in Tie position
            print(f"Tie:- Both Players have no cards left after multiple Ties")
        elif not len(player1) and len(player2):
            # only player1 out of cards and cant play further:
            print(f"{player2.get_name()} Won!, {player1.get_name()} out of cards")
        else:
            # player 2 is out of Cards
            print(
                f"{player1.get_name()} won the Game!, {player2.get_name()} out of cards")
            # Ask if user wants to play again:
    game_on = wanna_play_again()
