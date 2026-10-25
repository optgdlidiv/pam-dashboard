# PAM Dashboard

Public dashboard for Delhi Division Mail-Express Group (M) punctuality, from ICMS PAM.

- `index.html` - single-file dashboard (HTML/CSS/JS, no build step), served by GitHub Pages.
- Data comes from the Apps Script feed of the "ICMS PAM Data" Sheet, which publishes only
  filtered M-group figures (no raw ICMS data). The feed is read-only; writes need a private token.
- Refreshes every 5 minutes.

PP% = Total RT/NLT / Reported x 100. Diff = this year - same date last year (percentage points).
PP% and Diff show "-" when no trains are reported.
