// Vanilla JS implementation for 3D card hover effects
document.addEventListener('DOMContentLoaded', function() {
    const cardElements = document.querySelectorAll('.card-3d');
    
    cardElements.forEach(card => {
        card.addEventListener('mouseenter', function(ev) {
            const element = ev.currentTarget;
            element.bounds = element.getBoundingClientRect();
            element.addEventListener('mousemove', rotateToPointer);
        });

        card.addEventListener('mouseleave', function(ev) {
            const element = ev.currentTarget;
            element.removeEventListener('mousemove', rotateToPointer);
            element.style.transform = '';
            element.style.background = '';
        });

        // Touch events
        card.addEventListener('touchstart', function(ev) {
            const element = ev.currentTarget;
            element.bounds = element.getBoundingClientRect();
            element.addEventListener('touchmove', rotateToPointer, { passive: true });
            element.addEventListener('touchend', handleTouchEnd, { passive: true });
        }, { passive: true });
    });

    function handleTouchEnd(ev) {
        const element = ev.currentTarget;
        element.removeEventListener('touchmove', rotateToPointer);
        element.removeEventListener('touchend', handleTouchEnd);
        element.style.transform = '';
        element.style.background = '';
    }

    function rotateToPointer(ev) {
        const element = ev.currentTarget;
        const bounds = element.bounds;
        let x, y;
        
        if (ev.type === 'touchmove') {
            x = ev.touches[0].clientX - bounds.x - bounds.width / 2;
            y = ev.touches[0].clientY - bounds.y - bounds.height / 2;
        } else {
            x = ev.clientX - bounds.x - bounds.width / 2;
            y = ev.clientY - bounds.y - bounds.height / 2;
        }
        
        const d = Math.hypot(x, y);
        const amt = 1.5;
        
        element.style.transform = `scale3d(${1 + 0.07 * amt}, ${1 + 0.07 * amt}, 1.0)
                                   rotate3d(${y/100*amt}, ${-x/100*amt}, 0, ${Math.log(d)*2*amt}deg)`;
    }
});
