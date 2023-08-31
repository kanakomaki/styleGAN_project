import streamlit as st
from PIL import Image
import os
import re
from style_clip import style_clip, image_generator, save_image
from main import main



# Paths
##########################################################################################################################
output_path = './'
##########################################################################################################################

# Images paths
##########################################################################################################################
def catch_images_name(output_path):
    images=sorted(os.listdir(output_path))
    images_name = [re.sub('\.jpg$', '', image) for image in images if image.endswith(".jpg")]
    return images_name
##########################################################################################################################

# Page setup
##########################################################################################################################
#st.set_page_config(layout="wide")
st.set_page_config(layout="wide")

# Background color
page_bg_img= """<style> [data-testid=stAppViewContainer] {background-color:#FFFFFF;
                opacity:0.8; margin-top: -130px} </style> """
st.markdown(page_bg_img, unsafe_allow_html=True)
#e5e5f7
#d4e4dc
#FFFFFF




# Button behavior setup
##########################################################################################################################
if 'upload_clicked' not in st.session_state:
    st.session_state.upload_clicked = False
def click_upload_button():
    st.session_state.upload_clicked = True
def unclick_upload_button():
    st.session_state.upload_clicked = False

if 'generate_clicked' not in st.session_state:
    st.session_state.generate_clicked = False
def click_generate_button():
    st.session_state.generate_clicked = True
def unclick_generate_button():
    st.session_state.generate_clicked = False

def click_accept_button():
    st.session_state.image2.save('0.0.jpg')
    for img in st.session_state.images_in_folder:
        if img != '0.0':
            os.remove(f'{img}.jpg')
    pass
##########################################################################################################################


# Color configuration
##########################################################################################################################
##########################################################################################################################

# Slider Color Change
##########################################################################################################################
ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    background: rgb(1 1 0 / 0%); } </style>''', unsafe_allow_html = True)


Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: rgb(255, 0, 0); box-shadow: rgb(255 0 0 / 100%) 0px 0px 0px 0.1rem;} </style>''', unsafe_allow_html = True)

