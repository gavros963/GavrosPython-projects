import random

def shuffle(n):
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = deck + deck + deck + deck
    if n == 2:
        deck = deck + deck
    if n == 3:
        deck = deck + deck + deck
    if n == 4:
        deck = deck + deck + deck + deck
    random.shuffle(deck)
    return deck
print('===============')
print('===BLACKJACK===')
print('===============')
cash = 1000
bet = 0
def betting():
    global bet
    global cash
    print('You have', cash, 'amount to bet')
    bet = int(input('How much to bet?'))
    if bet > cash:
        print("Bet too high")
        bet = 0
    cash = cash - bet
    
def dealing():
    dealedcard = deck.pop()
    DealerHand.append(dealedcard)
    dealedcard = deck.pop()
    PlayerHand.append(dealedcard)
    dealedcard = deck.pop()
    DealerHand.append(dealedcard)
    dealedcard = deck.pop()
    PlayerHand.append(dealedcard)
soft = 0
def measure(n):
    global soft
    soft = 0
    hand = n
    i = 0
    count = 0
    while i < len(hand):
        if hand[i] == 'A':
            if soft == 1:
                count = count + 1
                i = i + 1
                continue
            count = count + 11
            soft = 1
            i = i + 1
            continue
        if hand[i] == 'J':
            count = count + 10
            i = i + 1
            continue
        if hand[i] == 'Q':
            count = count + 10
            i = i + 1
            continue
        if hand[i] == 'K':
            count = count + 10
            i = i + 1
            continue
        count = count + int(hand[i])
        i = i + 1
    if soft == 1:
        if count > 21:
            return count - 10
        return count
    return count

def displayHand():
    global soft
    measure(PlayerHand)
    if soft == 1:
        print('Dealers upcard:', DealerHand[1], 'Your hand:', PlayerHand, measure(PlayerHand), '/', measure(PlayerHand)-1)
    else:
        print('Dealers upcard:', DealerHand[1], 'Your hand:', PlayerHand, measure(PlayerHand))


BJWin = 0
def PlayerTurn():
    global PlayerHand
    global deck
    global bet
    global cash
    global BJWin
    turn = 'true'
    if measure(PlayerHand) == 21:
        
        bet = bet*2.5
        cash = cash + bet
        BJWin = 1
        return 
    first = 0
    while turn == 'true':
        action = input("'hit' 'stand' 'double down' or 'surrender'")
        if action == 'hit':
            dealedcard = deck.pop()
            PlayerHand.append(dealedcard)
            displayHand()
            if measure(PlayerHand) > 21:
                turn = 'false'
                break
            first = 1
        if action == 'double down':
            if cash < bet:
                print('not enough cash')
                continue
            cash = cash - bet
            bet = bet + bet
            dealedcard = deck.pop()
            PlayerHand.append(dealedcard)
            displayHand()
            turn = 'false'
            break
        if action == 'stand':
            turn = 'false'
        if action == 'surrender':
            if first == 1:
                print('illegal move')
                continue
            bet = bet/2
            cash = cash + bet
            bet = 0
            turn = 'false'
def DealerTurn():
    global deck
    global DealerHand
    turn = 'true'
    print(DealerHand, measure(DealerHand))
    while turn == 'true':
        if measure(DealerHand) <= 16:
            dealedcard = deck.pop()
            DealerHand.append(dealedcard)
            print(DealerHand, measure(DealerHand))
            if measure(DealerHand) > 21:
                turn = 'false'
                break
        else:
                turn = 'false'


escape = 0
deck = shuffle(int(input('how many decks?')))
while escape == 0:
    if len(deck) < 5:
        deck == shuffle(int(input('how many decks?')))
    betting()
    if bet == 0:
        continue
    PlayerHand = []
    DealerHand = []
    dealing()
    displayHand()
    if measure(DealerHand) == 21:
        bet = 0
        print('Dealer has BlackJack')
        escape = int(input('Wish to continue? 0 yes, 1 no.'))
        continue
    PlayerTurn()
    if BJWin == 1:
        BJWin = 0
        print('Blackjack!')
        escape = int(input('Wish to continue? 0 yes, 1 no.'))
        continue
    DealerTurn()
    if bet == 0:
        print('You Surrendered')
    if measure(PlayerHand) > 21:
        bet = 0
        print('You busted')
        escape = int(input('Wish to continue? 0 yes, 1 no.'))
        continue
    if measure(DealerHand) > 21:
        bet = bet * 2
        cash = cash + bet
        print('Dealer busts!')
        escape = int(input('Wish to continue? 0 yes, 1 no.'))
        continue
    if measure(PlayerHand) > measure(DealerHand):
        bet = bet * 2
        cash = cash + bet
        print('You win!')
        escape = int(input('Wish to continue? 0 yes, 1 no.'))
        continue
    if measure(PlayerHand) == measure(DealerHand):
        cash = bet + cash
        print('Push')
        escape = int(input('Wish to continue? 0 yes, 1 no.'))
        continue
    if measure(PlayerHand) < measure(DealerHand):
        bet = 0
        print('You lose!')
        escape = int(input('Wish to continue? 0 yes, 1 no.'))
        continue



    

