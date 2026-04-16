# AI Agent Instructions — Build Content Pages for Serving Society

## Project Overview

You are adding **11 new HTML pages** to an existing static website for "Serving Society", an NDIS provider. The existing site is vanilla HTML/CSS/JS with no framework. All new pages must match the existing design system.

**Existing files to reference:**
- `index.html` — current homepage (structure, nav, footer)
- `style.css` — full design system (variables, components, responsive)
- `script.js` — animations, nav toggle, reveal scroll, form validation
- `PAGES_CONTENT.md` — all text content for every page
- `IMAGE_PROMPTS_PAGES.md` — image generation prompts

---

## Design System (DO NOT CHANGE)

```css
--purple:       #5E2D6E;
--purple-dark:  #4A2356;
--purple-mid:   #7A3F8C;
--purple-light: #F4ECF7;
--lime:         #C6DA02;
--lime-dark:    #A8BC02;
--white:        #ffffff;
--off-white:    #F7F5F2;
```

**Font:** `'Public Sans', 'Outfit', system-ui, sans-serif`

**Border radius:** `4px` (sm), `8px` (md), `12px` (lg)

**Buttons:** Pill-shaped (border-radius: 100px). Primary = purple bg, white text. CTA variant = lime bg, purple text.

---

## Step-by-Step Build Instructions

### Step 1: Update Navigation (All Pages)

**File: `index.html` (and all new pages)**

Replace the current nav links with:

```html
<ul class="nav-links" id="navLinks">
  <li><a href="/index.html" class="nav-link">Home</a></li>
  <li><a href="/about.html" class="nav-link">About Us</a></li>
  <li class="nav-dropdown">
    <a href="#" class="nav-link nav-link-dropdown">Services <svg width="10" height="6" viewBox="0 0 10 6"><path d="M1 1l4 4 4-4" stroke="currentColor" fill="none" stroke-width="1.5"/></svg></a>
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
  <li><a href="#contact" class="nav-link nav-cta">Get in Touch</a></li>
</ul>
```

**Add CSS for dropdown (in `style.css`):**

```css
.nav-dropdown { position: relative; }
.nav-link-dropdown { display: flex; align-items: center; gap: 6px; }
.dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: var(--white);
  border: 1px solid var(--grey-200);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  min-width: 280px;
  padding: 8px 0;
  z-index: 100;
}
.nav-dropdown:hover .dropdown-menu { display: block; }
.dropdown-menu li a {
  display: block;
  padding: 10px 20px;
  font-size: .9rem;
  color: var(--text);
  transition: var(--transition);
}
.dropdown-menu li a:hover {
  background: var(--purple-light);
  color: var(--purple);
}
```

**Add JS for mobile dropdown toggle (in `script.js`):**

```js
document.querySelectorAll('.nav-link-dropdown').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    link.parentElement.classList.toggle('dropdown-open');
  });
});
```

---

### Step 2: Create Page Template

Every new page follows this HTML skeleton. Copy and fill per-page content from `PAGES_CONTENT.md`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="PAGE_DESCRIPTION" />
  <title>PAGE_TITLE | Serving Society</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/style.css" />
</head>
<body>

  <!-- NAVBAR (copy from index.html, update active link) -->

  <!-- PAGE BANNER -->
  <section class="page-banner">
    <div class="container">
      <h1 class="page-banner-title">PAGE_TITLE</h1>
    </div>
  </section>

  <!-- PAGE CONTENT (varies by page type — see below) -->

  <!-- TESTIMONIAL SECTION (shared component) -->

  <!-- ACKNOWLEDGEMENT OF COUNTRY (shared component) -->

  <!-- FOOTER (copy from index.html) -->

  <script src="/script.js"></script>
</body>
</html>
```

---

### Step 3: Create Shared CSS Components

**Add to `style.css`:**

```css
/* ── Page Banner ── */
.page-banner {
  background: var(--purple);
  padding: calc(var(--nav-h) + 40px) 0 40px;
  text-align: center;
}
.page-banner-title {
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  font-weight: 700;
  color: var(--white);
}

/* ── Service Page Layout ── */
.service-page-layout {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 48px;
  padding: 64px 0;
}
.service-main-content h2 {
  font-size: clamp(1.6rem, 3vw, 2.2rem);
  font-weight: 700;
  color: var(--purple);
  margin-bottom: 20px;
}
.service-main-content p {
  color: var(--text-soft);
  line-height: 1.7;
  margin-bottom: 16px;
}
.service-main-content h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--purple);
  margin: 24px 0 12px;
}

/* Checklist */
.support-checklist {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 24px;
}
.support-checklist li {
  font-size: .92rem;
  color: var(--text-soft);
  padding-left: 28px;
  position: relative;
  line-height: 1.5;
}
.support-checklist li::before {
  content: '\2713';
  position: absolute;
  left: 0;
  color: var(--lime-dark);
  font-weight: 700;
}

