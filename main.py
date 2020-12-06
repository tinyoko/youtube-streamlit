import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time


st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!'

# st.write('Interactive Widgets')
# st.sidebar.write('Interactive Widgets')




left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1回答を書く')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2回答を書く')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3回答を書く')

# text = st.text_input('あたなの趣味を教えて!。')
# text = st.sidebar.text_input('あたなの趣味を教えて!。')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あたなの趣味：', text
# 'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えて!。',
#     list(range(1,11))
# )
# 'あなたが好きな数字は、', option, 'です。'

# st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('../face_detection/sample_01.jpg')
#     st.image(img, caption='Session at Crawdaddy Club', use_column_width=True)

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)



# df = pd.DataFrame({
#     '1列目' : [1, 2, 3, 4],
#     '2列目' : [10, 20, 30, 40]
# })

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """