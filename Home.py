import base64
import streamlit as st

st.set_page_config(layout="wide")

def inject_custom_css():
    with open('Assets/styles.css') as f:
        st.markdown(f'<style> {f.read()}</style>', unsafe_allow_html=True)

inject_custom_css()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("Assets/images/african-american-woman-standing-blue-background-smiling-positive-doing-ok-sign-with-hand-fingers-successful-expression.jpg")


def show_home_page():
    banner_container = st.container()

    file_ = open("Assets/images/dsac_app_picture.jpg", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    with banner_container:
        st.write(
            f"""
            <div class="container-fluid" style="background-color: #ffffff; padding: 15px;" height>
                <h1 class="display-3" style="color: #1D2228; text-align: center;">Welcome to Lebitso App</h1>
                <h3 class="display-3" style="color: #1D2228; text-align: center;"> The App designed to facilitate engagement with the Deaf community by providing resources
                    and tools for learning and translating sign languages.</h3>
                <img src="data:image/gif;base64,{data_url}" alt="hello gif" style="max-width: 100%; height: auto;">
            </div>
            """,
            unsafe_allow_html=True
        )

        
    # page_bg_img = f"""
    #     <style>
    #     .st-emotion-cache-1biqz71 ezrtsby2 {{
    #         visibility: hidden;
    #     }}
    #     .main.st-emotion-cache-uf99v8.ea3mdgi3 > div:first-child {{
    #         background-image: url(data:image/jpg;base64,{img});
    #         background-position: center;
    #         background-size: cover;
    #         background-blend-mode: darken;
    #     }}
    #     </style>
    #     """
    # st.markdown(page_bg_img, unsafe_allow_html=True)

    
    st.write("---")

    col1, col2, col3 = st.columns(3)
    
    def create_card(header, body, description, href):
        st.write(
            f"""
            <a href="{href}" target="_self" style="text-decoration: none; color: inherit;">
                <div style="border-radius: 30px; background-color: #ffffff; padding: 20px; margin: 10px; text-align: center;">
                    <h2 style="color: #1D2228">{header}</h2>
                    <div style="margin: 10px 0; padding: 10px 0 0;">
                        {body}
                    </div>
                    <p style="font-size: 20px; color: #000000;">{description}</p>
                </div>
            </a>
            """
            , unsafe_allow_html=True
        )
        
    with col1:
        file_ = open("Assets/images/hello.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        create_card("Communication", f'<img src="data:image/gif;base64,{data_url}" alt="hello gif" width="265px " height="250px">', "Learn about effective communication tools.", "/Communication")

    with col2:
        file_ = open("Assets/images/mapgif.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        create_card("Map", f'<img src="data:image/gif;base64,{data_url}" alt="map gif"  width="265px" height="250px">', "Explore the interactive map and locations.", "/Map")

    with col3:
        file_ = open("Assets/images/giphy.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        create_card("Information", f'<img src="data:image/gif;base64,{data_url}" alt="giphy gif" width="265px" height="250px">', "Access helpful information and resources.", "https://sl.ern.ufs.ac.za/")

    st.write("---")
    
    st.write("<br>", unsafe_allow_html=True)
    
    footer_container = st.container()

    with footer_container:
        col1, col2, col3 = st.columns((2, 1, 1))

        with col1:
            st.write("""<h1 style="color: #1D2228">Mission</h2>""", unsafe_allow_html=True)
            st.write("""
                     <p style="color: #000000;">
                     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras id egestas lectus, vulputate imperdiet ligula. Suspendisse blandit erat at neque eleifend congue. In hac habitasse platea dictumst. Donec iaculis lectus vitae pharetra blandit. Curabitur pulvinar dolor justo, quis imperdiet metus iaculis a. Curabitur pulvinar, elit ut dictum blandit, metus leo ullamcorper nunc, a ornare dui massa eget mi. Donec mattis vitae lacus eget faucibus. Donec lacinia ligula at purus facilisis, nec scelerisque neque hendrerit. Mauris tempor metus at imperdiet malesuada. Suspendisse et scelerisque ligula, sit amet euismod justo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras ullamcorper vulputate ipsum sit amet tempor.
                     </p>
                     """, unsafe_allow_html=True)

        with col2:
            st.write("""<h1 style="color: #1D2228;">Policies</h1> """, unsafe_allow_html=True)

            st.write('<a style="color: #3498db; text-decoration: none;" href="#">Privacy Policy</a>', unsafe_allow_html=True)
            st.write('<a style="color: #3498db; text-decoration: none;" href="#">Terms and Conditions</a>', unsafe_allow_html=True)

            st.write("""<h2 style="color: #1D2228;">Support<h2>""", unsafe_allow_html=True)

            st.write('<a style="color: #3498db; text-decoration: none;" href="#">Disclaimer</a>', unsafe_allow_html=True)
            st.write('<a style="color: #3498db; text-decoration: none;" href="#">Help and FAQs</a>', unsafe_allow_html=True)

        with col3:
            st.write("""<h1 style="color: #1D2228;"> Contact Info <h1> """, unsafe_allow_html=True)
            css_example = """
            <i class="fa-regular fa-envelope"></i> info@ICDF.co.za
            <i class="fa-solid fa-phone"></i> +27 84 695 1479
            """
            
            st.write(css_example, unsafe_allow_html=True)

            st.write("""<h1 style="color: #1D2228;"> Social Media </h1> """, unsafe_allow_html=True)
            
            st.write("""<a style="color: #5C6BC0; text-decoration: none;" href="https://twitter.com">
                            <i class="fab fa-twitter"></i></a>
                        <a style="color: #5C6BC0; text-decoration: none;" href="https://instagram.com">
                            <i class="fab fa-instagram"></i></a>
                        <a style="color: #5C6BC0; text-decoration: none;" href="https://youtube.com">
                            <i class="fab fa-youtube"></i></a>""", unsafe_allow_html=True)

show_home_page()
