#!/usr/bin/env python3
import pathlib, re
HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path("/home/user/sampadahita")
STYLE = (HERE/"style.css").read_text()
FONTS = (HERE/"fontface.css").read_text()

MARK = '''<svg class="mark" viewBox="0 0 48 48" fill="none" aria-hidden="true">
  <rect x="1.5" y="1.5" width="45" height="45" rx="11" fill="var(--navy-800)"/>
  <rect x="1.5" y="1.5" width="45" height="45" rx="11" stroke="var(--gold-500)" stroke-width="1.4"/>
  <path d="M16 34V14M32 34V14M16 24h16" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
  <path d="M24 8.5l3.6 3.6L24 15.7l-3.6-3.6L24 8.5Z" fill="var(--gold-400)"/>
  <path d="M24 32.3l3.6 3.6L24 39.5l-3.6-3.6 3.6-3.6Z" fill="var(--gold-400)"/>
</svg>'''

NAVITEMS = [
    ("home","index.html","Home"),
    ("about","about.html","About"),
    ("services","services.html","Services"),
    ("tax","tax-strategies.html","Tax Strategies"),
    ("serve","who-we-serve.html","Who We Serve"),
    ("partnership","partnership.html","Partnership"),
    ("resources","resources.html","Resources"),
    ("contact","contact.html","Contact"),
]

def nav(active):
    def link(key,href,label):
        cls = ' class="active"' if key==active else ''
        return f'      <a href="{href}"{cls}>{label}</a>'
    links = "\n".join(link(*it) for it in NAVITEMS)
    mlinks = "\n".join(
        f'    <a href="{href}" data-close>{label}</a>' for key,href,label in NAVITEMS)
    return f'''<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="index.html" aria-label="SampadaHita home">
      {MARK}
      <span class="lockup"><span class="name">Sampada<b>Hita</b></span><span class="tag">Well-Wisher of Your Wealth</span></span>
    </a>
    <nav class="nav-links" aria-label="Primary">
{links}
    </nav>
    <div class="nav-cta"><a class="btn btn-gold" href="contact.html">Schedule a Meeting</a></div>
    <button class="hamburger" id="menuOpen" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
  </div>
</header>
<div class="mobile" id="mobile" aria-hidden="true">
  <div class="mobile-top">
    <span class="brand"><span class="lockup"><span class="name">Sampada<b>Hita</b></span></span></span>
    <button class="mobile-close" id="menuClose" aria-label="Close menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
  </div>
  <nav aria-label="Mobile">
{mlinks}
  </nav>
  <div class="m-actions"><a class="btn btn-gold btn-lg" href="contact.html" data-close>Schedule a Meeting</a></div>
</div>'''

FOOTER = '''<footer class="footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <span class="brand"><span class="lockup"><span class="name">Sampada<b>Hita</b></span><span class="tag">Well-Wisher of Your Wealth</span></span></span>
        <p class="foot-about">Empowering families and individuals to navigate financial complexity — and shape a future of security and prosperity.</p>
        <div class="foot-social">
          <a href="https://www.linkedin.com/company/sampadahita" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3zM10 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21H18.6v-5.4c0-1.29-.02-2.95-1.8-2.95-1.8 0-2.08 1.4-2.08 2.85V21H10z"/></svg></a>
          <a href="mailto:info@sampadahita.com" aria-label="Email"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></a>
        </div>
      </div>
      <div class="foot-col">
        <h4>Company</h4>
        <a href="about.html">About Us</a>
        <a href="services.html">Services</a>
        <a href="who-we-serve.html">Who We Serve</a>
        <a href="partnership.html">Partnership</a>
      </div>
      <div class="foot-col">
        <h4>Explore</h4>
        <a href="tax-strategies.html">Tax Strategies</a>
        <a href="resources.html">Resources</a>
        <a href="contact.html">Book a Call</a>
        <a href="contact.html">Free Webinar</a>
      </div>
      <div class="foot-col foot-contact">
        <h4>Contact</h4>
        <p>Email: <b>info@sampadahita.com</b></p>
        <p>Free webinar every Sunday · 7:00 PM CST</p>
        <form class="news" id="newsForm" style="margin-top:14px">
          <input type="email" placeholder="Email address" aria-label="Email address" required>
          <button class="btn btn-gold" type="submit">Subscribe</button>
        </form>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© <span id="year">2026</span> SampadaHita. All rights reserved.</span>
      <span>Powered by Galaxy Educations Online Training Platform — a venture of SNS System.</span>
    </div>
  </div>
</footer>'''