/* Service Sidebar */
.service-sidebar {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
.sidebar-nav {
  background: var(--purple);
  border-radius: var(--radius-md);
  padding: 24px;
}
.sidebar-nav h4 {
  color: var(--white);
  font-size: 1rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 16px;
}
.sidebar-nav ul { display: flex; flex-direction: column; gap: 4px; }
.sidebar-nav a {
  display: block;
  padding: 10px 16px;
  border-radius: var(--radius-sm);
  font-size: .88rem;
  color: rgba(255,255,255,.85);
  transition: var(--transition);
}
.sidebar-nav a:hover { background: rgba(255,255,255,.15); }
.sidebar-nav a.active {
  background: var(--lime);
  color: var(--purple-dark);
  font-weight: 600;
}

/* Question widget */
.question-widget {
  background: var(--purple-light);
  border-radius: var(--radius-md);
  padding: 32px 24px;
  text-align: center;
}
.question-widget h4 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--purple);
  margin-bottom: 10px;
}
.question-widget p {
  font-size: .88rem;
  color: var(--text-soft);
  line-height: 1.6;
  margin-bottom: 16px;
}

/* Service hero image */
.service-hero-img {
  width: 100%;
  height: 320px;
  object-fit: cover;
  border-radius: var(--radius-md);
  margin-bottom: 32px;
}

/* ── How To Book Section ── */
.how-to-book {
  background: linear-gradient(135deg, #1a6b7a, #1a8a6b);
  padding: 80px 0;
  text-align: center;
  color: var(--white);
}
.how-to-book .section-tag { background: rgba(255,255,255,.2); color: var(--white); }
.how-to-book .section-title { color: var(--white); }
.how-to-book .section-title::after { background: var(--lime); }
.book-steps {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  margin-top: 48px;
}
.book-step-number {
  font-size: 3rem;
  font-weight: 700;
  color: rgba(255,255,255,.3);
  margin-bottom: 12px;
}
.book-step h4 {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 12px;
}
.book-step p {
  font-size: .9rem;
  color: rgba(255,255,255,.8);
  line-height: 1.6;
  margin-bottom: 16px;
}

/* ── Why Choose Us ── */
.why-choose-us {
  background: var(--text);
  padding: 80px 0;
}
.why-choose-us .section-title { color: var(--white); }
.why-choose-us .section-title::after { background: var(--lime); }
.why-choose-us .section-subtitle { color: rgba(255,255,255,.7); }
.why-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 48px;
}
.why-card {
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: var(--radius-md);
  padding: 32px 24px;
  transition: var(--transition);
}
.why-card:hover {
  background: rgba(255,255,255,.1);
  transform: translateY(-4px);
}
.why-card-icon {
  width: 48px; height: 48px;
  background: var(--purple);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 16px;
  color: var(--white);
}
.why-card h4 {
  font-size: 1rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 10px;
}
.why-card p {
  font-size: .88rem;
  color: rgba(255,255,255,.65);
  line-height: 1.6;
}

/* ── Testimonial Section ── */
.testimonial-section {
  background: var(--grey-700);
  padding: 80px 0;
}
.testimonial-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
}
.testimonial-left h2 {
  font-size: clamp(1.6rem, 3vw, 2.4rem);
  font-weight: 700;
  color: var(--white);
  line-height: 1.2;
  margin-bottom: 16px;
}
.testimonial-left h2 span { color: var(--lime); }
.testimonial-left p {
  color: rgba(255,255,255,.7);
  line-height: 1.7;
  margin-bottom: 20px;
}
.testimonial-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 32px;
}
.testimonial-stars { color: var(--lime-dark); font-size: 1.2rem; margin-bottom: 12px; }
.testimonial-card blockquote {
  font-size: .95rem;
  color: var(--text-soft);
  line-height: 1.7;
  margin-bottom: 16px;
  font-style: italic;
}
.testimonial-author { font-weight: 700; color: var(--text); }
.testimonial-role { font-size: .82rem; color: var(--purple); }

/* ── Acknowledgement of Country ── */
.acknowledgement {
  background: var(--lime);
  padding: 48px 0;
  text-align: center;
}
.acknowledgement h2 {
  font-size: clamp(1.4rem, 3vw, 2rem);
  font-weight: 700;
  color: var(--purple-dark);
  margin-bottom: 12px;
}
.acknowledgement p {
  font-size: .95rem;
  color: var(--text);
  max-width: 720px;
  margin: 0 auto 20px;
  line-height: 1.7;
}
.flags { display: flex; justify-content: center; gap: 16px; }
.flags img { height: 48px; border-radius: 4px; box-shadow: var(--shadow-sm); }

/* ── Appointment Form ── */
.appointment-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 56px;
  padding: 80px 0;
  align-items: start;
}

