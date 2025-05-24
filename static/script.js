function createPolygonPath(coords) {
    const points = coords.split(',').map(Number);
    let path = '';
    for (let i = 0; i < points.length; i += 2) {
        path += `${points[i]},${points[i + 1]} `;
    }
    return path.trim();
}

function getPointsFromCoords(coords) {
    const points = coords.split(',').map(Number);
    const result = [];
    for (let i = 0; i < points.length; i += 2) {
        result.push({ x: points[i], y: points[i + 1] });
    }
    return result;
}

function createSparkle(container, x, y) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    
    // Add offset to position sparkles outside the border (adjust these values as needed)
    const angle = Math.random() * Math.PI * 2;
    const distance = 10; // Distance from the border in pixels
    const offsetX = Math.cos(angle) * distance;
    const offsetY = Math.sin(angle) * distance;
    
    sparkle.style.left = `${x + offsetX}px`;
    sparkle.style.top = `${y + offsetY}px`;
    sparkle.style.animation = `sparkle ${1.5 + Math.random()}s ease-in-out infinite`;
    sparkle.style.animationDelay = `${Math.random() * 3}s`;
    container.appendChild(sparkle);
    return sparkle;
}

function createHighlight(area) {
    const container = area.closest('.image-container');
    if (!container) {
        console.error('Could not find .image-container for area', area);
        return;
    }

    let sparkleContainer = container.querySelector('.sparkle-container');
    if (!sparkleContainer) {
        sparkleContainer = document.createElement('div');
        sparkleContainer.className = 'sparkle-container';
        container.appendChild(sparkleContainer);
    }

    // Store the container reference on the area element
    area.sparkleContainer = sparkleContainer;
    area.sparkles = []; // Array to store sparkle elements
    
    // Create initial sparkles
    animateSparklesAlongPath(area);
}

function animateSparklesAlongPath(area) {
    if (!area.sparkleContainer) return;
    
    // Clear existing sparkles
    area.sparkles.forEach(sparkle => sparkle.remove());
    area.sparkles = [];

    const points = getPointsFromCoords(area.coords);
    const numSparkles = Math.floor(points.length * 0.25); // Reduced density from 0.5 to 0.25

    // Create sparkles along the path
    for (let i = 0; i < numSparkles; i++) {
        // Get two random adjacent points
        const idx = Math.floor(Math.random() * (points.length - 1));
        const p1 = points[idx];
        const p2 = points[idx + 1];

        // Interpolate between points
        const t = Math.random();
        const x = p1.x + (p2.x - p1.x) * t;
        const y = p1.y + (p2.y - p1.y) * t;

        // Create sparkle at interpolated position
        const sparkle = createSparkle(area.sparkleContainer, x, y);
        area.sparkles.push(sparkle);
    }
}

function hideSparkles(area) {
    if (area.sparkleContainer) {
        // Instead of hiding, make all sparkles golden
        area.sparkles.forEach(sparkle => {
            sparkle.classList.add('golden');
        });
    }
}

function showSparkles(area) {
    if (area.sparkleContainer) {
        // Remove golden class instead of showing
        area.sparkles.forEach(sparkle => {
            sparkle.classList.remove('golden');
        });
    }
}

function initializeHighlights(container) {
    const areas = container.querySelectorAll('area');
    areas.forEach(area => {
        createHighlight(area);

        area.addEventListener('mouseenter', () => {
            hideSparkles(area);
        });

        area.addEventListener('mouseleave', () => {
            showSparkles(area);
        });
    });
}

window.addEventListener('load', () => {
    const currentMapDiv = document.querySelector('.image-map');
    if (currentMapDiv) {
        initializeHighlights(currentMapDiv);
    } else {
        console.error("No element with class '.image-map' found on this page.");
    }
}); 