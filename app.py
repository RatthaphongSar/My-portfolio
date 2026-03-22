from flask import Flask, render_template_string

app = Flask(__name__)

portfolio = {
    "name": "Ratthaphong",
    "name_th": "รัฐพงค์",
    "role": "Computer Engineering Student",
    "level": "Junior Developer",
    "tagline": "Engineering real systems — not just writing code.",
    "objective": "พัฒนาทักษะ Software Development, Backend Systems และ Cloud Infrastructure เพื่อสร้างระบบที่รองรับการทำงานระดับ Enterprise เช่น ระบบตรวจสอบ Server, Automation และ Network Integration",
    "email": "rattapong.101@gmail.com",
    "github": "https://github.com/RatthaphongSar",
    "linkedin": "https://linkedin.com",
    "languages_spoken": [
        {"lang": "Thai",    "level": "Native"},
        {"lang": "English", "level": "Technical Working"},
    ],
    "skills_lang": [
        {"name": "C#",         "desc": "Backend / Tools / Automation",    "level": 60},
        {"name": "Python",     "desc": "Scripting, GUI (Tkinter)",         "level": 80},
        {"name": "JavaScript", "desc": "React + Vite",                     "level": 72},
        {"name": "SQL",        "desc": "Advanced Query / Store Procedure", "level": 88},
    ],
    "skills_infra": [
        {"name": "AWS",        "desc": "S3, Athena — Data Query & Storage"},
        {"name": "Azure",      "desc": "Cloud Service พื้นฐาน"},
        {"name": "Networking", "desc": "Cisco / Router / AP Config"},
        {"name": "Remote",     "desc": "Remote Desktop / CLI"},
        {"name": ".NET",       "desc": "C# Framework"},
        {"name": "Git",        "desc": "Version Control"},
    ],
    "db_skills": [
        "ออกแบบและจัดการ Database",
        "Advanced Query & Optimization",
        "Store Procedure",
        "Data Validation / Data Checking",
    ],
    "strengths": [
        {"icon": "◈", "name": "Problem Solving",         "desc": "แก้ปัญหาระบบจริง Network / Server"},
        {"icon": "◈", "name": "System Thinking",          "desc": "ออกแบบระบบขนาดใหญ่ Enterprise"},
        {"icon": "◈", "name": "Performance Optimization", "desc": "เน้น Scalability และ Efficiency"},
        {"icon": "◈", "name": "Automation Mindset",       "desc": "ลด Manual ด้วย Automation"},
    ],
    "projects": [
        {
            "name":  "Server Monitoring System",
            "scale": "~16,000 servers",
            "desc":  "ออกแบบและพัฒนาระบบตรวจสอบ Server จำนวนกว่า 16,000 เครื่อง ตรวจสอบการติดตั้งโปรแกรม, Database, Query และ Store Procedure รองรับการเลือกจำนวน Server ได้ยืดหยุ่น เน้น Performance และ Scalability",
            "tech":  ["C#", ".NET", "SQL", "Store Procedure", "Automation"],
            "highlights": ["16,000+ servers", "Performance-first", "Scalable design"],
            "type": "enterprise",
        },
        {
            "name":  "Automation Toolkit",
            "scale": "Internal Tools",
            "desc":  "ชุดเครื่องมือ Automation ที่ช่วยลดงาน Manual ตรวจสอบสถานะระบบอัตโนมัติ ลด Human Error และเพิ่มความเร็วในการ Deploy และ Monitor",
            "tech":  ["Python", "C#", "SQL", "Scripting"],
            "highlights": ["Zero manual steps", "Auto status check", "Error reduction"],
            "type": "tool",
        },
        {
            "name":  "AWS Data Pipeline",
            "scale": "Cloud Infrastructure",
            "desc":  "ออกแบบระบบจัดเก็บและ Query ข้อมูลบน AWS ใช้ S3 เป็น Data Lake และ Athena สำหรับ Query เพื่อ Analytics และ Reporting",
            "tech":  ["AWS S3", "AWS Athena", "SQL", "Cloud Architecture"],
            "highlights": ["Serverless query", "Cost-optimized", "Scalable storage"],
            "type": "cloud",
        },
        {
            "name":  "React Dashboard",
            "scale": "Frontend App",
            "desc":  "พัฒนา Web Dashboard ด้วย React + Vite แสดงผลข้อมูลจาก Backend API มี Data Visualization และ Real-time update สำหรับ Monitor ระบบ",
            "tech":  ["React", "Vite", "JavaScript", "REST API"],
            "highlights": ["Real-time UI", "Fast build", "Component-driven"],
            "type": "frontend",
        },
    ],
    "work_experience": [
        {
            "position": "Trainee Software support Engineer",
            "unit": "IT System Store Service Unit",
            "company": "Gosoft (thailand) co. ltd",
            "date_from": "Oct 2024",
            "date_to": "Present",
            "responsibilities": [
                "Resolved incidents in the Mobile Service Ordering Service reported by the Helpdesk and performed troubleshooting according to the reported issues.",
                "Developed SQL Query scripts for the Mobile Service Ordering Service.",
                "Developed tools for use within the Unit Stack, utilizing Python, FastAPI, and C# .NET Core.",
                "Maintained the local server database using Microsoft SQL Server, Azure Data, AWS and HeidiSQL Cloud.",
                "Support the back-end system of \"7-Eleven\" in the \"CP ALL group\"",
                "Check the system operation and check the database to support 7-Eleven stores"
            ]
        }
    ],
    "growth": [
        {"item": "Backend Architecture", "status": "learning"},
        {"item": "Distributed Systems",           "status": "learning"},
        {"item": "CI-CD",                "status": "next"},
        {"item": "Cloud Scaling & Microservices", "status": "next"},
    ],
}

