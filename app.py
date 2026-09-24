import streamlit as st
import plotly.express as px
import pandas as pd
from data import budget, living, reason, category, priority

st.set_page_config(page_title="大学生情绪价值消费洞察", layout="wide")
st.markdown("""
<style>
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
[data-testid="stMetric"], .stPlotlyChart, h1, h2, h3 {
    animation: fadeInUp 0.8s ease-out;
}
[data-testid="stMetric"]:hover {
    transform: scale(1.03);
    transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* 让所有主要元素浮现 */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
[data-testid="stMetric"], .stPlotlyChart, h1, h2, h3 {
    animation: fadeInUp 0.8s ease-out;
}
/* 悬停卡片时稍微放大 */
[data-testid="stMetric"]:hover {
    transform: scale(1.03);
    transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)
st.title("🎓 大学生情绪价值消费洞察")
st.caption("数据来源：问卷调查 | 多选题已标注")

col1, col2, col3 = st.columns(3)
col1.metric("样本总量", "76 人")
col2.metric("主流生活费", "1500-3000 元")
col3.metric("主流单笔预算", "≤100 元")

st.divider()

st.sidebar.header("🔍 筛选")
dim = st.sidebar.selectbox("选择查看维度", ["情绪消费原因","消费类型选择","消费优先项","单笔支出预算","生活费区间"])

data_map = {"情绪消费原因":reason,"消费类型选择":category,"消费优先项":priority,"单笔支出预算":budget,"生活费区间":living}
selected = data_map[dim]

st.subheader(dim)
df = pd.DataFrame({"类别": list(selected.keys()), "人数": list(selected.values())})
fig = px.bar(df, x="人数", y="类别", orientation="h", text="人数", color="人数", color_continuous_scale="Blues")
fig.update_layout(yaxis=dict(autorange="reversed"), height=400)
st.plotly_chart(fig, use_container_width=True)

st.divider()

col_a, col_b = st.columns(2)
with col_a:
    df1 = pd.DataFrame({"原因": list(reason.keys()), "人数": list(reason.values())})
    fig1 = px.bar(df1, x="人数", y="原因", orientation="h", text="人数", title="情绪消费原因", color="人数", color_continuous_scale="Greens")
    fig1.update_layout(yaxis=dict(autorange="reversed"), height=350, showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

    df2 = pd.DataFrame({"优先项": list(priority.keys()), "人数": list(priority.values())})
    fig2 = px.pie(df2, names="优先项", values="人数", hole=0.4, title="消费优先项")
    st.plotly_chart(fig2, use_container_width=True)

with col_b:
    df3 = pd.DataFrame({"类型": list(category.keys()), "人数": list(category.values())}).sort_values("人数")
    fig3 = px.bar(df3, x="人数", y="类型", orientation="h", text="人数", title="消费类型选择", color="人数", color_continuous_scale="Oranges")
    fig3.update_layout(yaxis=dict(autorange="reversed"), height=700, showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

col_c, col_d = st.columns(2)
with col_c:
    df4 = pd.DataFrame({"区间": list(budget.keys()), "人数": list(budget.values())})
    fig4 = px.bar(df4, x="区间", y="人数", text="人数", title="单笔支出预算")
    st.plotly_chart(fig4, use_container_width=True)
with col_d:
    df5 = pd.DataFrame({"区间": list(living.keys()), "人数": list(living.values())})
    fig5 = px.bar(df5, x="区间", y="人数", text="人数", title="生活费区间")
    st.plotly_chart(fig5, use_container_width=True)