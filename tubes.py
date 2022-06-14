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

    # Process of the Lexical Analyzer
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
            st.error('ERROR')
            break;
        idx_char += 1

    # Conclusion
    if state == 'accept':
        st.write('Semua token di input: ', sentence, ', VALID')
        st.subheader('Accept')
        # Trigger the ballons
        st.balloons()

    # Process of the Parser
    tokens = sentence.lower().split()
    tokens.append('EOS')

    # Symbol definition
    non_terminals = ['S', 'NN', 'VB']
    terminals = ['lui', 'voi', 'lei', 'vestire', 'libro', 'timone', 'sedia', 'uso', 'portare', 'leggere']

    # Parse table definition
    parse_table = {}

    # For Subject (S)
    parse_table[('S', 'lui')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'voi')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'lei')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'vestire')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'libro')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'timone')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'sedia')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'uso')] = ['error']
    parse_table[('S', 'portare')] = ['error']
    parse_table[('S', 'leggere')] = ['error']
    parse_table[('S', 'EOS')] = ['error']


    # For Noun (NN)
    parse_table[('NN', 'lui')] = ['lui']
    parse_table[('NN', 'voi')] = ['voi']
    parse_table[('NN', 'lei')] = ['lei']
    parse_table[('NN', 'vestire')] = ['vestire']
    parse_table[('NN', 'libro')] = ['libro']
    parse_table[('NN', 'timone')] = ['timone']
    parse_table[('NN', 'sedia')] = ['sedia']
    parse_table[('NN', 'uso')] = ['error']
    parse_table[('NN', 'portare')] = ['error']
    parse_table[('NN', 'leggere')] = ['error']
    parse_table[('NN', 'EOS')] = ['error']

    # For Verb (VB)
    parse_table[('VB', 'lui')] = ['error']
    parse_table[('VB', 'voi')] = ['error']
    parse_table[('VB', 'lei')] = ['error']
    parse_table[('VB', 'vestire')] = ['error']
    parse_table[('VB', 'libro')] = ['error']
    parse_table[('VB', 'timone')] = ['error']
    parse_table[('VB', 'sedia')] = ['error']
    parse_table[('VB', 'uso')] = ['uso']
    parse_table[('VB', 'portare')] = ['portare']
    parse_table[('VB', 'leggere')] = ['leggere']
    parse_table[('VB', 'EOS')] = ['error']


    # Stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # Input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    # For typo input
    if symbol not in terminals:
        st.error("SALAH INPUT, MOHON PERIKSA KEMBALI")
    else:
        
        # Parsing process
        while (len(stack) > 0):
            top = stack[len(stack)-1]
            st.write("Top : ", top)
            st.write("Symbol : ", symbol)

            if top in terminals:
                st.write("Top adalah simbol terminal")

                if top == symbol:
                    stack.pop()
                    idx_token += 1
                    symbol = tokens[idx_token]

                    if symbol == 'EOS':
                        st.write("Isi stack : ", stack)
                        stack.pop()

                else:
                    st.write("error")
                    break;
            elif top in non_terminals:
                st.write("Top adalah simbol non-terminal")
                if parse_table[(top, symbol)] != 'error':
                    stack.pop()
                    symbolsToBePushed = parse_table[(top, symbol)]
                    for i in range(len(symbolsToBePushed)-1,-1,-1):
                        stack.append(symbolsToBePushed[i])
                else:
                    st.write("error")
                    break;
            else:
                st.write("error")
                break;
            
            st.write("Isi stack : ", stack)
            st.write("")

        # Conclusion
        st.write("")
        if (symbol == 'EOS') and (len(stack)== 0):
            scs = "Input string: " + '"' + sentence + '"' + " diterima, sesuai Grammar"
            st.success(scs)
        else:
            fail = "ERROR, input string: " + '"' + sentence + '"' + " tidak diterima, tidak sesuai Grammar"
            st.error(fail)
    


# Triggred by enter button
elif sentence:
    st.subheader(" ")
    st.error('MOHON GUNAKAN "Check!" BUTTON!')