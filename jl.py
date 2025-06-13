import streamlit as st
from datetime import time, datetime
st.set_page_config(page_title='个人简历生成器',layout='wide',page_icon="📄")
st.title("🎨个人简历生成器")
st.text('''使用Streamlit创建您的个性化简历''')
c1,c2=st.columns([1,2])
with c1:
    st.subheader("个人信息表单")
    st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] hr {
    border: none;
    height: 2px;
    background-color: #2563eb;
    margin: 20px 0;
}
</style>
<hr>
""", unsafe_allow_html=True)
    # 姓名
    name = st.text_input("姓名")
    # 职位
    position = st.text_input("职位")
    # 电话
    phone = st.text_input("电话")
    # 邮箱
    email = st.text_input("邮箱")
    # 出生日期
    birth_date = st.date_input("出生日期", value=None)
    # 性别
    st.session_state['xb'] = st.radio(
        '性别',
        ['男', '女', '其他'],
        horizontal=True
        )

    st.session_state['xl'] = st.selectbox(
        '学历',
        ['小学', '初中', '高中', '专科', '本科', '硕士', '博士']
        )

    language = st.multiselect(
        '语言能力（可多选）',
        ['中文', '英语', '日语', '韩语', '法语', '德语', '其他'],
        default=None,
        help="请选择您的语言能力，最多可选择3项"
    )
    
    # 技能 - 优化多选下拉按钮
    st.session_state['jn'] = st.multiselect(
        '技能（可多选）',
        ['文职类', 'IT类', '销售类', '通用类', '会计类', '财务类', '心理学类', '艺术类', 
         '教育类', '医疗类', '设计类', '管理类', '市场营销', '人力资源', '项目管理'],
        max_selections=3,
        default=None,
        help="请选择您的专业技能，最多可选择3项"
    )
    
    workage = st.slider('工作经验（年）', 0, 30, 0)
    
    start_color, end_color = st.select_slider(
        '期望薪资范围（元）',
        options=['5000', '10000', '15000', '20000', '25000', '30000', '35000''40000', '45000', '50000'],
        value=('10000', '20000'))
    
    personal_intro=st.text_area('个人简历：',
                                placeholder='请简要介绍您的专业背景、职业目标和个人特点......',
                                height=200,
                                max_chars=200)

    w2 = st.time_input("每日最佳联系时间段", time(20, 44))
    
    # 最主要联系问题
    contact_question = st.selectbox("最主要联系问题", ["2044", "其他"])
    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # 显示上传的图片
    st.image(uploaded_file, caption='上传的照片',width=100)
    
with c2:
    st.subheader("简历实时预览")
    st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] hr {
    border: none;
    height: 2px;
    background-color: #2563eb;
    margin: 20px 0;
}
</style>
<hr>
""", unsafe_allow_html=True)
    b1,b2=st.columns([1,2])
    with b1:
        st.title(f"{name}")
        # 预览照片
        if uploaded_file is not None:
            st.image(uploaded_file, caption='上传的照片',width=100)
    


        st.write(f"**职位**: {position}")
        st.write(f"**电话**: {phone}")
        st.write(f"**邮箱**: {email}")
        if birth_date:
            st.write(f"**出生日期**: {birth_date.strftime('%Y-%m-%d')}")
    with b2:
        st.write(f"**性别**: {st.session_state['xb']}")
        st.write(f"**学历**: {st.session_state['xl']}")
        st.write(f"**工作经验**: {workage} 年")
        st.write(f"**期望薪资**: {start_color}-{end_color} 元")
        st.write(f"**每日最佳联系时间段**: {w2}")
        st.write(f"**语言能力**: {', '.join(language) if language else '未选择'}")
    st.markdown("<hr style='border: 1px solid #444; margin: 10px 0;'>",
                unsafe_allow_html=True)

    st.subheader('个人简介')
    st.write(personal_intro)
    st.subheader('专业技能')
    if st.session_state['jn']:
        for skill in st.session_state['jn']:
            st.write(skill)


    st.markdown("<hr style='border: 1px solid #444; margin: 10px 0;'>",
                    unsafe_allow_html=True)
    
    
