import streamlit as st

# Removes top bar and deploy button
st.markdown(
    """
<style>
/* Hide Streamlit header (includes the black bar + deploy button) */
header {visibility: hidden;}

/* Hide Streamlit footer */
footer {visibility: hidden;}

/* Extra: remove navbar height spacing */
header {height: 0px;}
</style>
""",
    unsafe_allow_html=True,
)


st.markdown(
    """
<style>

/* Base glow animation class */
.flicker-glow {
    font-size: 20px;
    font-weight: bold;
    color: white;

}

/* Keyframes for flicker effect */
@keyframes flicker {
    0%, 90% {
        /* Regular BLUE glow */
        text-shadow:
            0 0 5px #00aaff,
            0 0 10px #00aaff,
            0 0 20px #00aaff,
            0 0 40px #0099ff,
            0 0 80px #0077cc;
        color: white;
    }

    92%, 96% {
        /* Temporary PINK glow */
        text-shadow:
            0 0 5px #ff4dd8,
            0 0 10px #ff1fc9,
            0 0 20px #ff00c8,
            0 0 40px #ff0088,
            0 0 80px #ff00cc;
        color: #ffd6f7;
    }

    98% {
        /* Slight dim before returning to blue */
        text-shadow:
            0 0 5px #003355,
            0 0 10px #002244;
        color: #cccccc;
    }
}

</style>

<p class="flicker-glow">Team Agartha</p>

""",
    unsafe_allow_html=True,
)


WHITE = "#FFFFFF"
BLACK = "#000000"
ACCENT = "#00f5ff"  # neon cyan
BG = "#12112"


st.markdown(
    """
<p class="flicker-glow" style="animation: flicker 3s infinite;text-align:center; font-size:40px; font-family:'Orbitron', 'Courier New', monospace;">
    HackDécouverte Privacy Test
</p>
""",
    unsafe_allow_html=True,
)

if "q_index" not in st.session_state:
    st.session_state.q_index = 0


if "score" not in st.session_state:
    st.session_state.score = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

# Set Background Color
st.markdown(
    """
<style>
.main {
    background-color: #12112;
}
</style>
""",
    unsafe_allow_html=True,
)


