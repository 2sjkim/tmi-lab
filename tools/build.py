import pathlib,json,html
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'
D=json.loads((OUT/'content.json').read_text(encoding='utf-8'))
E=html.escape
NAV=[('Home','index.html'),('Research','research.html'),('People','people.html'),('Publications','journal.html'),('Patents','patents.html'),('Join Us','join.html')]
def page(filename,title,content,active,sub='',source=None):
    nav=''.join(f'<a href="{url}"'+(' aria-current="page"' if name==active else '')+f'>{name}</a>' for name,url in NAV)
    head='' if filename=='index.html' else f'<div class="page-heading"><h1>{title}</h1><p>{sub}</p></div>'
    output=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} | TMI Lab · Yonsei University</title><meta name="description" content="Translational Medical Intelligence Lab at Yonsei University. Medical imaging, trustworthy AI, computational imaging, and clinical translation."><meta name="theme-color" content="#0b2e76"><link rel="icon" type="image/svg+xml" href="favicon.svg"><link rel="stylesheet" href="style.css"><script src="site.js" defer></script></head><body><a class="skip" href="#main">Skip to main content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html" aria-label="TMI Lab home"><img src="assets/tmi-logo.png" alt="TMI"><span>Yonsei University</span></a><button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="navigation" aria-expanded="false">☰</button><nav id="navigation" class="nav" aria-label="Main navigation">{nav}</nav></div></header><main id="main" class="wrap">{head}{content}</main><footer class="site-footer"><div class="wrap"><div class="footer-grid"><div><h3>TMI Lab</h3><p>Translational Medical Intelligence Laboratory<br>Department of Artificial Intelligence · Yonsei University</p><a href="mailto:jongdukbaek@yonsei.ac.kr">jongdukbaek@yonsei.ac.kr</a></div><div class="footer-links"><a href="people.html">People</a><a href="journal.html">Publications</a><a href="join.html">Join Us</a></div></div><p class="copyright">© 2026 TMI Lab, Yonsei University.</p></div></footer></body></html>'''
    (OUT/filename).write_text(output,encoding='utf-8')
def tabs(items,current):return '<nav class="subnav" aria-label="Section navigation">'+''.join(f'<a href="{f}"'+(' aria-current="page"' if f==current else '')+f'>{name}</a>' for name,f in items)+'</nav>'
PEOPLE=[('Principal Investigator','people.html'),('Researchers','researchers.html'),('Alumni','alumni.html')]
PUBS=[('Journal','journal.html'),('Conference','conference.html')]
areas=[('Real-world imaging systems','We study medical images as outputs of physical acquisition systems.',['Imaging physics & geometry','Scanners, protocols & dose','Artifacts & acquisition variability','Real patient data']),('Clinical intelligence under image quality variation','We develop restoration and diagnostic AI that is robust in the real world.',['Artifact reduction & restoration','Image quality assessment','Uncertainty modeling','Downstream task performance']),('Evidence-driven translation','We bridge AI development and real clinical impact.',['Foundation data infrastructure','Task-based & reader-aligned evaluation','Clinical workflow integration','MVP, IP, and startup-driven translation'])]
def area_grid(images=False):
    out='<div class="approach">'
    for n,(title,desc,points) in enumerate(areas):
        image=f'<img class="research-visual" src="{D["images"]["home"][n]}" alt="{E(title)}" loading="lazy">' if images else ''
        out+=f'<article>{image}<span class="number">0{n+1}</span><h3>{title}</h3><p>{desc}</p><ul class="bullets">'+''.join(f'<li>{E(p)}</li>' for p in points)+'</ul></article>'
    return out+'</div>'
def publication(p):
    links=' '.join(f'<a href="{E(a["url"],quote=True)}">{E(a["text"])}</a>' for a in p['links'])
    return f'<article class="publication"><h3>{E(p["title"])}</h3><p>{E(p["authors"])}</p><p class="venue">{E(p["venue"])}</p>'+ (f'<p class="paper-links">{links}</p>' if links else '')+'</article>'
