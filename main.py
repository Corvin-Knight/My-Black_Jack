import streamlit as st
import random

# --- CONFIG & ASSETS ---
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# --- HELPER FUNCTIONS ---
def deal_card():
    card = random.choice(cards)
    return card

def ace_check(hand):
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return hand

# --- SESSION STATE (Game Memory) ---
if 'player_hand' not in st.session_state:
    st.session_state.player_hand = []
    st.session_state.computer_hand = []
    st.session_state.game_active = False
    st.session_state.message = ""

# --- GAME LOGIC ---
def start_new_game():
    st.session_state.player_hand = [deal_card(), deal_card()]
    st.session_state.computer_hand = [deal_card(), deal_card()]
    st.session_state.player_hand = ace_check(st.session_state.player_hand)
    st.session_state.computer_hand = ace_check(st.session_state.computer_hand)
    st.session_state.game_active = True
    st.session_state.message = ""

def hit():
    st.session_state.player_hand.append(deal_card())
    st.session_state.player_hand = ace_check(st.session_state.player_hand)
    if sum(st.session_state.player_hand) > 21:
        st.session_state.game_active = False
        st.session_state.message = f"You busted with {sum(st.session_state.player_hand)}! You lose."

def stand():
    st.session_state.game_active = False
    # Dealer hits until 17
    while sum(st.session_state.computer_hand) < 17:
        st.session_state.computer_hand.append(deal_card())
        st.session_state.computer_hand = ace_check(st.session_state.computer_hand)
    
    p_score = sum(st.session_state.player_hand)
    c_score = sum(st.session_state.computer_hand)
    
    if c_score > 21:
        st.session_state.message = "Computer busted! You win!"
    elif p_score > c_score:
        st.session_state.message = f"You win with {p_score} vs {c_score}!"
    elif p_score == c_score:
        st.session_state.message = f"It's a draw! Both have {p_score}."
    else:
        st.session_state.message = f"You lose! Computer has {c_score}."

# --- UI LAYOUT ---
st.title("🎰 Blackjack")

if st.button("New Game"):
    start_new_game()

if st.session_state.player_hand:
    st.divider()
    
    # Display Player Info
    st.subheader(f"Your Hand: {sum(st.session_state.player_hand)}")
    st.write(st.session_state.player_hand)
    
    # Display Computer Info
    st.subheader("Computer's Hand")
    if st.session_state.game_active:
        # Show only first card during play
        st.write([st.session_state.computer_hand[0], "??"])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Hit"):
                hit()
                st.rerun()
        with col2:
            if st.button("Stand"):
                stand()
                st.rerun()
    else:
        # Reveal full hand when game is over
        st.write(st.session_state.computer_hand)
        st.info(st.session_state.message)