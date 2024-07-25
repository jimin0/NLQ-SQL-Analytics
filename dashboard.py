import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import get_database2


def render_dashboard():
    st.title("Northwind 대시보드")

    # 데이터베이스 연결
    engine = get_database2()

    # 상반기 매출액 # 225,096,743.77
    sales_query = "SELECT SUM(od.UnitPrice * od.Quantity) as total_sales FROM [Order Details] od JOIN Orders o ON od.OrderID = o.OrderID WHERE strftime('%m', o.OrderDate) <= '06'"
    sales_df = pd.read_sql_query(sales_query, engine)

    # 큰 숫자로 총 매출액 표시
    st.markdown(
        f"<h1 style='text-align: center; color: #1E90FF;'>${sales_df['total_sales'].iloc[0]:,.2f}</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("<p style='text-align: center;'>총 매출액</p>", unsafe_allow_html=True)

    # 2x2 그리드 레이아웃
    col1, col2 = st.columns(2)

    with col1:
        # 분기별 주문량 및 매출액
        quarters_query = """
        SELECT 
            CASE 
                WHEN strftime('%m', OrderDate) IN ('01','02','03') THEN '1Q'
                WHEN strftime('%m', OrderDate) IN ('04','05','06') THEN '2Q'
            END AS Quarter,
            COUNT(DISTINCT o.OrderID) as order_cnt,
            SUM(od.UnitPrice * od.Quantity) as sales
        FROM Orders o
        JOIN [Order Details] od ON o.OrderID = od.OrderID
        WHERE Quarter IS NOT NULL
        GROUP BY Quarter
        """
        quarters_df = pd.read_sql_query(quarters_query, engine)

        fig1 = px.bar(
            quarters_df,
            x="Quarter",
            y=["order_cnt", "sales"],
            barmode="group",
            title="분기별 주문량 및 매출액",
        )
        fig1.update_layout(height=300)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        # 월별 주문량 및 매출액
        monthly_query = """
        SELECT 
            strftime('%m', OrderDate) as Month,
            COUNT(DISTINCT o.OrderID) as order_cnt,
            SUM(od.UnitPrice * od.Quantity) as sales
        FROM Orders o
        JOIN [Order Details] od ON o.OrderID = od.OrderID
        GROUP BY Month
        ORDER BY Month
        """
        monthly_df = pd.read_sql_query(monthly_query, engine)

        fig2 = px.line(
            monthly_df,
            x="Month",
            y=["order_cnt", "sales"],
            title="월별 주문량 및 매출액",
        )
        fig2.update_layout(height=300)
        st.plotly_chart(fig2, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        # 카테고리별 매출액
        category_query = """
        SELECT 
            c.CategoryName,
            SUM(od.UnitPrice * od.Quantity) as sales
        FROM Categories c
        JOIN Products p ON c.CategoryID = p.CategoryID
        JOIN [Order Details] od ON p.ProductID = od.ProductID
        JOIN Orders o ON od.OrderID = o.OrderID
        GROUP BY c.CategoryName
        """
        category_df = pd.read_sql_query(category_query, engine)

        fig3 = px.pie(
            category_df, values="sales", names="CategoryName", title="카테고리별 매출액"
        )
        fig3.update_layout(height=300)
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        # 주별 매출액 (예시 - 실제 데이터에 맞게 수정 필요)
        state_query = """
        SELECT 
            ShipRegion as State,
            SUM(od.UnitPrice * od.Quantity) as sales
        FROM Orders o
        JOIN [Order Details] od ON o.OrderID = od.OrderID
        WHERE ShipRegion != ''
        GROUP BY ShipRegion
        ORDER BY sales DESC
        LIMIT 10
        """
        state_df = pd.read_sql_query(state_query, engine)

        fig4 = px.bar(state_df, x="State", y="sales", title="상위 10개 주별 매출액")
        fig4.update_layout(height=300)
        st.plotly_chart(fig4, use_container_width=True)


if __name__ == "__main__":
    render_dashboard()