home='''<section class="hero"><p class="university">YONSEI</p><h1>Translational Medical <em>Intelligence</em> Lab</h1><p class="subtitle">From medical imaging AI to Translational Medical Intelligence.</p></section><section class="intro"><div class="intro-copy"><p>We develop <strong>trustworthy AI</strong> that advances real-world medical imaging systems, clinical workflows, and translational medical technologies.</p><p><strong>TMI Lab</strong> connects real-world imaging, reliable AI, and clinical translation to create meaningful impact in healthcare.</p><div class="statement">From imaging systems to clinical impact.</div></div><div class="lab-mark"><img src="assets/tmi-logo.png" alt="TMI — Translational Medical Imaging" width="1262" height="506"></div></section>'''
home+='<section class="section"><div class="section-heading"><h2>Our Approach</h2><a href="research.html">Explore our research</a></div>'+area_grid()+'</section>'
home+='<section class="section"><div class="section-heading"><h2>Recent Publications</h2><a href="journal.html">All publications</a></div>'+''.join(publication(p) for p in D['journal'][:3])+'</section>'
home+='''<section class="section contact"><div><h2>Contact</h2><h3>Translational Medical Intelligence Lab</h3><p>Department of Artificial Intelligence<br>Yonsei University</p><a href="mailto:jongdukbaek@yonsei.ac.kr">jongdukbaek@yonsei.ac.kr</a></div><div><h2>Join TMI</h2><p>Build the future of medical imaging with us.<br>We value strong fundamentals, curiosity, and a collaborative attitude.</p><a class="button" href="join.html">Join our research</a></div></section>'''
page('index.html','Home',home,'Home')
page('research.html','Research','<section class="section"><p class="eyebrow">Our approach</p><h2>From imaging systems to clinical impact.</h2><p>TMI Lab connects real-world imaging, reliable AI, and clinical translation to create meaningful impact in healthcare.</p>'+area_grid(True)+'</section>','Research',sub='Advancing medical imaging through AI, physics, and clinical translation.')
bio=D['professor']['bio']
affiliations=D['professor']['affiliations']
profile=tabs(PEOPLE,'people.html')+f'''<section class="profile"><img src="{D['images']['professor'][0]}" alt="Jongduk Baek"><div><p class="eyebrow">Principal Investigator</p><h2>Jongduk Baek, Ph.D.</h2><p class="role">Professor &amp; Chair</p><p>Department of Artificial Intelligence<br>Yonsei University</p><p>{E(bio)}</p><a href="mailto:jongdukbaek@yonsei.ac.kr">jongdukbaek@yonsei.ac.kr</a></div></section><section class="section"><h2>Selected Affiliations</h2><ul class="affiliations">'''+''.join(f'<li>{E(a)}</li>' for a in affiliations)+'</ul></section>'
profile+='<section class="section values">'+''.join(f'<div><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a,b in [('Our Mission','Advance trustworthy AI that improves patient care.'),('Our Approach','From real-world imaging systems to clinical impact.'),('Our Commitment','Rigor, transparency, and responsible innovation.'),('Our Vision','Translational medical intelligence for a healthier world.')])+'</section>'
page('people.html','Principal Investigator',profile,'People',sub='Leading innovation in medical imaging, AI, and clinical translation.')
def person(p):
    photo=f'<img src="{p["image"]}" alt="{E(p["name"])}" loading="lazy">' if p['image'] else '<div class="portrait-fallback" aria-hidden="true">'+''.join(w[0] for w in p['name'].split())+'</div>'
    parts=''.join(f'<p class="'+('role' if n==0 else '')+'">'+(f'<a href="mailto:{E(t)}">{E(t)}</a>' if '@' in t else E(t))+'</p>' for n,t in enumerate(p['details']))
    return f'<article class="person">{photo}<div><h3>{E(p["name"])}</h3>{parts}</div></article>'
for key,title,desc in [('researchers','Researchers','Researchers advancing medical imaging through artificial intelligence, reconstruction, and computational imaging.'),('alumni','Alumni','Advancing medical imaging and AI beyond TMI.')]:
    members=[p for p in D[key] if p['details'][0]!='Staff'];staff=[p for p in D[key] if p['details'][0]=='Staff']
    content=tabs(PEOPLE,key+'.html')+'<div class="people-grid">'+''.join(person(p) for p in members)+'</div>'
    if staff:content+='<h2>Staff</h2><div class="people-grid">'+''.join(person(p) for p in staff)+'</div>'
    page(key+'.html',title,content,'People',sub=desc)
for key,title,desc in [('journal','Journal','Research outputs supporting TMI’s translational medical intelligence pipeline.'),('conference','Conference','Selected conference papers and presentations from TMI.')]:
    years=list(dict.fromkeys(p['year'] for p in D[key]))
    content=tabs(PUBS,key+'.html')+'<div class="pub-layout"><nav class="year-nav" aria-label="Publication years">'+''.join(f'<a href="#year-{y.replace(" ","-")}">{y}</a>' for y in years)+'</nav><div>'
    for year in years:content+=f'<section class="year-group" id="year-{year.replace(" ","-")}"><h2>{year}</h2>'+''.join(publication(p) for p in D[key] if p['year']==year)+'</section>'
    page(key+'.html',title,content+'</div></div>','Publications',sub=desc)
page('patents.html','Patents','<section>'+''.join(publication(p) for p in D['patents'])+'</section>','Patents',sub='Innovations and intellectual property developed at TMI.')
join='''<p class="join-intro">We work at the intersection of artificial intelligence, imaging physics, and clinical translation.</p><section class="section"><p class="eyebrow">Research with us</p><h2>Work on problems that connect imaging physics,<br>artificial intelligence, and medicine.</h2><div class="approach">'''
for n,(title,points) in enumerate([('Physical AI for Imaging',['X-ray imaging systems','Imaging physics & acquisition','Dose efficiency & system modeling']),('Computational Imaging',['CT reconstruction','Inverse problems & optimization','Artifact reduction & image quality']),('Medical Intelligence',['Diagnostic AI & decision support','Foundation models for imaging','Synthetic data & clinical validation'])]):join+=f'<article><span class="number">0{n+1}</span><h3>{title}</h3><ul class="bullets">'+''.join(f'<li>{E(p)}</li>' for p in points)+'</ul></article>'
join+='</div></section><section class="section"><p class="eyebrow">Who we’re looking for</p><h2>You may be a good fit if you are interested in…</h2><div class="interests">'+''.join(f'<span>{x}</span>' for x in ['Deep Learning','Computer Vision','Signal Processing','Inverse Problems','Probability & Statistics','Software Engineering','Medical Imaging'])+'</div><p>We value strong fundamentals, curiosity, and a collaborative attitude.</p><div class="join-contact"><h2>Join TMI and work on the next generation<br>of intelligent medical imaging.</h2><p>Please contact <a href="mailto:jongdukbaek@yonsei.ac.kr">jongdukbaek@yonsei.ac.kr</a>.</p></div></section>'
page('join.html','Join TMI',join,'Join Us',sub='Build the future of medical imaging with us.')
(OUT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="8" fill="#0b2e76"/><text x="24" y="31" text-anchor="middle" font-family="Arial,sans-serif" font-weight="bold" font-size="21" fill="white">TMI</text></svg>',encoding='utf-8')
(OUT/'.nojekyll').touch()
print('Built 9 static pages.')
