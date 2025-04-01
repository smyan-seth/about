
import streamlit as st

st.set_page_config(page_title="Smyan Seth's Portfolio", layout="centered")

st.title("Hey there 👋, I am Smyan Seth")
st.divider()

tab = st.tabs([
    'About me', "Projects", 'Currently learning','Languages and Tools', 'Connect with me'
])

with tab[0]:
  st.write(
      '\n-I’m a zealous teen passionate about coding and learning new things . \n- An aspiring Software Engineer'
  )

with tab[1]:
  st.subheader("👨🏻‍💻")
  st.write(
      "Check out my [GitHub](https://github.com/smyan-seth)."
  )

with tab[2]:
  st.subheader("📚 Currently Learning")
  st.write("- Python\n- HTML")

with tab[3]:
    st.html('''
    <p><a><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> Python</a></p>
        <p><a><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> HTML</a></p>
        <p><a><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> CSS</a></p>
        <p><a><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> MySQL</a></p>
    ''')

with tab[4]:
    st.header("📫 Email")
    st.subheader(
      "Email me at [seth.smyan@gmail.com](mailto:seth.smyan@gmail.com)")
    st.divider()
    st.header("📱 Socials")
    st.write('\n')
    st.html(
          '''<a href="https://linkedin.com/in/smyanseth" target="_blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="smyan-seth" height="30" width="40" /></a>
    <a href="https://instagram.com/smyanseth" target="_blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="smyan_seth" height="30" width="40" /></a>
    <a href="https://twitter.com/smyanseth" target="_blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="smyanseth" height="30" width="40" /></a>''')

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button('🎈 Balloon'):
        st.balloons()

with col2:
    if st.button('❄️ Snow'):
        st.snow()
