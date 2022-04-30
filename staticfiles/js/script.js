const skillSec = document.querySelector(".section-skills");
const projectSec = document.querySelector(".section-projects");
const contactSec = document.querySelector(".section-contact");


document.querySelector(".contact-link").addEventListener("click", (e) => {
    e.preventDefault()
    contactSec.scrollIntoView({ behavior: "smooth" });
})

document.querySelector(".skills-link").addEventListener("click", (e) => {
    e.preventDefault();
    skillSec.scrollIntoView({ behavior: "smooth" });
})

document.querySelector(".projects-link").addEventListener("click", (e) => {
    e.preventDefault();
    projectSec.scrollIntoView({ behavior: "smooth" });
})