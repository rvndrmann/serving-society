#!/usr/bin/env python3
"""Generate all 9 service pages from template + data"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

NAV = '''  <nav class="navbar scrolled" id="navbar">
    <div class="nav-container">
      <a href="/index.html" class="nav-logo"><img src="/Logo Serving Society.png" alt="Serving Society Logo" class="logo-img" /></a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/index.html" class="nav-link">Home</a></li>
        <li><a href="/about.html" class="nav-link">About Us</a></li>
        <li class="nav-dropdown">
          <a href="#" class="nav-link nav-link-dropdown active">Services <svg width="10" height="6" viewBox="0 0 10 6"><path d="M1 1l4 4 4-4" stroke="currentColor" fill="none" stroke-width="1.5"/></svg></a>
          <ul class="dropdown-menu">
            <li><a href="/services/accommodation-tenancy.html">Accommodation / Tenancy</a></li>
            <li><a href="/services/life-stage-transition.html">Assist Life Stage, Transition</a></li>
            <li><a href="/services/daily-tasks-shared-living.html">Daily Tasks / Shared Living</a></li>
            <li><a href="/services/development-life-skills.html">Development Life Skills</a></li>
            <li><a href="/services/community-participation.html">Community Participation</a></li>
            <li><a href="/services/assist-personal-activities.html">Assist Personal Activities</a></li>
            <li><a href="/services/assist-travel-transport.html">Assist Travel / Transport</a></li>
            <li><a href="/services/innovative-community-participation.html">Innovative Community Participation</a></li>
            <li><a href="/services/household-tasks.html">Household Tasks</a></li>
          </ul>
        </li>
        <li><a href="/appointment.html" class="nav-link">Appointment</a></li>
        <li><a href="/index.html#contact" class="nav-link nav-cta">Get in Touch</a></li>
      </ul>
    </div>
  </nav>'''

SIDEBAR_SERVICES = [
    ("Accommodation / Tenancy", "/services/accommodation-tenancy.html"),
    ("Assist Life Stage, Transition", "/services/life-stage-transition.html"),
    ("Daily Tasks / Shared Living", "/services/daily-tasks-shared-living.html"),
    ("Development Life Skills", "/services/development-life-skills.html"),
    ("Community Participation", "/services/community-participation.html"),
    ("Assist Personal Activities", "/services/assist-personal-activities.html"),
    ("Assist Travel / Transport", "/services/assist-travel-transport.html"),
    ("Innovative Community Participation", "/services/innovative-community-participation.html"),
    ("Household Tasks", "/services/household-tasks.html"),
]

BOTTOM = '''
  <!-- How To Book -->
  <section class="how-to-book">
    <div class="container">
      <div class="section-header"><span class="section-tag">How To Book Our Services?</span><h2 class="section-title">Easy Ways To Get Serving Society Support</h2></div>
      <div class="book-steps">
        <div class="book-step reveal"><div class="book-step-number">01</div><h4>Call Us Directly</h4><p>Have questions or need support straight away? Our friendly team is just a call away. We're ready to chat about your needs and guide you through the next steps.</p><a href="tel:+61400000000" class="btn btn-primary">Call Now</a></div>
        <div class="book-step reveal"><div class="book-step-number">02</div><h4>Email Us Anytime</h4><p>Prefer to reach out in writing? Send us an email with your details, and one of our care coordinators will be in touch to assist and communicate with you.</p><a href="mailto:info@servingsociety.com.au" class="btn btn-primary">Send an Email</a></div>
        <div class="book-step reveal"><div class="book-step-number">03</div><h4>Fill Out Our Contact Form</h4><p>Quick and convenient — just fill out our contact form on the website and we'll get back to you shortly to discuss how we can support you.</p><a href="/index.html#contact" class="btn btn-primary">Submit Contact Form</a></div>
      </div>
    </div>
  </section>

  <!-- Why Choose Us -->
  <section class="why-choose-us">
    <div class="container">
      <div class="section-header"><h2 class="section-title">Trusted NDIS Care Across Australia</h2><p class="section-subtitle">At Serving Society, we treat every participant like a valued member of our own family. Our personalised NDIS services are delivered with kindness, reliability, and a genuine commitment to your goals.</p></div>
      <div class="why-cards">
        <div class="why-card reveal"><div class="why-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div><h4>Compassionate, Qualified Team</h4><p>Our team is not only highly trained but genuinely passionate about making a positive impact. We treat every participant with the dignity, care, and respect they deserve.</p></div>
        <div class="why-card reveal"><div class="why-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h4>Culturally Respectful &amp; Inclusive</h4><p>We embrace diversity and provide inclusive support that respects your cultural values, language, and background — making sure you always feel seen and heard.</p></div>
        <div class="why-card reveal"><div class="why-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div><h4>Person-Centred Approach</h4><p>Every plan we create starts with you. We tailor our services to your individual goals, preferences, and lifestyle — because your journey is unique.</p></div>
        <div class="why-card reveal"><div class="why-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="5" r="3"/><circle cx="4" cy="19" r="3"/><circle cx="20" cy="19" r="3"/><path d="M12 8v4m0 0l-4 4m4-4l4 4"/></svg></div><h4>Local Knowledge, Community Connection</h4><p>With strong roots in Australian communities, we understand local needs and resources. Our support extends beyond the home and into the heart of the community.</p></div>
        <div class="why-card reveal"><div class="why-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><polyline points="9 10 12 13 16 9"/></svg></div><h4>Clear Communication &amp; Transparency</h4><p>We value open, honest communication and keep you informed every step of the way. No surprises — just respectful, transparent care.</p></div>
        <div class="why-card reveal"><div class="why-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 12 15 16 10"/></svg></div><h4>Reliability You Can Count On</h4><p>We show up, follow through, and deliver consistent support. Families trust us because we're dependable, professional, and committed to getting things right.</p></div>
      </div>
    </div>
  </section>

  <!-- Testimonials -->
  <section class="testimonial-section">
    <div class="container">
      <div class="testimonial-grid">
        <div class="testimonial-left reveal"><span class="section-tag" style="background:rgba(255,255,255,.15);color:var(--white);">Testimonial</span><h2>What Our Participants <span>Say</span> About Us?</h2><p>Every testimonial is a reflection of the care, trust, and personalised support we provide.</p></div>
        <div class="reveal">
          <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><blockquote>"Serving Society has been a true blessing for our family. Their team is kind, responsive, and truly committed to my son's wellbeing. We feel supported every single day."</blockquote><div class="testimonial-author">Sarah L.</div><div class="testimonial-role">Parent of NDIS Participant</div></div>
          <div class="testimonial-card" style="display:none;"><div class="testimonial-stars">★★★★★</div><blockquote>"From day one, I felt like I was more than just a client — I was part of a family. The support workers are amazing, respectful, and always go the extra mile."</blockquote><div class="testimonial-author">James T.</div><div class="testimonial-role">Participant</div></div>
          <div class="testimonial-dots"><div class="testimonial-dot active"></div><div class="testimonial-dot"></div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Acknowledgement -->
  <section class="acknowledgement">
    <div class="container">
      <h2>Acknowledgement Of Country</h2>
      <p>We would like to acknowledge the traditional custodians of this land and pay our respects to the Elders both past, present and future for they hold the memories, the traditions, the culture and hope of their people.</p>
      <div class="flags">
        <svg viewBox="0 0 80 40" width="80" height="40"><rect width="80" height="40" fill="#00008B"/><rect x="0" y="0" width="40" height="20" fill="#00008B"/><line x1="0" y1="0" x2="40" y2="20" stroke="white" stroke-width="2"/><line x1="40" y1="0" x2="0" y2="20" stroke="white" stroke-width="2"/><line x1="20" y1="0" x2="20" y2="20" stroke="white" stroke-width="3"/><line x1="0" y1="10" x2="40" y2="10" stroke="white" stroke-width="3"/><line x1="20" y1="0" x2="20" y2="20" stroke="red" stroke-width="1.5"/><line x1="0" y1="10" x2="40" y2="10" stroke="red" stroke-width="1.5"/></svg>
        <svg viewBox="0 0 80 40" width="80" height="40"><rect width="80" height="20" fill="#000"/><rect y="20" width="80" height="20" fill="#CC0000"/><circle cx="40" cy="20" r="10" fill="#FFCD00"/></svg>
        <svg viewBox="0 0 80 40" width="80" height="40"><rect width="80" height="40" fill="#009E49"/><rect x="0" y="12" width="80" height="16" fill="#00008B"/><rect x="0" y="14" width="80" height="1" fill="#fff"/><rect x="0" y="25" width="80" height="1" fill="#fff"/><circle cx="40" cy="20" r="6" fill="#fff"/></svg>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-logo-row"><img src="/Logo Serving Society.png" alt="Serving Society" class="footer-logo" /></div>
      <div class="footer-top">
        <div class="footer-brand"><p>Person-centred NDIS support services delivered with compassion, dignity, and respect.</p><div class="footer-badge">NDIS Registered Provider</div></div>
        <div class="footer-links"><h4>Services</h4><ul><li><a href="/services/accommodation-tenancy.html">Accommodation / Tenancy</a></li><li><a href="/services/community-participation.html">Community Participation</a></li><li><a href="/services/assist-personal-activities.html">Assist Personal Activities</a></li><li><a href="/services/household-tasks.html">Household Tasks</a></li></ul></div>
        <div class="footer-links"><h4>Quick Links</h4><ul><li><a href="/about.html">About Us</a></li><li><a href="/appointment.html">Appointment</a></li><li><a href="/index.html#contact">Contact</a></li><li><a href="https://www.ndis.gov.au" target="_blank" rel="noopener">NDIS Website</a></li></ul></div>
        <div class="footer-contact"><h4>Contact</h4><p><a href="tel:+61400000000">0400 000 000</a></p><p><a href="mailto:info@servingsociety.com.au">info@servingsociety.com.au</a></p></div>
      </div>
      <div class="footer-bottom"><p>&copy; 2026 Serving Society. All rights reserved.</p><p>ABN: XX XXX XXX XXX &nbsp;|&nbsp; NDIS Provider</p></div>
    </div>
  </footer>
  <script src="/script.js"></script>
</body>
</html>'''

SERVICES = [
    {
        "file": "accommodation-tenancy.html",
        "title": "Accommodation / Tenancy",
        "image": "accommodation-tenancy",
        "desc": "Serving Society — Accommodation and Tenancy assistance for NDIS participants.",
        "body": """<p>At Serving Society, we understand how important a secure and suitable living environment is to your overall wellbeing and independence. Our <strong>Accommodation and Tenancy Assistance</strong> service is designed to help NDIS participants find, maintain, and thrive in appropriate housing.</p>
      <p>Whether you need help understanding rental agreements, applying for accommodation, or resolving tenancy issues, our experienced team is here to guide and support you every step of the way.</p>""",
        "checklist_title": "Our Support Includes:",
        "checklist": [
            "Identifying suitable accommodation based on your needs and preferences",
            "Assistance with tenancy applications and housing paperwork",
            "Support with rental negotiations and lease agreements",
            "Developing individualised housing goals and tenancy plans",
            "Liaising with real estate agents, housing providers, and government services",
            "Assistance with sustaining your tenancy and addressing housing issues",
        ],
        "closing": "<p>We work closely with you to ensure your housing supports align with your NDIS goals, helping you achieve a stable and independent lifestyle in a place you can truly call home.</p>",
    },
    {
        "file": "life-stage-transition.html",
        "title": "Assist Life Stage, Transition",
        "image": "life-stage-transition",
        "desc": "Serving Society — Life stage transition support for NDIS participants.",
        "body": """<p>Life is full of transitions — starting a new job, moving to a new home, or adjusting to greater independence. At Serving Society, we're here to support you through these significant life stages with compassion, planning, and personalised care.</p>
      <p>Our <strong>Assist Life Stage, Transition</strong> service is designed to help NDIS participants navigate life's changes, develop essential skills, and connect with the right supports to achieve long-term stability and independence.</p>""",
        "checklist_title": "We Support You With:",
        "checklist": [
            "Strengthening daily living and decision-making skills",
            "Short and long-term goal setting and planning",
            "Support with moving into independent or supported living",
            "Guidance through school-to-work or youth-to-adult transitions",
            "Coordinating services and building informal support networks",
            "Assistance with employment or education pathways",
            "Mentoring, peer support, and capacity building",
        ],
        "closing": "<p>Whether you're moving into a new home, leaving school, or seeking greater independence, our experienced team will walk alongside you with care and respect. We take the time to understand your journey and provide the right tools and resources to make your transitions smoother and more successful.</p><p>Let Serving Society be your trusted support through life's changes — empowering you every step of the way.</p>",
    },
    {
        "file": "daily-tasks-shared-living.html",
        "title": "Daily Tasks / Shared Living",
        "image": "daily-tasks-shared-living",
        "desc": "Serving Society — Daily tasks and shared living support for NDIS participants.",
        "body": """<p>At Serving Society, we recognise that everyday tasks are the building blocks of independence. Our <strong>Daily Tasks / Shared Living</strong> service provides practical, hands-on support to help you manage daily routines and shared living arrangements with comfort and confidence.</p>
      <p>Whether you live alone or share your home, our friendly support workers are here to help you maintain a clean, safe, and welcoming environment while building your independent living skills.</p>""",
        "checklist_title": "We Can Assist With:",
        "checklist": [
            "Meal planning, preparation, and cooking support",
            "Budgeting and financial management guidance",
            "Shared living coordination and housemate communication",
            "Personal organisation and time management",
            "Grocery shopping and errands",
            "Light household management in shared settings",
            "Building routines that support your goals",
        ],
        "closing": "<p>Our team works with you to build confidence and practical skills that empower you to manage your daily life — whether in your own home or in a shared living arrangement. We provide respectful, participant-led support that adapts to your pace and preferences.</p>",
    },
    {
        "file": "development-life-skills.html",
        "title": "Development Life Skills",
        "image": "development-life-skills",
        "desc": "Serving Society — Life skills development for NDIS participants.",
        "body": """<p>Building life skills is essential to achieving independence and confidence. At Serving Society, our <strong>Development Life Skills</strong> service is designed to help NDIS participants learn, practice, and master the skills they need to thrive in everyday life.</p>
      <p>We take a person-centred approach, focusing on your individual goals and working at your pace to develop skills that matter most to you.</p>""",
        "checklist_title": "Our Support Includes:",
        "checklist": [
            "Cooking and kitchen safety skills",
            "Managing personal hygiene and self-care routines",
            "Money management and budgeting",
            "Using public transport independently",
            "Time management and daily scheduling",
            "Social skills and communication building",
            "Problem-solving and decision-making support",
            "Technology and digital literacy",
        ],
        "closing": "<p>Our experienced and patient support workers create a safe, encouraging environment where you can build confidence through practice and real-world experience. We celebrate every milestone with you.</p><p>Let Serving Society help you unlock your potential — one skill at a time.</p>",
    },
    {
        "file": "community-participation.html",
        "title": "Community Participation",
        "image": "community-participation",
        "desc": "Serving Society — Community participation support for NDIS participants.",
        "body": """<p>Being part of your community is vital for wellbeing, connection, and personal growth. At Serving Society, our <strong>Community Participation</strong> service supports NDIS participants to engage in meaningful social, recreational, and community activities.</p>
      <p>We believe everyone deserves to feel connected, included, and valued. Our team is here to help you explore new interests, build friendships, and become an active member of your local community.</p>""",
        "checklist_title": "We Can Support You With:",
        "checklist": [
            "Attending social and recreational events",
            "Joining community groups, clubs, or classes",
            "Volunteering and civic engagement opportunities",
            "Visiting local facilities like libraries, parks, and community centres",
            "Developing social skills and confidence in group settings",
            "Exploring hobbies and interests",
            "Building meaningful relationships and networks",
        ],
        "closing": "<p>Whether you want to try something new, reconnect with your community, or simply enjoy a day out, our team provides friendly, respectful support tailored to your interests and goals.</p>",
    },
    {
        "file": "assist-personal-activities.html",
        "title": "Assist Personal Activities",
        "image": "assist-personal-activities",
        "desc": "Serving Society — Personal activities assistance for NDIS participants.",
        "body": """<p>At Serving Society, we understand that daily personal tasks can sometimes be challenging. That's why our <strong>Assist Personal Activities</strong> service is here to provide reliable and respectful support, helping you carry out essential routines while promoting independence and self-confidence.</p>
      <p>Our trained and friendly support workers deliver care with a person-centred approach, ensuring your comfort, preferences, and dignity are always prioritised.</p>""",
        "checklist_title": "We Assist With:",
        "checklist": [
            "Personal hygiene (showering, grooming, dressing)",
            "Toileting and continence care",
            "Assistance with eating and drinking",
            "Mobility and transfers (getting in/out of bed or wheelchair)",
            "Medication reminders and basic health monitoring",
            "Personal safety and supervision as needed",
            "Morning and bedtime routines",
            "Support with daily planning and scheduling",
        ],
        "closing": "<p>Whether you need short-term assistance or ongoing daily support, we tailor our services to your individual needs, goals, and lifestyle. Our aim is to empower you to live as independently and confidently as possible — while ensuring you feel safe, supported, and in control.</p><p>At Serving Society, we're here to make every day smoother, easier, and more empowering.</p>",
    },
    {
        "file": "assist-travel-transport.html",
        "title": "Assist Travel / Transport",
        "image": "assist-travel-transport",
        "desc": "Serving Society — Travel and transport assistance for NDIS participants.",
        "body": """<p>At Serving Society, we understand the importance of being able to move freely and access your community with ease. Our <strong>Assist Travel / Transport</strong> service is designed to support NDIS participants who need help getting to and from essential places safely, comfortably, and on time.</p>
      <p>Whether it's attending medical appointments, going to work or school, or participating in social and recreational activities, our team is here to make travel stress-free and accessible.</p>""",
        "checklist_title": "We Can Assist You With Transport To:",
        "checklist": [
            "Medical and health appointments",
            "School, training, or educational programs",
            "Employment and volunteer activities",
            "Social, community, and recreational events",
            "Shopping trips and essential errands",
            "Therapy and support service appointments",
        ],
        "closing": "<p>All our support workers and drivers are fully qualified, experienced, and committed to providing safe, respectful, and friendly assistance. We prioritise your comfort, punctuality, and independence — offering flexible transport options based on your schedule and mobility needs.</p><p>Let Serving Society help you stay connected to the things that matter most — with confidence, convenience, and care.</p>",
    },
    {
        "file": "innovative-community-participation.html",
        "title": "Innovative Community Participation",
        "image": "innovative-community",
        "desc": "Serving Society — Innovative community participation for NDIS participants.",
        "body": """<p>At Serving Society, we go beyond traditional support by offering <strong>Innovative Community Participation</strong> services that are designed to unlock creativity, promote independence, and foster meaningful community involvement.</p>
      <p>This service supports NDIS participants to engage in uniquely tailored activities that build confidence, develop new skills, and encourage personal growth in dynamic, non-traditional ways.</p>""",
        "checklist_title": "Our Innovative Programs Can Include:",
        "checklist": [
            "Art, music, or creative workshops",
            "Social enterprise and small business mentoring",
            "Digital literacy and technology training",
            "Leadership and advocacy development",
            "Community volunteering and project involvement",
            "Skill-building programs for employment readiness",
            "Personal development and confidence-building activities",
        ],
        "closing": "<p>Through this service, we aim to help you explore exciting opportunities outside the standard offerings, based on your interests and aspirations. Whether it's learning a new skill, discovering your passion, or engaging in a project that inspires you — our team is here to guide and support your journey.</p><p>Let Serving Society help you think outside the box and create your own path in the community — where your voice matters, and your potential is limitless.</p>",
    },
    {
        "file": "household-tasks.html",
        "title": "Household Tasks",
        "image": "household-tasks",
        "desc": "Serving Society — Household tasks support for NDIS participants.",
        "body": """<p>At Serving Society, we know that keeping up with household tasks can be challenging at times. That's why we offer reliable and respectful support to help you manage everyday chores and maintain a living space that supports your health, wellbeing, and independence.</p>
      <p>Our <strong>Household Tasks</strong> service is tailored to suit your individual needs, preferences, and abilities — so you can feel confident and comfortable in your own home.</p>""",
        "checklist_title": "We Can Assist With:",
        "checklist": [
            "General house cleaning (vacuuming, mopping, dusting)",
            "Dishwashing and kitchen cleaning",
            "Laundry and ironing",
            "Changing bed linen and making beds",
            "Bathroom and toilet cleaning",
            "Grocery shopping and unpacking",
            "Meal preparation and basic cooking support",
            "Organising and tidying living spaces",
        ],
        "closing": "<p>Our friendly and trustworthy support workers ensure tasks are carried out with care and attention to detail — always respecting your routines, privacy, and choices. Whether you need occasional help or ongoing assistance, we're here to make your home a safer, healthier, and more enjoyable place to live.</p><p>With Serving Society, keeping your home in order is simple, stress-free, and empowering.</p>",
    },
]

