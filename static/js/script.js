// Scroll to top button 








// const scrollTop = () => {
    // element.scrollIntoView({ behavior: "smooth" });
// }

// projectLink.addEventListener("click", scrollTop))



// Smooth scrolling effects

const contactSection = document.querySelector(".section-contact");
const projectSection = document.querySelector(".section-projects");
const skillSection = document.querySelector(".section-skills");

document.querySelector(".projects-link").addEventListener("click", (e) => {
    e.preventDefault();
    projectSection.scrollIntoView({ behavior: "smooth" });
})

document.querySelector(".skills-link").addEventListener("click", (e) => {
    e.preventDefault();
    skillSection.scrollIntoView({ behavior: "smooth" });
})

document.querySelector(".contact-link").addEventListener("click", (e) => {
    e.preventDefault();
    contactSection.scrollIntoView({ behavior: "smooth" });
})


// lazy images loading

// const imgRef = document.querySelector('img[data-src]');

// const lazyImage = (entries) => {
//     const [entry] = entries;
//     // console.log(entry);
//     if(!entry.isIntersecting) return;
//     entry.target.src = imgRef.dataset.src;
// }

// const imagesObserver = new IntersectionObserver(lazyImage,{root:null, threshold:0})

// imagesObserver.observe(imgRef);