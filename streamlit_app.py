import html

import streamlit as st

PROFILE = {
	"name": "배서현",
	"headline": "배우고 만들며, 나만의 방향을 찾아갑니다.",
	"introduction": "전공과 관심 분야, 나를 잘 설명하는 이야기를 적어 보세요.",
	"dream": "앞으로 이루고 싶은 꿈과 그 꿈을 꾸게 된 이유를 적어 보세요.",
	"affiliation": "학교명 · 학과명 · 학년을 입력하세요",
	"email": "hello@example.com",
}

COURSES = [
	("수업 이름 1", "수업에서 배운 내용이나 기억에 남는 활동을 적어 보세요."),
	("수업 이름 2", "관심 분야와 연결된 내용 또는 프로젝트를 소개해 보세요."),
	("수업 이름 3", "새롭게 알게 된 점이나 앞으로 더 배우고 싶은 것을 적어 보세요."),
]

COURSE_ROWS = "".join(
	f'<article class="course-row"><span class="course-index">0{index}</span>'
	f'<div><h3>{html.escape(title)}</h3><p>{html.escape(description)}</p></div>'
	f'<span class="course-mark">+</span></article>'
	for index, (title, description) in enumerate(COURSES, start=1)
)

st.set_page_config(page_title=f"{PROFILE['name']} | 자기소개", page_icon="P", layout="wide")

st.markdown(
	"""
	<style>
	:root {
		--paper: #f1f3ed;
		--ink: #192622;
		--muted: #64716b;
		--line: #cbd2c9;
		--coral: #d65b45;
		--mint: #c1e3d2;
	}
	.stApp { background: var(--paper); color: var(--ink); }
	.block-container { max-width: 1180px; padding: 0 42px 64px; }
	header[data-testid="stHeader"] { background: transparent; }
	#MainMenu, footer { visibility: hidden; }
	.profile-nav {
		height: 76px; display: flex; align-items: center; justify-content: space-between;
		border-bottom: 1px solid var(--line); font-family: sans-serif;
	}
	.nav-brand { color: var(--ink); font-size: 13px; font-weight: 800; letter-spacing: 1px; }
	.nav-links { display: flex; gap: 30px; }
	.nav-links a { color: var(--ink); font-size: 12px; text-decoration: none; }
	.nav-links a:hover { color: var(--coral); }
	.hero {
		min-height: 490px; margin: 0 -42px; padding: 60px max(42px, calc((100vw - 1096px) / 2));
		display: flex; flex-direction: column; justify-content: flex-end; position: relative;
		overflow: hidden; background-color: #31443d;
		background-image: url("https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=2200&q=85");
		background-size: cover; background-position: center 52%; color: white;
		animation: arrive .7s ease-out both;
	}
	.hero::before { content: ""; position: absolute; inset: 0; background: rgba(15, 29, 25, .58); }
	.hero-content { max-width: 760px; position: relative; z-index: 1; }
	.eyebrow { color: var(--mint); font: 700 12px sans-serif; letter-spacing: 2px; }
	.hero h1 { margin: 18px 0 12px; color: white; font-size: 58px; line-height: 1.14; font-weight: 750; }
	.hero h1 span { color: var(--mint); }
	.hero p { max-width: 620px; margin: 0; color: #f0f3ef; font-size: 19px; line-height: 1.7; }
	.section { padding: 82px 0; border-bottom: 1px solid var(--line); }
	.section-label { color: var(--coral); font: 800 12px sans-serif; letter-spacing: 1.7px; }
	.section h2 { margin: 14px 0 22px; color: var(--ink); font-size: 34px; line-height: 1.25; }
	.section p { margin: 0; color: var(--muted); font-size: 17px; line-height: 1.85; }
	.about-grid { display: grid; grid-template-columns: 1fr 1.45fr; gap: 72px; align-items: start; }
	.about-note { border-left: 3px solid var(--coral); padding-left: 22px; }
	.dream-band { display: grid; grid-template-columns: .8fr 1.2fr; gap: 72px; align-items: center; }
	.dream-quote { color: var(--ink) !important; font-size: 25px !important; line-height: 1.55 !important; }
	.affiliation { display: flex; justify-content: space-between; align-items: center; gap: 24px; }
	.affiliation-value { color: var(--ink) !important; font-size: 22px !important; }
	.course-list { border-top: 1px solid var(--line); margin-top: 34px; }
	.course-row {
		min-height: 108px; display: grid; grid-template-columns: 64px 1fr 32px; gap: 18px;
		align-items: center; border-bottom: 1px solid var(--line); animation: arrive .5s ease-out both;
	}
	.course-row:nth-child(2) { animation-delay: .08s; }
	.course-row:nth-child(3) { animation-delay: .16s; }
	.course-index { color: var(--coral); font: 700 13px sans-serif; }
	.course-row h3 { margin: 0 0 7px; color: var(--ink); font-size: 19px; }
	.course-row p { font-size: 14px; }
	.course-mark { color: var(--coral); font-size: 22px; }
	.profile-footer { padding: 34px 0 6px; display: flex; justify-content: space-between; gap: 16px; }
	.profile-footer p { margin: 0; color: var(--muted); font-size: 13px; }
	.profile-footer a { color: var(--ink); text-decoration-color: var(--coral); text-underline-offset: 4px; }
	@keyframes arrive { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
	@media (max-width: 700px) {
		.block-container { padding: 0 22px 40px; }
		.profile-nav { height: 64px; }
		.nav-links { gap: 14px; }
		.nav-links a { font-size: 10px; }
		.hero { min-height: 430px; margin: 0 -22px; padding: 42px 22px; background-position: 58% center; }
		.hero h1 { font-size: 42px; }
		.hero p { font-size: 16px; }
		.section { padding: 58px 0; }
		.section h2 { font-size: 29px; }
		.about-grid, .dream-band { grid-template-columns: 1fr; gap: 24px; }
		.affiliation { align-items: flex-start; flex-direction: column; gap: 14px; }
		.course-row { grid-template-columns: 38px 1fr 20px; gap: 10px; }
		.course-row p { font-size: 13px; }
		.profile-footer { flex-direction: column; }
	}
	</style>
	""",
	unsafe_allow_html=True,
)

