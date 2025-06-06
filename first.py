import streamlit as st
import time
import pandas as pd
st.title("🕶学生 余阅万 -数字档案")
st.header("🔑 基础信息" )
st.text("学生ID:230511702xx")
st.markdown('**注册时间:**:green[2025-06-04] |精神状态:  ✅ 正常')
st.markdown('**当前教室:**:green[实训楼301] |安全等级:  :green[绝密]')
st.header("📊 技能矩阵" ) 
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言",help='这是工具提示', value="99%", delta="2%")
c2.metric(label="Python",value="88%", delta="-1%")
c3.metric(label="Java",help='这是工具提示', value="66%", delta="10%")
st.markdown('### Streamlit课程进度')
st.progress(value=30,text='Streamlit课程进度')
import streamlit as st
import pandas as pd
data = {
'日期':['2023-10-1','2023-10-5','2023-10-12'],
'任务':['学生数字档案','课程管理系统', '数据图表展示'],
'状态':['✅完成','�进行中','未完成'],
'难度':['★★☆☆☆','★☆☆☆☆','★★★☆☆']}

index = pd.Series(['0','1','2'], name='')
df = pd.DataFrame(data, index=index)

st.subheader('任务日志')

st.dataframe(df)
st.markdown('### 🔐 最新代码成果')
python_code = '''def matrix_breach():
    while True:
          if detect_vulnerability():
               exploit()
               return "ACCESS GRANTED"
          else:
               stealth_evade()
'''
st.code(python_code)
st.write("`&gt;&gt;SYSTEM MESSAGE:`下一个任务目标已解锁")
st.write("`&gt;&gt;TARGET:`课程管理系统")
st.write("`&gt;&gt;COUNTDOWN:`2025-06-04 17:20:20")
st.text("系统状态:在线 连接状态:已加密")
