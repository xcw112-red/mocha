import streamlit as st
import numpy as np
import time
import pandas as pd
from datetime import datetime, time
st.set_page_config(page_title='多页面应用-顶部栏页面',layout='wide')
st.image("https://www.gxvnu.edu.cn/images/QQtupian20240701090920_fuben.png")
tab1, tab2, tab3, tab4, tab5= st.tabs(["数字档案", "南宁美食数据", "音乐播放器", "个人简历生成器", "动物图鉴"])

with tab1:
    st.title("🕶学生 余阅万 -数字档案")
    st.header("🔑基础信息" )
    st.text("学生ID:230511702xx")
    st.markdown('**注册时间:**`2025-06-04` |精神状态: ✅ 正常')
    st.markdown('**当前教室:**`实训楼301` |安全等级: `绝密`')
    st.header("📊技能矩阵" )
    c1, c2, c3 = st.columns(3)
    c1.metric(label="C语言",help='这是工具提示', value="99%", delta="2%")
    c2.metric(label="Python",value="88%", delta="-1%")
    c3.metric(label="Java",help='这是工具提示', value="66%", delta="10%")
    st.markdown('### Streamlit课程进度')
    st.progress(value=30,text='Streamlit课程进度')

    data = {
    '日期':['2023-10-1','2023-10-5','2023-10-12'],
    '任务':['学生数字档案','课程管理系统', '数据图表展示'],
    '状态':['✅完成','🕒进行中','未完成'],
    '难度':['★★☆☆☆','★☆☆☆☆','★★★☆☆']}

    index = pd.Series(['0','1','2'], name='')
    df = pd.DataFrame(data, index=index)

    st.subheader('📝任务日志')

    st.dataframe(df)
    st.markdown('### 🔐最新代码成果')
    python_code = '''def matrix_breach():
        while True:
              if detect_vulnerability():
                    exploit()
                    return "ACCESS GRANTED"
              else:
                    stealth_evade()
        '''
    st.code(python_code)
    st.write("`>>SYSTEM MESSAGE:`下一个任务目标已解锁")
    st.write("`>>TARGET:`课程管理系统")
    st.write("`>>COUNTDOWN:`2025-06-04 17:20:20")
    st.text("系统状态:在线 连接状态:已加密")

