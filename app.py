import streamlit as st
import rapidfuzz

# Set the page configuration with a new title and favicon
st.set_page_config(
    page_title="Pio-Tech Fuzzy Similarity",  # Change to your desired name
    # page_icon="piotechlogo.ico",  # Change to your favicon path
    layout="centered"  # You can set the layout as 'centered' or 'wide'
)

# Display the logo
# logo_path = "piotechlogo.png"  # Replace with your logo path
#st.image(logo_path, width=200)  # Adjust width as needed

# Add company logo
# st.image("pio-tech logo.png", use_column_width=True)

# Add a title for the app with larger font size
st.markdown("<h1 style='text-align: center; color: #2b6179;'>Fuzzy String Similarity Comparison</h1>", unsafe_allow_html=True)

# Create two sections for input text fields with bold labels
st.markdown("### Enter Texts to Compare")
name1 = st.text_input("Text 1")
name2 = st.text_input("Text 2")

# Add a button to trigger the comparison
if st.button("Compare"):
    st.markdown("### **Results**")

    # Create two columns for percentage-based metrics
    col1, col2 = st.columns(2)

    # Token Sort Ratio
    fz_tsortr = rapidfuzz.fuzz.token_sort_ratio(name1, name2, processor=rapidfuzz.utils.default_process)
    with col1:
        st.markdown(
            f'<div style="font-size:20px;"><strong>Token Sort Ratio: </strong>'
            f'<span style="color:#2b6179;"><strong>{round(fz_tsortr)}%</strong></span></div>',
            unsafe_allow_html=True
        )

    # Token Set Ratio
    fz_tsetr = rapidfuzz.fuzz.token_set_ratio(name1, name2, processor=rapidfuzz.utils.default_process)
    with col2:
        st.markdown(
            f'<div style="font-size:20px;"><strong>Token Set Ratio: </strong>'
            f'<span style="color:#2b6179;"><strong>{round(fz_tsetr)}%</strong></span></div>',
            unsafe_allow_html=True
        )

    # Create two columns for distance-based metrics
    col3, col4 = st.columns(2)

    # Levenshtein Distance (keeping as is, since it’s not a percentage)
    lv_dis = rapidfuzz.distance.Levenshtein.distance(name1, name2, processor=rapidfuzz.utils.default_process)
    with col3:
        st.markdown(
            f'<div style="font-size:20px;"><strong>Levenshtein Distance: </strong>'
            f'<span style="color:#2b6179;">{lv_dis}</span></div>',
            unsafe_allow_html=True
        )

    # Indel Distance (keeping as is, since it’s not a percentage)
    indel_dis = rapidfuzz.distance.Indel.distance(name1, name2, processor=rapidfuzz.utils.default_process)
    with col4:
        st.markdown(
            f'<div style="font-size:20px;"><strong>Indel Distance: </strong>'
            f'<span style="color:#2b6179;">{indel_dis}</span></div>',
            unsafe_allow_html=True
        )



    # # Normalized Indel Similarity
    # norm_indel_dis = rapidfuzz.distance.Indel.normalized_similarity(name1, name2, processor=rapidfuzz.utils.default_process)
    # annotated_text(
    #     ("Normalized Indel Similarity", f"**{round(norm_indel_dis)}%**", "#FCF8E3", "24px")
    # )

    # Explanation for Token Sort Ratio Calculation
    st.markdown("#### **Token Sort Ratio Calculation Breakdown**")
    
    with st.container(border=True):
        # Step 1: Show token list of each name (using rapidfuzz default processing)
        name1_tokens = rapidfuzz.utils.default_process(name1).split()
        name2_tokens = rapidfuzz.utils.default_process(name2).split()
        
        st.subheader("1. Tokenizing", divider="blue")
        
        st.markdown(f"**Tokens of Text 1**: `{name1_tokens}`")
        st.markdown(f"**Tokens of Text 2**: `{name2_tokens}`")
        
    
        # Step 2: Sort the token list of each name
        sorted_name1_tokens = sorted(name1_tokens)
        sorted_name2_tokens = sorted(name2_tokens)
        
        st.subheader("2. Sorting", divider="blue")
        
        st.markdown(f"**Sorted Tokens of Text 1**: `{sorted_name1_tokens}`")
        st.markdown(f"**Sorted Tokens of Text 2**: `{sorted_name2_tokens}`")
    
        # Step 3: Rejoining sorted tokens
        sorted_name1 = ' '.join(sorted_name1_tokens)
        sorted_name2 = ' '.join(sorted_name2_tokens)
        
        st.subheader("3. Rejoin Sorted Tokens", divider="blue")
        
        st.markdown(f"**Sorted Text 1**: '{sorted_name1}'")
        st.markdown(f"**Sorted Text 2**: '{sorted_name2}'")

    
        # Step 4: Calculate Indel distance between the sorted token strings
        indel_distance = rapidfuzz.distance.Indel.distance(sorted_name1, sorted_name2)
        
        st.subheader("4. Calculate matching ratio", divider="blue")
        
        st.markdown(f"**Indel Distance between Sorted Tokens**: `{indel_distance}`")
    
        # Step 5: Show the lengths of name1 and name2
        len_name1 = len(sorted_name1)
        len_name2 = len(sorted_name2)
        
        st.markdown(f"**Length of Sorted Text 1**: `{len_name1}`")
        st.markdown(f"**Length of Sorted Text 2**: `{len_name2}`")
    
        # Step 6: Calculate the Token Sort Ratio manually using the formula
        try:
            token_sort_ratio_manual = 100 - (indel_distance / (len_name1 + len_name2)) * 100
            st.latex(r"""
                \text{Token Sort Ratio = } 
                100 - \left(\frac{\text{Indel Distance}}{\text{Length of Text 1} + \text{Length of Text 2}}\right) \times 100
                """)
            st.latex(rf"""
                \text{{Token Sort Ratio = }} 
                100 - \left(\frac{{{indel_distance}}}{{{len_name1} + {len_name2}}}\right) \times 100
                """)
            
            # st.markdown(f"**Manual Token Sort Ratio Calculation**: `100 - (Indel Distance / (Length of Text 1 + Length of Text 2)) * 100`")
            # st.markdown(f"**Manual Token Sort Ratio Calculation**: `100 - ({indel_distance} / {len_name1} + {len_name2}) * 100`")
            st.markdown(f"**Manual Token Sort Ratio Result**: `{round(token_sort_ratio_manual)}%`")
        except Exception as e:
            st.error(f"Error: {e}")

 # Footer
    st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p>Powered by <a href='https://www.pio-tech.com/' target='_blank'>Pio-Tech</a></p>
    </div>
    """, unsafe_allow_html=True)