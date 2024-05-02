import streamlit as st
from PIL import Image
import numpy as np

from app.controller.detect import detect_equipment
from app.controller.gpt import generate_llm_output
 

EQUIP_TRANS_MAP = {'Back Extension': '백 익스텐션', 'Chest Fly' : '체스트 플라이', 'Chest Press' : '체스트 프레스', 
                   'Lat Pulldown' : '랫 풀다운', 'Leg Extension' : '레그 익스텐션', 'Leg Press' : '레그 프레스', 'Shoulder Press' : '숄더 프레스'}

EQUIP_VIDEO_MAP = {
    '백 익스텐션': 'https://youtu.be/2SVRupci_j8?si=DPzExhpWpgoxL2-v',
    '체스트 플라이': 'https://youtu.be/UAz5zIzkTA4?si=5cFz-5kDuYC4Itkd',
    '체스트 프레스': 'https://youtu.be/1pBcQ-77ho4?si=v0g5wIXaancf_WPM',
    '랫 풀다운': 'https://youtu.be/G11ySWVXA48?si=EOrWX44Ie5OYDazP',
    '레그 익스텐션': 'https://youtu.be/ayQpSM04iEc?si=YI-QI_mJV_m88rz9',
    '레그 프레스': 'https://youtu.be/hYwJrXpzEfs?si=7DF2ga-Gqkz0MVpe',
    '숄더 프레스': 'https://youtu.be/vM3H17ip4Zk?si=T-JkxJ9Ryjg_Zj9r'
}

def process_image(image):
    equipment_name, equipment_img = detect_equipment(image)
    equipment_name = EQUIP_TRANS_MAP[equipment_name]
    return equipment_name, equipment_img


def process_text(equipment_name):
    llm_output = generate_llm_output(equipment_name)

    return llm_output

st.title("운동법을 알려주는 AI 코치 LookForFit")
st.subheader("기구 이미지 입력")

uploaded_file = st.file_uploader("이미지 업로드", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file).convert("RGB")
    input_image_array = np.array(input_image)

    st.image(input_image, caption="입력 이미지", use_column_width='auto')
    equipment_name, output_image_array = process_image(input_image_array)
    output_image = Image.fromarray(output_image_array)
    st.image(output_image, caption=equipment_name, use_column_width='auto')
    
    description = process_text(equipment_name)
    st.subheader("이 기구에 대해 알려드립니다")
    st.write(description)

    video_url = EQUIP_VIDEO_MAP[equipment_name]
    st.subheader(f"{equipment_name} 운동 영상")
    st.video(video_url)