questions = [
    {
        "str": "How often do you reuse the same password across university accounts?",
        "weight": 5,
        "ans": ["Always", "Often", "Sometimes", "Never"],
        "feedback": [
            "Reusing passwords across multiple accounts significantly increases your risk: one breach compromises all connected services. Use a password manager to generate and store unique passwords for every platform.",
            "Using the same password often still exposes you to credential-stuffing attacks. Begin transitioning to unique passwords using a secure manager like Bitwarden or 1Password.",
            "Occasional reuse is better than constant reuse, but it still leaves you vulnerable to cross-site breaches. Aim to fully eliminate password repetition and adopt a password manager workflow.",
            "Good password hygiene reduces your exposure in case of a breach. Maintain this practice and enable two-factor authentication on critical accounts for additional protection.",
        ],
    },
    {
        "str": "Do you let your college apps (Moodle, Omnivox,  etc.) access your location?",
        "weight": 3,
        "ans": ["Always", "Only when required", "Rarely", "Never"],
        "feedback": [
            "Allowing constant location access expands the data footprint apps collect about you. Restrict location access to essential use cases only.",
            "Allowing location access only when needed is solid. Review app permissions regularly and remove location permission when not required.",
            "Limiting location access reduces unnecessary tracking. Continue reviewing permissions for outdated apps.",
            "Denying location access unless necessary ensures apps gather only what they need. This reduces tracking risk.",
        ],
    },
    {
        "str": "How often do you submit assignments or access grades using unsecured public Wi-Fi?",
        "weight": 5,
        "ans": ["Daily", "Weekly", "Occasionally", "Never"],
        "feedback": [
            "Public Wi-Fi exposes you to packet sniffing and rogue access points. Avoid logging into sensitive accounts on open networks and use a VPN if needed.",
            "Weekly access on unsecured networks still poses substantial risk. Use a VPN or a personal hotspot for any sensitive data.",
            "Occasional use is less dangerous but avoid logging into grades or emails on public Wi-Fi. Prefer secured networks.",
            "Avoiding unsecured public Wi-Fi for sensitive tasks is best practice. Continue using secured networks or VPNs for academic info.",
        ],
    },
    {
        "str": "How much personal info do you expose on class group chats or Discord servers?",
        "weight": 4,
        "ans": ["A lot", "A fair amount", "Some", "Almost none"],
        "feedback": [
            "Sharing a lot of personal info increases exposure to leaks and impersonation. Limit info and use private messages for sensitive details.",
            "Sharing a fair amount is risky as group chats aren’t secure. Share only what is required for coursework or coordination.",
            "Keeping personal details minimal is good. Continue verifying necessity of what you share.",
            "Sharing almost no personal data reduces profiling risk. Maintain cautious communication practices.",
        ],
    },
    {
        "str": "Do you store your school documents (ID scans, transcripts, essays) in cloud drives?",
        "weight": 4,
        "ans": ["Yes, unprotected", "Yes, encrypted", "Only temporarily", "Never"],
        "feedback": [
            "Storing documents unprotected in the cloud exposes them if your account is compromised. Use encrypted storage or password-protected archives.",
            "Encrypted cloud storage is strong. Protect encryption keys and credentials securely.",
            "Temporary storage is acceptable but often becomes long-term. Treat temporary uploads securely.",
            "Avoiding cloud storage removes breach risk. If using cloud, ensure end-to-end encryption and access control.",
        ],
    },
    {
        "str": "How secure is your laptop that you use for lectures?",
        "weight": 4,
        "ans": [
            "No password",
            "Weak password",
            "Strong password",
            "Strong password + 2FA",
        ],
        "feedback": [
            "A device with no password is highly vulnerable. Set a strong password and enable screen lock.",
            "Weak passwords can be compromised. Strengthen credentials and enable encryption or biometrics.",
            "Strong password provides baseline protection. Pair with disk encryption and enable 2FA for accounts.",
            "Strong password + 2FA is excellent. Keep software updated and enable device encryption.",
        ],
    },
    {
        "str": "How often do you leave your devices unattended in the library or cafeteria?",
        "weight": 2,
        "ans": ["Constantly", "Sometimes", "Rarely", "Never"],
        "feedback": [
            "Leaving devices unattended frequently increases risk of theft or unauthorized access. Lock your screen and take devices with you.",
            "Occasionally leaving devices unattended is still risky. Develop habit of locking devices and keeping them physically close.",
            "Rarely leaving devices unattended is good. Continue locking consistently.",
            "Never leaving devices unattended is ideal. Enable screen locks and use cable locks if needed.",
        ],
    },
    {
        "str": "Do you use your school email to sign up for random services?",
        "weight": 3,
        "ans": ["All the time", "Sometimes", "Rarely", "Never"],
        "feedback": [
            "Using academic email for unrelated services increases spam, phishing, and long-term data retention. Reserve school email for institutional use only.",
            "Occasional use still creates exposure. Use a separate personal email for sign-ups.",
            "Rare use is safer. Keep academic accounts isolated.",
            "Keeping school email private prevents spam, phishing, and data leaks. Maintain separation.",
        ],
    },
    {
        "str": "How often do you post your class schedule or campus location online?",
        "weight": 4,
        "ans": ["Regularly", "Sometimes", "Rarely", "Never"],
        "feedback": [
            "Posting schedule regularly exposes predictable routines. Avoid sharing location patterns publicly.",
            "Sharing location occasionally is risky. Keep schedules private.",
            "Rare posting minimizes exposure. Remove identifying details.",
            "Not sharing schedules preserves physical privacy. Continue keeping info offline.",
        ],
    },
    {
        "str": "Do you back up your notes and academic files somewhere safe?",
        "weight": 2,
        "ans": ["Never", "Occasionally", "Frequently", "Always"],
        "feedback": [
            "Not backing up academic material risks loss due to device failure. Use automated backups with cloud or encrypted external storage.",
            "Occasional backups leave gaps. Enable scheduled backups.",
            "Frequent backups are solid. Verify backups and test restores.",
            "Always backing up notes is ideal. Maintain redundant backups offline and in cloud.",
        ],
    },
]

