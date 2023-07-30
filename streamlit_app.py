from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = "https://www.alipay.com/x/personal"
CONTACT_EMAIL = "jcklee0010@gmail.com"
DEMO_VIDEO = ASSETS_DIR / "00.mp4"
PRODUCT_NAME = "新型电磁驱动霍普金森杆动态力学性能测试系统"
PRODUCT_TAGLINE = "产品介绍"
PRODUCT_DESCRIPTION = """
传统气动霍普金森杆那么难用，为什么不试试我们的产品呢？:

- 比它们测得准
- 比它们测得全
- 比它们测得了
- ...
- **新型电磁驱动霍普金森杆动态力学性能测试系统的时代就要来了，你还想要固步自封吗？**
"""


def load_css_file(css_file_path):
    with open(css_file_path, encoding='utf-8') as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
load_css_file(CSS_FILE)




# --- MAIN SECTION ---

st.markdown(
    f"<h1 style='display:inline-block; font-size: 36px;'>{PRODUCT_NAME}</h1>",
    unsafe_allow_html=True
)

st.subheader(PRODUCT_TAGLINE)
# ... (rest of the code remains unchanged)


left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button">👉 在线购买</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open(ASSETS_DIR / "装置图1.png")
    product_image = product_image.resize((product_image.width // 1, product_image.height // 1))
    st.image(product_image, width=450)


# --- FEATURES ---
st.write("")
st.write("---")
st.subheader(":rocket: 我们的特点")
features = {
    "特点1_原理1.png": [
        "我们使用电磁驱动",
        "包括发射筒、抗电磁干扰屏蔽壳、子弹装在发射筒中心的发射腔内，发射腔两端分别设置有三级电磁线圈的子弹加速通道，通过对各级电磁线圈加载不同电压，可由低至高逐级调节发射速度，使子弹以设定速度朝对应方向发射。",
    ],
    "特点1_双向拉压1.png": [
        "我们可以实现双向拉压",
        "两套拉压同体霍普金森装置呈十字交叉布置，底座交汇处可设置缺口，避免相互干扰，储能电容柜控制两套拉压同体霍普金森装置，通过控制柜旋钮调节两套装置各级电磁线圈加载电压，两套装置发射速度是否相等均可自由设置，按下充电按钮，各级电容自动充入设定电压，充能结束后按下放电按钮，两套电磁发射装置精确同步发射，完成双向拉压实验。",
    ],
    "特点3_数控.png": [
        "我们可以实现全数控操作",
        "在经过小型和大型电磁驱动装置研发，制成一套电压0-5000V连续可调的大型电磁驱动装置，将该电磁驱动技术与霍普金森杆实验技术相结合，研制出一套电磁驱动多级连续加载的拉压同体霍普金森杆装置以后，团队着力进行装置控制系统升级，最终制成全数控电磁驱动多级连续加载的拉压同体霍普金森杆装置。。",
    ],
}
for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])

# ... (previous code remains unchanged)

# --- DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: 演示视频")
# Convert DEMO_VIDEO path to string using str()
st.video(str(DEMO_VIDEO), format="video/mp4", start_time=0)

# ... (rest of the code remains unchanged)


# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: 答疑")
faq = {
    "你们的产品和现在的其他霍普金森杆有什么不同？": "我们的转置目前已经实现了全数控电磁驱动多级连续加载，并且实验效率与准确率远超同类产品。",
    "你们定价多少？": "我们目前暂定60~300万，薄利多销，您可按需购买。",
    "你们团队有多少人？": "我们是一个只有十余人小团队，但团队成员均为各个行业内的领军人物。",
    "产品有什么权威背书吗？": "我们的产品收到了中国工程院院士任辉启院士的大力支持，有院士背书。",
    "你们目前是什么商业模式？": "我们目前以销售转置为主，也兼顾维修仪器。",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

# --- CONTACT FORM ---
st.write("")
st.write("---")
st.subheader(":mailbox: 你现在还有疑问? 请马上联系我们!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="你的名字" required>
     <input type="email" name="email" placeholder="你的电子邮箱" required>
     <textarea name="message" placeholder="你的疑问"></textarea>
     <button type="submit" class="button">发送 ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