def sidebar_html(active_title):
    items = []
    for name, href in SIDEBAR_SERVICES:
        cls = ' class="active"' if name == active_title else ''
        items.append(f'            <li><a href="{href}"{cls}>{name}</a></li>')
    return "\n".join(items)

def build_service(s):
    checklist = "\n".join(f'        <li>{item}</li>' for item in s["checklist"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{s['desc']}" />
  <title>{s['title']} | Serving Society</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/style.css" />
</head>
<body>

{NAV}

  <section class="page-banner">
    <div class="container"><h1 class="page-banner-title">{s['title']}</h1></div>
  </section>

  <section class="container">
    <div class="service-page-layout">
      <div class="service-main-content reveal">
        <img src="/images/{s['image']}.png" alt="{s['title']}" class="service-hero-img" />
        <h2>{s['title']}</h2>
        {s['body']}
        <h3>{s['checklist_title']}</h3>
        <ul class="support-checklist">
{checklist}
        </ul>
        {s['closing']}
        <a href="/appointment.html" class="btn btn-primary" style="margin-top:16px;">Contact Now &rarr;</a>
      </div>
      <aside class="service-sidebar">
        <nav class="sidebar-nav">
          <h4>Other Services</h4>
          <ul>
{sidebar_html(s['title'])}
          </ul>
        </nav>
        <div class="question-widget">
          <h4>Have Any Question?</h4>
          <p>Not sure where to start or need more information about our services? Our friendly team is just a call or message away.</p>
          <a href="tel:+61400000000" class="btn btn-primary">Call Now</a>
        </div>
      </aside>
    </div>
  </section>
{BOTTOM}'''

if __name__ == "__main__":
    os.makedirs(os.path.join(BASE, "services"), exist_ok=True)
    for s in SERVICES:
        path = os.path.join(BASE, "services", s["file"])
        with open(path, "w") as f:
            f.write(build_service(s))
        print(f"  Created: services/{s['file']}")
    print(f"\n  Done: {len(SERVICES)} service pages created.")