total_weight = 0
for q in questions:
    total_weight += q["weight"]


def on_answer(index, weight):
    st.session_state.answers.append(index)
    st.session_state.q_index += 1
    st.session_state.score += (index / 3) * weight


def reset():
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answers = []


if st.session_state.q_index == -1:
    if st.button("Reset", on_click=reset):
        st.experimental_rerun()

    st.markdown('<div class="centered-strip">', unsafe_allow_html=True)

    # 2. Insert the Streamlit text area component inside the visual wrapper
    # We assign it to a variable 'user_input' so we can use the text later if needed
    user_input = st.text_area(
        "User Input",
        height=100,
        label_visibility="collapsed",
        placeholder="Type your message here...",
    )

    st.markdown(
        """
    <style>
        /* This targets the specific div we create below */
        .centered-strip {
            background-color: #3cb371; /* MediumSeaGreen */
            min-height: 150px;         /* Use min-height since st.code size is variable */
            width: 800px;              /* Fixed width */
            border-radius: 10px;       /* Gentle corners */

            /* Center the element horizontally using margin auto */
            margin: 50px auto;

            /* Add padding so the text area doesn't touch the edge */
            padding: 20px;

            /* Optional: Shadow for depth */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        /* NOTE: We remove the old CSS for .centered-strip textarea
        because we are now using the st.code widget.
        */
    </style>
""",
        unsafe_allow_html=True,
    )
    # ---------------------------

    # --- APPLICATION OUTPUT CONTENT ---
    terminal_output = """
    $ initializing_system... done
    $ user_access_granted: GUEST
    $ status: RUNNING QUIZ APP
    $ output_log: Ready for next instruction...
    """

    # --- HTML ELEMENT CREATION WRAPPER ---
    # 1. Open the custom styled div
    st.markdown('<div class="centered-strip">', unsafe_allow_html=True)

    # 3. Close the custom styled div
    st.markdown("</div>", unsafe_allow_html=True)