name = html.escape(PROFILE["name"])
headline = html.escape(PROFILE["headline"])
introduction = html.escape(PROFILE["introduction"])
dream = html.escape(PROFILE["dream"])
affiliation = html.escape(PROFILE["affiliation"])
email = html.escape(PROFILE["email"])

st.markdown(
	f"""
	<nav class="profile-nav">
		<div class="nav-brand">MY PROFILE / 2026</div>
		<div class="nav-links">
			<a href="#about">소개</a><a href="#dream">꿈</a>
			<a href="#affiliation">소속</a><a href="#courses">수업</a>
		</div>
	</nav>
	<section class="hero">
		<div class="hero-content">
			<div class="eyebrow">A LITTLE ABOUT ME</div>
			<h1>안녕하세요,<br><span>{name}</span>입니다.</h1>
			<p>{headline}</p>
		</div>
	</section>
	<section class="section about-grid" id="about">
		<div><div class="section-label">01 / INTRODUCTION</div><h2>저를 소개합니다</h2></div>
		<div class="about-note"><p>{introduction}</p></div>
	</section>
	<section class="section dream-band" id="dream">
		<div><div class="section-label">02 / MY DREAM</div><h2>그리고, 나의 꿈</h2></div>
		<p class="dream-quote">“{dream}”</p>
	</section>
	<section class="section affiliation" id="affiliation">
		<div><div class="section-label">03 / AFFILIATION</div><h2>지금의 소속</h2></div>
		<p class="affiliation-value">{affiliation}</p>
	</section>
	<section class="section" id="courses">
		<div class="section-label">04 / WHAT I'VE LEARNED</div>
		<h2>제가 들었던 수업</h2>
		<div class="course-list">{COURSE_ROWS}</div>
	</section>
	<footer class="profile-footer">
		<p>조금씩 배우고, 차근차근 만들어 갑니다.</p>
		<p>연락하기 · <a href="mailto:{email}">{email}</a></p>
	</footer>
	""",
	unsafe_allow_html=True,
)