col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
    background: linear-gradient(to right, rgb(1, 183, 158) 0%,
                                rgb(1, 183, 158)0%,
                                rgba(151, 166, 195, 0.25)0%,
                                rgba(151, 166, 195, 0.25) 100%); }} </style>'''

ColorSlider = st.markdown(col, unsafe_allow_html = True)
##########################################################################################################################


tabs_font_css = """
                <style>
                .css-q8sbsg.e1nzilvr5 {
                font-size: 30px;
                color: black;
                }

                </style>
                """

st.write(tabs_font_css, unsafe_allow_html=True)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.3rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)








# Main function
##########################################################
def main2():
    tab1, tab2, tab3 = st.tabs(["Home", "Demo", "Contacts"])

    # Home page
    #############################
    with tab1:
        st.markdown("""
                    <style>
                    #tabs-bui3-tabpanel-0 .css-1kyxreq.e115fcil2{
                        display: flex;
                        aligh-items: center;
                        justify-content: center;
                        margin-top: 150px;
                    }
                    #tabs-bui3-tabpanel-0 .css-1v0mbdj.e115fcil1 img {
                        display: flex;
                        width: 1000px;
                        height: 200px;
                        margin-top: 75px;
                    }

                    </style>
                    """, unsafe_allow_html=True)

        st.image("./images/logo-ai-2.png", width=500)
        #st.markdown("<h1 style='text-align: center; color: black;'>Welcome to AIdentikit</h1>", unsafe_allow_html=True)
        #st.markdown("<h5 style='text-align: center; color: black;'>An identikit or an identikit picture is a drawing of the face of someone the police want to question. It is made from descriptions given to them by witnesses to a crime.</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: black;'>An identikit or an identikit picture is a drawing of the face of someone the police want to question.</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: black;'>It is made from descriptions given to them by witnesses to a crime.</h5>", unsafe_allow_html=True)
    #############################

# Features to search a image:
#     5oClock Shadow, male, pale skin, young

# Features to change image:
#forehead
#beard
#wrinkle
#more beard
#glasses




    # Demo page
    #############################
    with tab2:
        # Input and Output text - Page - Put the text input in here
        ########################################################
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                #st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)
                #st.markdown('<p class="big-font">Input image</p>', unsafe_allow_html=True)
                #text_input1 = st.text_input("Describe",key='placeholder')
                st.markdown("<h3 style='color: black;'>Describe the features of a person you are looking for:</h3>", unsafe_allow_html=True)
                text_input1 = st.text_input("Describe the features of a person you are looking for:", label_visibility='collapsed')
                st.button('Search image', on_click=click_upload_button)

            with col2:
                #st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)
                #st.markdown('<p class="big-font">Output image</p>', unsafe_allow_html=True)
                #text_input2 = st.text_input("Enter",key='placeholder')
                st.markdown("<h3 style='color: black;'>Enter the feature you want to change:</h3>", unsafe_allow_html=True)
                text_input2 = st.text_input("Enter the feature you want to change:", label_visibility='collapsed') #disabled=st.session_state.disabled)
                #text_input2 = st.text_input("Enter the feature you want to change:") #disabled=st.session_state.disabled)
                st.button('Modify image', on_click=click_generate_button)

        ##########################################################################################################################

        # To create a image
        ##########################################################################################################################
        with st.container():
            # Create two columns with equal width
            col1, col2 = st.columns(2)

            if text_input1 and st.session_state.upload_clicked:
                st.session_state.original_image = '0.0.jpg'

                original_test = main(text_input1)
                output = image_generator(image=original_test, target='hair', manipulation=0.0)
                st.session_state.output_image = save_image(link=output, manipulation=0.0)

                # Original image
                #############################################################
            try:
                with col1:
                    image1 = Image.open('0.0.jpg') # return from previous part
                    disabled=st.session_state
                    #st.image(image1, use_column_width=True)
                    st.image(image1, width=500)
                    with open('0.0.jpg', "rb") as file:
                        st.download_button(label="Download", data=file,
                                        file_name="download_image.png", mime="image/png")
            except:
                pass

            if text_input1 and text_input2 and st.session_state.generate_clicked:
                # Call style_clip and web_load_images
                manipulation_strength = [4.5]
                style_clip(original_image_path=st.session_state.original_image, target=text_input2, manipulation_strength=manipulation_strength)

            # Sidebar part 2
            #############################################################

            st.session_state.images_in_folder = catch_images_name(output_path)
            if len(st.session_state.images_in_folder) > 1:
                # Generated image
                #############################################################
                with col2:
                    st.session_state.image2 = Image.open('4.5.jpg')
                    #st.image(st.session_state.image2, use_column_width=True)
                    st.image(st.session_state.image2, width=500)
                    #st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)
                    #st.markdown("<h3 style='color: black;'>Do you like this image?</h3>", unsafe_allow_html=True)
                    st.button('Change more features', on_click=click_accept_button)

            unclick_upload_button()
            unclick_generate_button()

        ##########################################################################################################################

    with tab3:
        with st.container():
            st.markdown("<h1 style='text-align: center; font-size:50px; color: black;'>Thank you for visiting!</h1>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<h2 style='text-align: center; color: black;'>Our team</h2>", unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown("""
                    <style>
                    #tabs-bui3-tabpanel-2 .css-1v0mbdj.e115fcil1 {
                        width: 200px;
                        height: 200px;
                        border-radius: 50%;
                        overflow: hidden;
                        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
                    }
                    #tabs-bui3-tabpanel-2 .css-1v0mbdj.e115fcil1 img {
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                    }
                    </style>
                    """, unsafe_allow_html=True)

                st.image("./images/shiori.jpeg", width=200)
                st.markdown("<h3 style='color: black;'>Shiori Miwa</h3>", unsafe_allow_html=True)
                #st.markdown("<h3 style='color: black;'>Manager</h3>", unsafe_allow_html=True)
            with col2:
                st.image("./images/kanae.jpeg", width=200)
                st.markdown("<h3 style='color: black;'>Kanae Komaki</h3>", unsafe_allow_html=True)
                #st.markdown("<h3 style='color: black;'>NLP Model</h3>", unsafe_allow_html=True)
            with col3:
                st.image("./images/koga.jpg", width=200)
                st.markdown("<h3 style='color: black;'>Koga Takahashi</h3>", unsafe_allow_html=True)
                #st.markdown("<h3 style='color: black;'>Shiori Miwa</h3>", unsafe_allow_html=True)
            with col4:
                st.image("./images/lucas.jpg", width=200)
                st.markdown("<h3 style='color: black;'>Lucas Kawasaki</h3>", unsafe_allow_html=True)
                #st.markdown("<h3 style='color: black;'>Machine Learning</h3>", unsafe_allow_html=True)

        # with st.container():
        #     col1, col2, col3, col4 = st.columns(4)
        #     with col1:
        #         logos = ['/Users/lucaskawasaki/Desktop/Logos/LI-In-Bug.png', '/Users/lucaskawasaki/Desktop/Logos/Wantedly_Mark_LightBG.png', '/Users/lucaskawasaki/Desktop/Logos/github-mark.png']
        #         st.image(logos, width=40)
        #     with col2:
        #         logos = ['/Users/lucaskawasaki/Desktop/Logos/LI-In-Bug.png', '/Users/lucaskawasaki/Desktop/Logos/Wantedly_Mark_LightBG.png', '/Users/lucaskawasaki/Desktop/Logos/github-mark.png']
        #         st.image(logos, width=40)
        #     with col3:
        #         logos = ['/Users/lucaskawasaki/Desktop/Logos/LI-In-Bug.png', '/Users/lucaskawasaki/Desktop/Logos/Wantedly_Mark_LightBG.png', '/Users/lucaskawasaki/Desktop/Logos/github-mark.png']
        #         st.image(logos, width=40)
        #     with col4:
        #         logos = ['/Users/lucaskawasaki/Desktop/Logos/LI-In-Bug.png', '/Users/lucaskawasaki/Desktop/Logos/Wantedly_Mark_LightBG.png', '/Users/lucaskawasaki/Desktop/Logos/github-mark.png']
        #         st.image(logos, width=40)

if __name__ == "__main__":
    main2()