with tab2:
    st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
    st.header("📍南宁美食地图")
    st.map(pd.DataFrame({
    "latitude":[22.794320,22.763607,22.816398,22.861110,22.965046,],
    "longitude":[108.306371,108.315012,108.320781,108.308625,108.353921]}))

    data = {
    "评分": [3.7, 4.6, 4.4, 4.0, 3.7],
    "餐厅": ["肯德基", "小放肆", "尝不忘", "三品王", "高峰柠檬鸭"],}
    df = pd.DataFrame(data)
    index = pd.Series([1, 2, 3, 4, 5], name='编号')
    df.index = index
    st.header("⭐餐厅评分")
    st.bar_chart(df, x='餐厅', y='评分')

    st.header("💰不同类型餐厅价格")
    data = {
    '餐厅类型': ['中餐', '快餐', '自助餐','西餐'],
    '肯德基': [15, 50, 120, 78],
    '尝不忘': [12, 16, 30, 70],
    '小放肆': [40, 18, 60, 90],
    '三品王': [13, 12, 33, 40],
    '高峰柠檬鸭': [110, 100, 160, 140]}
    df = pd.DataFrame(data)
    index = pd.Series([1,2,3,4],name='编号')
    df.index = index
    st.line_chart(df,x='餐厅类型')

    data = {
        '时间':['11', '12','13','17','18', '19'],
        '肯德基':[40, 80, 50, 45, 75, 55],
        '小放肆':[30, 95, 70, 40, 85, 60],
        '尝不忘':[21, 85, 65, 35, 90, 65],}
    df = pd.DataFrame(data)
    index = pd.Series([1, 2, 3, 4, 5, 6], name='序号')
    df.index = index
    st.header("⏱用餐高峰时段")
    df.set_index('时间', inplace=True)
    st.area_chart(df,y=['肯德基','小放肆','尝不忘'])

    def my_format_func(option):
        return f'{option}'
    st.header('🍽餐厅详细')
    dp = st.selectbox('选择餐厅查看详细：', ['肯德基','小放肆','尝不忘', '三品王', '高峰柠檬鸭'], format_func=my_format_func, index=2)
    if dp == '肯德基':
        c1,c2=st.columns(2)
        with c1:
            st.subheader('肯德基')
            st.metric(label="评分", value="3.7/5.0")
            st.metric(label="人均消费", value="25元")
        with c2:
            st.write("**推荐菜品**")
            st.markdown('''- 特色套餐
- 小食饮品
- 全鸡可乐餐''')
        st.subheader('当前拥挤程度')
        st.progress(value=40,text='40%拥挤')
        
    elif dp == '小放肆':
        c1,c2=st.columns(2)
        with c1:
            st.subheader('小放肆')
            st.metric(label="评分", value="4.6/5.0")
            st.metric(label="人均消费", value="47元")
        with c2:
            st.write("**推荐菜品**")
            st.markdown('''- 招牌黑猪五花肉
- 暴脾气鱿鱼丝
- 金针菇''')
        st.subheader('当前拥挤程度')
        st.progress(value=55,text='55%拥挤')
    
    elif dp == '尝不忘':
        c1,c2=st.columns(2)
        with c1:
            st.subheader('尝不忘')
            st.metric(label="评分", value="4.4/5.0")
            st.metric(label="人均消费", value="15元")
        with c2:
            st.write("**推荐菜品**")
            st.markdown('''- 招牌桂林卤粉
- 卤味脆皮粉
- 卤味叉烧粉''')
        st.subheader('当前拥挤程度')
        st.progress(value=66,text='66%拥挤')

    elif dp == '三品王':
        c1,c2=st.columns(2)
        with c1:
            st.subheader('三品王')
            st.metric(label="评分", value="4.0/5.0")
            st.metric(label="人均消费", value="13元")
        with c2:
            st.write("**推荐菜品**")
            st.markdown('''- 酸菜牛肉粉
- 柳州螺蛳粉
- 原汤牛肉粉''')
        st.subheader('当前拥挤程度')
        st.progress(value=33,text='33%拥挤')

    else:
        c1,c2=st.columns(2)
        with c1:
            st.subheader('高峰柠檬鸭')
            st.metric(label="评分", value="3.7/5.0")
            st.metric(label="人均消费", value="30元")
        with c2:
            st.write("**推荐菜品**")
            st.markdown('''- 特色套餐
- 地方小吃
- 时令蔬菜''')
        st.subheader('当前拥挤程度')
        st.progress(value=70,text='70%拥挤')
        
    st.subheader("🎲今日午餐推荐")
    if st.button('帮我选午餐'):
        lunch = st.selectbox(
            '你中午想吃什么？',
            ['今日推荐:尝不忘(中餐)'],
            label_visibility='hidden')
        st.image("https://static.yueya.net/shuomingshu.cn//wp-content/uploads/images/2022/12/31/c01384f218134323a67d24a5b5483c26_c3ial2au1ri.jpg", caption='美味午餐等着你')

    months = [f"{i}月" for i in range(1, 13)]
    restaurants = ["肯德基", "尝不忘", "小放肆", "三品王", "高峰柠檬鸭"]

    np.random.seed(42)
    price_data = {}
    price_data["肯德基"] = np.random.normal(25, 3, 12).round(1) + np.linspace(0, 5, 12)
    price_data["尝不忘"] = np.random.normal(15, 2, 12).round(1) + np.linspace(0, 3, 12)
    base = np.random.normal(45, 5, 12).round(1)
    summer_discount = [0, 0, 0, -2, -5, -3, -2, 0, 0, 0, 0, 0]
    price_data["小放肆"] = base + summer_discount + np.linspace(0, 4, 12)
    price_data["三品王"] = np.random.normal(13, 1, 12).round(1) + np.linspace(0, 3, 12)
    base = np.random.normal(60, 8, 12).round(1)
    season_effect = [0, 5, 3, 0, -3, -5, -4, -2, 0, 3, 6, 8]
    price_data["高峰柠檬鸭"] = base + season_effect + np.linspace(0, 5, 12)
    price_df = pd.DataFrame(price_data)
    price_df.insert(0, "月份", months)
    selected_restaurants = st.multiselect(
        "选择餐厅查看价格走势",
        restaurants,
        default=restaurants)
    if selected_restaurants:
        st.line_chart(price_df, x="月份", y=selected_restaurants)
        
with tab3:
    if 'a' not in st.session_state:
        st.session_state['a'] = 0
    image_arr = [{
        '时长':'03:35',
        '歌手':'黄子弘凡/高睿/逆水长琴/逆水寒/雷火音频',
        'p':'https://p1.music.126.net/JJjprsDKl8IfceDn52so8g==/109951170027513371.jpg',
        'url': 'https://music.163.com/song/media/outer/url?id=2634596254.mp3',
        'title': '着魔'
        },{
        '时长':'04:18',
        '歌手':'刘可以',
        'p':'http://p2.music.126.net/RM8h6DB4wELN08AAg0lCuA==/109951169654574512.jpg',
        'url': 'https://music.163.com/song/media/outer/url?id=2163223946.mp3',
        'title': '情歌'
        },{
        '时长':'03:00',
        '歌手':'文韬',
        'p':'https://p1.music.126.net/k1yZYmlQN1PwEHcNDebrIA==/109951169490500312.jpg',
        'url': 'https://music.163.com/song/media/outer/url?id=2144741708.mp3',
        'title': '勇敢的人先享受世界'
        }]
    def next():
        st.session_state['a'] = (st.session_state['a'] + 1) % len(image_arr)
        st.text(st.session_state['a'])
    def prev():
        st.session_state['a'] = (st.session_state['a'] - 1) % len(image_arr)
        st.text(st.session_state['a'])
    c1, c2 = st.columns(2)
    with c1:
        st.image(image_arr[st.session_state['a']]['p'], caption=image_arr[st.session_state['a']]['title'])
    with c2:
        st.markdown(f"**{image_arr[st.session_state['a']]['title']}**")
        st.write(f"歌手: {image_arr[st.session_state['a']]['歌手']}")
        st.write(f"时长: {image_arr[st.session_state['a']]['时长']}")
        button_container = st.container()
        with button_container:
            b1, b2 = st.columns(2)
            with b1:
                st.button('上一首', on_click=prev, use_container_width=True)
            with b2:
                st.button('下一首', on_click=next, use_container_width=True)
    st.audio(image_arr[st.session_state['a']]['url'])

