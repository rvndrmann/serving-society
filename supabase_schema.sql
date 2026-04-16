-- ============================================================
-- SERVING SOCIETY — Supabase Schema
-- Run this in the Supabase SQL Editor
-- ============================================================

-- ── Enable UUID extension (already enabled on Supabase by default) ──
-- create extension if not exists "uuid-ossp";

-- ============================================================
-- TABLE: contacts
-- Stores submissions from the Contact Us form on index.html
-- ============================================================
create table if not exists contacts (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  name        text,
  phone       text,
  email       text,
  service     text,
  message     text
);

-- Enable Row Level Security
alter table contacts enable row level security;

-- Policy: anyone (anon) can insert (form submission)
create policy "Allow anon insert on contacts"
  on contacts
  for insert
  to anon
  with check (true);

-- Policy: authenticated users (admin) can read all contacts
create policy "Allow authenticated select on contacts"
  on contacts
  for select
  to authenticated
  using (true);

-- ============================================================
-- TABLE: appointments
-- Stores submissions from the Appointment Request form
-- ============================================================
create table if not exists appointments (
  id              uuid primary key default gen_random_uuid(),
  created_at      timestamptz not null default now(),
  first_name      text,
  last_name       text,
  email           text,
  phone           text,
  contact_method  text,
  services        text,
  preferred_date  date,
  preferred_time  time,
  notes           text
);

-- Enable Row Level Security
alter table appointments enable row level security;

-- Policy: anyone (anon) can insert (form submission)
create policy "Allow anon insert on appointments"
  on appointments
  for insert
  to anon
  with check (true);

-- Policy: authenticated users (admin) can read all appointments
create policy "Allow authenticated select on appointments"
  on appointments
  for select
  to authenticated
  using (true);

-- ============================================================
-- NOTES FOR SETUP
-- ============================================================
-- 1. Run this SQL in Supabase > SQL Editor
-- 2. Go to Authentication > Users and create an admin user manually
-- 3. Copy your Project URL and anon key from Settings > API
-- 4. Replace YOUR_SUPABASE_URL and YOUR_SUPABASE_ANON_KEY in:
--    - script.js
--    - admin.html
-- ============================================================
