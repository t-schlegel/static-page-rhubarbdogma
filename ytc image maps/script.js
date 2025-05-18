function createPolygonPath(coords) {
    const points = coords.split(',').map(Number);
    let path = '';
    for (let i = 0; i < points.length; i += 2) {
        path += `${points[i]},${points[i + 1]} `;
    }
    return path.trim();
}

function createHighlight(area) {
    const container = area.closest('.image-container');
    if (!container) {
        console.error('Could not find .image-container for area', area);
        return;
    }
    const img = container.querySelector('img');
    if (!img) {
        console.error('Could not find img in .image-container for area', area);
        return;
    }

    let highlightContainer = container.querySelector('.highlight-container');
    if (!highlightContainer) {
        highlightContainer = document.createElement('div');
        highlightContainer.className = 'highlight-container';
        container.appendChild(highlightContainer);
    }

    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.position = 'absolute';
    svg.style.top = '0';
    svg.style.left = '0';
    svg.style.width = '100%';
    svg.style.height = '100%';
    
    // Wait for image to load to get naturalWidth/Height if not already loaded
    if (img.naturalWidth === 0 || img.naturalHeight === 0) {
        img.onload = () => {
            svg.setAttribute('viewBox', `0 0 ${img.naturalWidth} ${img.naturalHeight}`);
        };
    } else {
        svg.setAttribute('viewBox', `0 0 ${img.naturalWidth} ${img.naturalHeight}`);
    }
    svg.style.pointerEvents = 'none';

    const polygon = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    polygon.setAttribute('points', createPolygonPath(area.coords));
    polygon.setAttribute('fill', 'none');

    svg.appendChild(polygon);
    highlightContainer.appendChild(svg);

    area.polygonEl = polygon;
}

function redirectToMainMap() {
    window.location.href = 'cluton_map.html'; // This is level1, the main Cluton Map
}

function initializeHighlights(container) {
    const areas = container.querySelectorAll('area');
    areas.forEach(area => {
        createHighlight(area);

        area.addEventListener('mouseenter', () => {
            if (area.polygonEl) {
                area.polygonEl.setAttribute('stroke', 'rgba(105, 105, 105, 0.5)');
                area.polygonEl.setAttribute('stroke-width', '2');
                area.polygonEl.style.filter = 'drop-shadow(0 0 20px dimgrey)';
            }
        });

        area.addEventListener('mouseleave', () => {
            if (area.polygonEl) {
                area.polygonEl.removeAttribute('stroke');
                area.polygonEl.removeAttribute('stroke-width');
                area.polygonEl.style.filter = 'none';
            }
        });
    });
}

window.addEventListener('load', () => {
    const currentMapDiv = document.querySelector('.image-map'); 
    if (currentMapDiv) {
        // Ensure image is loaded before initializing highlights, especially for viewBox calculation
        const img = currentMapDiv.querySelector('img');
        if (img) {
            if (img.complete) {
                 initializeHighlights(currentMapDiv);
            } else {
                img.addEventListener('load', () => {
                    initializeHighlights(currentMapDiv);
                });
            }
        } else {
            console.error("No img element found in .image-map for highlight initialization.");
        }
    } else {
        console.error("No element with class '.image-map' found on this page.");
    }
}); 