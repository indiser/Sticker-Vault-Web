// Stop the interval
clearInterval(window.scraperInterval);

function downloadExtractedStickers() {
    let urls = Array.from(window.extractedStickers);
    console.log(`Initializing download sequence for ${urls.length} files...`);
    
    urls.forEach((url, index) => {
        // Stagger the downloads to prevent the browser from crashing or throttling
        setTimeout(() => {
            let a = document.createElement('a');
            a.href = url;
            a.download = `raw_sticker_${index}.webp`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }, index * 250); // 250ms delay between each download
    });
}

// Execute the download
downloadExtractedStickers();