HTML = r"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{{ p.name }} — Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Barlow:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@400;600;700;800&family=Noto+Sans+Thai:wght@400;600;700&display=swap" rel="stylesheet"/>
<style>
:root{
  --bg:#07090d;--surface:#0c0f15;--card:#10141c;--border:#1c2433;--border2:#243042;
  --accent:#e8a020;--accent2:#f0c060;--blue:#4a9eff;--green:#3dd68c;
  --text:#c8d4e0;--muted:#4a5e72;--muted2:#6a7e92;
  --mono:'Share Tech Mono',monospace;--sans:'Barlow',sans-serif;--cond:'Barlow Condensed',sans-serif;--thai:'Noto Sans Thai',sans-serif;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--sans);font-size:15px;line-height:1.7;overflow-x:hidden}
body::before{
  content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(74,158,255,.04) 1px,transparent 1px),
    linear-gradient(90deg,rgba(74,158,255,.04) 1px,transparent 1px),
    linear-gradient(rgba(74,158,255,.015) 1px,transparent 1px),
    linear-gradient(90deg,rgba(74,158,255,.015) 1px,transparent 1px);
  background-size:80px 80px,80px 80px,16px 16px,16px 16px;
}
::-webkit-scrollbar{width:3px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--border2)}
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  background:rgba(7,9,13,.92);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--border);
}
.nav-inner{
  max-width:1100px;margin:0 auto;padding:0 32px;
  display:flex;align-items:center;justify-content:space-between;height:56px;
}
.nav-logo{font-family:var(--mono);font-size:12px;color:var(--accent);display:flex;align-items:center;gap:8px}
.nav-bracket{color:var(--muted)}
.nav-id{font-family:var(--mono);font-size:10px;color:var(--muted);border-left:1px solid var(--border);padding-left:12px;letter-spacing:.1em}
.nav-links{display:flex;gap:4px}
.nav-links a{font-family:var(--mono);font-size:11px;color:var(--muted);text-decoration:none;padding:6px 12px;border-radius:3px;letter-spacing:.08em;transition:color .2s,background .2s}
.nav-links a:hover{color:var(--accent);background:rgba(232,160,32,.06)}
.wrap{max-width:1100px;margin:0 auto;padding:0 32px;position:relative;z-index:1}
.hero{min-height:100vh;display:flex;align-items:center;padding:120px 0 80px;position:relative}
.hero-inner{display:grid;grid-template-columns:1fr 320px;gap:72px;align-items:center}
.hero-eyebrow{font-family:var(--mono);font-size:11px;color:var(--blue);letter-spacing:.2em;margin-bottom:20px;display:flex;align-items:center;gap:12px}
.hero-eyebrow::before{content:'';display:block;width:28px;height:1px;background:var(--blue)}
.hero-name{font-family:var(--cond);font-size:clamp(3.5rem,7vw,6.5rem);font-weight:800;line-height:.92;letter-spacing:-.02em;color:#dce8f0;margin-bottom:6px}
.hero-name-th{font-family:var(--thai);font-size:1.3rem;font-weight:600;color:var(--muted2);margin-bottom:20px;letter-spacing:.05em}
.hero-role{font-family:var(--mono);font-size:13px;color:var(--accent);margin-bottom:6px}
.hero-role::before{content:'> ';color:var(--muted)}
.hero-level{font-family:var(--mono);font-size:11px;color:var(--muted);margin-bottom:28px}
.hero-desc{font-size:16px;line-height:1.8;color:var(--muted2);max-width:480px;margin-bottom:36px;font-family:var(--thai)}
.hero-btns{display:flex;gap:12px;flex-wrap:wrap}
.btn{font-family:var(--mono);font-size:11px;letter-spacing:.1em;padding:11px 22px;border-radius:2px;text-decoration:none;transition:all .2s;border:none;cursor:pointer}
.btn-primary{background:var(--accent);color:#07090d;font-weight:600}
.btn-primary:hover{background:var(--accent2);transform:translateY(-2px)}
.btn-ghost{background:transparent;color:var(--muted2);border:1px solid var(--border2)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent);transform:translateY(-2px)}
.status-bar{background:var(--surface);border:1px solid var(--border);border-radius:2px;padding:10px 20px;display:inline-flex;align-items:center;gap:16px;margin-bottom:32px;font-family:var(--mono);font-size:10px}
.status-item{display:flex;align-items:center;gap:6px;color:var(--muted)}
.sdot{width:5px;height:5px;border-radius:50%}
.sd-g{background:var(--green);animation:blink 2s step-end infinite}
.sd-b{background:var(--blue)}
.sd-a{background:var(--accent)}
@keyframes blink{50%{opacity:0}}
.panel{background:var(--card);border:1px solid var(--border);border-radius:4px;overflow:hidden;position:relative}
.panel::before,.panel::after{content:'';position:absolute;width:12px;height:12px;border-color:var(--accent);border-style:solid;opacity:.4}
.panel::before{top:8px;left:8px;border-width:1px 0 0 1px}
.panel::after{bottom:8px;right:8px;border-width:0 1px 1px 0}
.panel-hdr{background:var(--surface);border-bottom:1px solid var(--border);padding:10px 16px;font-family:var(--mono);font-size:10px;color:var(--muted);display:flex;align-items:center;gap:8px;letter-spacing:.08em}
.pdot{width:6px;height:6px;border-radius:50%}
.pd-r{background:#ff5b5b}.pd-y{background:var(--accent)}.pd-g{background:var(--green)}
.panel-body{padding:20px}
.pl{font-family:var(--mono);font-size:11px;line-height:2.1;color:var(--muted)}
.pk{color:var(--blue)}.pv{color:var(--green)}.pvy{color:var(--accent)}.pw{color:var(--text)}
section{padding:96px 0}
.sec-hdr{margin-bottom:52px}
.sec-label{font-family:var(--mono);font-size:10px;color:var(--blue);letter-spacing:.25em;text-transform:uppercase;margin-bottom:6px;display:flex;align-items:center;gap:10px}
.sec-label::after{content:'';flex:1;max-width:60px;height:1px;background:var(--border2)}
.sec-title{font-family:var(--cond);font-size:clamp(1.8rem,3.5vw,2.6rem);font-weight:800;letter-spacing:-.01em;color:#dce8f0;line-height:1}
.sec-title .hl{color:var(--accent)}
.skills-outer{display:grid;grid-template-columns:1fr 1fr;gap:48px}
.blk-title{font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:.15em;text-transform:uppercase;margin-bottom:18px;padding-bottom:8px;border-bottom:1px solid var(--border)}
.skill-row{margin-bottom:18px}
.skill-meta{display:flex;justify-content:space-between;margin-bottom:6px}
.skill-n{font-family:var(--mono);font-size:12px;color:var(--text)}
.skill-d{font-size:13px;color:var(--muted);margin-top:1px}
.skill-pct{font-family:var(--mono);font-size:11px;color:var(--accent)}
.skill-track{height:2px;background:var(--border2);border-radius:1px;overflow:hidden}
.skill-bar{height:100%;width:0;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1.4s cubic-bezier(.16,1,.3,1)}
.infra-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:24px}
.infra-item{background:var(--surface);border:1px solid var(--border);border-radius:3px;padding:12px 14px}
.infra-n{font-family:var(--mono);font-size:12px;color:var(--blue);margin-bottom:3px}
.infra-d{font-size:13px;color:var(--muted)}
.db-list{display:flex;flex-direction:column;gap:8px}
.db-item{display:flex;align-items:center;gap:10px;font-family:var(--mono);font-size:12px;color:var(--muted2)}
.db-item::before{content:'▸';color:var(--accent);font-size:10px;flex-shrink:0}
.projects-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.proj-card{background:var(--card);border:1px solid var(--border);border-radius:4px;padding:28px;position:relative;overflow:hidden;transition:border-color .25s,transform .25s}
.proj-card:hover{border-color:var(--accent);transform:translateY(-4px)}
.proj-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--accent),var(--blue));opacity:0;transition:opacity .25s}
.proj-card:hover::after{opacity:1}
.proj-type{font-family:var(--mono);font-size:9px;letter-spacing:.2em;color:var(--muted);text-transform:uppercase;margin-bottom:14px}
.proj-scale{display:inline-block;font-family:var(--mono);font-size:9px;padding:2px 8px;border-radius:2px;background:rgba(232,160,32,.1);color:var(--accent);border:1px solid rgba(232,160,32,.2);margin-left:10px}
.proj-name{font-family:var(--cond);font-size:1.3rem;font-weight:700;color:#dce8f0;margin-bottom:12px;line-height:1.1}
.proj-desc{font-size:15px;color:var(--muted2);line-height:1.75;margin-bottom:16px;font-family:var(--thai)}
.proj-hls{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.proj-hl{font-family:var(--mono);font-size:10px;padding:3px 10px;border-radius:2px;background:rgba(74,158,255,.07);color:var(--blue);border:1px solid rgba(74,158,255,.15)}
.proj-tech{display:flex;flex-wrap:wrap;gap:5px}
.proj-tag{font-family:var(--mono);font-size:10px;padding:2px 8px;border-radius:2px;background:var(--surface);color:var(--muted2);border:1px solid var(--border)}
.work-list{display:flex;flex-direction:column;gap:24px}
.work-item{border-left:3px solid var(--accent);padding-left:24px;padding-top:12px;padding-bottom:12px;transition:border-color .2s}
.work-item:hover{border-color:var(--accent2)}
.work-position{font-family:var(--cond);font-size:15px;font-weight:700;color:#dce8f0}
.work-company{font-family:var(--thai);font-size:14px;color:var(--muted2);margin-top:4px}
.work-date{font-family:var(--mono);font-size:10px;color:var(--blue);letter-spacing:.08em;margin-top:8px;margin-bottom:12px}
.work-responsibilities{display:flex;flex-direction:column;gap:10px}
.work-resp-item{font-size:14px;color:var(--muted2);line-height:1.7;font-family:var(--thai);padding-left:16px;position:relative}
.work-resp-item::before{content:'▸';position:absolute;left:0;color:var(--accent);font-size:10px}
.str-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.str-card{background:var(--card);border:1px solid var(--border);border-radius:4px;padding:24px 20px;text-align:center;transition:border-color .2s}
.str-card:hover{border-color:var(--accent)}
.str-icon{font-size:22px;color:var(--accent);margin-bottom:14px;display:block;font-family:var(--mono)}
.str-name{font-family:var(--cond);font-size:14px;font-weight:700;color:#dce8f0;margin-bottom:8px}
.str-desc{font-size:14px;color:var(--muted);line-height:1.6;font-family:var(--thai)}
.growth-list{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.growth-item{background:var(--card);border:1px solid var(--border);border-radius:3px;padding:16px 20px;display:flex;align-items:center;gap:14px}
.g-badge{font-family:var(--mono);font-size:9px;padding:3px 10px;border-radius:2px;letter-spacing:.1em;white-space:nowrap;flex-shrink:0}
.g-learn{background:rgba(61,214,140,.08);color:var(--green);border:1px solid rgba(61,214,140,.2)}
.g-next{background:rgba(74,158,255,.08);color:var(--blue);border:1px solid rgba(74,158,255,.2)}
.g-txt{font-family:var(--mono);font-size:12px;color:var(--text)}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.contact-left{background:var(--card);border:1px solid var(--border);border-radius:4px;padding:40px;position:relative;overflow:hidden}
.contact-left::before{content:'';position:absolute;top:-40px;right:-40px;width:160px;height:160px;border:1px solid var(--border);border-radius:50%}
.c-label{font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:.15em;margin-bottom:12px}
.c-email{font-family:var(--mono);font-size:15px;color:var(--accent);text-decoration:none;display:block;margin-bottom:28px;word-break:break-all}
.c-email:hover{text-decoration:underline}
.social-row{display:flex;gap:10px}
.social-btn{font-family:var(--mono);font-size:11px;padding:9px 18px;border-radius:2px;border:1px solid var(--border2);color:var(--muted2);text-decoration:none;letter-spacing:.08em;transition:all .2s}
.social-btn:hover{border-color:var(--accent);color:var(--accent)}
.contact-right{background:var(--card);border:1px solid var(--border);border-radius:4px;padding:28px}
.lang-row{display:flex;flex-direction:column;gap:10px;margin-bottom:24px}
.lang-item{display:flex;align-items:center;justify-content:space-between;padding:11px 16px;background:var(--surface);border:1px solid var(--border);border-radius:3px}
.lang-n{font-family:var(--mono);font-size:12px;color:var(--text)}
.lang-b{font-family:var(--mono);font-size:9px;padding:2px 8px;border-radius:2px;background:rgba(74,158,255,.08);color:var(--blue);border:1px solid rgba(74,158,255,.2)}
.obj-box{background:var(--surface);border:1px solid var(--border);border-left:2px solid var(--accent);border-radius:3px;padding:16px;font-size:15px;color:var(--muted2);line-height:1.8;font-family:var(--thai)}
footer{border-top:1px solid var(--border);padding:24px 0}
.foot-inner{max-width:1100px;margin:0 auto;padding:0 32px;display:flex;justify-content:space-between;align-items:center}
.foot-copy{font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:.08em}
.foot-copy span{color:var(--accent)}
.foot-r{font-family:var(--mono);font-size:10px;color:var(--muted)}
hr.div{border:none;border-top:1px solid var(--border)}
.fi{opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s ease}
.fi.vis{opacity:1;transform:translateY(0)}
.d1{transition-delay:.1s}.d2{transition-delay:.2s}.d3{transition-delay:.3s}
@media(max-width:768px){
  .hero-inner{grid-template-columns:1fr}
  .panel{display:none}
  .skills-outer,.projects-grid,.contact-grid,.growth-list{grid-template-columns:1fr}
  .str-grid{grid-template-columns:1fr 1fr}
  .infra-grid{grid-template-columns:1fr}
  .nav-links{display:none}
}
</style>
</head>
<body>
<nav>
  <div class="nav-inner">
    <div class="nav-logo">
      <span class="nav-bracket">[</span>{{ p.name.upper() }}<span class="nav-bracket">]</span>
      <span class="nav-id">CE / DEV</span>
    </div>
    <div class="nav-links">
      <a href="#skills">skills</a>
      <a href="#projects">projects</a>
      <a href="#strengths">strengths</a>
      <a href="#growth">growth</a>
      <a href="#contact">contact</a>
    </div>
  </div>
</nav>

<section class="hero">
  <div class="wrap">
    <div class="hero-inner">
      <div>
        <div class="status-bar">
          <div class="status-item"><span class="sdot sd-g"></span>OPEN TO WORK</div>
          <div class="status-item"><span class="sdot sd-b"></span>CE STUDENT</div>
          <div class="status-item"><span class="sdot sd-a"></span>BACKEND / INFRA</div>
        </div>
        <div class="hero-eyebrow">COMPUTER ENGINEERING STUDENT</div>
        <div class="hero-name">{{ p.name.upper() }}</div>
        <div class="hero-name-th">{{ p.name_th }}</div>
        <div class="hero-role">{{ p.role }}</div>
        <div class="hero-level">// {{ p.level }}</div>
        <p class="hero-desc">{{ p.objective }}</p>
        <div class="hero-btns">
          <a href="#projects" class="btn btn-primary">VIEW PROJECTS</a>
          <a href="#contact"  class="btn btn-ghost">CONTACT</a>
        </div>
      </div>
      <div class="panel">
        <div class="panel-hdr">
          <span class="pdot pd-r"></span><span class="pdot pd-y"></span><span class="pdot pd-g"></span>
          profile.json
        </div>
        <div class="panel-body">
          <div class="pl"><span style="color:var(--muted)">{</span></div>
          <div class="pl">&nbsp;&nbsp;<span class="pk">"name"</span>: <span class="pv">"{{ p.name }}"</span>,</div>
          <div class="pl">&nbsp;&nbsp;<span class="pk">"role"</span>: <span class="pv">"CE Student"</span>,</div>
          <div class="pl">&nbsp;&nbsp;<span class="pk">"level"</span>: <span class="pvy">"Junior"</span>,</div>
          <div class="pl">&nbsp;&nbsp;<span class="pk">"focus"</span>: [</div>
          <div class="pl">&nbsp;&nbsp;&nbsp;&nbsp;<span class="pv">"Backend"</span>,</div>
          <div class="pl">&nbsp;&nbsp;&nbsp;&nbsp;<span class="pv">"Cloud"</span>,</div>
          <div class="pl">&nbsp;&nbsp;&nbsp;&nbsp;<span class="pv">"Automation"</span></div>
          <div class="pl">&nbsp;&nbsp;],</div>
          <div class="pl">&nbsp;&nbsp;<span class="pk">"scale"</span>: <span class="pvy">"Enterprise"</span>,</div>
          <div class="pl">&nbsp;&nbsp;<span class="pk">"servers"</span>: <span class="pvy">16000</span>,</div>
          <div class="pl">&nbsp;&nbsp;<span class="pk">"lang"</span>: [<span class="pv">"C#"</span>, <span class="pv">"Python"</span>, <span class="pv">"SQL"</span>]</div>
          <div class="pl"><span style="color:var(--muted)">}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="div"/>

<section id="skills">
  <div class="wrap">
    <div class="sec-hdr fi">
      <div class="sec-label">01 / skills</div>
      <div class="sec-title">Technical <span class="hl">Stack</span></div>
    </div>
    <div class="skills-outer">
      <div class="fi d1">
        <div class="blk-title">PROGRAMMING LANGUAGES</div>
        {% for s in p.skills_lang %}
        <div class="skill-row">
          <div class="skill-meta">
            <div><div class="skill-n">{{ s.name }}</div><div class="skill-d">{{ s.desc }}</div></div>
            <div class="skill-pct">{{ s.level }}%</div>
          </div>
          <div class="skill-track"><div class="skill-bar" data-level="{{ s.level }}"></div></div>
        </div>
        {% endfor %}
      </div>
      <div>
        <div class="fi d1">
          <div class="blk-title">FRAMEWORK & INFRASTRUCTURE</div>
          <div class="infra-grid">
            {% for s in p.skills_infra %}
            <div class="infra-item"><div class="infra-n">{{ s.name }}</div><div class="infra-d">{{ s.desc }}</div></div>
            {% endfor %}
          </div>
        </div>
        <div class="fi d2">
          <div class="blk-title">DATABASE SKILLS</div>
          <div class="db-list">
            {% for d in p.db_skills %}
            <div class="db-item">{{ d }}</div>
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="div"/>

<section id="experience">
  <div class="wrap">
    <div class="sec-hdr fi">
      <div class="sec-label">02 / experience</div>
      <div class="sec-title">Work <span class="hl">Experience</span></div>
    </div>
    <div class="work-list">
      {% for exp in p.work_experience %}
      <div class="work-item fi d1">
        <div class="work-position">{{ exp.position }}</div>
        <div class="work-company">{{ exp.unit }} | {{ exp.company }}</div>
        <div class="work-date">{{ exp.date_from }} - {{ exp.date_to }}</div>
        <div class="work-responsibilities">
          {% for resp in exp.responsibilities %}
          <div class="work-resp-item">{{ resp }}</div>
          {% endfor %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<hr class="div"/>

<section id="projects">
  <div class="wrap">
    <div class="sec-hdr fi">
      <div class="sec-label">03 / projects</div>
      <div class="sec-title">System <span class="hl">Experience</span></div>
    </div>
    <div class="projects-grid">
      {% for proj in p.projects %}
      <div class="proj-card fi d{{ loop.index0 % 2 + 1 }}">
        <div class="proj-type">{{ proj.type.upper() }}<span class="proj-scale">{{ proj.scale }}</span></div>
        <div class="proj-name">{{ proj.name }}</div>
        <div class="proj-desc">{{ proj.desc }}</div>
        <div class="proj-hls">{% for h in proj.highlights %}<span class="proj-hl">{{ h }}</span>{% endfor %}</div>
        <div class="proj-tech">{% for t in proj.tech %}<span class="proj-tag">{{ t }}</span>{% endfor %}</div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<hr class="div"/>

<section id="strengths">
  <div class="wrap">
    <div class="sec-hdr fi">
      <div class="sec-label">04 / strengths</div>
      <div class="sec-title">Core <span class="hl">Strengths</span></div>
    </div>
    <div class="str-grid">
      {% for s in p.strengths %}
      <div class="str-card fi d{{ loop.index0 % 3 + 1 }}">
        <span class="str-icon">{{ s.icon }}</span>
        <div class="str-name">{{ s.name }}</div>
        <div class="str-desc">{{ s.desc }}</div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<hr class="div"/>

<section id="growth">
  <div class="wrap">
    <div class="sec-hdr fi">
      <div class="sec-label">05 / growth</div>
      <div class="sec-title">Learning <span class="hl">Direction</span></div>
    </div>
    <div class="growth-list">
      {% for g in p.growth %}
      <div class="growth-item fi d{{ loop.index0 % 2 + 1 }}">
        <span class="g-badge {{ 'g-learn' if g.status == 'learning' else 'g-next' }}">
          {{ 'LEARNING' if g.status == 'learning' else 'NEXT UP' }}
        </span>
        <span class="g-txt">{{ g.item }}</span>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<hr class="div"/>

<section id="contact">
  <div class="wrap">
    <div class="sec-hdr fi">
      <div class="sec-label">05 / contact</div>
      <div class="sec-title">Get In <span class="hl">Touch</span></div>
    </div>
    <div class="contact-grid">
      <div class="contact-left fi d1">
        <div class="c-label">EMAIL</div>
        <a href="mailto:{{ p.email }}" class="c-email">{{ p.email }}</a>
        <div class="social-row">
          <a href="{{ p.github }}"   class="social-btn" target="_blank">GITHUB</a>
          <a href="{{ p.linkedin }}" class="social-btn" target="_blank">LINKEDIN</a>
        </div>
      </div>
      <div class="contact-right fi d2">
        <div class="blk-title" style="margin-bottom:16px">LANGUAGES</div>
        <div class="lang-row">
          {% for l in p.languages_spoken %}
          <div class="lang-item">
            <span class="lang-n">{{ l.lang }}</span>
            <span class="lang-b">{{ l.level }}</span>
          </div>
          {% endfor %}
        </div>
        <div class="blk-title" style="margin-bottom:12px">OBJECTIVE</div>
        <div class="obj-box">{{ p.tagline }}</div>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <div class="foot-copy">&copy; 2025 <span>{{ p.name.upper() }}</span> — All rights reserved.</div>
    <div class="foot-r">Built with Flask + Python</div>
  </div>
</footer>

<script>
const obs = new IntersectionObserver(e => {
  e.forEach(x => { if(x.isIntersecting) x.target.classList.add('vis'); });
}, {threshold: 0.1});
document.querySelectorAll('.fi').forEach(el => obs.observe(el));

const barObs = new IntersectionObserver(e => {
  e.forEach(x => {
    if(x.isIntersecting)
      x.target.querySelectorAll('.skill-bar').forEach(b => {
        setTimeout(() => { b.style.width = b.dataset.level + '%'; }, 200);
      });
  });
}, {threshold: 0.3});
const sl = document.querySelector('.skills-outer');
if(sl) barObs.observe(sl);
</script>
</body>
</html>"""

@app.route("/")
def index():
    return render_template_string(HTML, p=portfolio)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
    app.run(debug=True)
