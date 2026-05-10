import pandas as pd
import streamlit as st

from pathlib import Path


st.set_page_config(
    page_title="Vision Guard AI",
    page_icon="🛵",
    layout="wide"
)


st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
    }

    h1, h2, h3 {
        color: white;
    }

    .stMetric {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #334155;
    }

    .title-box {
        background: linear-gradient(to right, #2563eb, #7c3aed);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }

    .status-box {
        background-color: #16a34a;
        color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="title-box">
        <h1>🛵 Vision Guard AI Dashboard</h1>
        <h3>AI-Based Helmet Detection & Cloud Monitoring System</h3>
    </div>
    """,
    unsafe_allow_html=True
)


csv_file = Path("s3_logs.csv")


if not csv_file.exists():

    st.warning(
        "No violation logs found."
    )

else:

    df = pd.read_csv(csv_file)

    total_violations = len(df)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🚨 Total Violations",
            total_violations
        )

    with col2:

        st.metric(
            "📸 Images Captured",
            total_violations
        )

    with col3:

        st.markdown(
            """
            <div class="status-box">
                ✅ SYSTEM ACTIVE
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader(
        "📋 Violation Logs"
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=300
    )

    if total_violations > 0:

        latest = df.iloc[-1]

        image_url = str(
            latest["s3_url"]
        ).strip()

        latest_image = Path(
            "captured_alerts"
        ) / latest["image_name"]

        st.divider()

        left, right = st.columns([1, 1])

        with left:

            st.subheader(
                "⚠️ Latest Violation Details"
            )

            st.success(
                f"📅 Timestamp: {latest['timestamp']}"
            )

            st.info(
                f"🖼️ Image Name: {latest['image_name']}"
            )

            st.code(
                image_url
            )

        with right:

            st.subheader(
                "📸 Latest Uploaded Image"
            )

            if latest_image.exists():

                st.image(
                    str(latest_image),
                    caption="Latest Uploaded Violation",
                    use_container_width=True
                )

            else:

                st.error(
                    "Image not found in captured_alerts folder."
                )

    st.divider()

    st.markdown(
        """
        <center>
        <h4 style='color:gray;'>
        Vision Guard AI • Real-Time Helmet Detection System
        </h4>
        </center>
        """,
        unsafe_allow_html=True
    )