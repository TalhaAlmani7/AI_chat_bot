
import streamlit as st

from agent import run_agent


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Tool-Calling Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM UI / CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GLOBAL APP
       ===================================================== */

    .stApp {
        background: #0b1220;
    }

    .main .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #263244;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    section[data-testid="stSidebar"] * {
        color: #f8fafc;
    }

    .sidebar-title {
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 4px;
    }

    .sidebar-subtitle {
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 20px;
    }


    /* =====================================================
       SIDEBAR BUTTONS
       ===================================================== */

    section[data-testid="stSidebar"] .stButton {
        margin-bottom: 8px;
    }

    section[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: #1e293b;
        color: #f8fafc !important;
        border: 1px solid #334155;
        border-radius: 12px;
        min-height: 44px;
        font-size: 15px;
        font-weight: 600;
        transition: 0.2s ease;
    }

    section[data-testid="stSidebar"] .stButton > button:hover {
        background: #263b59;
        border-color: #60a5fa;
        color: #ffffff !important;
    }


    /* =====================================================
       MAIN HEADER
       ===================================================== */

    .main-title {
        font-size: 42px;
        font-weight: 750;
        color: #ffffff;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }

    .main-subtitle {
        font-size: 16px;
        color: #94a3b8;
        margin-bottom: 28px;
    }


    /* =====================================================
       CHAT AREA
       ===================================================== */

    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 14px 18px;
        margin-bottom: 14px;
        border: 1px solid #334155;
    }

    /* User bubble */
    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {
        background: #17345c;
        border-color: #2563eb;
    }

    /* Assistant bubble */
    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) {
        background: #162235;
        border-color: #334155;
    }

    /* Chat text */
    [data-testid="stChatMessage"] p {
        color: #f8fafc !important;
        font-size: 16px !important;
        line-height: 1.65 !important;
    }


    /* =====================================================
       CHAT INPUT - IMPORTANT FIX
       ===================================================== */

    [data-testid="stChatInput"] {
        background: #111827 !important;
        border: 1px solid #475569 !important;
        border-radius: 16px !important;
        padding: 4px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    [data-testid="stChatInput"] > div {
        background: #111827 !important;
        border-radius: 14px !important;
    }

    [data-testid="stChatInput"] textarea {
        background: #111827 !important;
        color: #ffffff !important;
        caret-color: #60a5fa !important;
        font-size: 16px !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }

    [data-testid="stChatInput"] textarea:focus {
        background: #111827 !important;
        color: #ffffff !important;
    }

    /* Send button */
    [data-testid="stChatInput"] button {
        background: #2563eb !important;
        border-radius: 10px !important;
    }

    [data-testid="stChatInput"] button:hover {
        background: #1d4ed8 !important;
    }


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {
        border-color: #263244 !important;
    }


    /* =====================================================
       SPINNER
       ===================================================== */

    [data-testid="stSpinner"] {
        color: #60a5fa !important;
    }


    /* =====================================================
       MOBILE / SMALL SCREEN
       ===================================================== */

    @media (max-width: 768px) {

        .main-title {
            font-size: 30px;
        }

        .main-subtitle {
            font-size: 14px;
        }

        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🤖 AI Agent</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-subtitle">Tool-Calling Assistant</div>',
        unsafe_allow_html=True,
    )

    st.caption("Powered by Qwen 2.5 + Ollama")

    st.divider()

    st.subheader("🛠️ Available Tools")

    st.button(
        "🧮  Calculator",
        use_container_width=True,
    )

    st.button(
        "🌤️  Weather",
        use_container_width=True,
    )

    st.button(
        "🌐  Web Search",
        use_container_width=True,
    )

    st.button(
        "🕒  Date & Time",
        use_container_width=True,
    )

    st.button(
        "📏  Unit Conversion",
        use_container_width=True,
    )

    st.divider()

    st.subheader("💡 Example Prompts")

    st.caption("• What is 25% of 800?")

    st.caption("• What's the weather in Lahore?")

    st.caption("• Search the latest AI news.")

    st.caption("• Convert 10 km to miles.")


# =========================================================
# CONVERSATION MEMORY
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant. "
                "Use tools when necessary. "
                "For calculations, use calculator tools. "
                "For weather questions, use the weather tool. "
                "For current or web-based information, use web_search. "
                "Do not invent tool results. "
                "Always follow the user's requested format and length. "
                "If the user asks for 2 lines, answer in exactly 2 lines. "
                "Do not copy or repeat raw tool results. "
                "Summarize tool results into a concise final answer."
            ),
        }
    ]


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 AI Tool-Calling Agent</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-subtitle">'
    'Powered by Qwen 2.5 + Ollama'
    '</div>',
    unsafe_allow_html=True,
)


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    # Never display system message
    if message["role"] == "system":
        continue

    # User
    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤",
        ):
            st.markdown(message["content"])


    # Assistant
    elif message["role"] == "assistant":

        with st.chat_message(
            "assistant",
            avatar="🤖",
        ):
            st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

user_input = st.chat_input(
    "Ask your AI agent anything..."
)


# =========================================================
# PROCESS MESSAGE
# =========================================================

if user_input:

    # ---------------------------------------------
    # USER MESSAGE
    # ---------------------------------------------

    with st.chat_message(
        "user",
        avatar="👤",
    ):
        st.markdown(user_input)


    # ---------------------------------------------
    # SAVE USER MESSAGE
    # ---------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )


    # ---------------------------------------------
    # ASSISTANT RESPONSE
    # ---------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖",
    ):

        with st.spinner("🤔 Thinking..."):

            answer = run_agent(
                user_input,
                st.session_state.messages,
            )

        st.markdown(answer)


    # ---------------------------------------------
    # SAVE ASSISTANT RESPONSE
    # ---------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

