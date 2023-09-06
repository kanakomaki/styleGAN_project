import streamlit as st
from PIL import Image
import os
import re
from style_clip import style_clip, image_generator, save_image
from main import main



# Paths - NOTE: CHANGE TO GCP
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

# Page and button behavior setup
##########################################################################################################################
st.set_page_config(layout="wide")

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

def click_download_button():
    pass

def click_accept_button():
    st.session_state.image2.save('0.0.jpg')
    st.session_state.images_in_folder
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


def main2():
    # Sidebar part 1
    ##########################################################################################################################
    with st.sidebar:
        # Store the initial value of widgets in session state
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False

        text_input1 = st.text_input("Describe the features of a person you are looking for:",key='placeholder')
        upload_image = st.button('Upload image', on_click=click_upload_button)

        text_input2 = st.text_input("Enter the feature you want to change:")
        generate_image = st.button('Generate images', on_click=click_generate_button)
    ##########################################################################################################################

    # Input and Output text - Page
    ##########################################################################################################################
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)
            st.markdown('<p class="big-font">Input image</p>', unsafe_allow_html=True)
        with col2:
            st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)
            st.markdown('<p class="big-font">Output image</p>', unsafe_allow_html=True)
    ##########################################################################################################################

    # To create a image
    ##########################################################################################################################
    with st.container():
        # Create two columns with equal width
        col1, col2 = st.columns(2)

        if text_input1 and st.session_state.upload_clicked:

            st.session_state.original_test = main(text_input1)
            #print(st.session_state.original_test)

            output = image_generator(image=st.session_state.original_test, target='hair', manipulation=0.0)
            st.session_state.output_image = save_image(link=output, manipulation=0.0)

            # Original image
            #############################################################
        try:
            with col1:
                image1 = Image.open('0.0.jpg') # return from previous part
                disabled=st.session_state
                st.image(image1, use_column_width=True)
        except:
            pass

        if text_input1 and text_input2 and st.session_state.generate_clicked:
            # Call style_clip and web_load_images
            manipulation_strength = [-4.5, 4.5]
            style_clip(original_image_path=st.session_state.original_test, target=text_input2, manipulation_strength=manipulation_strength)

        # Sidebar part 2
        #############################################################

        st.session_state.images_in_folder = catch_images_name(output_path)
        if len(st.session_state.images_in_folder) > 1:
            with st.sidebar:
                color = st.select_slider(
                    'Select the level of change',
                    options=st.session_state.images_in_folder,
                    value=('0.0')
                )
            # Generated image
            #############################################################
            with col2:
                st.session_state.image2 = Image.open(f'{output_path}{color}.jpg')
                st.image(st.session_state.image2, use_column_width=True)

            # Buttons
            #############################################################
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns([1,1,1,1,1,1.1,1,1,1,1])
            with col1: st.write('')
            with col2: st.write('')
            with col3: st.write('')
            with col4: st.write('')
            with col5: st.write('')
            with col6:
                st.button('Download', on_click=click_download_button)
                # Download image
            with col7:
                st.button('Accept', on_click=click_accept_button)
            with col8: st.write('')
            with col9: st.write('')
            with col10: st.write('')

        unclick_upload_button()
        unclick_generate_button()

    ##########################################################################################################################

if __name__ == "__main__":
    main2()
