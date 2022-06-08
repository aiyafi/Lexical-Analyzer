import streamlit as st
import string

# Title
st.title("ITALIAN")

# Header
st.header("Lexical Analyzer and Grammar Checker")

# Caption
st.caption("By 1301200362, 1301204238, 1301204407")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("##### Subjects")
    st.markdown("- lui (he)")
    st.markdown("- voi (you)")
    st.markdown("- lei (she)")

with col2:
    st.markdown("##### Verbs")
    st.markdown("- uso (use)")
    st.markdown("- portare (bring)")
    st.markdown("- leggere (read)")

with col3:
    st.markdown("##### Nouns")
    st.markdown("- vestire (shirt)")
    st.markdown("- libro (book)")
    st.markdown("- timone (helmet)")
    st.markdown("- sedia (chair) ")

# Input example
sentence = st.text_input("Input sentence: ")

# Button check
checker = st.button("Check!")
st.write(" ")

# Lexical analyzer
# Triggers the checker button by click the button
if checker:
    input_string = sentence.lower() + '#'

    # Initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    # Spaces before input string
    transition_table['1', ' '] = '1'

    # Update the transition table for the following token: 'lui'
    transition_table[('1', 'l')] = '2'
    transition_table[('2', 'u')] = '3'
    transition_table[('3', 'i')] = '25'
    transition_table[('25', ' ')] = '26'
    transition_table[('25', '#')] = 'accept'
    transition_table[('26', ' ')] = '26'
    transition_table[('26', '#')] = 'accept'

    # Transition tabble 'lei'
    transition_table[('2', 'e')] = '3'

    # Transition tabble 'libro'
    transition_table[('2', 'i')] = '5'
    transition_table[('5', 'b')] = '6'

    # Update the transition table for the following token: 'leggere'
    transition_table[('3', 'g')] = '4'
    transition_table[('4', 'g')] = '4'
    transition_table[('4', 'e')] = '6'

    # Update the transition table for the following token: 'voi'
    transition_table[('1', 'v')] = '8'
    transition_table[('8', 'o')] = '3'

    # Update the transition table for the following token: 'uso'
    transition_table[('1', 'u')] = '12'
    transition_table[('12', 's')] = '7'
    transition_table[('7', 'o')] = '25'

    # Update the transition table for the following token: 'vestire'
    transition_table[('1', 'v')] = '8'
    transition_table[('8', 'e')] = '9'
    transition_table[('9', 's')] = '10'
    transition_table[('10', 't')] = '11'
    transition_table[('11', 'i')] = '6'
    transition_table[('6', 'r')] = '7'
    transition_table[('7', 'e')] = '25'

    # Update the transition table for the following token: 'portare'
    transition_table[('1', 'p')] = '13'
    transition_table[('13', 'o')] = '14'
    transition_table[('14', 'r')] = '15'
    transition_table[('15', 't')] = '16'
    transition_table[('16', 'a')] = '6'

    # Update the transition table for the following token: 'timone'
    transition_table[('1', 't')] = '17'
    transition_table[('17', 'i')] = '18'
    transition_table[('18', 'm')] = '19'
    transition_table[('19', 'o')] = '20'
    transition_table[('20', 'n')] = '7'

    # Update the transition table for the following token: 'sedia'
    transition_table[('1', 's')] = '21'
    transition_table[('21', 'e')] = '22'
    transition_table[('22', 'd')] = '23'
    transition_table[('23', 'i')] = '24'
    transition_table[('24', 'a')] = '25'

    # Transition for new token
    transition_table[('26', 'l')] = '2'
    transition_table[('26', 'v')] = '8'
    transition_table[('26', 'u')] = '12'
    transition_table[('26', 'p')] = '13'
    transition_table[('26', 't')] = '17'
    transition_table[('26', 's')] = '21'

    # Lexical analysis
    idx_char = 0
    state = '1'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == '25':
            
            st.write('Current token: ', current_token, ', VALID')
            current_token = ''
        if state == 'error':
            st.write('error')
            break;
        idx_char += 1

    # Conclusion
    if state == 'accept':
        st.write('Semua token di input: ', sentence, ', VALID')
        st.subheader('Accept')
        # Trigger the ballons
        st.balloons()

# Triggred by enter button
elif sentence:
    st.subheader(" ")
    st.error('MOHON GUNAKAN "Check!" BUTTON!')