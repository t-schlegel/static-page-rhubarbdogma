const modal = document.getElementById("imageModal");
const modalImg = document.getElementById("modalImage");
const images = document.querySelectorAll(".gallery img");
let currentImageIndex = 0;

// Add click handlers to all gallery images
images.forEach((img, index) => {
  img.addEventListener("click", () => {
    currentImageIndex = index;
    openModal(img.src);
  });
});

function openModal(src) {
  modal.style.display = "block";
  modalImg.src = src;
  updateModalLayout();
}

function closeModal() {
  modal.style.display = "none";
}

function showImage(index) {
  currentImageIndex = index;
  if (currentImageIndex >= images.length) currentImageIndex = 0;
  if (currentImageIndex < 0) currentImageIndex = images.length - 1;
  modalImg.src = images[currentImageIndex].src;
}

// Navigation buttons
document.getElementById("prev").addEventListener("click", () => {
  showImage(currentImageIndex - 1);
});

document.getElementById("next").addEventListener("click", () => {
  showImage(currentImageIndex + 1);
});

// Close modal when clicking outside the image
modal.addEventListener("click", (e) => {
  if (
    e.target !== modalImage &&
    e.target !== prev &&
    e.target !== next &&
    !e.target.classList.contains("nav-button")
  ) {
    closeModal();
  }
});

// Keyboard navigation
document.addEventListener("keydown", (e) => {
  if (modal.style.display === "block") {
    // if (e.target !== modalImage && (e.target !== prev && e.target !== next)) {
    if (e.key === "ArrowLeft" || e.key === "h" || e.key === "k") {
      showImage(currentImageIndex - 1);
    } else if (e.key === "ArrowRight" || e.key === "l" || e.key === "j") {
      showImage(currentImageIndex + 1);
    } else if (e.key === "Escape") {
      closeModal();
    } else {
      closeModal();
    }
  }
});

// Function to adjust modal layout based on screen size
function updateModalLayout() {
  const modalContent = document.querySelector(".modal-content");
  const prevButton = document.getElementById("prev");
  const nextButton = document.getElementById("next");
  const prevArrow = prevButton.querySelector("img");
  const nextArrow = nextButton.querySelector("img");

  if (window.innerWidth <= 768) {
    // Mobile layout
    // Set modal content to flex-column
    modalContent.style.flexDirection = "column";
    modalContent.style.alignItems = "center";

    // Position prev button above image
    prevButton.style.order = "1";
    // Position image in the middle
    modalImg.style.order = "2";
    // Position next button below image
    nextButton.style.order = "3";

    // Rotate arrows to point up/down
    prevArrow.style.transform = "rotate(90deg)"; // Left arrow becomes up arrow
    nextArrow.style.transform = "rotate(90deg)"; // Right arrow becomes down arrow

    // Allow image to take full width
    modalImg.style.maxWidth = "100%";
    modalImg.style.maxHeight = "calc(80vh - 120px)"; // Adjust for button heights
  } else {
    // Desktop layout
    // Reset to horizontal layout
    modalContent.style.flexDirection = "row";
    modalContent.style.alignItems = "center";

    // Reset order
    prevButton.style.order = "";
    modalImg.style.order = "";
    nextButton.style.order = "";

    // Reset arrow rotation
    prevArrow.style.transform = "";
    nextArrow.style.transform = "";

    // Reset image size
    modalImg.style.maxWidth = "";
    modalImg.style.maxHeight = "";
  }
}

// Apply layout on initial load and window resize
window.addEventListener("resize", updateModalLayout);
updateModalLayout();

//const modal = document.getElementById('imageModal');
//const modalImg = document.getElementById('modalImage');
//const images = document.querySelectorAll('.gallery img');
//let currentImageIndex = 0;
//
//// Add click handlers to all gallery images
//images.forEach((img, index) => {
//  img.addEventListener('click', () => {
//    currentImageIndex = index;
//    openModal(img.src);
//  });
//});
//
//function openModal(src) {
//  modal.style.display = 'block';
//  modalImg.src = src;
//}
//
//function closeModal() {
//  modal.style.display = 'none';
//}
//
//function showImage(index) {
//  currentImageIndex = index;
//  if (currentImageIndex >= images.length) currentImageIndex = 0;
//  if (currentImageIndex < 0) currentImageIndex = images.length - 1;
//  modalImg.src = images[currentImageIndex].src;
//}
//
//// Navigation buttons
//document.getElementById('prev-button').addEventListener('click', () => {
//  showImage(currentImageIndex - 1);
//});
//
//document.getElementById('next-button').addEventListener('click', () => {
//  showImage(currentImageIndex + 1);
//});
//
//// Close modal when clicking outside the image
//modal.addEventListener('click', (e) => {
//  if (e.target === modal) {
//    closeModal();
//  }
//});
//
//// Keyboard navigation
//document.addEventListener('keydown', (e) => {
//  if (modal.style.display === 'block') {
//    if (e.key === 'ArrowLeft') {
//      showImage(currentImageIndex - 1);
//    } else if (e.key === 'ArrowRight') {
//      showImage(currentImageIndex + 1);
//    } else if (e.key === 'Escape') {
//      closeModal();
//    }
//  }
//});