SCRIPT = '''<script>
(function(){"use strict";var d=document;
var y=d.getElementById('year');if(y)y.textContent=new Date().getFullYear();
var nav=d.getElementById('nav');function os(){if(nav)nav.classList.toggle('scrolled',window.scrollY>8);}os();window.addEventListener('scroll',os,{passive:true});
var mob=d.getElementById('mobile'),ob=d.getElementById('menuOpen'),cb=d.getElementById('menuClose');
function sm(o){if(!mob)return;mob.classList.toggle('open',o);mob.setAttribute('aria-hidden',String(!o));if(ob)ob.setAttribute('aria-expanded',String(o));d.body.style.overflow=o?'hidden':'';}
if(ob)ob.addEventListener('click',function(){sm(true);});if(cb)cb.addEventListener('click',function(){sm(false);});
d.querySelectorAll('[data-close]').forEach(function(a){a.addEventListener('click',function(){sm(false);});});
d.addEventListener('keydown',function(e){if(e.key==='Escape')sm(false);});
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var items=d.querySelectorAll('.reveal');
if(reduce||!('IntersectionObserver' in window)){items.forEach(function(el){el.classList.add('in');});}
else{var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{threshold:.12,rootMargin:'0px 0px -6% 0px'});items.forEach(function(el){io.observe(el);});}
var cv=d.getElementById('stars');
if(cv&&!reduce){var ctx=cv.getContext('2d'),stars=[],W,H,DPR=Math.min(window.devicePixelRatio||1,2);
function sz(){var r=cv.getBoundingClientRect();W=cv.width=r.width*DPR;H=cv.height=r.height*DPR;mk();}
function mk(){stars=[];var n=Math.round((W*H)/(14000*DPR));for(var i=0;i<n;i++){stars.push({x:Math.random()*W,y:Math.random()*H,r:(Math.random()*1.3+.2)*DPR,a:Math.random(),s:Math.random()*.015+.004,g:Math.random()<.15});}}
function dr(){ctx.clearRect(0,0,W,H);for(var i=0;i<stars.length;i++){var s=stars[i];s.a+=s.s;var o=.35+Math.abs(Math.sin(s.a))*.55;ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,6.283);ctx.fillStyle='rgba('+(s.g?'231,196,119':'255,255,255')+','+o+')';ctx.fill();}requestAnimationFrame(dr);}
sz();dr();var t;window.addEventListener('resize',function(){clearTimeout(t);t=setTimeout(sz,180);},{passive:true});}
function ok(f){var a=f.querySelector('#formFields'),b=f.querySelector('#formOk');if(a)a.style.display='none';if(b)b.classList.add('show');}
d.querySelectorAll('form[data-cb]').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var bad=false,first=null;f.querySelectorAll('[required]').forEach(function(x){if(!x.value.trim()){x.style.borderColor='#c0492f';bad=true;if(!first)first=x;}else{x.style.borderColor='';}});if(bad){if(first)first.focus();return;}ok(f);});});
var nf=d.getElementById('newsForm');if(nf)nf.addEventListener('submit',function(e){e.preventDefault();var i=nf.querySelector('input');if(i&&i.value.trim()){i.value='';i.placeholder='Subscribed \\u2713';}});
// scheduler
var cal=d.getElementById('cal');
if(cal){var times=d.getElementById('times');
 cal.addEventListener('click',function(e){var b=e.target.closest('button');if(!b||b.disabled)return;cal.querySelectorAll('button').forEach(function(x){x.classList.remove('sel');});b.classList.add('sel');});
 if(times)times.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;times.querySelectorAll('button').forEach(function(x){x.classList.remove('sel');});b.classList.add('sel');});}
})();
</script>'''

def page(active, title, desc, body, hero_theme="#0c2417"):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="{hero_theme}">
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<title>{title}</title>
<style>
{FONTS}
{STYLE}
</style>
</head>
<body>
{nav(active)}
{body}
{FOOTER}
{SCRIPT}
</body>
</html>
'''

PAGES = [
    ("home","index.html","SampadaHita — Well-Wisher of Your Wealth","Education-first wealth management for families and high earners: free financial analysis, advanced tax strategy, retirement, investment and legacy planning."),
    ("about","about.html","About — SampadaHita","Meet Nithya Ananda and the SampadaHita team. Our mission: demystify personal finance and help families protect and grow their wealth."),
    ("services","services.html","Services — SampadaHita","Our four-pillar approach: Plan, Protect, Preserve, and Prosper. Comprehensive financial solutions for every stage of life."),
    ("tax","tax-strategies.html","Tax Strategies — SampadaHita","Keep more of what you earn. Advanced, legal tax strategies for families and high-income professionals, plus our book From Paycheck to Prosperity."),
    ("serve","who-we-serve.html","Who We Serve — SampadaHita","Tailored strategies for families, high-income professionals, pre-retirees and retirees, and aspiring finance professionals."),
    ("partnership","partnership.html","Partnership — SampadaHita","Build a rewarding career as a financial strategist with SampadaHita — training, mentorship, and true ownership from day one."),
    ("resources","resources.html","Resources — SampadaHita","Free guides, downloads, and answers to common questions about tax planning, retirement, and wealth management."),
    ("contact","contact.html","Contact — SampadaHita","Book a free, no-obligation strategy session with SampadaHita. We educate, you decide."),
]

for key,out,title,desc in PAGES:
    body = (HERE/"pages"/f"{key}.html").read_text()
    (OUT/out).write_text(page(key,title,desc,body))
    print("built", out, (OUT/out).stat().st_size)
print("done")
