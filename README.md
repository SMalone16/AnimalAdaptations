# Animal Adaptations Biome Explorer

This project is a GitHub Pages-friendly site that helps first grade students explore how animals survive in different biomes. Students begin on a colorful landing page and tap their biome to discover animals, learn about their adaptations, and listen to each fact using built-in speech synthesis.

## Structure

- `index.html` – main landing page with biome selection buttons.
- `biomes/` – biome-specific folders that contain the animal selection page (`index.html`) and individual animal research pages.
- `assets/css/styles.css` – shared styling for the entire site.
- `assets/js/script.js` – adds click-to-hear functionality with the browser's SpeechSynthesis API.
- `generate_animals.py` – helper script that regenerates all individual animal pages from structured data.

## Content Highlights

- Four biomes: Rainforest, Savannah, Desert, and Tundra.
- Each biome features 12 animals with image buttons leading to research pages.
- Every animal page includes:
  - Friendly introduction text and a large supporting image.
  - Three adaptation sections that describe unique survival traits.
  - "Hear this adaptation" buttons that read each fact aloud.

## Local Preview

You can open `index.html` directly in a browser or use a lightweight web server (for example, `python -m http.server`) to preview and test the SpeechSynthesis audio interactions.
