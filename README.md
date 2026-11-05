# Therapy Mock Up

An independent, reusable HTML/CSS/JavaScript therapy website template by 2e Studio. The existing logo is retained. All therapist and practice information is placeholder content; the profile image is a neutral avatar.

## Personalize

Edit `dist/index.html` and replace bracketed labels: Practice Name, Therapist Name, First Name, Credentials, License Type & Number, optional Supervision Details, City/State, Street Address, Suite, ZIP Code, Phone Number, Email Address, Year, Consultation Details, fees, Map Link, biography and approach. Review all service and availability copy for the new practice.

Replace `dist/assets/profile-placeholder.svg` with the therapist’s authorized portrait and update its path, alt text, and dimensions. Keep the approved logo in `dist/assets/emblem.webp`.

The call placeholder opens the demo form rather than dialing anyone. Connect it to the practice’s real `tel:` link after customization. The professional-profile and map placeholders have no client-specific destinations.

## Forms

The consultation modal is a visual demo. It sends and saves nothing. Its submit button is disabled. Before going live, connect the approved Formspree endpoint or other form service, add appropriate visitor information, and test actual delivery.

## Deploy

Publish the contents of `dist/` on any static host. No build command is required. Before a client launch, replace the template preview origin in canonical, Open Graph, Twitter/X, structured data, robots.txt and sitemap.xml with the final domain. This repository is not connected to a live host. The `https://example.com` domain in the metadata is a reserved placeholder; replace it everywhere before deployment. The current page is intentionally `noindex`; remove that only when the client site is approved for indexing. Replace template WebSite metadata with accurate practice information.

Generate a new 1200 × 630 social image using `scripts/create-social-preview.py` (Python + Pillow) after adapting the artwork/text. Complete `docs/website-launch-checklist.md` and record final-domain/crawler/debugger results before launch.

Keep the exact “Designed by 2e Studio” footer credit and its supplied destination.

## Open in VS Code

Open this folder, or open `therapy-mock-up.code-workspace`. All website files live in `dist/`.

## Project separation

This is a new repository with fresh history. It does not include any hosting project ID, original repository settings, client portrait, or client-specific contact details. Editing or publishing this repository does not update the Systemic Solutions repository.