/* ── Responsive additions ── */
@media (max-width: 1024px) {
  .service-page-layout { grid-template-columns: 1fr; }
  .service-sidebar { order: -1; }
  .book-steps { grid-template-columns: 1fr; gap: 24px; }
  .why-cards { grid-template-columns: repeat(2, 1fr); }
  .testimonial-grid { grid-template-columns: 1fr; }
  .appointment-layout { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
  .why-cards { grid-template-columns: 1fr; }
  .dropdown-menu {
    position: static;
    box-shadow: none;
    border: none;
    padding-left: 24px;
  }
}
```

---

### Step 4: Create Directory Structure

```
mkdir -p services
```

Then create each file as listed in the Pages table from `PAGES_CONTENT.md`.

---

### Step 5: Build Each Service Page

For every service page, follow this structure (example: Accommodation / Tenancy):

```html
<!-- After navbar and page-banner -->
<section class="container">
  <div class="service-page-layout">
    <div class="service-main-content reveal">
      <img src="/images/accommodation-tenancy.webp" alt="Accommodation and tenancy support" class="service-hero-img" />
      <h2>Accommodation / Tenancy</h2>
      <!-- Body paragraphs from PAGES_CONTENT.md -->
      <h3>Our Support Includes:</h3>
      <ul class="support-checklist">
        <!-- Checklist items from PAGES_CONTENT.md -->
      </ul>
      <!-- Closing paragraph from PAGES_CONTENT.md -->
      <a href="/appointment.html" class="btn btn-primary" style="margin-top:16px;">Contact Now →</a>
    </div>
    <aside class="service-sidebar">
      <nav class="sidebar-nav">
        <h4>Other Services</h4>
        <ul>
          <li><a href="/services/accommodation-tenancy.html" class="active">Accommodation / Tenancy</a></li>
          <li><a href="/services/life-stage-transition.html">Assist Life Stage, Transition</a></li>
          <!-- ... all 9 services ... -->
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

<!-- How To Book Section -->
<!-- Why Choose Us Section -->
<!-- Appointment Form Section (optional — or link to appointment.html) -->
<!-- Testimonial Section -->
<!-- Acknowledgement of Country -->
<!-- Footer -->
```

---

### Step 6: Build About Us Page

Refer to `PAGES_CONTENT.md` > "PAGE: About Us" section. Structure:

1. Page banner with "About Us" title
2. Two-column hero: left = image + stat badge, right = heading + body text
3. Values icon row (3 icons: heart, shield, star)
4. Vision & Mission section with image, checklist
5. Testimonial section
6. Acknowledgement of Country
7. Footer

---

### Step 7: Build Appointment Page

Refer to `PAGES_CONTENT.md` > "PAGE: Make An Appointment". Structure:

1. Page banner
2. Two-column layout: left = form, right = heading + description + image
3. Form fields as specified in content doc
4. Footer

---

### Step 8: Create `images/` Directory

```
mkdir -p images
```

Use placeholder images initially. Generate from `IMAGE_PROMPTS_PAGES.md` later. For now, use colored placeholder divs or a placeholder service like `https://placehold.co/1200x800/5E2D6E/C6DA02?text=Service+Name`.

---

### Step 9: Update Home Page

1. Update `index.html` navbar to include the new dropdown nav
2. Add Testimonial section before footer
3. Add Acknowledgement of Country section before footer
4. Ensure all service card links point to their respective service pages

---

### Step 10: Verify

- [ ] All 11 new pages load without errors
- [ ] Navigation works across all pages (dropdown, mobile)
- [ ] Sidebar "Other Services" highlights the active page on each service page
- [ ] All content matches `PAGES_CONTENT.md` exactly
- [ ] Responsive layout works at mobile (375px), tablet (768px), desktop (1280px)
- [ ] Testimonial carousel/cards display correctly
- [ ] Acknowledgement of Country appears on every page
- [ ] Appointment form validates required fields
- [ ] Footer is consistent across all pages
- [ ] All links use correct relative paths (`/services/...`)

---

## File Checklist

```
serving-society/
├── index.html                    (UPDATE: new nav, testimonials, acknowledgement)
├── about.html                    (NEW)
├── appointment.html              (NEW)
├── style.css                     (UPDATE: add new component styles)
├── script.js                     (UPDATE: add dropdown toggle)
├── services/
│   ├── accommodation-tenancy.html
│   ├── life-stage-transition.html
│   ├── daily-tasks-shared-living.html
│   ├── development-life-skills.html
│   ├── community-participation.html
│   ├── assist-personal-activities.html
│   ├── assist-travel-transport.html
│   ├── innovative-community-participation.html
│   └── household-tasks.html
├── images/                        (placeholder images)
├── PAGES_CONTENT.md
├── IMAGE_PROMPTS_PAGES.md
└── AGENT_INSTRUCTIONS.md
```
