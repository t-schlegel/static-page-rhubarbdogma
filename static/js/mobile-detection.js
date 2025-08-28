(function() {
    // Function to detect mobile devices
    function isMobileDevice() {
        // Check for mobile user agents
        const mobileRegex = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i;
        const userAgent = navigator.userAgent;
        
        // Check screen width as additional criteria
        const screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        const isMobileWidth = screenWidth <= 768;
        
        // Check for touch support
        const hasTouch = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
        
        // Return true if any mobile indicators are present
        return mobileRegex.test(userAgent) || (isMobileWidth && hasTouch);
    }
    
    // Function to check if user is on homepage
    function isHomepage() {
        const path = window.location.pathname;
        return path === '/' || path === '/index.html' || path.endsWith('/');
    }
    
    // Function to check if user already dismissed warning
    function hasWarningBeenDismissed() {
        return sessionStorage.getItem('mobile-warning-dismissed') === 'true';
    }
    
    // Function to redirect to warning page
    function redirectToWarning() {
        // Prevent infinite redirects
        if (!window.location.pathname.includes('warning.html')) {
            window.location.href = 'warning.html';
        }
    }
    
    // Main logic
    function init() {
        // Only run on homepage
        if (!isHomepage()) {
            return;
        }
        
        // Check if mobile device
        if (isMobileDevice()) {
            // If warning hasn't been dismissed, redirect to warning page
            if (!hasWarningBeenDismissed()) {
                redirectToWarning();
            }
        }
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();