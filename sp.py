import streamlit as st

st.set_page_config(page_title='简易音乐播放器', page_icon='🐨')

st.header("🎵简易音乐播放器" )
# 判断内存中（session_state中）有没有a
if 'a' not in st.session_state:
    st.session_state['a'] = 0

# 数组  图片：链接、图注   音乐：链接、图片、歌手、专辑.....

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
    # 做什么事？？让索引+1
    st.session_state['a'] = (st.session_state['a'] + 1) % len(image_arr)
   
def prev():
    # 索引-1，实现上一张图片浏览
    st.session_state['a'] = (st.session_state['a'] - 1) % len(image_arr)
    
c1, c2 = st.columns([1, 2])

with c1:
    st.image(image_arr[st.session_state['a']]['p'], caption=image_arr[st.session_state['a']]['title'])

with c2:
    # 显示歌曲信息
    st.markdown(f"**{image_arr[st.session_state['a']]['title']}**")
    st.write(f"歌手: {image_arr[st.session_state['a']]['歌手']}")
    st.write(f"时长: {image_arr[st.session_state['a']]['时长']}")
    
    # 创建一个新的容器用于放置按钮，确保它们在同一行
    button_container = st.container()
    with button_container:
        # 将按钮放在同一行并设置相同的宽度
        b1, b2 = st.columns(2)
        with b1:
            st.button('上一首', on_click=prev, use_container_width=True)
        with b2:
            st.button('下一首', on_click=next, use_container_width=True)

st.audio(image_arr[st.session_state['a']]['url'])