elif st.session_state.q_index < len(questions):
    # Calculate Progress
    total_questions = len(questions)
    current_progress = st.session_state.q_index
    progress_percent = int((current_progress / total_questions) * 100)

    # Custom Progress Bar CSS
    st.markdown(
        f"""
    <style>
    /* --- CYBERPUNK PROGRESS BAR --- */
    .cyber-progress-bar-container {{
        width: 100%;
        height: 30px;
        background-color: #2e083a; /* Dark background for the bar track */
        border: 2px solid #ff0099; /* Pink outer border */
        border-radius: 5px;
        margin: 20px 0;
        box-shadow: 0 0 10px #ff009966, inset 0 0 5px #ff009933; /* Pink outer glow */
        overflow: hidden;
    }}

    .cyber-progress-bar-fill {{
        height: 100%;
        width: {progress_percent}%; /* Progress based on calculation */
        background: linear-gradient(90deg, #00c7ff, #00f5ff); /* Cyan gradient fill */
        transition: width 0.4s ease-in-out;
        position: relative;
        box-shadow: 0 0 8px #00f5ff, inset 0 0 4px #00f5ff; /* Cyan inner glow */
    }}

    .cyber-progress-bar-label {{
        position: absolute;
        top: 0%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #ffd6f7; /* Light pink/white text */
        font-size: 18px;
        font-weight: bold;
        text-shadow: 0 0 5px #ff0099, 0 0 3px #ff0099; /* Pink text glow */
        white-space: nowrap;
    }}
    </style>

    <div class="cyber-progress-bar-container">
        <div class="cyber-progress-bar-fill"></div>
        <div class="cyber-progress-bar-label">
            QUESTION {current_progress + 1} / {total_questions} ({progress_percent}%)
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<h2 style='text-align:center; color:#00f5ff; font:ComicSans font-weight:bold;'>{questions[st.session_state.q_index]['str']}</h2>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:120px;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
<style>

/* Center buttons inside columns */
div.stButton {
    display: flex;
    justify-content: center;
}

/* --- CYBERPUNK BUTTON --- */
div.stButton > button {
    width: 220px;
    height: 65px;
    padding: 0;
    font-size: 18px;
    font-weight: 600;

    background: #0d0f16;                /* deep dark bg */
    color: #00f5ff;                     /* neon cyan text */
    border: 2px solid #00f5ffcc;        /* neon border */
    border-radius: 14px;

    box-shadow:
        0 0 12px #00eaff55,
        inset 0 0 12px #00eaff33;

    text-shadow: 0 0 6px #00f6ff;
    transition: all 0.18s ease-in-out;
}

/* --- HOVER GLOW --- */
div.stButton > button:hover {
    border-color: #ff0099;
    color: #ff6ad5;
    text-shadow: 0 0 8px #ff6ad5;

    box-shadow:
        0 0 25px #ff009988,
        inset 0 0 20px #ff009944;

    transform: translateY(-3px) scale(1.03);
}

/* --- CLICK EFFECT --- */
div.stButton > button:active {
    transform: scale(0.96);
    box-shadow:
        0 0 10px #ff009955,
        inset 0 0 10px #ff009944;
}

/* --- ANIMATED NEON PULSE --- */
@keyframes pulseGlow {
  0% {
    box-shadow: 0 0 12px #00eaff55;
  }
  50% {
    box-shadow: 0 0 28px #00eaffaa;
  }
  100% {
    box-shadow: 0 0 12px #00eaff55;
  }
}

div.stButton > button {
    animation: pulseGlow 2.4s infinite ease-in-out;
}

</style>
""",
        unsafe_allow_html=True,
    )

    # Create 4 equal columns for buttons
    cols = st.columns(4)
    for i, col in enumerate(cols):
        with col:
            if st.button(
                questions[st.session_state.q_index]["ans"][i],
                key=f"{st.session_state.q_index}_{i}",
                on_click=on_answer,
                args=[i, questions[st.session_state.q_index]["weight"]],
            ):
                pass


else:
    score_percent = int(st.session_state.score / total_weight * 100)

    if score_percent >= 75:
        verdict = "Excellent: your privacy practices are strong. Maintain your protections and review periodically."
        color = "#2ECC71"
    elif score_percent >= 50:
        verdict = "Moderate: reasonable practices, but some areas need improvement. Focus on authentication and network safety."
        color = "#F1C40F"
    else:
        verdict = "Needs significant improvement: several privacy controls are weak. Act immediately on high-risk items."
        color = "#E74C3C"

    st.markdown(
        f"<h2 style='text-align:center; color:{ACCENT};'>Your Privacy Assessment</h2>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
    <div style="text-align:center; margin-bottom:20px;">
        <div style="width:180px; height:180px; border-radius:50%; border:8px solid {color};
                    color:{color}; font-size:48px; font-weight:700; display:inline-flex;
                    align-items:center; justify-content:center; margin:auto;">
            {score_percent}%
        </div>
        <p style="color:white; font-size:16px; max-width:600px; margin:auto;">{verdict}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if st.button("Reset", on_click=reset):
        st.experimental_rerun()
    st.markdown(
        "<h3 style='color:white;'>Detailed Professional Advice</h3>",
        unsafe_allow_html=True,
    )
    if st.button("Get advice from Gemini"):
        st.session_state.q_index = -1
    for i, q in enumerate(questions):
        ans_idx = st.session_state.answers[i]
        # st.write(ans_idx)
        st.markdown(
            f"""
        <div style="background-color:#0d0f16; padding:12px; border-radius:10px; margin-bottom:8px;
                    border:1px solid #22272a;">
            <p style="color:{ACCENT}; font-weight:bold;">Q{i + 1}: {q["str"]}</p>
            <p style="color:#ffffff; margin:4px 0 0 0;">Your answer: {q["ans"][ans_idx]}</p>
            <p style="color:#d0d0d0; margin:4px 0 0 0;">Advice: {q["feedback"][ans_idx]}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
