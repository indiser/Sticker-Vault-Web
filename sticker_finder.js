// Initialize a Set to prevent duplicates
window.extractedStickers = window.extractedStickers || new Set();

// Start a highly aggressive interval to scrape blob URLs as they render
window.scraperInterval = setInterval(() => {
    // WhatsApp typically renders stickers as images with blob URLs
    document.querySelectorAll('img[src^="blob:"]').forEach(img => {
        window.extractedStickers.add(img.src);
    });
    console.clear();
    console.log(`Scraping... Currently captured: ${window.extractedStickers.size} unique stickers. Keep scrolling up.`);
}, 400); // Runs every 400ms