with tab4:
    st.title("🎨个人简历生成器")
    st.text("使用Streamlit创建您的个性化简历")

    c1, c2 = st.columns([1, 2])

    with c1:
        st.header("个人信息表单")
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

        st.session_state['xm'] = st.text_input('姓名')
        st.session_state['zw'] = st.text_input('职位')
        st.session_state['dh'] = st.text_input('电话')
        st.session_state['yx'] = st.text_input('邮箱')
        date = st.date_input("出生日期", value=None)

        st.session_state['xb'] = st.radio(
            '性别',
            ['男', '女', '其他'],
            horizontal=True)

        st.session_state['xl'] = st.selectbox(
            '学历',
            ['小学', '初中', '高中', '专科', '本科', '硕士', '博士'])

        st.session_state['yynl'] = st.multiselect(
            '语言能力',
            ['中文', '日语', '英语'])

        st.session_state['jn'] = st.multiselect(
            '技能（可多选）',
            ['Java', 'HTML/CSS', '机器学习', 'Python', 'C/C++', 'IDE', '数据库'])

        workage = st.slider('工作经验（年）', 0, 30, 0)

        start_color, end_color = st.select_slider(
            '期望薪资范围（元）',
            options=['5000', '10000', '15000', '20000', '25000', '30000', '35000', '40000', '45000', '50000'],
            value=('10000', '20000'))

        grjl = st.text_area(label='个人简历：', placeholder='请简要介绍您的专业背景、职业目标和个人特点......', height=200, max_chars=200)

        sj = st.time_input("每日最佳联系时间段", time(20, 44))

        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # 显示上传的图片
            st.image(uploaded_file, caption='上传的照片', width=100)

    with c2:
        st.header("简历实时预览")
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

        st.subheader(st.session_state['xm'])
        a1, a2 = st.columns(2)
        with a1:
            st.write('**职位:**', st.session_state['zw'])
            st.write('**电话:**', st.session_state['dh'])
            st.write('**邮箱:**', st.session_state['yx'])
            if date:
                formatted_date = date.strftime("%Y/%m/%d")
                st.write(f"**出生日期：{formatted_date}**")
            else:
                st.write("**出生日期:**")
        with a2:
            st.write(f"**性别：{st.session_state['xb']}**")
            st.write('**学历:**', st.session_state['xl'])
            st.write(f"**工作经验:{workage}年**")
            st.write('**期望薪资:**', start_color, '-', end_color, '元')
            st.write(f"**最佳联系时间:{sj}**")
            if st.session_state['yynl']:
                selected_languages = "，".join(st.session_state['yynl'])
                st.write(f"**语言能力：{selected_languages}**")
            else:
                st.write("**语言能力:**")

        st.markdown("<hr style='border: 1px solid #444; margin: 10px 0;'>", unsafe_allow_html=True)
        st.header("个人简介")
        st.write(grjl)
        st.markdown("<hr style='border: 1px solid #444; margin: 10px 0;'>", unsafe_allow_html=True)
        st.header("专业技能")
        if st.session_state['jn']:
            for skill in st.session_state['jn']:
                st.write(skill)

with tab5:
    # 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    # 图片数组-装很多的图片
    image_obj = [
        {
            'url': 'https://mindfulspirituallife.com/wp-content/uploads/2023/12/cat.jpg ',
            'title': '猫'
        },
        {
            'url': 'https://www.allaboutbirds.org/news/wp-content/uploads/2020/07/STanager-Shapiro-ML.jpg ',
            'title': '鸟'
        },
        {
            'url': 'https://a-z-animals.com/media/2023/02/shutterstock_2152176495.jpg ',
            'title': '鱼'
        }
    ]

    st.image(image_obj[st.session_state['ind']]['url'], caption=image_obj[st.session_state['ind']]['title'])

    # 显示按钮
    def nextImg():
        # 点击下一张按钮要做的事
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_obj)

    c1, c2 = st.columns(2)

    with c1:
        st.button('上一张', use_container_width=True)

    with c2:
        st.button('下一张', on_click=nextImg, use_container_width=True)
