import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="🍔南宁美食地图🍔")
st.title("🍔南宁美食探索")
st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
st.header("📍南宁美食地图")
st.map(pd.DataFrame({
"latitude":[22.794320,22.763607,22.816398,22.861110,22.965046,],
"longitude":[108.306371,108.315012,108.320781,108.308625,108.353921]

}))

import streamlit as st
import pandas as pd
data = {
"评分": [4.2, 4.5, 4.0, 4.7, 4.3],
"餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
}
# 创建数据框
df=pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4, 5], name='编号')
# 将新索引应用到数据框上
df.index = index
st.header("⭐ 餐厅评分")
# 使用write()方法展示数据框

# 正确的条形图调用：使用餐厅名称作为类别，评分作为数值
st.bar_chart(df, x='餐厅', y='评分')


st.header("💰不同类型餐厅价格")
# 定义数据,以便创建数据框
data = {
'餐厅类型': ['中餐', '快餐', '自助餐','西餐'],
'肯德基': [15, 50, 120, 78],
'尝不忘': [12, 16, 30, 70],
'小放肆': [40, 18, 60, 90],
'三品王': [13, 12, 33, 40],
'高峰柠檬鸭': [110, 100, 160, 140],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1,2,3,4],name='编号')
# 将新索引应用到数据框上
df.index = index

st.line_chart(df,x='餐厅类型')

data = {
'时间':['11', '12','13','17','18', '19'],
'肯德基':[40, 80, 50, 45, 75, 55],
'小放肆':[30, 95, 70, 40, 85, 60],
'尝不忘':[21, 85, 65, 35, 90, 65],
}
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4, 5, 6], name='序号')
df.index = index
st.header("门店数据")

st.header("⏱用餐高峰时段")
df.set_index('时间', inplace=True)
st.area_chart(df,y=['肯德基','小放肆','尝不忘'])

import streamlit as st
def my_format_func(option):
      return f'{option}'


st.header('🍽餐厅详细')

dp = st.selectbox('选择餐厅查看详细：', ['肯德基','小放肆','尝不忘', '三品王', '高峰柠檬鸭'], format_func=my_format_func, index=2)
if dp == '肯德基':
     st.subheader('肯德基')
     st.metric(label="评分", value="3.7/5.0")
     st.metric(label="人均消费", value="25元")
     st.subheader('当前拥挤程度')
     st.progress(value=40,text='40%拥挤')
elif dp == '小放肆':
     st.subheader('小放肆')
     st.metric(label="评分", value="4.6/5.0")
     st.metric(label="人均消费", value="47元")
     st.subheader('当前拥挤程度')
     st.progress(value=55,text='55%拥挤')
elif dp == '尝不忘':
     st.subheader('尝不忘')
     st.metric(label="评分", value="4.4/5.0")
     st.metric(label="人均消费", value="15元")
     st.subheader('当前拥挤程度')
     st.progress(value=66,text='66%拥挤')
elif dp == '三品王':
     st.subheader('三品王')
     st.metric(label="评分", value="4.0/5.0")
     st.metric(label="人均消费", value="13元")
     st.subheader('当前拥挤程度')
     st.progress(value=33,text='33%拥挤')
else:
     st.subheader('高峰柠檬鸭')
     st.metric(label="评分", value="3.7/5.0")
     st.metric(label="人均消费", value="30元")
     st.subheader('当前拥挤程度')
     st.progress(value=70,text='70%拥挤')

# 今日午餐推荐模块
st.subheader("🎲今日午餐推荐")
st.button('帮我选午餐')
lunch = st.selectbox(
    '你中午想吃什么？',
    ['今日推荐:尝不忘(中餐)'],
    label_visibility='hidden'
)
st.image("https://static.yueya.net/shuomingshu.cn//wp-content/uploads/images/2022/12/31/c01384f218134323a67d24a5b5483c26_c3ial2au1ri.jpg", caption='美味午餐等着你！')
st.header("📈 餐厅12个月价格走势")

# 生成模拟数据
months = [f"{i}月" for i in range(1, 13)]
restaurants = ["肯德基", "尝不忘", "小放肆", "三品王", "高峰柠檬鸭"]

# 为每家餐厅生成不同的价格趋势
np.random.seed(42)
price_data = {}

# 肯德基：价格较稳定，略有增长
price_data["肯德基"] = np.random.normal(25, 3, 12).round(1) + np.linspace(0, 5, 12)

# 尝不忘：价格较低，波动不大
price_data["尝不忘"] = np.random.normal(15, 2, 12).round(1) + np.linspace(0, 3, 12)

# 小放肆：价格中等，夏季略有下降
base = np.random.normal(45, 5, 12).round(1)
summer_discount = [0, 0, 0, -2, -5, -3, -2, 0, 0, 0, 0, 0]
price_data["小放肆"] = base + summer_discount + np.linspace(0, 4, 12)

# 三品王：价格较低，年底上涨
price_data["三品王"] = np.random.normal(13, 1, 12).round(1) + np.linspace(0, 3, 12)

# 高峰柠檬鸭：价格较高，季节性波动
base = np.random.normal(60, 8, 12).round(1)
season_effect = [0, 5, 3, 0, -3, -5, -4, -2, 0, 3, 6, 8]
price_data["高峰柠檬鸭"] = base + season_effect + np.linspace(0, 5, 12)

# 创建价格数据框
price_df = pd.DataFrame(price_data)
price_df.insert(0, "月份", months)

# 选择要显示的餐厅
selected_restaurants = st.multiselect(
    "选择餐厅查看价格走势",
    restaurants,
    default=restaurants
)

if selected_restaurants:
    st.line_chart(price_df, x="月份", y=selected_restaurants)
    
 