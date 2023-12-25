import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import streamlit as st
import urllib
from func import DataAnalyzer, BrazilMapPlotter
from babel.numbers import format_currency

sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

# INISIALISASI DATASET
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
all_df = pd.read_csv("https://raw.githubusercontent.com/raffly10/dicoding-proyek-analisis-data/main/DATAREAL/DATASET123.csv")
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

# DATASET_GEOLOCATION
geolocation = pd.read_csv("https://raw.githubusercontent.com/raffly10/dicoding-proyek-analisis-data/main/DATAREAL/DATA_GEOLOCATION.csv")
data = geolocation.drop_duplicates(subset='customer_unique_id')

for col in datetime_cols:
    all_df[col] = pd.to_datetime(all_df[col])

min_date = all_df["order_approved_at"].min()
max_date = all_df["order_approved_at"].max()

# SIDEBAR
with st.sidebar:
    # Title
    st.title("MY NAME IS MUHAMMAD RAFLY")

    # GAMBAR LOGO
    st.image("./dashboard/LOGO STREAMLIT.png")

    # RENTANG TANGGAL
    start_date, end_date = st.date_input(
        label="Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# MAIN
main_df = all_df[(all_df["order_approved_at"] >= str(start_date)) & 
                 (all_df["order_approved_at"] <= str(end_date))]

function = DataAnalyzer(main_df)
map_plot = BrazilMapPlotter(data, plt, mpimg, urllib, st)

daily_orders_df = function.create_daily_orders_df()
sum_spend_df = function.create_sum_spend_df()
sum_order_items_df = function.create_sum_order_items_df()
review_score, common_score = function.review_score_df()
state, most_common_state = function.create_bystate_df()
order_status, common_status = function.create_order_status()

# DEFINISIKAN LAYAR UTAMA STREAMLIT
st.title("E-COMMERCE DATA SCIENTIST")

# MASUKAN TEKS DESKRIPSI
st.write("**Dashboard dibuat untuk e-commerce data scientist.**")

# PESANAN HARIAN
st.subheader("PESANAN HARIAN")
col1, col2 = st.columns(2)

with col1:
    total_order = daily_orders_df["order_count"].sum()
    st.markdown(f"Total Order: **{total_order}**")

with col2:
    total_revenue = format_currency(daily_orders_df["revenue"].sum(), "IDR", locale="id_ID")
    st.markdown(f"Total Revenue: **{total_revenue}**")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    daily_orders_df["order_approved_at"],
    daily_orders_df["order_count"],
    marker="o",
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

# PENGELUARAN UANG CUSTOMER
st.subheader("PENGELUARAN UANG PELANGGAN")
col1, col2 = st.columns(2)

with col1:
    total_spend = format_currency(sum_spend_df["total_spend"].sum(), "IDR", locale="id_ID")
    st.markdown(f"Total Spend: **{total_spend}**")

with col2:
    avg_spend = format_currency(sum_spend_df["total_spend"].mean(), "IDR", locale="id_ID")
    st.markdown(f"Average Spend: **{avg_spend}**")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    sum_spend_df["order_approved_at"],
    sum_spend_df["total_spend"],
    marker="o",
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

# ITEM YANG DI-ORDER
st.subheader("ITEM YANG DIORDER")
col1, col2 = st.columns(2)

with col1:
    total_items = sum_order_items_df["product_count"].sum()
    st.markdown(f"Total Items: **{total_items}**")

with col2:
    avg_items = sum_order_items_df["product_count"].mean()
    st.markdown(f"Average Items: **{avg_items}**")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(45, 25))

sns.barplot(x="product_count", y="product_category_name_english", data=sum_order_items_df.head(5), palette="viridis", ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("NOMOR PENJUALAN", fontsize=75)
ax[0].set_title("PRODUK TERLARIS", loc="center", fontsize=85)
ax[0].tick_params(axis ='y', labelsize=60)
ax[0].tick_params(axis ='x', labelsize=55)

sns.barplot(x="product_count", y="product_category_name_english", data=sum_order_items_df.sort_values(by="product_count", ascending=True).head(5), palette="viridis", ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("NOMOR PENJUALAN", fontsize=75)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("PRODUK KURANG LARIS", loc="center", fontsize=85)
ax[1].tick_params(axis='y', labelsize=60)
ax[1].tick_params(axis='x', labelsize=55)

st.pyplot(fig)

# CEK NILAI
st.subheader("CEK NILAI")
col1,col2 = st.columns(2)

with col1:
    avg_review_score = review_score.mean()
    st.markdown(f"CEK NILAI RATA-RATA: **{avg_review_score}**")

with col2:
    most_common_review_score = review_score.value_counts().index[0]
    st.markdown(f"SKOR ULASAN PALING UMUM: **{most_common_review_score}**")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=review_score.index, 
            y=review_score.values, 
            order=review_score.index,
            palette=["#068DA9" if score == common_score else "#D3D3D3" for score in review_score.index]
            )

plt.title("NILAI RATING PELANGGAN UNTUK LAYANAN", fontsize=15)
plt.xlabel("RATING")
plt.ylabel("PERHITUNGAN")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# TAMBAH LABEL DI SETIAP BAR
for i, v in enumerate(review_score.values):
    ax.text(i, v + 5, str(v), ha='center', va='bottom', fontsize=12, color='black')

st.pyplot(fig)

# DEMOGRAFI PELANGGAN
st.subheader("DEMOGRAFI PELANGGAN")
tab1, tab2, tab3 = st.tabs(["State", "Order Status", "Geolocation"])

with tab1:
    most_common_state = state.customer_state.value_counts().index[0]
    st.markdown(f"NEGARA PALING UMUM: **{most_common_state}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=state.customer_state.value_counts().index,
                y=state.customer_count.values, 
                data=state,
                palette=["#068DA9" if score == most_common_state else "#D3D3D3" for score in state.customer_state.value_counts().index]
                    )

    plt.title("NOMOR PELANGGAN DARI NEGARA", fontsize=15)
    plt.xlabel("NEGARA")
    plt.ylabel("NOMOR PELANGGAN")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab2:
    common_status_ = order_status.value_counts().index[0]
    st.markdown(f"pesanan paling umum: **{common_status_}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=order_status.index,
                y=order_status.values,
                order=order_status.index,
                palette=["#068DA9" if score == common_status else "#D3D3D3" for score in order_status.index]
                )
    
    plt.title("Status Pesanan", fontsize=15)
    plt.xlabel("Status")
    plt.ylabel("Perhitungan")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab3:
    map_plot.plot()

    with st.expander("PENJELASAN"):
        st.write('Berdasarkan grafik yang ditampilkan, pelanggan di wilayah tenggara dan selatan mendominasi. Mengenai informasi lainnya, pelanggan lebih yang mendominasi berada di kota-kota yang merupakan ibu kota dari negara tersebut yaitu (Sao Paulo, Rio de Janeiro, Porto Alegre, dan lain sebagainya).')

st.caption('Copyright (C) Muhammad Rafly 2023')